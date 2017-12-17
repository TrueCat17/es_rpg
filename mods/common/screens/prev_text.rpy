init python:
	pt_background = im.Rect('#181818')
	
	pt_x_indent = 20
	
	pt_viewport_y = 0.05
	pt_viewport_ysize = 1 - pt_viewport_y * 2
	pt_viewport_content_y = 0.01
	
	pt_viewport_scroll_part = 1.0 / 2
	
	
	def pt_add_viewport_content_y(v):
		global pt_viewport_content_y
		pt_viewport_content_y = in_bounds(pt_viewport_content_y + v, 0.01, 0.99)
	def pt_set_viewport_content_y(v):
		global pt_viewport_content_y
		pt_viewport_content_y = in_bounds(v, 0.01, 0.99)
	
	pt_scroll_hovered = False
	pt_scrolling = False
	pt_scroll_y = 0


screen prev_text:
	modal True
	zorder 10000
	
	key 'ESCAPE' action [HideMenu('prev_text'), SetVariable('pause_hided_time', time.time())]
	
	
	image pt_background:
		size (1.0, 1.0)
	
	button:
		pos    (get_stage_width() - 30, 30)
		anchor (0.5, 0.5)
		size   (pause_close_size, pause_close_size)
		ground pause_close
		action HideMenu('prev_text')
	
	python:
		pt_viewport_content_height = len(db_prev_texts) * db_text_size * 2
		pt_viewport_scroll_height = int(pt_viewport_content_height * 0.8)
		y = int(pt_viewport_y * get_stage_height() -
		          pt_viewport_content_y * abs(get_stage_height() * (1 - pt_viewport_y * 2) - pt_viewport_content_height) + 10)
	
	vbox:
		size (1.0, 1.0)
		ypos y
		spacing 5
		
		for name_text, name_color, text, text_color in db_prev_texts:
			$ tmp_name = ('{color=' + str(name_color) + '}' + name_text + '{/color}: ') if name_text else ''
					
			text (tmp_name + text):
				text_size db_text_size
				color text_color
				xsize get_stage_width() - pt_x_indent * 3
				xpos pt_x_indent
	
	if pt_viewport_content_height > get_stage_height() * 0.95:
		vbox:
			xpos get_stage_width() - pt_x_indent
			xanchor 0.5
			xsize 35
			yalign 0.5
			
			textbutton '/\\':
				color 0xFFFFFF
				xalign 0.5
				size (25, 25)
				action pt_add_viewport_content_y(-0.25)
			
			$ image = im.Bar(pt_viewport_content_y * (1 - pt_viewport_scroll_part) + pt_viewport_scroll_part,
					         pt_viewport_content_y * (1 - pt_viewport_scroll_part),
					         vertical = True)
			button:
				ground image
				hover  image
				xalign 0.5
				size (35, 0.6)
				unhovered SetVariable('pt_scroll_hovered', False)
				action [SetVariable('pt_scroll_hovered', True),
						pt_set_viewport_content_y(
							(get_local_mouse()[1] / (0.6 * get_stage_height())) * (1 + pt_viewport_scroll_part) - pt_viewport_scroll_part / 2)]
			python:
				pt_scroll_local_y = get_local_mouse()[1]
				
				if not pt_scrolling and pt_scroll_hovered and get_mouse_down():
					pt_scrolling = True
					pt_scroll_y = get_mouse()[1] - pt_scroll_local_y
				if not get_mouse_down():
					pt_scrolling = False
				
				if pt_scrolling:
					y = get_mouse()[1] - pt_scroll_y
					pt_set_viewport_content_y(
						(y / (0.6 * get_stage_height())) * (1 + pt_viewport_scroll_part) - pt_viewport_scroll_part / 2)
			
			textbutton '\\/':
				color 0xFFFFFF
				xalign 0.5
				size (25, 25)
				action pt_add_viewport_content_y(+0.25)

