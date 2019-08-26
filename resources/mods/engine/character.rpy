init -1001 python:
	
	character_ext = 'png'
	
	
	character_walk_fps          =   4
	character_run_fps           =  12
	character_acceleration_time = 0.5
	character_walk_speed        =  50
	character_run_speed         = 150*1
	
	character_walk_acceleration = character_walk_speed / character_acceleration_time
	character_run_acceleration = character_run_speed / character_acceleration_time
	
	
	character_max_frame = 4
	character_max_direction = 4
	
	character_radius = 10 # used physics.rpy
	
	character_xsize = 48
	character_ysize = 96
	
	
	# directions
	to_forward = 3
	to_back = 0
	to_left = 1
	to_right = 2
	
	def characters_moved():
		if cur_location:
			for obj in cur_location.objects:
				if isinstance(obj, Character) and not obj.ended_move_waiting():
					return False
		return True
	can_exec_next_check_funcs.append(characters_moved)
	
	def characters_to_end():
		if cur_location:
			for obj in cur_location.objects:
				if isinstance(obj, Character):
					obj.move_to_end()
	can_exec_next_skip_funcs.append(characters_to_end)
	
	
	
	def register_character_animation(character, anim_name, path, xoffset, yoffset,
	                                 count_frames, start_frame, end_frame, time = 1.0):
		if type(xoffset) is not int or type(yoffset) is not int:
			out_msg('register_character_animation',
			        'On registration of animation <' + str(anim_name) + '> of character <' + str(character) + '>\n' +
			        'set invalid offset: <' + str(xoffset) + ', ' + str(yoffset) + '>, expected ints')
			return
		
		if count_frames <= 0 or not (0 <= start_frame < count_frames) or not (0 <= end_frame < count_frames):
			out_msg('register_character_animation',
			        'On registration of animation <' + str(anim_name) + '> of character <' + str(character) + '>\n' +
			        'set invalid frames:\n' +
			        'count, start, end = ' + str(count_frames) + ', ' + str(start_frame) + ', ' + str(end_frame))
			return
		
		animations = character.animations
		if animations.has_key(anim_name):
			out_msg('register_character_animation', 'Animation <' + str(anim_name) + '> of character <' + str(character) + '> already exists')
			return
		
		animations[anim_name] = Object(
			name = anim_name,
			path = path,
			
			count_frames = count_frames,
			start_frame  = start_frame,
			end_frame    = end_frame,
			time         = float(time),
		
			xoffset = xoffset,
			yoffset = yoffset,
			xsize = 0,
			ysize = 0,
			loaded = False
		)
	
	def characters_anim_ended():
		if cur_location:
			for obj in cur_location.objects:
				if isinstance(obj, Character) and not obj.ended_anim_waiting():
					return False
		return True
	can_exec_next_check_funcs.append(characters_anim_ended)
	
	def characters_anim_to_end():
		if cur_location:
			for obj in cur_location.objects:
				if isinstance(obj, Character):
					obj.anim_to_end()
	can_exec_next_skip_funcs.append(characters_anim_to_end)
	
	
	
	characters = []
	class Character(Object):
		def __init__(self, name, **kwargs):
			Object.__init__(self)
			characters.append(self)
			
			self.real_name = name
			self.unknown_name = kwargs.get('unknown_name', name)
			
			self.name = name
			self.name_prefix = kwargs.get('name_prefix', '')
			self.name_postfix = kwargs.get('name_postfix', '')
			self.color = kwargs.get('color', 0)
			if type(self.color) is not int:
				r, g, b, a = renpy.easy.color(self.color)
				self.color = (r << 16) + (g << 8) + b
			
			self.text_prefix = kwargs.get('text_prefix', '')
			self.text_postfix = kwargs.get('text_postfix', '')
			self.text_color = kwargs.get('text_color', 0xFFFF00)
			if type(self.text_color) is not int:
				r, g, b, a = renpy.easy.color(self.text_color)
				self.text_color = (r << 16) + (g << 8) + b
			
			# rpg-props:
			self.directory = None
			self.dress = None
			
			self.frame = 0
			self.direction = 0
			self.run = False
			self.pose = 'stance'       # 'stance' | 'sit'
			self.move_kind = 'stay'    #  'stay'  | 'walk' | 'run'
			self.fps = character_walk_fps
			
			self.moving_start_time = time.time()
			
			self.end_stop_time = None
			self.moving_ended = True
			
			self.x, self.y = 0, 0
			self.xanchor, self.yanchor = 0.5, 0.8
			self.xoffset, self.yoffset = 0, 0
			self.xsize, self.ysize = character_xsize, character_ysize
			self.crop = (0, 0, self.xsize, self.ysize)
			
			self.location = None
			self.to_places = []
			self.place_index = 0
			
			self.animations = Object()
			self.animation = None
		
		def __str__(self):
			return str(self.name)
		
		def __call__(self, text):
			show_text(self.name, self.name_prefix, self.name_postfix, self.color,
			          text, self.text_prefix, self.text_postfix, self.text_color)
		
		
		#rpg-funcs:
		
		def make_rpg(self, directory, rpg_name, start_dress):
			self.directory = directory + ('' if directory.endswith('/') else '/')
			self.rpg_name = rpg_name
			self.set_dress(start_dress)
		
		def set_dress(self, dress):
			self.dress = dress
		def set_frame(self, frame):
			self.frame = frame
		def set_direction(self, direction):
			self.direction = direction % character_max_direction
		
		def main(self):
			if self.animation_start_time is not None:
				return get_location_image(self.animation, self.animation.path, '', '', character_ext, False)
			return get_location_image(self, self.directory, self.rpg_name, self.dress, character_ext, False)
		
		def set_pose(self, pose):
			if pose == 'sit' or pose == 'stance':
				self.pose = pose
				if pose == 'stance':
					self.move_kind = 'stay'
			else:
				self.pose, self.move_kind = 'stance', 'stay'
				out_msg('Character.set_pose', 'Unexpected pose <' + str(pose) + '>\n' + 'Expected "sit" or "stance"')
		
		def update_crop(self):
			frame = self.frame
			if self.animation_start_time is None:
				if self.pose == 'sit':
					frame = character_max_frame
				elif self.move_kind == 'stay':
					frame = character_max_frame - 1
				else:
					 frame %= character_max_frame
				
				y = self.direction * self.ysize
			else:
				y = 0
			x = frame * self.xsize
			
			self.crop = (x, y, self.xsize, self.ysize)
		
		def to_next_place(self):
			if not self.place_names:
				return
			
			place_name = self.place_names[self.place_index]
			place = self.place = self.location.get_place(place_name)
			if not place:
				out_msg('Character.to_next_place', 'Place <' + str(place_name) + '> not found in location <' + self.location.name + '>')
				return
			
			self.moving_start_time = time.time()
			
			self.from_x, self.from_y = int(self.x), int(self.y)
			self.to_x, self.to_y = get_place_center(place)
			self.dx, self.dy = self.to_x - self.from_x, self.to_y - self.from_y
			
			if self.dx == 0 and self.dy == 0:
				self.place_index += 1
				if self.place_index < len(self.place_names):
					self.to_next_place()
				return
			
			def direction_from_d(dx, dy):
				if abs(dx) > abs(dy):
					return to_left if dx < 0 else to_right
				return  to_forward if dy < 0 else to_back
			direction = direction_from_d(self.dx, self.dy)
			self.set_direction(direction)
			
			acceleration_path = self.acceleration * (character_acceleration_time ** 2) / 2 # s = (at^2) / 2
			
			self.dist = get_dist(self.from_x, self.from_y, self.to_x, self.to_y)
			if acceleration_path > self.dist / 2:
				self.acceleration_time = (2 * (self.dist / 2) / self.acceleration) ** 0.5 # t = sqrt(2s / a)
				self.no_acceleration_time = 0
				self.moving_full_time = self.acceleration_time * 2
			else:
				self.acceleration_time = character_acceleration_time
				no_acceleration_path = self.dist - acceleration_path * 2
				self.no_acceleration_time = no_acceleration_path / float(self.speed) # t = s / v (if a == 0)
				self.moving_full_time = self.no_acceleration_time + character_acceleration_time * 2
			
			size = len(self.place_names)
			self.place_index = (self.place_index + 1) % size
			
			if self.place_index == 0:
				self.place_names = None
			elif self.place_index == size - 1:
				place_name = self.place_names[self.place_index]
				if type(place_name) is int:
					if place_name < 0:
						place_name -= 1
					self.place_index = place_name
		
		def move_to_place(self, place_names, run = False, exec_stop_time = -1):
			if not self.location:
				out_msg('Character.to_next_place', 'Character there is not in some location')
				return
			
			if type(place_names) not in (list, tuple):
				place_names = [place_names]
			self.place_index = 0
			self.place_names = place_names
			
			self.moving_ended = False
			
			self.move_kind = 'run' if run else 'walk'
			g = globals()
			for prop in ('fps', 'speed', 'acceleration'):
				self[prop] = g['character_' + self.move_kind + '_' + prop] # for example: self.fps = character_run_fps
			
			self.to_next_place()
			
			if exec_stop_time >= 0:
				self.end_stop_time = time.time() + exec_stop_time
			else:
				self.end_stop_time = None
		
		def move_to_end(self):
			if self.end_stop_time:
				self.moving_start_time -= self.end_stop_time - self.moving_start_time
				self.end_stop_time = time.time()
			elif not (self.place_names and type(self.place_names[-1]) is int): # not cycled path
				self.moving_start_time = 0
				self.update()
		
		def ended_move_waiting(self):
			if self.end_stop_time:
				return self.end_stop_time < time.time()
			if self.place_names and type(self.place_names[-1]) is int: # cycled path
				return True
			return self.moving_ended
		
		def start_animation(self, anim_name, repeat = 0):
			if not self.animations.has_key(anim_name):
				out_msg('start_animation', 'Animation <' + str(anim_name) + '> not found in character <' + str(self) + '>')
				return
			
			animation = self.animation = self.animations[anim_name]
			animation.first_update = True
			
			self.xoffset, self.yoffset = animation.xoffset, animation.yoffset
			
			self.animation_start_time = time.time()
			self.repeat = int(repeat)
		
		def remove_animation(self):
			self.animation_start_time = None
			self.xoffset, self.yoffset = 0, 0
			self.xsize, self.ysize = character_xsize, character_ysize
		
		def anim_to_end(self):
			self.remove_animation()
		
		def ended_anim_waiting(self):
			if self.repeat < 0 or self.animation_start_time is None:
				return True
			if self.repeat > 0:
				return False
			return time.time() - self.animation_start_time > self.animation.time
		
		def update(self):
			moving_dtime = time.time() - self.moving_start_time
			
			if self.animation_start_time is None:
				self.set_frame(int(moving_dtime * self.fps))
			else:
				animation = self.animation
				dtime = time.time() - self.animation_start_time
				
				time_k = 1
				if animation.time > 0:
					if dtime > animation.time:
						if self.repeat:
							self.animation_start_time = time.time()
							time_k = 0
						if self.repeat > 0:
							self.repeat -= 1
					else:
						time_k = dtime / animation.time
				
				if animation.first_update:
					animation.first_update = False
					
					if not animation.loaded:
						animation.loaded = True
						animation.xsize, animation.ysize = get_image_size(self.main())
						animation.xsize = int(math.ceil(animation.xsize / animation.count_frames))
					
					self.xsize, self.ysize = animation.xsize, animation.ysize
				
				start_frame = animation.start_frame
				end_frame = animation.end_frame
				if end_frame < start_frame:
					frame = start_frame - int((start_frame - end_frame + 1) * time_k)
					frame = in_bounds(frame, end_frame, start_frame)
				else:
					frame = start_frame + int((end_frame - start_frame + 1) * time_k)
					frame = in_bounds(frame, start_frame, end_frame)
				
				self.set_frame(frame)
			
			self.update_crop()
			
			if self.pose == 'sit' or self.move_kind == 'stay':
				return
			if self.x == self.to_x and self.y == self.to_y:
				return
			
			# save before self.to_next_place()
			from_x, from_y = self.from_x, self.from_y
			dx, dy = self.dx, self.dy
			dist = self.dist
			
			if moving_dtime < self.acceleration_time:                               # acceleration, s = a*(t^2)/2
				cur_dist = self.acceleration * (moving_dtime ** 2) / 2
			elif moving_dtime < self.acceleration_time + self.no_acceleration_time: # usual moving, s = a*(t^2)/2 + v*t
				cur_dist = self.acceleration * (self.acceleration_time ** 2) / 2 + self.speed * (moving_dtime - self.acceleration_time)
			elif moving_dtime < self.moving_full_time:                              # deceleration, s = full_s - a*((full_t-t)^2)/2
				cur_dist = self.dist - self.acceleration * ((self.moving_full_time - moving_dtime) ** 2) / 2
			else:                                                                   # end, stop,    s = full_s
				cur_dist = self.dist
				
				next_cycle = self.place_names is not None
				if not next_cycle:
					self.move_kind = 'stay'
					self.moving_ended = True
				else:
					self.to_next_place()
			
			self.x = from_x + dx * cur_dist / dist
			self.y = from_y + dy * cur_dist / dist
	
	
	def set_name(who, name):
		g = globals()
		if g.has_key(who):
			g[who].name = name
		else:
			out_msg('set_name', 'Character <' + who + '> not found')
	meet = set_name
	
	def make_names_unknown():
		for character in characters:
			character.name = character.unknown_name
	def make_names_known():
		for character in characters:
			character.name = character.real_name
	
	
	
	def show_character(character, place, location = None):
		if location is None:
			if cur_location is None:
				out_msg('show_character', 'Current location is not defined, need to call set_location')
				return
			location = cur_location
		elif type(location) is str:
			if not locations.has_key(location):
				out_msg('show_character', 'Location <' + location + '> not registered')
				return
			location = locations[location]
		
		if type(place) is str:
			place_name = place
			place = location.get_place(place)
			if not place:
				out_msg('show_character', 'Place <' + place_name + '> not found in location <' + str(location.name) + '>')
				return
		
		if character.location:
			character.location.objects.remove(character)
		
		character.location = location
		location.objects.append(character)
		
		character.x, character.y = get_place_center(place)
		character.place_names = None
	
	def hide_character(character):
		if character.location:
			character.location.objects.remove(character)
			character.location = None
		else:
			out_msg('hide_character', 'Character <' + character.real_name + ', ' + character.unknow_name + '> not shown')
	
	
	tmp_character = Character('TMP', color = 0xFFFFFF)
	
	narrator = Character('')
	th = Character('', text_prefix='~', text_postfix='~')
	extend = Character(None)

