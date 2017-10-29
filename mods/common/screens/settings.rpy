init -1 python:
	settings_background = es2d_gui + 'menu/main/back.png'
	
	settings_usual_btn = style.textbutton.ground
	settings_selected_btn = im.MatrixColor(settings_usual_btn, im.matrix.contrast(2.0))
	
	settings_resolutions = ((640, 360), (960, 540), (1200, 675), (1366, 768), (1920, 1080))
	
	
	def settings_add_text_cps(d):
		show_all_text = config.text_cps > 100000
		text_cps = in_bounds((config.text_cps % 100000) + d, 20, 220)
		config.text_cps = (100000 if show_all_text else 0) + text_cps
	
	def settings_set_text_cps_on(v):
		config.text_cps = (100000 if v else 0) + (config.text_cps % 100000)
	
	
	settings_viewport_y = 0.15
	settings_viewport_ysize = 1 - settings_viewport_y * 2
	settings_viewport_content_y = 0.01
	settings_viewport_content_height = 500
	
	settings_viewport_scroll_height = int(settings_viewport_content_height * 0.8)
	settings_viewport_scroll_part = 1.0 / 3
	
	w, h = get_texture_width(settings_background), get_texture_height(settings_background)
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


screen settings:
	zorder 10001
	modal  True
	
	image settings_background:
		size (1.0, 1.0)
	
	vbox:
		ypos int(settings_viewport_y * get_stage_height() -
		         settings_viewport_content_y * abs(get_stage_height() * (1 - settings_viewport_y) - settings_viewport_content_height) + 10)
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
		align (0.95, 0.5)
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
			size (35, 300)
			unhovered SetVariable('settings_scroll_hovered', False)
			action [SetVariable('settings_scroll_hovered', True),
					settings_set_viewport_content_y(
						(get_local_mouse()[1] / 300.0) * (1 + settings_viewport_scroll_part) - settings_viewport_scroll_part / 2)]
		python:
			if settings_scroll_hovered and get_mouse_down():
				settings_set_viewport_content_y(
					(get_local_mouse()[1] / 300.0) * (1 + settings_viewport_scroll_part) - settings_viewport_scroll_part / 2)
		
		textbutton '\\/':
			color 0xFFFFFF
			xalign 0.5
			size (25, 25)
			action settings_add_viewport_content_y(+0.25)
	
	
	textbutton 'Назад':
		align (0.95, 0.95)
		action HideMenu('settings')
	key 'ESCAPE' action HideMenu('settings')

