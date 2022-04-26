init python:
	
	def cloud__update_wind():
		dtime = get_last_tick()
		
		max_speed_change = dtime * cloud.max_speed_change
		max_angle_change = dtime * cloud.max_angle_change
		
		cloud.speed = in_bounds(cloud.speed + random.uniform(-max_speed_change, +max_speed_change), cloud.min_speed, cloud.max_speed)
		cloud.move_angle += random.uniform(-max_angle_change, +max_angle_change)
	
	
	def cloud__on_change_location():
		if cur_location.is_room:
			return
		if not cloud.usuals:
			return
		
		objects = cur_location.objects
		i = 0
		while i < len(objects):
			if isinstance(objects[i], Cloud):
				objects.pop(i)
			else:
				i += 1
		
		count = cloud.get_count_for_location(cur_location)
		for i in xrange(count):
			obj = add_location_object(cur_location_name, {'x': 0, 'y': 0}, Cloud)
			obj.set_init_params(inside=True)
	
	def cloud__default_get_count_for_location(location):
		size = cur_location.xsize + cur_location.ysize
		if size >= 3500:
			return 4
		return max(1, size / 1000)
	
	
	def cloud__init(**kwargs):
		cloud.get_count_for_location = kwargs.get('get_count_for_location', cloud.default_get_count_for_location)
		
		cloud.min_alpha = kwargs.get('min_alpha', 0.20)
		cloud.max_alpha = kwargs.get('max_alpha', 0.50)
		
		cloud.min_zoom = kwargs.get('min_zoom', 1)
		cloud.max_zoom = kwargs.get('max_zoom', 4)
		
		cloud.min_speed = kwargs.get('min_speed', 20)
		cloud.max_speed = kwargs.get('max_speed', 70)
		cloud.max_speed_change = kwargs.get('max_speed_change', 10)
		cloud.max_angle_change = kwargs.get('max_angle_change', 50)
		
		cloud.speed = random.randint(cloud.min_speed, cloud.max_speed)
		cloud.move_angle = random.randint(0, 359)
		
		cloud.specials_chance = kwargs.get('specials_chance', 0.10)
		
		cloud.directory = os.path.dirname(get_filename(0)) + '/images/'
		cloud.usuals = []
		cloud.specials = []
		
		for i in os.listdir(cloud.directory):
			if not os.path.isfile(cloud.directory + i): continue
			if not i.endswith('.png') and not i.endswith('.webp'): continue
			
			name, ext = os.path.splitext(i)
			if name.isdigit():
				cloud.usuals.append(i)
			else:
				cloud.specials.append(i)
		
		if not cloud.registered_signals:
			cloud.registered_signals = True
			signals.add('enter_frame', cloud.update_wind)
			signals.add('rpg-location', cloud.on_change_location)
	
	build_object('cloud')
	
	class Cloud(Object):
		
		def __init__(self, xpos, ypos, xsize, ysize):
			Object.__init__(self)
		
		def __str__(self):
			return '<Cloud %s in (%s, %s)>' % (self.parts, int(self.x), int(self.y))
		
		def set_init_params(self, inside = False):
			self.speed_k = random.uniform(0.5, 1)
			self.alpha = random.uniform(cloud.min_alpha, cloud.max_alpha)
			
			zoom = random.randint(cloud.min_zoom, cloud.max_zoom)
			self.xsize, self.ysize = 80 * zoom, 50 * zoom
			self.part_xsize, self.part_ysize = self.xsize / 2, self.ysize / 2
			
			w, h = self.location.xsize, self.location.ysize
			self.x = absolute(random.randint(0, w - 1))
			self.y = absolute(random.randint(0, h - 1))
			
			if not inside:
				dx = _cos(int(cloud.move_angle)) * cloud.speed
				dy = _sin(int(cloud.move_angle)) * cloud.speed
				while rects_intersects(self.x, self.y, self.xsize, self.ysize, 0, 0, w, h):
					self.x -= dx
					self.y -= dy
				self.invisible = True
			
			# 4 parts:
			#  0, 1,
			#  2, 3
			self.parts = []
			for i in xrange(4):
				image = random.choice(cloud.usuals)
				while image in self.parts and len(cloud.usuals) >= 4:
					image = random.choice(cloud.usuals)
				self.parts.append(image)
			
			if cloud.specials and random.random() < cloud.specials_chance:
				self.parts[random.randint(0, 3)] = random.choice(cloud.specials)
		
		def update(self):
			if self.location not in (cur_location, draw_location):
				self.location.objects.remove(self)
				return
			
			dtime = get_last_tick()
			speed = dtime * cloud.speed * self.speed_k
			self.x += _cos(int(cloud.move_angle)) * speed
			self.y += _sin(int(cloud.move_angle)) * speed
			
			w, h = self.location.xsize, self.location.ysize
			in_location = rects_intersects(self.x, self.y, self.xsize, self.ysize, 0, 0, w, h)
			if self.invisible and in_location:
				self.invisible = False
			if not self.invisible and not in_location:
				self.set_init_params()
		
		def get_part_draw_data(self, num):
			hflip = num == 1 or num == 3
			vflip = num == 2 or num == 3
			part_x = int(hflip) * self.part_xsize
			part_y = int(vflip) * self.part_ysize
			
			return {
				'image': im.flip(cloud.directory + self.parts[num], hflip, vflip),
				'pos':  (self.x + part_x, self.y + part_y),
				'size': (self.part_xsize, self.part_ysize),
				'alpha': self.alpha,
				'zorder': 1e7,
			}
		
		def get_draw_data(self):
			return [self.get_part_draw_data(i) for i in xrange(4)]
