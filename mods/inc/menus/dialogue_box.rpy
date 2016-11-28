init -1000000 python:
	read = True


init -1001 python:
	# db = dialogue box
	
	db_background = 'images/bg/black.jpg'
	
	def set_background(path):
		global db_background
		db_background = path
	
	def set_scene(name):
		path = get_image(name)
		if path:
			set_background(path)
		else:
			set_background(None)
	
	
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
			
			# Определяем кол-во символов до конца последнего слова
			# Чтобы заполнить их неразрывными пробелами, чтобы не было переноса текста внутри недопечатанного слова
			extra = 0
			while False and n + extra < l and db_voice_full_text[n + extra] != ' ':
				if is_first_byte(db_voice_full_text[n + extra]):
					extra += 1
			
			db_voice_text = db_voice_full_text[0:n] + chr(160) * extra # 160 - код неразрывного пробела в Unicode
	
	
	def db_on_enter():
		global db_voice_text, read
		
		if db_voice_text == db_voice_full_text:
			read = True
		else:
			db_voice_text = db_voice_full_text




screen dialogue_box:
	window:
		$ db_update()
		
		image db_background:
			xysize (1, 1)
		
		
		button:
			background db_menu_btn
			
			anchor	(1, 0)
			pos		(get_stage_width() - db_menu_btn_indent, db_menu_btn_indent)
			xysize	(db_menu_btn_size, db_menu_btn_size)
		
		vbox:
			align (0.5, 0.99)
			
			image db_name:
				xalign 0.1
				xysize (0.2, 30)
				
				text db_name_text:
					text_align 'center'
					size 20
					color db_name_color
					align (0.5, 0.9)
			
			hbox:
				spacing 5
				xalign 0.5
				
				button:
					yalign		0.5
					background	db_prev_btn
					xysize		(db_prev_btn_size, db_prev_btn_size)
#					action		db_on_enter
				
				image db_voice:
					xysize (0.9, 0.2)
			
					text db_voice_text:
						size	20
						color	db_voice_color
						align	(0.5, 0.5)
						xysize	(0.85, 0.18)
				
				button:
					yalign 		0.5
					background	db_next_btn
					xysize		(db_next_btn_size, db_next_btn_size)
					action		db_on_enter
		
		key 'RETURN' action db_on_enter
		key 'SPACE' action db_on_enter
		
		if renpy.config.fps_meter:
			use fps_meter

