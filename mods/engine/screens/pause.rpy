init python:
	
	pause_showed_time = 0
	pause_hided_time  = 0
	
	pause_show = 'inventory'
	
	def get_back_with_color(image, color = '#000', alpha = 0.05):
		w, h = get_texture_width(image), get_texture_height(image)
		return im.Composite((w, h),
		                    (0, 0), im.Alpha(im.Rect(color, w, h), alpha),
		                    (0, 0), image)
	
	
	pause_back       = es2d_gui + 'menu/pause/back.png'
	pause_inventory  = es2d_gui + 'menu/pause/inventory.png'
	pause_notes      = es2d_gui + 'menu/pause/notes.png'
	
	pause_close_size = 25
	pause_close      = get_back_with_color(es2d_gui + 'menu/pause/close.png')
	
	
	pause_button          = im.MatrixColor(es2d_gui + 'menu/pause/button.png', im.matrix.invert() * im.matrix.tint(  0, 0.5, 1))
	pause_button_hover    = im.MatrixColor(es2d_gui + 'menu/pause/button.png', im.matrix.invert() * im.matrix.tint(0.4, 0.8, 1))
	pause_button_selected = im.MatrixColor(es2d_gui + 'menu/pause/button.png', im.matrix.invert() * im.matrix.tint(  1, 0.5, 0))
	
	pause_button          = get_back_with_color(pause_button,          alpha = 0.5)
	pause_button_hover    = get_back_with_color(pause_button_hover,    alpha = 0.2)
	pause_button_selected = get_back_with_color(pause_button_selected, alpha = 0.5)
	
	
	style.pause_button = Style(style.textbutton)
	style.pause_button.ground = pause_button
	style.pause_button.hover  = pause_button_hover
	style.pause_button.xsize = 0.2
	style.pause_button.ysize = 0.1
	


screen pause:
	zorder 10000
	modal  True
	
	
	key 'ESCAPE' action If(time.time() - pause_showed_time > 0.4,
	                       true  = [SetVariable('pause_hided_time', time.time()), HideMenu('pause')],
	                       false =  None)
	
	
	image 'images/bg/black.jpg':
		alpha 0.4
		pos  (0, 0)
		size (1.0, 1.0)
	
	hbox:
		align (0.5, 0.5)
		
		vbox:
			spacing 5
			yalign 0.5
			
			textbutton 'Продолжить'   style pause_button action HideMenu('pause')
			textbutton 'Загрузить'    style pause_button action ShowMenu('load')
			textbutton 'Сохранить'    style pause_button action ShowMenu('save')
			textbutton 'Настройки'    style pause_button action ShowMenu('settings')
			textbutton 'Выход в меню' style pause_button action Function(start_mod, 'main_menu')
		
		null xsize 10
		
		vbox:
			hbox:
				xalign 0.5
				
				textbutton 'Инвентарь':
					style pause_button
					xsize  0.2
					ground (pause_button if pause_show != 'inventory' else pause_button_selected)
					action SetVariable('pause_show', 'inventory')
				textbutton 'Записи':
					style pause_button
					xsize  0.2
					ground (pause_button if pause_show != 'notes'     else pause_button_selected)
					action SetVariable('pause_show', 'notes')
				
			image pause_back:
				size (0.4, 0.6)
				
				image (globals()['pause_' + pause_show]):
					align (0.5, 0.5)
					size  (0.3, 0.25)
				
				button:
					pos    (get_stage_width() * 0.4 + 10 + pause_close_size / 2, -10 - pause_close_size / 2)
					anchor (0.5, 0.5)
					size   (pause_close_size, pause_close_size)
					ground pause_close
					action HideMenu('pause')

