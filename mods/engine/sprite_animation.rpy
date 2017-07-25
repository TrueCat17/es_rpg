init -9000 python:
	
	def linear(t):
		return t
	def ease(t):
		return 0.5 - math.cos(math.pi * t) / 2.0
	def easein(t):
		return math.cos((1.0 - t) * math.pi / 2.0)
	def easeout(t):
		return 1.0 - math.cos(t * math.pi / 2.0)
	
	
	atl_props = (
		('xpos', 'ypos', 'pos'),
		('xanchor', 'yanchor', 'anchor'),
		('xalign', 'yalign', 'align'),
		('xsize', 'ysize', 'xysize'),
		('xcrop', 'ycrop', 'xsizecrop', 'ysizecrop', 'crop'),
		('alpha'),
		('rotate')
	)
	
	# alpha -> [alpha]
	# xpos  -> [xpos]
	#  pos  -> [xpos, ypos]
	def get_atl_props(prop):
		for props in atl_props:
			if prop in props:
				if len(props) == 1 or props[-1] != prop:
					return [prop]
				return props[0:-1]
		return None
	
	
	
	class SpriteAnimation(Object):
		def __init__(self, actions, spr = None):
			Object.__init__(self)
			
			self.ended = False
			self.repeated = {}
			
			self.action_num = 0
			self.actions = actions
			self.last_command = ''
			
			self.block = None
			self.parallels = []
			
			self.sprite = spr
			self.data = spr.new_data if spr else None
			
			self.end_pause_time = 0
			
			self.start_changing_time = 0
			self.end_changing_time = 0
		
		
		def copy(self):
			return SpriteAnimation(self.actions)
		
		
		def update(self):
			now = time.time()
			
			if now < self.end_pause_time:
				return
			
			
			if self.start_changing_time:
				self.update_changing()
				if now <= self.end_changing_time:
					return
				else:
					self.start_changing_time = 0
			
			
			if self.block:
				self.block.update()
				if self.block.ended:
					self.block = None
				
				return
			
			
			if self.parallels:
				for parallel in self.parallels:
					parallel.update()
				
				for parallel in self.parallels:
					if not parallel.ended:
						break
				else:
					self.parallels = []
				
				return
			
			
			if self.action_num >= len(self.actions):
				self.ended = True
				return
			
			
			
			while self.action_num < len(self.actions):
				action = ''
				while not action and self.action_num < len(self.actions):
					action = self.actions[self.action_num]
					self.action_num += 1
				
				if not action:
					return
				
				if type(action) is str:
					if self.parallels:
						self.action_num -= 1
						return
					
					args = get_args(action)
					if len(args) == 0:
						continue
				
					command = args[0]
					self.last_command = command
					
					if command == 'pause':
						if len(args) == 2:
							self.end_pause_time = time.time() + float(args[1])
						else:
							out_msg('SpriteAnimation.update', 'pause ожидает 1 аргумент: время\n' + action)
						return
					elif command == 'repeat':
						if len(args) > 2:
							out_msg('SpriteAnimation.update', 'repeat ожидает 1 необязательный аргумент: количество повторов\n' + action)
						
						count = int(10e9) if len(args) == 1 else int(args[1])
						num = self.action_num - 1
						repeated = self.repeated.get(num, 0)
						
						if repeated < count:
							self.action_num = 0
							self.repeated[num] = self.repeated.get(num, 0) + 1
							
							for key in self.repeated.keys():
								if key < num:
									self.repeated[key] = 0
							
							return
					else:
						is_prop = get_atl_props(command) is not None
						if is_prop:
							if len(args) % 2:
								out_msg('SpriteAnimation.update', 'Ожидалось чётное количество аргументов: [параметр значение]+\n' + action)
							else:
								for i in xrange(0, len(args), 2):
									self.set_prop(args[i], eval(args[i + 1]))
						else:
							try:
								evaled = eval(action)
								if isinstance(evaled, str):
									if image_was_registered(evaled):
										image_actions = get_image(evaled)
										self.action_num -= 1
										self.actions = self.actions[0:self.action_num] + image_actions + self.actions[self.action_num+1:]
									else:
										self.data.contains = []
										self.data.image = evaled
								elif isinstance(evaled, int) or isinstance(evaled, float):
									self.end_pause_time = time.time() + float(evaled)
								else:
									out_msg('SpriteAnimation.update', 'Unknown command:\n' + action)
							except:
								try:
									evaled = eval(command)
									if str(type(evaled)) == "<type 'function'>":
										if len(args) % 2:
											desc = command + ' ожидает нечётное количество аргументов: время, [параметр значение]+\n' + action
											out_msg('SpriteAnimation.update', desc)
										else:
											self.change_func = evaled
											self.start_changing_time = time.time()
											self.end_changing_time = time.time() + float(args[1])
											self.save_change_params(args[2:])
										return
									else:
										out_msg('SpriteAnimation.update', 'Unknown command:\n' + action)
								except:
									out_msg('SpriteAnimation.update', 'Exception:\n' + action)
				elif type(action) is list:
					if ' ' in action[0]:
						index = action[0].index(' ')
						command = action[0][0:index]
						extra_param = action[0][index+1:]
						action = [command] + [extra_param] + [action[1:]]
					else:
						command = action[0]
						extra_param = str(self.sprite) + ': ' + command + '_' + str(self.action_num)
					
					
					if self.parallels and command != 'parallel':
						self.action_num -= 1
						return
					
					
					if command == 'contains':
						if self.last_command != command:
							self.data.contains = []
						spr = Sprite([], [], action[1:], None)
						spr.call_str = extra_param
						self.data.contains.append(spr)
					elif command == 'block':
						self.block = SpriteAnimation(action[1:], self.sprite)
						return
					elif command == 'parallel':
						if self.last_command != command:
							self.parallels = []
						self.parallels.append(SpriteAnimation(action[1:], self.sprite))
					else:
						out_msg('SpriteAnimation.update', 'Ожидались блоки <contains>, <block> или <parallel>, получен <' + str(action[0]) + '>')
					
					self.last_command = command
				else:
					out_msg('SpriteAnimation.update', 'Command type is not str or list:\n' + type(action) + '\n' + str(action))
		
		def save_change_params(self, args):
			self.change_props = []
			
			for i in xrange(0, len(args), 2):
				names = self.get_prop_names(args[i])
				
				if isinstance(names, list) or isinstance(names, tuple):
					new_value = eval(args[i + 1])
					if not isinstance(new_value, list) and not isinstance(new_value, tuple):
						new_value = [new_value] * len(names)
					old_value = [self.data[name] for name in names]
				else:
					new_value = eval(args[i + 1])
					old_value = self.data[names]
				
				self.change_props.append((names, old_value, new_value))
		
		def update_changing(self):
			now = time.time()
			dtime = now - self.start_changing_time
			all_time = max(self.end_changing_time - self.start_changing_time, 0.001)
			
			t = in_bounds(dtime / all_time, 0.0, 1.0)
			t = in_bounds(self.change_func(t), 0.0, 1.0)
			for prop in self.change_props:
				name, old_value, new_value = prop
				
				if isinstance(new_value, list) or isinstance(new_value, tuple):
					value = []
					for i in xrange(len(old_value)):
						new_v = new_value[i]
						old_v = old_value[i]
						type_v = type(new_v)
						v = type_v((new_v - old_v) * t + old_v)
						value.append(v)
				else:
					type_v = type(new_value)
					value = type_v((new_value - old_value) * t + old_value)
				self.set_prop(name, value)
		
		
		def get_prop_names(self, prop):
			props = get_atl_props(prop)
			
			if len(props) == 1:
				if prop == 'xalign':
					return ['xpos', 'xanchor']
				if prop == 'yalign':
					return ['ypos', 'yanchor']
				return prop
			return props
		
		def set_prop(self, prop, value):
			if isinstance(prop, str):
				props = get_atl_props(prop)
			else:
				props = prop
			
			if props == ['xalign']:
				self.data.xalign = value
				props = ['xpos', 'xanchor']
				value = [value] * 2
			elif props == ['yalign']:
				self.data.yalign = value
				props = ['ypos', 'yanchor']
				value = [value] * 2
			
			if len(props) == 1:
				self.data[prop] = value
			else:
				if (not isinstance(value, list) and not isinstance(value, tuple)) or len(props) != len(value):
					out_msg('SpriteAnimation.set_prop',
							'Значением ожидался список из ' + str(len(props)) + ' элементов, получено: <' +str(value)+ '>')
				else:
					for i in xrange(len(props)):
						self.set_prop(props[i], value[i])
	
	
	
	
	
	def get_sprite_place(xpos, ypos, xanchor, yanchor):
		actions = (
			'pos ' + str((xpos, ypos)),
			'anchor ' + str((xanchor, yanchor))
		)
		
		res = SpriteAnimation(actions)
		return res
	
	fleft  = get_sprite_place(0.16,  1.0, 0.5, 1.0)
	left   = get_sprite_place(0.28,  1.0, 0.5, 1.0)
	cleft  = get_sprite_place(0.355, 1.0, 0.5, 1.0)
	center = get_sprite_place(0.50,  1.0, 0.5, 1.0)
	cright = get_sprite_place(0.645, 1.0, 0.5, 1.0)
	right  = get_sprite_place(0.72,  1.0, 0.5, 1.0)
	fright = get_sprite_place(0.84,  1.0, 0.5, 1.0)
	
	true_center = get_sprite_place(0.5, 0.5, 0.5, 0.5)
	
