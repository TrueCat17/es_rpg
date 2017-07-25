init python:
	
	loc__background_alpha = 0.0
	
	draw_location = draw_location_name = None
	draw_objects_on_location = []
	
	max_time = time.time() * 2
	
	
	control = False
	loc__prev_left = loc__prev_right = loc__prev_up = loc__prev_down = False
	loc__left = loc__right = loc__up = loc__down = False
	
	loc__directions = [to_left, to_right, to_forward, to_back]
	loc__direction = to_back
	loc__left_time = loc__right_time = loc__up_time = loc__down_time = max_time
	
	
	def loc__get_min(a, b, c, d):
		return [a, b, c, d].index(min(a, b, c, d))
	
	
	loc__prev_time = 0
	def loc__move_character(dx, dy):
		global loc__prev_time
		
		if me.pose != 'stance' or character_moving or not control:
			loc__prev_time = time.time()
			return
		
		if dx == 0 and dy == 0:
			me.move_kind = 'stay'
			loc__prev_time = time.time()
			return
		
		if dx and dy:
			dx /= 2 ** 0.5
			dy /= 2 ** 0.5
		
		me.fps = 			 character_run_fps 	if loc__ctrl_is_down else  character_walk_fps
		me.move_kind = 				'run'		if loc__ctrl_is_down else 		'walk'
		character_speed = 	character_run_speed if loc__ctrl_is_down else character_walk_speed
		
		dtime = time.time() - loc__prev_time
		loc__prev_time = time.time()
		
		dx *= character_speed * dtime
		dy *= character_speed * dtime
		
		to_x, to_y = get_end_point(me.x, me.y, dx, dy)
		dx, dy = to_x - me.x, to_y - me.y
		if dx or dy:
			me.x = me.to_x = to_x
			me.y = me.to_y = to_y
		else:
			me.move_kind = 'stay'


screen location:
	zorder -4
	
	python:
		if time.time() - location_start_time < location_fade_time and cur_location_name:
			loc__background_alpha = (time.time() - location_start_time) / location_fade_time
		elif time.time() - location_start_time < location_fade_time * 2:
			if not cur_location_name:
				location_start_time -= location_fade_time
			loc__background_alpha = 1.0 - (time.time() - location_start_time - location_fade_time) / location_fade_time
			
			if draw_location_name != cur_location_name:
				draw_location, draw_location_name = cur_location, cur_location_name
				
				draw_objects_on_location = objects_on_location
				was_out_exit = False
				show_character(me, cur_to_place)
				cam_object = me
		else:
			loc__background_alpha = 0.0
	
	
	if draw_location_name:
		$ exec_action = False
		key 'E' action SetVariable('exec_action', True)
		
		$ loc__ctrl_is_down = False
		key 'LEFT CTRL' 	action SetVariable('loc__ctrl_is_down', True) first_delay 0.01
		key 'RIGHT CTRL' 	action SetVariable('loc__ctrl_is_down', True) first_delay 0.01
		key 'LEFT SHIFT' 	action SetVariable('loc__ctrl_is_down', True) first_delay 0.01
		key 'RIGHT SHIFT' 	action SetVariable('loc__ctrl_is_down', True) first_delay 0.01
		
		python:
			loc__prev_left, loc__prev_right, loc__prev_up, loc__prev_down = loc__left, loc__right, loc__up, loc__down
			loc__start_moving = not(loc__left or loc__right or loc__up or loc__down)
			if loc__start_moving:
				loc__prev_time = time.time() - 0.1
			loc__left = loc__right = loc__up = loc__down = False
		
		key 'LEFT' 		action SetVariable('loc__left', 	True) first_delay 0.0
		key 'RIGHT' 	action SetVariable('loc__right', 	True) first_delay 0.0
		key 'UP' 		action SetVariable('loc__up', 		True) first_delay 0.0
		key 'DOWN' 		action SetVariable('loc__down', 	True) first_delay 0.0
		key 'a' 		action SetVariable('loc__left', 	True) first_delay 0.0
		key 'd' 		action SetVariable('loc__right', 	True) first_delay 0.0
		key 'w' 		action SetVariable('loc__up', 		True) first_delay 0.0
		key 's' 		action SetVariable('loc__down', 	True) first_delay 0.0
		
		python:
			if draw_location_name == cur_location_name:
				loc__character_dx = loc__character_dy = 0
				if loc__left:
					loc__character_dx -= 1
				if loc__right:
					loc__character_dx += 1
				if loc__up:
					loc__character_dy -= 1
				if loc__down:
					loc__character_dy += 1
				loc__move_character(loc__character_dx, loc__character_dy)
				
			
				if control:
					if loc__left and not loc__prev_left:
						loc__left_time = time.time()
					if loc__right and not loc__prev_right:
						loc__right_time = time.time()
					if loc__up and not loc__prev_up:
						loc__up_time = time.time()
					if loc__down and not loc__prev_down:
						loc__down_time = time.time()
			
					if loc__left or loc__right or loc__up or loc__down:
						loc__direction = loc__directions[loc__get_min(	loc__left_time if loc__left else max_time,
																		loc__right_time if loc__right else max_time,
																		loc__up_time if loc__up else max_time,
																		loc__down_time if loc__down else max_time
						)]
						me.set_direction(loc__direction)
		
		
		python:
			update_location_scale()
			
			for obj in objects_on_location:
				if obj.update:
					obj.update()
			objects_on_location.sort(key = lambda obj: obj.y)
			
			draw_location.update_pos()
		
		image draw_location.main:
			pos (draw_location.x, draw_location.y)
			xysize (draw_location.width * location_scale, draw_location.height * location_scale)
			
			for obj in objects_on_location:
				python:
					obj_x, obj_y = obj.x * location_scale, obj.y * location_scale
					obj_width, obj_height = obj.width * location_scale, obj.height * location_scale
					
					obj_xanchor, obj_yanchor = obj.xanchor, obj.yanchor
					if type(obj_xanchor) == int:
						obj_xanchor *= location_scale
					if type(obj_yanchor) == int:
						obj_yanchor *= location_scale
				
				image obj.image:
					pos 	(int(obj_x), int(obj_y))
					anchor 	(obj_xanchor, obj_yanchor)
					xysize 	(obj_width, obj_height)
					crop 	obj.crop
		
		if draw_location.over:
			image draw_location.over:
				pos (draw_location.x, draw_location.y)
				xysize (draw_location.width * location_scale, draw_location.height * location_scale)
		
		
		image 'images/bg/black.jpg':
			xysize (1.0, 1.0)
			alpha loc__background_alpha 


