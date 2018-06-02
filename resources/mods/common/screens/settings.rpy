init -1 python:
	settings_background = gui + 'menu/main/back.png'
	
	settings_usual_btn = style.textbutton.ground
	settings_selected_btn = im.MatrixColor(settings_usual_btn, im.matrix.contrast(2.0))
	
	k = get_from_hard_config("window_w_div_h", float)
	settings_resolutions = tuple((i, int(i/k)) for i in (640, 960, 1200, 1366, 1920))
	
	settings_show_mods = False
	
	
	settings_autosave_times = (0.5, 1, 2, 3, 5, 7, 10, 15, 0)
	def settings_prev_autosave_time():
		autosave = config.autosave / 60.0
		if autosave <= 0:
			config.autosave = int(settings_autosave_times[-2] * 60)
		else:
			i = 0
			while i < len(settings_autosave_times) - 1 and autosave > settings_autosave_times[i]:
				i += 1
			config.autosave = int(settings_autosave_times[max(i - 1, 0)] * 60)
	def settings_next_autosave_time():
		autosave = config.autosave / 60.0
		if autosave > 0:
			i = 0
			while i < len(settings_autosave_times) - 1 and autosave > settings_autosave_times[i]:
				i += 1
			config.autosave = int(settings_autosave_times[i + 1] * 60)
	
	
	def settings_add_text_cps(d):
		show_all_text = config.text_cps > 100000
		text_cps = in_bounds((config.text_cps % 100000) + d, 20, 220)
		config.text_cps = (100000 if show_all_text else 0) + text_cps
	
	def settings_set_text_cps_on(v):
		config.text_cps = (100000 if v else 0) + (config.text_cps % 100000)
	
	
	settings_viewport_y = 0.15
	settings_viewport_ysize = 1 - settings_viewport_y * 2
	settings_viewport_content_y = 0.01
	settings_viewport_content_height = 600
	
	settings_viewport_scroll_height = int(settings_viewport_content_height * 0.8)
	settings_viewport_scroll_part = 1.0 / 3
	
	
	settings_inited = False
	def init_settings():
		global settings_inited, settings_background_up, settings_background_down
		settings_inited = True
		
		w, h = get_texture_size(settings_background)
		settings_background_up   = im.Crop(settings_background,
			                               (0, 0, w, h * settings_viewport_y))
		settings_background_down = im.Crop(settings_background,
			                               (0, (1 - settings_viewport_y) * h, w, settings_viewport_y * h))
	
	def settings_add_viewport_content_y(v):
		global settings_viewport_content_y
		settings_viewport_content_y = in_bounds(settings_viewport_content_y + v, 0.01, 0.99)
	def settings_set_viewport_content_y(v):
		global settings_viewport_content_y
		settings_viewport_content_y = in_bounds(v, 0.01, 0.99)
	
	settings_scroll_hovered = False
	settings_scrolling = False
	settings_scroll_y = 0


screen settings:
	zorder 10001
	modal  True
	
	image settings_background:
		size (1.0, 1.0)
	
	python:
		if not checkboxes_inited:
			init_checkboxes()
		if not settings_inited:
			init_settings()
		
		y = int(settings_viewport_y * get_stage_height() -
		        settings_viewport_content_y * abs(get_stage_height() * (1 - settings_viewport_y * 2) - settings_viewport_content_height) + 10)
	
	if settings_show_mods:
		$ mods = get_mods()
		
		vbox:
			ypos y
			xalign 0.5
			spacing 10
			
			for name in mods:
				textbutton name:
					action start_mod(mods[name])
	else:
		vbox:
			ypos y
			spacing 50
			
			vbox:
				xalign 0.5
				xsize 1.0
				
				null:
					xalign 0.5
					size (350, 25)
					
					$ is_fullscreen = get_from_hard_config('window_fullscreen', bool)
					button:
						ground (checkbox_yes if is_fullscreen else checkbox_no)
						action set_fullscreen(not is_fullscreen)
						size (25, 25)
					text 'Развернуть на весь экран':
						xpos 40
						color 0
						text_size 25
				
				null ysize 15
				
				vbox:
					xsize 1.0
					spacing 5
					
					text 'Разрешение:':
						xalign 0.5
						color 0
					hbox:
						xalign 0.5
						spacing 10
						
						$ sw, sh = get_stage_width(), get_stage_height()
						for resolution in settings_resolutions:
							textbutton (str(resolution[0]) + 'x' + str(resolution[1])):
								xsize 100
								ground (settings_selected_btn if resolution == (sw, sh) else settings_usual_btn)
								action set_stage_size(resolution[0], resolution[1])
			
			vbox:
				xsize 1.0
				xalign 0.5
				spacing 5
				
				text 'Громкость':
					xalign 0.5
					color 0
				
				for i in xrange(len(std_mixers)):
					$ mixer, mixer_name = std_mixers[i], std_mixer_names[i]
					hbox:
						xalign 0.5
						spacing 5
						
						text (mixer_name + ':'):
							color 0
							yalign 0.5
							xsize 100
						
						textbutton '-':
							size (25, 25)
							action renpy.music.add_mixer_volume(-0.1, mixer)
						image im.Bar(config[mixer + '_volume']):
							size (300, 25)
						textbutton '+':
							size (25, 25)
							action renpy.music.add_mixer_volume(+0.1, mixer)
			
			vbox:
				xsize 1.0
				
				null:
					xalign 0.5
					size (350, 25)
					
					$ show_all_text = config.text_cps > 100000
					button:
						ground (checkbox_yes if show_all_text else checkbox_no)
						action settings_set_text_cps_on(not show_all_text)
						size (25, 25)
					text 'Показывать весь текст сразу':
						xpos 40
						color 0
						text_size 25
				null ysize 10
				
				text 'Скорость показа текста:':
					xalign 0.5
					color 0
				hbox:
					xalign 0.5
					spacing 5
					
					textbutton '-':
						size (25, 25)
						action settings_add_text_cps(-20)
					image im.Bar(((config.text_cps % 100000) - 20) / 200.0):
						size (300, 25)
					textbutton '+':
						size (25, 25)
						action settings_add_text_cps(+20)
			
			null:
				xalign 0.5
				size (350, 25)
				
				button:
					ground (checkbox_yes if config.fps_meter else checkbox_no)
					action SetDict(config, 'fps_meter', not config.fps_meter)
					size (25, 25)
				text 'Показывать FPS':
					xpos 40
					color 0
					text_size 25
			
			vbox:
				xsize 1.0
				spacing 5
				
				text 'Авто-Сохранение':
					xalign 0.5
					color 0
					text_size 15
				
				hbox:
					xalign 0.5
					spacing 5
					
					textbutton '<-':
						size (25, 25)
						action settings_prev_autosave_time
					text ((str(config.autosave / 60.0) + ' мин.') if config.autosave > 0 else 'Отключено'):
						xsize 300
						text_align 'center'
						color 0
						text_size 25
					textbutton '->':
						size (25, 25)
						action settings_next_autosave_time
	
	
	image settings_background_up:
		size (1.0, settings_viewport_y)
		
		text 'Настройки':
			align (0.5, 0.02)
			
			color 0xFFFFFF
			text_size get_stage_height() / 10
	
	image settings_background_down:
		ypos 1 - settings_viewport_y
		size (1.0, settings_viewport_y)
	
	
	vbox:
		align (0.97, 0.5)
		xsize 35
		
		textbutton '/\\':
			color 0xFFFFFF
			xalign 0.5
			size (25, 25)
			action settings_add_viewport_content_y(-0.25)
		
		$ image = im.Bar(settings_viewport_content_y * (1 - settings_viewport_scroll_part) + settings_viewport_scroll_part,
			             settings_viewport_content_y * (1 - settings_viewport_scroll_part),
			             vertical = True)
		button:
			ground image
			hover  image
			xalign 0.5
			size (35, 0.6)
			unhovered SetVariable('settings_scroll_hovered', False)
			action [SetVariable('settings_scroll_hovered', True),
					settings_set_viewport_content_y(
						(get_local_mouse()[1] / (0.6 * get_stage_height())) * (1 + settings_viewport_scroll_part) - settings_viewport_scroll_part / 2)]
		python:
			settings_scroll_local_y = get_local_mouse()[1]
			
			if not settings_scrolling and settings_scroll_hovered and get_mouse_down():
				settings_scrolling = True
				settings_scroll_y = get_mouse()[1] - settings_scroll_local_y
			if not get_mouse_down():
				settings_scrolling = False
			
			if settings_scrolling:
				y = get_mouse()[1] - settings_scroll_y
				settings_set_viewport_content_y(
					(y / (0.6 * get_stage_height())) * (1 + settings_viewport_scroll_part) - settings_viewport_scroll_part / 2)
		
		textbutton '\\/':
			color 0xFFFFFF
			xalign 0.5
			size (25, 25)
			action settings_add_viewport_content_y(+0.25)
	
	textbutton ('Настройки' if settings_show_mods else 'Моды'):
		align (0.05, 0.95)
		action SetVariable('settings_show_mods', not settings_show_mods)
	
	textbutton 'Назад':
		align (0.95, 0.95)
		action HideMenu('settings')
	key 'ESCAPE' action HideMenu('settings')

