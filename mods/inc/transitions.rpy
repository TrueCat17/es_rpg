init -1001 python:
	
	def linear(t):
		return t
	def ease(t):
		return 0.5 - math.cos(math.pi * t) / 2.0
	def easein(t):
		return math.cos((1.0 - t) * math.pi / 2.0)
	def easeout(t):
		return 1.0 - math.cos(t * math.pi / 2.0)
	
	
	transition_changing_commands = ('linear', 'ease', 'easein', 'easeout')
	
	transition_props = (
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
	def get_transition_props(prop):
		for props in transition_props:
			if prop in props:
				if len(props) == 1 or props[-1] != prop:
					return [prop]
				return props[0:-1]
		return None
	
	
	class Transform(Object):
		def __init__(self):
			Object.__init__(self)
		
		def get_all_transforms(self):
			sw, sh = get_stage_width(), get_stage_height()
			
			self.real_xpos    = get_absolute(self.xpos, sw)
			self.real_ypos    = get_absolute(self.ypos, sh)
			self.real_xanchor = get_absolute(self.xanchor, self.real_xsize)
			self.real_yanchor = get_absolute(self.yanchor, self.real_ysize)
			self.real_alpha   = self.alpha
			self.real_rotate  = self.rotate
			
			res = [self]
			
			for spr in self.contains:
				for spr_trans in spr.new_old_ordered:
					for trans in spr_trans.get_all_transforms():
						trans.real_xpos    += self.real_xpos
						trans.real_ypos    += self.real_ypos
						trans.real_xanchor += self.real_xanchor
						trans.real_yanchor += self.real_yanchor
						trans.real_alpha   *= self.real_alpha
						trans.real_rotate  += self.real_rotate
						res.append(trans)
			
			return res
	
	def get_inited_transform():
		res = Transform()
		res.xpos, res.ypos = 0, 0
		res.xanchor, res.yanchor = 0, 0
		res.xsize, res.ysize = None, None
		res.xcrop, res.ycrop, res.xsizecrop, res.ysizecrop = 0, 0, 1.0, 1.0
		res.alpha = 1.0
		res.rotate = 0
	
		res.end_pause_time = 0
	
		res.start_changing_time = 0
		res.end_changing_time = 0
	
		res.contains = []
		res.image = None
		return res
	
	
	class Transition(Object):
		def __init__(self, actions, spr = None):
			Object.__init__(self)
			
			self.action_num = 0
			self.actions = actions
			self.last_command = ''
			
			self.sprite = spr
		
		def copy(self):
			return Transition(self.actions)
		
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
			
			if self.action_num >= len(self.actions):
				return
			
			
			while self.action_num < len(self.actions):
				action = ''
				while not action and self.action_num < len(self.actions):
					action = self.actions[self.action_num]
					self.action_num += 1
				
				if not action:
					return
				
				if type(action) is str:
					args = get_args(action)
					if len(args) == 0:
						continue
				
					command = args[0]
					self.last_command = command
					
					if command == 'pause':
						if len(args) == 2:
							self.end_pause_time = time.time() + float(args[1])
						else:
							out_msg('Transition.update', 'pause ожидает 1 аргумент: время\n' + action)
						return
					elif command == 'repeat':
						self.action_num = 0
						return
					else:
						is_prop = get_transition_props(command) is not None
						if is_prop:
							if len(args) % 2:
								out_msg('Transition.update', 'Ожидалось чётное количество аргументов: [параметр значение]+\n' + action)
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
										self.sprite.new.contains = []
										self.sprite.new.image = evaled
								elif isinstance(evaled, int) or isinstance(evaled, float):
									self.end_pause_time = time.time() + float(evaled)
								else:
									out_msg('Transition.update', 'Unknown command:\n' + action)
							except:
								try:
									evaled = eval(command)
									if str(type(evaled)) == "<type 'function'>":
										if len(args) % 2:
											desc = command + ' ожидает нечётное количество аргументов: время, [параметр значение]+\n' + action
											out_msg('Transition.update', desc)
										else:
											self.change_func = evaled
											self.start_changing_time = time.time()
											self.end_changing_time = time.time() + float(args[1])
											self.save_change_params(args[2:])
										return
									else:
										out_msg('Transition.update', 'Unknown command:\n' + action)
								except:
									out_msg('Transition.update', 'Exception:\n' + action)
				elif type(action) is list:
					if ' ' in action[0]:
						index = action[0].index(' ')
						command = action[0][0:index]
						extra_param = action[0][index+1:]
						action = [command] + [extra_param] + [action[1:]]
					else:
						command = action[0]
						extra_param = str(self.sprite) + ': ' + command + '_' + str(self.action_num)
					
#					print action, '---', command
					
					if command == 'contains':
						if self.last_command != command:
							self.sprite.new.contains = []
						spr = Sprite([], [], action[1:], None)
						spr.call_str = extra_param
						self.sprite.new.contains.append(spr)
					elif command == 'parallel':
						pass
					else:
						out_msg('Transition.update', 'Ожидались блоки <contains> или <parallel>, получен <' + str(action[0]) + '>')
					
					self.last_command = command
				else:
					out_msg('Transition.update', 'Command type is not str or list:\n' + type(action) + '\n' + str(action))
		
		def save_change_params(self, args):
			self.change_props = []
			
			for i in xrange(0, len(args), 2):
				names = self.get_prop_names(args[i])
				
				if isinstance(names, list) or isinstance(names, tuple):
					new_value = eval(args[i + 1])
					if not isinstance(new_value, list) and not isinstance(new_value, tuple):
						new_value = [new_value] * len(names)
					old_value = [self.sprite.new[name] for name in names]
				else:
					new_value = eval(args[i + 1])
					old_value = self.sprite.new[names]
				
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
			props = get_transition_props(prop)
			
			if len(props) == 1:
				if prop == 'xalign':
					return ['xpos', 'xanchor']
				if prop == 'yalign':
					return ['ypos', 'yanchor']
				return prop
			return props
		
		def set_prop(self, prop, value):
			if isinstance(prop, str):
				props = get_transition_props(prop)
			else:
				props = prop
			
			if props == ['xalign']:
				self.sprite.new.xalign = value
				props = ['xpos', 'xanchor']
				value = [value] * 2
			elif props == ['yalign']:
				self.sprite.new.yalign = value
				props = ['ypos', 'yanchor']
				value = [value] * 2
			
			if len(props) == 1:
				self.sprite.new[prop] = value
			else:
				if (not isinstance(value, list) and not isinstance(value, tuple)) or len(props) != len(value):
					out_msg('Transition.set_prop', 'Значением ожидался список из ' + str(len(props)) + ' элементов, получено: <' +str(value)+ '>')
				else:
					for i in xrange(len(props)):
						self.set_prop(props[i], value[i])
	
	
	
	
	
	def get_place_transition(xpos, ypos, xanchor, yanchor):
		actions = (
			'pos ' + str((xpos, ypos)),
			'anchor ' + str((xanchor, yanchor))
		)
		
		res = Transition(actions)
		return res
	
	fleft  = get_place_transition(0.16,  1.0, 0.5, 1.0)
	left   = get_place_transition(0.28,  1.0, 0.5, 1.0)
	cleft  = get_place_transition(0.355, 1.0, 0.5, 1.0)
	center = get_place_transition(0.50,  1.0, 0.5, 1.0)
	cright = get_place_transition(0.645, 1.0, 0.5, 1.0)
	right  = get_place_transition(0.72,  1.0, 0.5, 1.0)
	fright = get_place_transition(0.84,  1.0, 0.5, 1.0)
	
	true_center = get_place_transition(0.5, 0.5, 0.5, 0.5)
	
	
	
	
	class Fade(Object):
		def __init__(self, out_time, hold_time = 0, in_time = None, color = '000', spr = None):
			Object.__init__(self)
			
			if in_time is None:
				in_time = out_time
			
			if out_time <= 0:
				out_time = 0.001
			if hold_time <= 0:
				hold_time = 0.001
			if in_time <= 0:
				in_time = 0.001
			
			self.out_time, self.hold_time, self.in_time = out_time, hold_time, in_time
			self.start_time = time.time()
			
			self.color = color
			
			self.sprite = spr
			if spr:
				self.set_new_old_order()
				
				global sprite_can_update
				sprite_can_update = False
		
		def copy(self, spr):
			res = Fade(self.out_time, self.hold_time, self.in_time, self.color, spr)
			return res
		
		def set_new_old_order(self):
			screen.background = get_inited_transform()
			screen.background.alpha = 0
			screen.background.image = im.Rect(self.color, 1, 1)
			
			screen.new.alpha = 0
			
			if self.sprite:
				screen.new_old_ordered = (self.sprite.old, self.sprite.new, self.sprite.background)
		
		def for_all_scene(self):
			return True
		
		
		def update(self):
			now = time.time()
			dtime = now - self.start_time
			
			screen.background.real_xsize, screen.background.real_ysize = screen.new.real_xsize, screen.new.real_ysize
			
			if dtime < self.out_time + self.hold_time:
				screen.background.alpha = in_bounds(dtime / self.out_time, 0.0, 1.0)
			else:
				global sprite_can_update
				
				if not sprite_can_update:
					to_delete = [] if self.sprite is not False else sprites_hide_list
					for spr in to_delete:
						spr.remove_with_at()
					
					screen.new.alpha = 1.0
					screen.new_old_ordered = (screen.new, screen.background)
				
				sprite_can_update = True
				
				screen.background.alpha = 1 - in_bounds((dtime - self.out_time - self.hold_time) / self.out_time, 0.0, 1.0)
				if screen.background.alpha == 0:
					if self.sprite:
						self.sprite.remove_with_at()
					elif self is screen.with_at:
						screen.remove_with_at()
	
	
	
	fade = Fade(0.5)
	fade2 = Fade(1)
	fade3 = Fade(1.5)
	
	flash = Fade(1, color="#FFF")
	flash2 = Fade(2, 2, 2, color="#FFF")
	flash_red = Fade(1, color="#E11")
	
	
	
	
	class Dissolve(Object):
		def __init__(self, t, spr = None):
			Object.__init__(self)
			
			if t <= 0:
				t = 0.001
			
			self.time = t
			self.start_time = time.time()
			
			self.sprite = spr
			if spr:
				self.set_new_old_order()
		
		def copy(self, spr):
			res = Dissolve(self.time, spr)
			return res
		
		def set_new_old_order(self):
			self.sprite.new_old_ordered = (self.sprite.old, self.sprite.new)
		
		def for_all_scene(self):
			return False
		
		
		def update(self):
			global sprites_show_list, sprites_hide_list
			
			now = time.time()
			dtime = now - self.start_time
			
			k = 1.8
			alpha = in_bounds(dtime / self.time * k, 0.0, 1.0)
			anti_alpha = in_bounds((1 - dtime / self.time) * k, 0.0, 1.0)
			
			if self.sprite:
				self.sprite.new.alpha = alpha
				self.sprite.old.alpha = anti_alpha
			
				if alpha == 1:
					self.sprite.remove_with_at()
			elif self.sprite is False:
				for spr in sprites_show_list:
					for trans in spr.new_old_ordered:
						trans.alpha = alpha
				for spr in sprites_hide_list:
					for trans in spr.new_old_ordered:
						trans.alpha = anti_alpha
				
				if alpha == 1:
					sprites_hide_list = []
					for spr in sprites_show_list:
						spr.remove_with_at()
	
	
	dspr = Dissolve(0.2)
	dissolve = Dissolve(0.5)
	dissolve2 = Dissolve(1)
	
	
	
	class Punch(Object):
		def __init__(self, prop, dist, time_one, time_all):
			Object.__init__(self)
			
			self.prop, self.dist, self.time_one, self.time_all = prop, dist, time_one, time_all
			self.start_time = time.time()
		
		def for_all_scene(self):
			return True
		
		def copy(self, spr = None):
			return Punch(self.prop, self.dist, self.time_one, self.time_all)
		
		
		def update(self):
			global sprites_hide_list
			i = 0
			for spr in sprites_hide_list:
				if spr.with_at is None:
					sprites_hide_list = sprites_hide_list[0:i] + sprites_hide_list[i+1:]
				else:
					i += 1
			
			now = time.time()
			dtime = now - self.start_time
			
			if dtime > self.time_all:
				screen.new[self.prop] = 0
				screen.remove_with_at()
			else:
				t = (dtime % self.time_one) / self.time_one # 0.0 -> 1.0
				
				if True:                      # Дёргано, резко
					t = 1 if t > 0.5 else -1
				else:                         # Плавно
					if t > 0.5:
						t = 1 - t
					t *= 2
				
				m = 1 if int(dtime / self.time_one) % 2 else -1
				
				screen.new[self.prop] = round(t * m * self.dist)
	
	
	hpunch = Punch('xpos', 10, 0.1, 0.5)
	vpunch = Punch('ypos',  7, 0.1, 0.5)












