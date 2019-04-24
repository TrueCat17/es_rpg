init -1000 python:
	# db = dialogue box
	
	pause_end = 0
	def pause_ended():
		return pause_end < time.time()
	can_exec_next_funcs.append(pause_ended)
	
	db_read = True
	can_exec_next_vars.append((None, 'db_read'))
	
	
	db_pause_after_text = 0
	db_pause_end = 0
	
	db_dialogue = []
	
	db_visible = False
	db_hide_interface = False
	db_skip_tab = False
	db_mode = 'adv'
	
	db_font = style.text.font
	
	db_name = gui + 'dialogue/name.png'
	db_name_color = 0xFF0000
	db_name_text = ''
	
	db_voice = gui + 'dialogue/voice.png'
	db_voice_color = 0xFFFF00
	db_voice_text = ''
	db_voice_full_text = ''
	db_voice_text_after_pause = ''
	
	db_menu_btn = gui + 'dialogue/to_menu.png'
	db_menu_btn_size = 50
	db_menu_btn_indent = 20
	
	db_next_btn = gui + 'dialogue/to_next.png'
	db_next_btn_size = 50
	
	db_prev_btn = gui + 'dialogue/to_prev.png'
	db_prev_btn_size = 50
	
	db_prev_texts = []
	
	
	def show_text(name, name_prefix, name_postfix, name_color, text, text_prefix, text_postfix, text_color):
		global db_name_text, db_name_color
		global db_voice_text, db_voice_full_text, db_last_text_postfix, db_voice_color
		global db_pause_after_text, db_voice_text_after_pause
		global db_read, db_start_time, db_prev_texts
		
		if '{w' in text:
			db_pause_after_text = 1000000
			
			start = text.index('{w')
			end = text.index('}', start)
			pause_str = text[start + 2:end]
			if '=' in pause_str:
				pause_str = pause_str[pause_str.rindex('=') + 1:]
			pause_str = pause_str.strip()
			
			if pause_str:
				db_pause_after_text = float(pause_str)
			
			db_voice_text_after_pause = text[end + 1:]
			text = text[0:start]
		else:
			db_pause_after_text = 0
			db_pause_end = 0
			db_voice_text_after_pause = ''
		
		db_read = False
		
		
		# new text
		if name is not None:
			db_start_time = time.time()
			
			db_name_text = name_prefix + name + name_postfix
			db_name_color = name_color
			
			db_voice_text = ''
			db_voice_full_text = text_prefix + text
			if not db_voice_text_after_pause:
				db_voice_full_text += text_postfix
			db_last_text_postfix = text_postfix
		
		# continuation of prev text
		else:
			db_start_time = time.time() - len_unicode(db_voice_text) / float(renpy.config.text_cps)
			
			db_voice_full_text += text
			if not db_voice_text_after_pause:
				db_voice_full_text += db_last_text_postfix
		
		text_object = (db_name_text, db_name_color, text, text_color)
		db_prev_texts.append(text_object)
		db_prev_texts = db_prev_texts[-config.count_prev_texts:]
		
		db_voice_color = text_color
		
		window_show()
	
	
	def db_update():
		global db_text_size
		db_text_size = max(14, get_stage_height() / 30)
		
		global db_voice_size
		db_voice_size = get_stage_width() - (db_prev_btn_size + db_next_btn_size + 20), int(max(80, 0.2 * get_stage_height()))
		
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
				
				# going to the next symbol
				#   [] - access to byte, not to symbol
				#   In UTF-8 many symbols take more 1 bytes
				while n < l and not is_first_byte(db_voice_full_text[n]):
					n += 1
				
				# All tags, that started to open/close, must be opened/closed fully
				while n < l and db_voice_full_text[0:n].count('{') != db_voice_full_text[0:n].count('}'):
					n += 1
				
				if t < 0:
					break
			
			next_text = db_voice_full_text[0:n]
			
			# Close opened tags to on addition of string with spaces
			#   it spaces was not underlines or strikes
			tags_close_str = ''
			for tag in ('u', 's'):
				count = next_text.count('{' + tag + '}') - next_text.count('{/' + tag + '}')
				tags_close_str += ('{/' + tag + '}') * count
			
			# Get count symbols before end last word,
			# to fill it nbsp (non-breaking space) to there is no wordwrap inside unprinted word
			t = 0
			while n + t < l and db_voice_full_text[n + t] != ' ':
				t += 1
			
			# find last word and remove in it all tags
			last_word = db_voice_full_text[n:n+t]
			while '{' in last_word:
				start_tag = last_word.index('{')
				if '}' in last_word[start_tag:]:
					end_tag = last_word.index('}', start_tag)
				else:
					end_tag = len(last_word)
				last_word = last_word[:start_tag] + last_word[end_tag + 1:]
			
			nbsp = chr(0xC2) + chr(0xA0) # 0xC2, 0xA0 - code non-breaking space in UTF-8
			db_voice_text = next_text + tags_close_str + nbsp * len_unicode(last_word)
	
	
	def db_on_enter():
		if not sprites_effects_ended():
			sprites_effects_to_end()
			return
		if not location_objects_animations_ended():
			location_objects_animations_to_end()
			return
		if not characters_moved():
			characters_to_end()
			return
		
		global pause_end, db_pause_end, db_dialogue, db_name_text, db_voice_text, db_voice_full_text, db_read
		
		if pause_end > time.time():
			pause_end = time.time()
		
		if db_pause_end > time.time():
			db_pause_end = time.time() - 1
			return
		
		if db_voice_text == db_voice_full_text:
			if db_read:
				return
			db_read = True
			
			if db_mode == 'nvl':
				db_dialogue += [(db_name_text, db_name_color, db_voice_text, db_voice_color)]
				db_name_text = db_voice_text = db_voice_full_text = ''
			else:
				db_dialogue = []
		else:
			db_voice_text = db_voice_full_text
	
	
	window_show = SetVariable('db_visible', True)
	window_hide = SetVariable('db_visible', False)
	
	def nvl_clear():
		global db_dialogue
		db_dialogue = []
	
	def set_mode_adv():
		global db_mode
		db_mode = 'adv'
		nvl_clear()
	def set_mode_nvl():
		global db_mode
		db_mode = 'nvl'
		nvl_clear()



screen dialogue_box_skip:
	zorder 10000
	
	if db_skip_ctrl or db_skip_tab:
		text 'Skip Mode':
			color 0xFFFFFF
			text_size 30
			pos (20, 20)


screen dialogue_box:
	zorder -2
	
	key 'h' action SetVariable('db_hide_interface', not db_hide_interface)
	
	$ db_to_next = False
	key 'RETURN' action If(db_hide_interface, SetVariable('db_hide_interface', False), SetVariable('db_to_next', True))
	key 'SPACE'  action If(db_hide_interface, SetVariable('db_hide_interface', False), SetVariable('db_to_next', True))
	if db_to_next:
		$ db_skip_tab = False
	
	$ db_skip_ctrl = False
	key 'LEFT CTRL'  action SetVariable('db_skip_ctrl', True) first_delay 0
	key 'RIGHT CTRL' action SetVariable('db_skip_ctrl', True)
	key 'TAB' action SetVariable('db_skip_tab', not db_skip_tab)
	python:
		if (db_skip_ctrl or db_skip_tab):
			db_hide_interface = False
			db_to_next = True
			show_screen('dialogue_box_skip')
		
		if db_to_next:
			db_on_enter()
	
	key 'ESCAPE' action SetVariable('db_hide_interface', False)
	
	
	if not db_hide_interface:
		$ db_update()
		
		if db_visible:
			
			button:
				ground 'images/bg/black.jpg'
				hover  'images/bg/black.jpg'
				
				size  (1.0, 1.0)
				alpha (0.01 if db_mode == 'adv' else 0.30)
				mouse False
				
				action db_on_enter
			
			if db_mode == 'adv':
				vbox:
					align (0.5, 0.99)
					
					image db_name:
						xpos max(get_stage_width() / 10, db_prev_btn_size * 2)
						size (max(250, get_stage_width() / 5), int(db_text_size * 1.5))
						
						text db_name_text:
							font       db_font
							text_align 'center'
							text_size  db_text_size
							color      db_name_color
							align      (0.5, 0.8)
					
					hbox:
						spacing 5
						xalign 0.5
						
						button:
							yalign 0.5
							ground db_prev_btn
							size   (db_prev_btn_size, db_prev_btn_size)
							action prev_text_show
						
						image db_voice:
							size db_voice_size
							
							text db_voice_text:
								font      db_font
								text_size db_text_size
								color     db_voice_color
								align     (0.5, 0.5)
								size      (db_voice_size[0] - 30, db_voice_size[1] - 15)
						
						button:
							yalign 0.5
							ground db_next_btn
							size   (db_next_btn_size, db_next_btn_size)
							action db_on_enter
			
			
			elif db_mode == 'nvl':
				vbox:
					anchor 	(0.5, 0.0)
					pos		(0.5, 0.05)
					
					
					$ db_last_dialogue = db_dialogue + [(db_name_text, db_name_color, db_voice_text, db_voice_color)]
					
					for db_name_text_i, db_name_color_i, db_voice_text_i, db_voice_color_i in db_last_dialogue:
						python:
							db_tmp_name = ('{color=' + hex(db_name_color_i)[2:] + '}' + db_name_text_i + '{/color}: ') if db_name_text_i else ''
							db_tmp_voice = db_voice_text_i if db_voice_text_i else ' '
						
						text (db_tmp_name + db_tmp_voice):
							font      db_font
							text_size db_text_size
							color     db_voice_color_i
							xsize     0.75
				
				vbox:
					align (0.5, 0.99)
					
					null ysize int(db_text_size * 1.5)
					
					hbox:
						spacing 5
						xalign 0.5
						
						button:
							yalign 0.5
							ground db_prev_btn
							size   (db_prev_btn_size, db_prev_btn_size)
							action prev_text_show
						
						null size db_voice_size
						
						button:
							yalign 0.5
							ground db_next_btn
							size   (db_next_btn_size, db_next_btn_size)
							action db_on_enter
		
		
		button:
			ground 	db_menu_btn
			
			anchor (0.5, 0.5)
			pos    (get_stage_width() - db_menu_btn_indent - db_menu_btn_size / 2, db_menu_btn_indent + db_menu_btn_size / 2)
			size   (db_menu_btn_size, db_menu_btn_size)
			action show_pause
	else:
		button:
			ground 'images/bg/black.jpg'
			hover  'images/bg/black.jpg'
			
			size   (1.0, 1.0)
			alpha  0.01
			mouse  False
			
			action SetVariable('db_hide_interface', False)

