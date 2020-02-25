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
			
			self.prev_update_time = time.time()
			self.moving_ended = True
			
			self.x, self.y = 0, 0
			self.xoffset, self.yoffset = 0, 0
			
			self.xanchor, self.yanchor = 0.5, 0.8
			self.xsize, self.ysize = character_xsize, character_ysize
			self.crop = (0, 0, self.xsize, self.ysize)
			
			self.location = None
			self.to_places = []
			self.place_index = 0
			
			self.animations = Object()
			self.animation = None
			self.start_anim_time = None
			self.end_wait_anim_time = None
		
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
			if direction is not None:
				self.direction = direction % character_max_direction
		
		def main(self):
			if self.start_anim_time is not None:
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
			if self.start_anim_time is None:
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
		
		
		def move_to_place(self, place_names, run = False, wait_time = -1, brute_force = False):
			if self.location is None:
				out_msg('Character.move_to_place', 'Character.location is None')
				return
			
			if self is me:
				ignore_prev_rpg_control()
				set_rpg_control(False)
			
			path_update_locations()
			
			if isinstance(place_names, tuple):
				place_names = list(place_names)
			elif not isinstance(place_names, list):
				place_names = [place_names]
			
			self.paths = []
			self.paths_index = 0
			self.point_index = 0
			
			from_location_name = self.location.name
			from_x, from_y = self.x, self.y
			for i in xrange(len(place_names)):
				place_elem = place_names[i]
				
				if i == len(place_names) - 1 and type(place_elem) is int: # last and int
					place_names.insert(place_names[place_elem], -1)
					break
				
				if isinstance(place_elem, (list, tuple)):
					location_name, place_elem = place_elem
				else:
					location_name = from_location_name
				
				location = locations.get(location_name, None)
				if not location:
					out_msg('Character.move_to_place', 'Location <' + str(location_name) + '> is not registered')
					return
				
				if type(place_elem) is str:
					place = location.places.get(place_elem, None)
					if place is None:
						out_msg('Character.move_to_place', 'Place <' + str(place_elem) + '> in location <' + location_name + '> not found')
						return
				else:
					place = place_elem
				
				to_x, to_y = get_place_center(place)
				path = path_between_locations(from_location_name, from_x, from_y, location_name, to_x, to_y, brute_force)
				if not path:
					self.paths = []
					return
				self.paths.append(path)
				
				from_location_name = location_name
				from_x, from_y = to_x, to_y
			
			
			self.moving_ended = False
			
			self.move_kind = 'run' if run else 'walk'
			g = globals()
			for prop in ('fps', 'speed', 'acceleration'):
				self[prop] = g['character_' + self.move_kind + '_' + prop] # for example: self.fps = character_run_fps
			
			if wait_time >= 0:
				self.end_stop_time = time.time() + wait_time
			else:
				self.end_stop_time = None
		
		def move_to_end(self):
			if self.end_stop_time:
				self.end_stop_time = time.time()
		
		def ended_move_waiting(self):
			if self.end_stop_time:
				return self.end_stop_time < time.time()
			if self.paths and type(self.paths[-1]) is int: # cycled path
				return True
			return self.moving_ended
		
		def start_animation(self, anim_name, repeat = 0, wait_time = -1):
			if not self.animations.has_key(anim_name):
				out_msg('start_animation', 'Animation <' + str(anim_name) + '> not found in character <' + str(self) + '>')
				return
			
			animation = self.animation = self.animations[anim_name]
			animation.first_update = True
			
			self.xoffset, self.yoffset = animation.xoffset, animation.yoffset
			
			self.start_anim_time = time.time()
			self.repeat = int(repeat)
			
			if wait_time >= 0:
				self.end_wait_anim_time = time.time() + wait_time
			else:
				self.end_wait_anim_time = None
		
		def remove_animation(self):
			self.start_anim_time = None
			self.end_wait_anim_time = None
			self.xoffset, self.yoffset = 0, 0
			self.xsize, self.ysize = character_xsize, character_ysize
		
		def anim_to_end(self):
			self.remove_animation()
		
		def ended_anim_waiting(self):
			if self.repeat < 0 or self.start_anim_time is None:
				return True
			if self.end_wait_anim_time is not None and self.end_wait_anim_time < time.time():
				return True
			
			if self.repeat > 0:
				return False
			return time.time() - self.start_anim_time > self.animation.time
		
		def update(self):
			dtime = time.time() - self.prev_update_time
			self.prev_update_time = time.time()
			
			if self.start_anim_time is None:
				self.set_frame(int(time.time() * self.fps))
			else:
				animation = self.animation
				dtime = time.time() - self.start_anim_time
				
				time_k = 1
				if animation.time > 0:
					if dtime > animation.time:
						if self.repeat:
							self.start_anim_time = time.time()
							time_k = 0
						else:
							self.remove_animation()
						
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
			if not self.paths:
				self.move_kind = 'stay'
				self.moving_ended = True
				return
			
			path = self.paths[self.paths_index]
			while True:
				to_x, to_y = path[self.point_index], path[self.point_index + 1]
				
				if type(to_x) is str:
					location_name, place_name = to_x, to_y
					show_character(self, place_name, location_name)
					continue
				
				dx = to_x - self.x
				dy = to_y - self.y
				
				if not (dx and dy) or self.point_index == 0: # not diagonal or first step
					if abs(dx) > abs(dy):
						self.set_direction(to_left if dx < 0 else to_right)
					else:
						self.set_direction(to_forward if dy < 0 else to_back)
					self.update_crop()
				
				need_dist = math.sqrt(dx*dx + dy*dy)
				need_time = need_dist / self.speed
				
				if need_time < dtime:
					self.x, self.y = to_x, to_y
					dtime -= need_time
					
					self.point_index += 2
					if self.point_index == len(path):
						self.point_index = 0
						
						self.paths_index += 1
						if self.paths_index == len(self.paths):
							self.paths = []
							self.x, self.y = to_x, to_y
							break
						
						path = self.paths[self.paths_index]
						if type(path) is int:
							if path < 0:
								path -= 1
							self.paths_index = path
							path = self.paths[self.paths_index]
				else:
					self.x += dx * dtime / need_time
					self.y += dy * dtime / need_time
					break
	
	
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

