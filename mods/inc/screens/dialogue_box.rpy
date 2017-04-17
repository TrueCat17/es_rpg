init -1000 python:
	# db = dialogue box
	
	pause_end = 0
	read = True
	
	db_pause_after_text = 0
	db_pause_end = 0
	
	db_dialogue = []
	
	db_visible = True
	db_mode = 'adv'
	
	db_name = es2d_gui + 'dialogue/name.png'
	db_name_color = 0xFF0000
	db_name_text = ''
	
	db_voice = es2d_gui + 'dialogue/voice.png'
	db_voice_color = 0xFFFF00
	db_voice_text = ''
	db_voice_full_text = ''
	db_voice_text_after_pause = ''
	
	db_menu_btn = es2d_gui + 'dialogue/to_menu.png'
	db_menu_btn_size = 50
	db_menu_btn_indent = 20
	
	db_next_btn = es2d_gui + 'dialogue/to_next.png'
	db_next_btn_size = 30
	
	db_prev_btn = es2d_gui + 'dialogue/to_prev.png'
	db_prev_btn_size = 30
	
	def show_text(name, name_prefix, name_postfix, name_color, text, text_prefix, text_postfix, text_color):
		global db_name_text, db_name_color
		global db_voice_text, db_voice_full_text, db_last_text_postfix, db_voice_color
		global db_pause_after_text, db_voice_text_after_pause
		global read, db_start_time
		
		if '{w' in text:
			db_pause_after_text = 1000000
			
			start = text.index('{w')
			end = text.index('}', start)
			pause_str = text[start + 3:end]
			if '=' in pause_str:
				pause_str = pause_str[pause_str.rindex('=') + 1:]
			while len(pause_str) and pause_str[0] == ' ':
				pause_str = pause_str[1:]
			
			if pause_str:
				db_pause_after_text = float(pause_str)
			
			db_voice_text_after_pause = text[end + 1:]
			text = text[0:start]
		else:
			db_pause_after_text = 0
			db_pause_end = 0
			db_voice_text_after_pause = ''
		
		read = False
		
		# Новый текст
		if name is not None:
			db_start_time = time.time()
			
			db_name_text = name_prefix + name + name_postfix
			db_name_color = name_color
			
			db_voice_text = ''
			db_voice_full_text = text_prefix + text
			if not db_voice_text_after_pause:
				db_voice_full_text += text_postfix
			db_last_text_postfix = text_postfix
		
		# Продолжение предыдущего
		else:
			db_start_time = time.time() - len_unicode(db_voice_text) / float(renpy.config.text_cps)
			
			db_voice_full_text = db_voice_full_text[0:len(db_voice_full_text)]
			db_voice_full_text += text
			if not db_voice_text_after_pause:
				db_voice_full_text += db_last_text_postfix
		
		db_voice_color = text_color
	
	
	def db_update():
		global db_voice_text, db_pause_after_text, db_pause_end
		
		if db_pause_after_text != 0:
			if db_pause_end == 0:
				db_pause_end = time.time() + db_pause_after_text
			elif db_pause_end < time.time():
				db_pause_after_text = 0
				db_pause_end = 0
				show_text(None, '', '', 0, db_voice_text_after_pause, '', db_last_text_postfix, db_voice_color)
		
		if db_voice_text != db_voice_full_text:
			l = len(db_voice_full_text)
			t = int((time.time() - db_start_time) * renpy.config.text_cps)
			t = min(t, l)
			
			n = 0
			for i in xrange(l):
				n += 1
				t -= 1
				
				while n < l and db_voice_full_text[n] == ' ':
					n += 1
				
				# Добираемся до следующего символа
				#   [] - доступ к байту строки, а не к символу
				#   И т. к. многие символы в Unicode занимают больше 1 байта,
				#     номер байта может не совпадать с номером символа
				while n < l and not is_first_byte(db_voice_full_text[n]):
					n += 1
				
				# Все теги, что начали открываться/закрываться, должны быть открыты/закрыты нормально
				while n < l and db_voice_full_text[0:n].count('{') != db_voice_full_text[0:n].count('}'):
					n += 1
				
				if t < 0:
					break
			
			next_text = db_voice_full_text[0:n]
			
			# Закрываем открытые теги, чтобы при дополнении строки "пробелами"
			#   эти пробелы не были подчёркнуты или зачёркнуты
			tags_close_str = ''
			for tag in ('u', 's'):
				count = next_text.count('{' + tag + '}') - next_text.count('{/' + tag + '}')
				tags_close_str += ('{/' + tag + '}') * count
			
			# Определяем кол-во символов до конца последнего слова,
			# Чтобы заполнить их неразрывными пробелами, чтобы не было переноса текста внутри недопечатанного слова
			t = 0
			while n + t < l and db_voice_full_text[n + t] != ' ':
				t += 1
			
			# Находим последнее слово и удаляем из него все тэги
			last_word = db_voice_full_text[n:n+t]
			while '{' in last_word:
				start_tag = last_word.index('{')
				if '}' in last_word[start_tag:]:
					end_tag = last_word.index('}', start_tag)
				else:
					end_tag = len(last_word)
				last_word = last_word[:start_tag] + last_word[end_tag + 1:]
				
			
			extra = 0
			for c in last_word:
				if is_first_byte(c):
					extra += 1
			
			nbsp = chr(0xC2) + chr(0xA0) # 0xC2, 0xA0 - код неразрывного пробела в utf-8
			db_voice_text = next_text + tags_close_str + nbsp * extra
	
	
	def db_on_enter():
		if not sprites_effects_ended():
			sprites_effects_to_end()
			return
		
		global pause_end, db_pause_end, db_dialogue, db_name_text, db_voice_text, db_voice_full_text, read
		
		if pause_end > time.time():
			pause_end = time.time()
		
		if db_pause_end > time.time():
			db_pause_end = time.time() - 1
			return
		
		if db_voice_text == db_voice_full_text:
			if read:
				return
			read = True
			
			if db_mode == 'nvl':
				db_dialogue += [(db_name_text, db_name_color, db_voice_text, db_voice_color)]
				db_name_text = db_voice_text = db_voice_full_text = ''
			else:
				db_dialogue = []
		else:
			db_voice_text = db_voice_full_text
	
	
	window_show = SetVariable('db_visible', True)
	window_hide = SetVariable('db_visible', False)
	
	set_mode_adv = SetVariable('db_mode', 'adv')
	set_mode_nvl = SetVariable('db_mode', 'nvl')
	
	def nvl_clear():
		global db_dialogue
		db_dialogue = []



screen dialogue_box:
	zorder -2
	
	key 'RETURN' action db_on_enter
	key 'SPACE' action db_on_enter
	
	$ db_update()
	
	$ db_text_size = max(14, get_stage_height() / 30)
	
	
	
	if db_visible:
		
		if db_mode == 'adv':
			vbox:
				align (0.5, 0.99)
				
				image db_name:
					xpos max(get_stage_width() / 10, db_prev_btn_size * 2)
					xysize (max(250, get_stage_width() / 5), db_text_size * 1.5)
					
					text db_name_text:
						text_align 'center'
						size db_text_size
						color db_name_color
						align (0.5, 0.7)
				
				hbox:
					spacing 5
					xalign 0.5
					
					button:
						yalign		0.5
						ground		db_prev_btn
						xysize		(db_prev_btn_size, db_prev_btn_size)
#						action		db_on_enter
					
					image db_voice:
						xysize (0.85, max(80, 0.2 * get_stage_height()))
		
						text db_voice_text:
							size	db_text_size
							color	db_voice_color
							align	(0.5, 0.5)
							xysize	(0.825, max(70, 0.18 * get_stage_height()))
					
					button:
						yalign 		0.5
						ground		db_next_btn
						xysize		(db_next_btn_size, db_next_btn_size)
						action		db_on_enter
		
		
		elif db_mode == 'nvl':
			image im.Alpha('images/bg/black.jpg', 0.3):
				xysize (1.0, 1.0)
				
				vbox:
					anchor 	(0.5, 0.0)
					pos		(0.5, 0.05)
				
				
					$ db_last_dialogue = db_dialogue + [(db_name_text, db_name_color, db_voice_text, db_voice_color)]
				
					for db_name_text_i, db_name_color_i, db_voice_text_i, db_voice_color_i in db_last_dialogue:
						python:
							db_tmp_name = ('{color=' + str(db_name_color_i) + '}' + db_name_text_i + '{/color}: ') if db_name_text_i else ''
							db_tmp_voice = db_voice_text_i if db_voice_text_i else ' '
					
						text (db_tmp_name + db_tmp_voice):
							size db_text_size
							color db_voice_color_i
							xsize 0.75
			
				hbox:
					spacing 5
					align (0.5, 0.99)
				
					button:
						yalign		0.5
						ground		db_prev_btn
						xysize		(db_prev_btn_size, db_prev_btn_size)
#						action		db_on_enter
				
					null xysize (0.9, 0.2)
				
					button:
						yalign 		0.5
						ground		db_next_btn
						xysize		(db_next_btn_size, db_next_btn_size)
						action		db_on_enter
		
		
		if renpy.config.fps_meter:
			use fps_meter
	
	
	button:
		ground 	db_menu_btn

		anchor	(1.0, 0.0)
		pos		(get_stage_width() - db_menu_btn_indent, db_menu_btn_indent)
		xysize	(db_menu_btn_size, db_menu_btn_size)

