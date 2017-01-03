init -1001 python:
	character_walk_fps =               get_from_hard_config('character_walk_fps', int)
	character_run_fps =                get_from_hard_config('character_run_fps', int)
	character_acceleration_time =      get_from_hard_config('character_acceleration_time', float)
	character_walk_speed =             get_from_hard_config('character_walk_speed', int)
	character_run_speed =              get_from_hard_config('character_run_speed', int)
	
	character_walk_acceleration = character_walk_speed / character_acceleration_time
	character_run_acceleration = character_run_speed / character_acceleration_time
	
	
	character_max_frame = 4
	character_max_direction = 4
	
	character_xsize = 48
	character_ysize = 96
	
	
	character_moving = False
	
	characters = []
	class Character(Object):
		def __init__(self, name, **kwargs):
			Object.__init__(self)
			characters.append(self)
			
			self.xanchor, self.yanchor = 0.5, 0.8
			self.width, self.height = character_xsize, character_ysize
			
			self.real_name = name
			self.unknow_name = kwargs.get('unknow_name', name)
			
			self.name = name
			self.name_prefix = kwargs.get('name_prefix', '')
			self.name_postfix = kwargs.get('name_postfix', '')
			self.color = kwargs.get('color', 0)
			
			self.text_prefix = kwargs.get('text_prefix', '')
			self.text_postfix = kwargs.get('text_postfix', '')
			self.text_color = kwargs.get('text_color', 0xFFFF00)
			
			# rpg-props:
			self.prefix_path_to_image = None
			self.dress = None
			
			self.frame = 0
			self.direction = 0
			self.pose = 'stance' # 'stance' | 'sit'
			self.move_kind = 'stay' # 'stay' | 'walk' | 'run'
			
			self.location = None
		
		def __call__(self, text):
			show_text(	self.name, self.name_prefix, self.name_postfix, self.color,
						text, self.text_prefix, self.text_postfix, self.text_color)
		
		
		#rpg-funcs:
		
		def make_rpg(self, prefix_path_to_image, default_dress):
			self.prefix_path_to_image = prefix_path_to_image
			self.dress = default_dress
		
		def set_dress(self, dress):
			self.dress = dress
		
		
		def set_frame(self, frame):
			self.frame = frame % character_max_frame
		
		def set_direction(self, direction):
			self.direction = direction % character_max_direction
		
		def set_pose(self, pose):
			if pose == 'sit' or pose == 'stance':
				self.pose = pose
				if pose == 'stance':
					self.move_kind = 'stay'
			else:
				self.pose, self.move_kind = 'stance', 'stay'
				out_msg('Character.set_pose', 'Неожидаемое значение параметра pose <' + str(pose) + '>\n' + 'Ожидалось "sit" или "stance"')
		
		def get_current_image(self):
			frame = self.frame
			if self.pose == 'sit':
				frame = character_max_frame
			elif self.move_kind == 'stay':
				frame = character_max_frame - 1
			
			x = frame * character_xsize
			y = self.direction * character_ysize
			
			image = self.prefix_path_to_image + self.dress + '.png'
			res = im.Crop(image, (x, y, character_xsize, character_ysize))
			return res
		
		def move_to_place(self, place_name, run = False):
			if not cur_location_name:
				out_msg('Character.move_to_place', 'Текущая локация не установлена, сначала следует вызвать set_location')
				return
			place = cur_location.get_place(place_name)
			if not place:
				out_msg('Character.move_to_place', 'В локации <' + cur_location_name + '> нет места с именем <' + place_name + '>')
				return
			
			global character_moving
			character_moving = True
			
			self.moving_start_time = time.time()
			
			self.pose = 'stance'
			self.move_kind = 'run' if run else 'walk'
			self.fps = character_run_fps if run else character_walk_fps
			self.from_x, self.from_y = self.x, self.y
			self.to_x, self.to_y = place.x, place.y
			self.dx, self.dy = self.to_x - self.from_x, self.to_y - self.from_y
			
			self.speed = character_run_speed if run else character_walk_speed
			self.acceleration = character_run_acceleration if run else character_walk_acceleration
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
		
		def update(self):
			self.image = self.get_current_image()
			if self.pose == 'sit' or self.move_kind == 'stay':
				return
			
			moving_dtime = time.time() - self.moving_start_time
			self.set_frame(int(moving_dtime * self.fps))
			
			if moving_dtime < self.acceleration_time:                               # Ещё не разогнались
				cur_dist = self.acceleration * (moving_dtime ** 2) / 2
			elif moving_dtime < self.acceleration_time + self.no_acceleration_time: # Ещё не тормозим
				cur_dist = self.acceleration * (self.acceleration_time ** 2) / 2 + self.speed * (moving_dtime - self.acceleration_time)
			elif moving_dtime < self.moving_full_time:                              # Ещё не пришли
				cur_dist = self.dist - (self.acceleration * (self.moving_full_time - moving_dtime) ** 2) / 2
			else:                                                                   # Всё, остановка
				cur_dist = self.dist
				
				global character_moving
				character_moving = False
				self.move_kind = 'stay'
			
			self.x = self.from_x + self.dx * cur_dist / self.dist
			self.y = self.from_y + self.dy * cur_dist / self.dist
	
	
	def set_name(who, name):
		g = globals()
		if g.has_key(who):
			g[who].name = name
		else:
			out_msg('set_name', 'Персонаж <' + who + '> не найден')
	meet = set_name
	
	def make_names_unknown():
		for character in characters:
			character.name = character.unknow_name
    def make_names_known():
    	for character in characters:
    		character.name = character.real_name
    
