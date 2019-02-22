init -1001 python:
	
	character_ext = 'png'
	
	
	character_walk_fps          =   4
	character_run_fps           =  12
	character_acceleration_time = 0.5
	character_walk_speed        =  50
	character_run_speed         = 150*5
	
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
	
	character_skip_start_time = None
	character_skip_acceleration = 5
	def character_accelerate():
		now = time.time()
		for obj in objects_on_location:
			if isinstance(obj, Character):
				last_start = obj.start_skip_times[-1] if obj.start_skip_times else None
				last_stop = obj.stop_skip_times[-1] if obj.stop_skip_times else None
				if last_start is None or last_start < last_stop:
					obj.start_skip_times.append(now)
	def character_unaccelerate():
		now = time.time()
		for obj in objects_on_location:
			if isinstance(obj, Character):
				last_start = obj.start_skip_times[-1] if obj.start_skip_times else None
				last_stop = obj.stop_skip_times[-1] if obj.stop_skip_times else None
				if last_start is not None and (last_stop is None or last_start > last_stop):
					obj.stop_skip_times.append(now)
	
	
	characters = []
	class Character(Object):
		def __init__(self, name, **kwargs):
			Object.__init__(self)
			characters.append(self)
			
			self.xanchor, self.yanchor = 0.5, 0.8
			self.xsize, self.ysize = character_xsize, character_ysize
			
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
			
			self.moving_start_time = time.time()
			self.start_skip_times = []
			self.stop_skip_times = []
			
			self.end_stop_time = None
			self.end_moved = True
			
			self.x, self.y = 0, 0
			self.crop = (0, 0, character_xsize, character_ysize)
			
			self.location = None
			self.to_places = []
			self.place_index = 0
		
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
			self.frame = frame % character_max_frame
		def set_direction(self, direction):
			self.direction = direction % character_max_direction
		
		def main(self):
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
			if self.pose == 'sit':
				frame = character_max_frame
			elif self.move_kind == 'stay':
				frame = character_max_frame - 1
			
			x = frame * character_xsize
			y = self.direction * character_ysize
			
			self.crop = (x, y, character_xsize, character_ysize)
		
		def to_next_place(self):
			if not self.place_names:
				return
			
			if not cur_location_name:
				out_msg('Character.next_index', 'Current location is not defined, need to call set_location')
				return
			
			place_name = self.place_names[self.place_index]
			place = cur_location.get_place(place_name)
			if not place:
				out_msg('Character.next_index', 'Place <' + str(place_name) + '> not found in location <' + cur_location_name + '>')
				return
			
			character_unaccelerate()
			self.moving_start_time = time.time()
			self.start_skip_times = []
			self.stop_skip_times = []
			
			self.from_x, self.from_y = int(self.x), int(self.y)
			self.to_x, self.to_y = int(place.x + place.width / 2), int(place.y + place.height / 2)
			self.dx, self.dy = self.to_x - self.from_x, self.to_y - self.from_y
			
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
			if type(place_names) not in (list, tuple):
				place_names = [place_names]
			self.place_index = 0
			self.place_names = place_names
			
			self.end_moved = False
			
			self.move_kind = 'run' if run else 'walk'
			g = globals()
			for prop in ('fps', 'speed', 'acceleration'):
				self[prop] = g['character_' + self.move_kind + '_' + prop] # for example: self.fps = character_run_fps
			
			self.to_next_place()
			
			if exec_stop_time >= 0:
				self.end_stop_time = time.time() + exec_stop_time
			else:
				self.end_stop_time = None
		
		def moved(self):
			if self.end_stop_time is None:
				return self.end_moved
			return self.end_stop_time < time.time()
		
		def update(self):
			self.update_crop()
			if self.pose == 'sit' or self.move_kind == 'stay':
				return
			
			usual_time = 0
			skip_time = 0
			
			now = time.time()
			
			if self.start_skip_times and not control:
				stop_skip_times  = [self.moving_start_time] + self.stop_skip_times + [now]
				start_skip_times = self.start_skip_times + [now]
				for i in xrange(len(stop_skip_times) - 1):
					usual_time += start_skip_times[i] - stop_skip_times[i]
					skip_time += stop_skip_times[i + 1] - start_skip_times[i]
			else:
				usual_time = now - self.moving_start_time
			
			moving_dtime = usual_time + skip_time * character_skip_acceleration
			self.set_frame(int(moving_dtime * self.fps))
			
			if self.x == self.to_x and self.y == self.to_y:
				return
			
			# save before self.to_next_place()
			from_x, from_y = self.from_x, self.from_y
			dx, dy = self.dx, self.dy
			dist = self.dist
			
			if moving_dtime < self.acceleration_time:                               # acceleration, s = a*(t^2)/2
				cur_dist = self.acceleration * (moving_dtime ** 2) / 2
			elif moving_dtime < self.acceleration_time + self.no_acceleration_time: # usual moving, s = a*(at^2)/2 + v*t
				cur_dist = self.acceleration * (self.acceleration_time ** 2) / 2 + self.speed * (moving_dtime - self.acceleration_time)
			elif moving_dtime < self.moving_full_time:                              # deceleration, s = full_s - a*((full_t-t)^2)/2
				cur_dist = self.dist - self.acceleration * ((self.moving_full_time - moving_dtime) ** 2) / 2
			else:                                                                   # end, stop,    s = full_s
				cur_dist = self.dist
				
				next_cycle = self.place_names is not None
				if not next_cycle:
					self.move_kind = 'stay'
					self.end_moved = True
					character_unaccelerate()
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
	
	
	
	def show_character(character, place):
		if not character:
			out_msg('show_character', 'character == None')
			return
		if not cur_location_name:
			out_msg('show_character', 'Current location is not defined, need to call set_location')
			return
		if type(place) is not dict:
			place = cur_location.get_place(place)
		if not place:
			out_msg('show_character', 'Place <' + str(place_name) + '> not found in location <' + cur_location_name + '>')
			return
		
		character.x, character.y = place['x'] + place['width'] / 2, place['y'] + place['height'] / 2
		objects_on_location.append(character)
	
	def hide_character(character):
		if not character:
			out_msg('hide_character', 'character == None')
			return
		
		if character in objects_on_location:
			objects_on_location.remove(character)
		else:
			out_msg('hide_character', 'Character <' + character.real_name + ', ' + character.unknow_name + '> not shown')
	
	
	tmp_character = Character('TMP', color = 0xFFFFFF)
	
	narrator = Character('')
	th = Character('', text_prefix='~', text_postfix='~')
	extend = Character(None)

