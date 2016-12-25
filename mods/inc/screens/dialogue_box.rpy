init -1000000 python:
	read = True


init -1001 python:
	# db = dialogue box
	
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
		global read, db_start_time
		
		read = False
		
		# Новый текст
		if name is not None:
			db_start_time = time.time()
			
			db_name_text = name_prefix + name + name_postfix
			db_name_color = name_color
			
			db_voice_text = ''
			db_voice_full_text = text_prefix + text + text_postfix
			db_last_text_postfix = text_postfix
		
		# Продолжение предыдущего
		else:
			db_start_time = time.time() - len_unicode(db_voice_text) / float(renpy.config.text_cps)
			
			db_voice_full_text = db_voice_full_text[0:len(db_voice_full_text) - len(db_last_text_postfix)]
			db_voice_full_text += text + db_last_text_postfix
		
		db_voice_color = text_color
	
	
	def db_update():
		global db_voice_text
		
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
				#   И т. к. некоторые символы в Unicode занимают больше 1 байта,
				#     номер байта может не совпадать с номером символа
				while n < l and not is_first_byte(db_voice_full_text[n]):
					n += 1
				
				if t < 0:
					break
			
			while db_voice_full_text[0:n].count('{') != db_voice_full_text[0:n].count('}'):
				n += 1
			
			# Определяем кол-во символов до конца последнего слова,
			# Чтобы заполнить их неразрывными пробелами, чтобы не было переноса текста внутри недопечатанного слова
			extra = 0
			t = 0
			while n + t < l and db_voice_full_text[n + t] != ' ':
				t += 1
				if n + t < l and is_first_byte(db_voice_full_text[n + t]):
					extra += 1
			
			nbsp = chr(0xC2) + chr(0xA0) # 0xC2, 0xA0 - код неразрывного пробела в utf-8
			db_voice_text = db_voice_full_text[0:n] + nbsp * extra
	
	
	def db_on_enter():
		global db_dialogue, db_voice_text, read
		
		if db_voice_text == db_voice_full_text:
			read = True
			
			if db_mode == 'nvl':
				db_dialogue += [(db_name_text, db_name_color, db_voice_text, db_voice_color)]
			else:
				db_dialogue = []
		else:
			db_voice_text = db_voice_full_text
	
	
	window_show = SetVariable('db_visible', True)
	window_hide = SetVariable('db_visible', False)
	
	set_mode_adv = SetVariable('db_mode', 'adv')
	set_mode_nvl = SetVariable('db_mode', 'nvl')
	
	nvl_clear = SetVariable('db_dialogue', [])



screen dialogue_box:
	window:
		$ db_update()
		
		
		button:
			background db_menu_btn
	
			anchor	(1, 0)
			pos		(get_stage_width() - db_menu_btn_indent, db_menu_btn_indent)
			xysize	(db_menu_btn_size, db_menu_btn_size)
		
		
		
		if db_visible:
			
			if db_mode == 'adv':
				vbox:
					align (0.5, 0.99)
					
					image db_name:
						xalign 0.1
						xysize (250, 30)
						
						text db_name_text:
							text_align 'center'
							size 20
							color db_name_color
							align (0.5, 0.7)
					
					hbox:
						spacing 5
						xalign 0.5
						
						button:
							yalign		0.5
							background	db_prev_btn
							xysize		(db_prev_btn_size, db_prev_btn_size)
#							action		db_on_enter
						
						image db_voice:
							xysize (0.9, 0.2)
			
							text db_voice_text:
								size	20
								color	db_voice_color
								align	(0.5, 0.5)
								xysize	(0.85, 0.15)
						
						button:
							yalign 		0.5
							background	db_next_btn
							xysize		(db_next_btn_size, db_next_btn_size)
							action		db_on_enter
			
			
			elif db_mode == 'nvl':
				vbox:
					anchor 	(0.5, 0)
					pos		(0.5, 0.05)
					
					
					$ db_last_dialogue = db_dialogue + [(db_name_text, db_name_color, db_voice_text, db_voice_color)]
					
					for db_name_text_i, db_name_color_i, db_voice_text_i, db_voice_color_i in db_last_dialogue:
						python:
							db_tmp_name = ('{color=' + str(db_name_color_i) + '}' + db_name_text_i + '{/color}: ') if db_name_text_i else ''
							db_tmp_voice = db_voice_text_i if db_voice_text_i else ' '
						
						text (db_tmp_name + db_tmp_voice):
							size 20
							color db_voice_color_i
							xsize 0.75
				
				hbox:
					spacing 5
					align (0.5, 0.99)
					
					button:
						yalign		0.5
						background	db_prev_btn
						xysize		(db_prev_btn_size, db_prev_btn_size)
#						action		db_on_enter
					
					null width 0.9 height 0.2
					
					button:
						yalign 		0.5
						background	db_next_btn
						xysize		(db_next_btn_size, db_next_btn_size)
						action		db_on_enter
				
			
			
			
			key 'RETURN' action db_on_enter
			key 'SPACE' action db_on_enter
		
			if renpy.config.fps_meter:
				use fps_meter

