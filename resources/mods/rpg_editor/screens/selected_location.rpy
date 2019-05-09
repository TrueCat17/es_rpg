init python:
	cam_x, cam_y = get_stage_width() / 2, get_stage_height() / 2
	
	selected_k = 1.0
	speed = 25

screen selected_location:
	key 'w' action AddVariable('cam_y', -speed)
	key 'a' action AddVariable('cam_x', -speed)
	key 's' action AddVariable('cam_y', +speed)
	key 'd' action AddVariable('cam_x', +speed)
	
	key '9' action SetVariable('selected_k', max(selected_k - 0.25, 0.25))
	key '0' action SetVariable('selected_k', min(selected_k + 0.25, 4.00))
	
	python:
		selected_location = locations[selected_location_name]
		
		x, y = int(-cam_x * selected_k), int(-cam_y * selected_k)
		w, h = selected_location.width, selected_location.height
		wk, hk = int(w * selected_k), int(h * selected_k)
		sw, sh = get_stage_width() - props_width, get_stage_height()
		
		if wk < sw:
			cam_x = (wk - sw) / 2 / selected_k
		else:
			if x > 0:
				cam_x = 0
			elif x + wk < sw:
				cam_x = (wk - sw) / selected_k
		
		if hk < sh:
			cam_y = (hk - sh) / 2 / selected_k
		else:
			if y > 0:
				cam_y = 0
			elif y + hk < sh:
				cam_y = (hk - sh) / selected_k
		
		x, y = int(-cam_x * selected_k), int(-cam_y * selected_k)
		selected_location_x, selected_location_y = x, y
		w, h = wk, hk
	
	null:
		pos (x, y)
		
		if not selected_location.hide_main:
			image selected_location.main():
				size (w, h)
		if not selected_location.hide_over and selected_location.over():
			image selected_location.over():
				size (w, h)
		if selected_location.show_free and selected_location.free():
			image selected_location.free():
				size (w, h)
		
		if not selected_location.hide_places:
			for place_name in selected_location.places:
				python:
					obj_image = None
					if '_pos' in place_name:
						obj_name = place_name[0:place_name.index('_pos')]
						if location_objects.has_key(obj_name):
							obj = location_objects[obj_name]
							main_frame = obj['animations'][None]
							obj_image = main_frame['directory'] + main_frame['main_image'] + '.' + location_object_ext
							obj_width, obj_height = get_image_size(obj_image)
					
					place = selected_location.places[place_name]
					if place.side_exit is None:
						image = im.Rect('#0B0')
					else:
						x, y, w, h, exit_x, exit_y, exit_w, exit_h = get_place_coords(place)
						image = im.Composite((place.width, place.height),
							                 (   x  ,    y  ), im.Rect('#0B0', w, h),
							                 (exit_x, exit_y), im.Rect('#B00', exit_w, exit_h))
				
				if obj_image:
					image obj_image:
						pos (int(place.x * selected_k), int(place.y * selected_k))
						size (int(obj_width * selected_k), int(obj_height * selected_k))
						anchor (0.5, 1.0)
				
				button:
					ground image
					action [SetVariable('selected_place_name', place_name), SetVariable('selected_exit_num', None)]
					
					pos  (int(place.x * selected_k),     int(place.y * selected_k))
					size (int(place.width * selected_k), int(place.height * selected_k))
					
					alpha 0.5
		
		if not selected_location.hide_exits:
			for i in xrange(len(selected_location.exits)):
				python:
					exit = selected_location.exits[i]
					real_to = locations.has_key(exit.to_location_name) and locations[exit.to_location_name].places.has_key(exit.to_place_name)
					image = im.Rect('#BB0' if real_to else '#440')
				
				button:
					ground image
					action [SetVariable('selected_exit_num', i), SetVariable('selected_place_name', None)]
					
					pos  (int(exit.x * selected_k),     int(exit.y * selected_k))
					size (int(exit.width * selected_k), int(exit.height * selected_k))
					
					alpha 0.5
	
	use location_props

