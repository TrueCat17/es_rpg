init python:
	selected_location = None
	
	drag_location_name = None
	
	local_mouse_pos = None
	start_mouse_pos = None
	mouse_moved = True
	
	k = 1.0
	
	def start_drag_location(name):
        global drag_location_name
        drag_location_name = name
        
		global local_mouse_pos, start_mouse_pos, mouse_moved
		local_mouse_pos = get_local_mouse()
        start_mouse_pos = get_mouse()
        mouse_moved = False
	
	def select_location(name):
		global selected_location_name
		selected_location_name = name
		
		hide_screen('all_locations')
		show_screen('selected_location')


screen all_locations:
	key '9' action SetVariable('k', max(k - 0.25, 0.25))
	key '0' action SetVariable('k', min(k + 0.25, 2.00))
	
	python:
		mouse_down = get_mouse_down()
		if not mouse_down:
			if not mouse_moved:
				select_location(drag_location_name)
			drag_location_name = None
			local_mouse_pos = None
			mouse_moved = True
		
		if not local_mouse_pos:
			drag_location_name = None
		
		if drag_location_name is not None:
			mouse_pos = get_mouse()
			if start_mouse_pos != mouse_pos:
				mouse_moved = True
			
			if mouse_pos[0] < get_stage_width() - locations_width:
				location = locations[drag_location_name]
				old_x, old_y = location.x, location.y
				x, y = (mouse_pos[0] - local_mouse_pos[0]) / k, (mouse_pos[1] - local_mouse_pos[1]) / k
				if old_x != x or old_y != y:
					location.x, location.y = x, y
					set_save_locations()
	
	for name in locations:
		python:
			location = locations[name]
			preview = get_preview(name)
		
		if location.using:
			button:
				pos (int(location.x * k), int(location.y * k))
				size (int(get_image_width(preview) * k), int(get_image_height(preview) * k))
				
				ground preview
				hover preview
				
				action start_drag_location(name)
	
	use locations_list

