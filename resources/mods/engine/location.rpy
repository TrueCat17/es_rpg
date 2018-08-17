init -1002 python:
	
	location_start_time = time.time()
	location_fade_time = 0.5
	
	cur_location = None
	cur_location_name = None
	cur_place_name = None
	cur_to_place = None
	
	
	cam_object = None
	def cam_to(obj):
		global cam_object
		
		if isinstance(obj, str):
			if not cur_location_name:
				out_msg('cam_to("place_name")', 'Текущая локация не установлена, сначала следует вызвать set_location')
				return
			place = cur_location.get_place(obj)
			if not place:
				out_msg('cam_to("place_name")', 'В локации <' + cur_location_name + '> нет места с именем <' + obj + '>')
				return
			cam_object = place
		else:
			cam_object = obj
	
	
	location_scale = 1
	upd_loc_psw, upd_loc_psh = -1.0, -1.0 # ps[w/h] = prev_stage_[width/height]
	def update_location_scale():
		global upd_loc_psw, upd_loc_psh
		stage_width, stage_height = float(get_stage_width()), float(get_stage_height())
		if stage_width == upd_loc_psw and stage_height == upd_loc_psh:
			return
		upd_loc_psw, upd_loc_psh = stage_width, stage_height
		
		
		round_part = 4
		spec_floor = lambda n: math.floor(n * round_part) / round_part
		spec_ceil  = lambda n: math.ceil( n * round_part) / round_part
		
		global location_scale
		location_scale = 1.0
		
		for location_name in locations.keys():
			location = locations[location_name]
			if location.is_room:  # Помещение (комната, автобус...)?
				scale = min(stage_width / location.width, stage_height / location.height) # Увеличение до одной из сторон экрана
				scale = spec_floor(scale) # Округление в меньшую сторону
			else:
				scale = max(stage_width / location.width, stage_height / location.height) # Увеличение до обоих сторон экрана
				scale = spec_ceil(scale)  # Округление в большую сторону
			
			location_scale = max(location_scale, scale)
		
		if location_scale > 2.5:
			location_scale = 2.5
	
	
	
	locations = dict()
	
	objects_on_location = []
	def characters_moved():
		for obj in objects_on_location:
			if isinstance(obj, Character):
				if not obj.moved():
					return False
		return True
	
	
	def register_location(name, path_to_images, is_room, width, height):
		location = Location(name, path_to_images, is_room, width, height)
		locations[name] = location
	
	def register_place(location_name, place_name, x, y, width, height):
		if not locations.has_key(location_name):
			out_msg('register_place', 'Локация <' + location_name + '> не зарегистрирована')
			return
		
		location = locations[location_name]
		if location.get_place(place_name):
			out_msg('register_place', 'Место <' + place_name + '> в локации <' + self.name + '> уже существует')
			return
		
		place = Place(x, y, width, height)
		location.add_place(place, place_name)
	
	def register_exit(location_name, to_location_name, to_place_name, x, y, width, height):
		if not locations.has_key(location_name):
			out_msg('register_exit', 'Локация <' + location_name + '> не зарегистрирована')
			return
		
		location = locations[location_name]
		exit = Exit(to_location_name, to_place_name, x, y, width, height)
		location.add_exit(exit)
	
	
	
	def set_location(location_name, place_name):
		if not locations.has_key(location_name):
			out_msg('set_location', 'Локация <' + location_name + '> не найдена')
			return
		if not locations[location_name].get_place(place_name):
			out_msg('set_location', 'Локация <' + location_name + '> не содержит места <' + place_name + '>')
			return
		
		if not has_screen('location'):
			show_screen('location')
			show_screen('inventory')
		
		global location_start_time, objects_on_location
		global cur_location, cur_location_name, cur_to_place
		global location_changed, draw_location, draw_location_name, draw_objects_on_location
		global was_out_exit, cam_object
		
		cur_location = locations[location_name]
		cur_location_name = location_name
		cur_to_place = place_name
		
		location_start_time = time.time()
		objects_on_location = list(cur_location.objects)
		
		main = cur_location.main()
		real_width, real_height = get_texture_size(main)
		reg_width, reg_height = cur_location.width, cur_location.height
		
		if draw_location is None:
			location_start_time -= location_fade_time
			
			location_changed = True
			draw_location, draw_location_name = cur_location, cur_location_name
			draw_objects_on_location = objects_on_location
			
			was_out_exit = False
			show_character(me, cur_to_place)
			cam_object = me
		
		if reg_width != real_width or reg_height != real_height:
			reg_size = str(reg_width) + 'x' + str(reg_height)
			real_size = str(real_width) + 'x' + str(real_height)
			out_msg('set_location', 
					'Размер локации при регистрации (' + reg_size + ') не соответствует реальному размеру (' + real_size + ')\n' + 
					'Локация: <' + cur_location_name + '>\n' + 
					'Основное изображение: <' + main + '>')
	
	def hide_location():
		global cur_location_name, cur_to_place
		
		cur_location_name = None
		cur_to_place = None
	
	
	
	def get_location_image(obj, directory, name, name_postfix, ext):
		if obj.cache is None:
			obj.cache = dict()
		cache = obj.cache
		
		mode = persistent.sprite_time
		key = name, name_postfix, mode
		if cache.has_key(key):
			return cache[key]
		
		path = directory + name + name_postfix + '_' + mode + ext
		if not os.path.exists(path):
			path = path_to_images + image_type + ext
			if os.path.exists(path):
				if image_type != 'free':
					r, g, b = persistent.lt_r, persistent.lt_g, persistent.lt_b
					path = im.recolor(path, r, g, b)
			else:
				path = None
		
		cache[key] = path
		return path
	
	
	class Location(Object):
		def __init__(self, name, path_to_images, is_room, width, height):
			Object.__init__(self)
			
			self.name = name
			self.path_to_images = path_to_images + ('/' if not path_to_images.endswith('/') else '')
			
			self.is_room = is_room
			self.width, self.height = width, height
			
			self.places = dict()
			self.exits = []
			
			self.objects = []
		
		def main(self):
			return get_location_image(self, 'main')
		def over(self):
			return get_location_image(self, 'over')
		def free(self):
			return get_location_image(self, 'free')
		
		def preload(self):
			load_image(self.main())
			if self.over():
				load_image(self.over())
			if self.free():
				load_image(self.free())
		
		def add_place(self, place, place_name):
			self.places[place_name] = place
		
		def get_place(self, place_name):
			return self.places.get(place_name, None)
		
		def add_exit(self, exit):
			self.exits.append(exit)
		
		
		def update_pos(self):
			main_width, main_height = self.width * location_scale, self.height * location_scale
			stage_width, stage_height = get_stage_width(), get_stage_height()
			
			cam_object_x = 0 if cam_object is None else cam_object.x * location_scale
			cam_object_y = 0 if cam_object is None else cam_object.y * location_scale
			
			if main_width < stage_width or cam_object is None:
				self.x = (stage_width - main_width) / 2
			else:
				if cam_object_x <= stage_width / 2:
					self.x = 0
				elif cam_object_x >= main_width - stage_width / 2:
					self.x = stage_width - main_width
				else:
					self.x = stage_width / 2 - cam_object_x
			
			if main_height < stage_height or cam_object is None:
				self.y = (stage_height - main_height) / 2
			else:
				if cam_object_y <= stage_height / 2:
					self.y = 0
				elif cam_object_y >= main_height - stage_height / 2:
					self.y = stage_height - main_height
				else:
					self.y = stage_height / 2 - cam_object_y
	
	
	class Place(Object):
		def __init__(self, x, y, width, height):
			Object.__init__(self)
			self.x, self.y = x, y
			self.width, self.height = width, height
		
		def inside(self, x, y):
			return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height
	
	class Exit(Object):
		def __init__(self, to_location_name, to_place_name, x, y, width, height):
			Object.__init__(self)
			self.to_location_name = to_location_name
			self.to_place_name = to_place_name
			self.x, self.y = x, y
			self.width, self.height = width, height
		
		def inside(self, x, y):
			return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height
	
	
	
	exec_action = False
	was_out_exit = False
	was_out_place = False
	
	def get_location_exit():
		global was_out_exit, was_out_place
		
		for exit in cur_location.exits:
			if exit.inside(me.x, me.y):
				can_exit = (not globals().has_key('can_exit_to')) or can_exit_to(exit.to_location_name, exit.to_place_name)
				if was_out_exit and can_exit:
					was_out_exit = False
					was_out_place = True
					return exit
				return None
		else:
			was_out_exit = True
		
		return None
	
	def get_location_place():
		global exec_action, was_out_place
		
		for place_name in cur_location.places.keys():
			place = cur_location.places[place_name]
			if place.inside(me.x, me.y):
				if was_out_place:
					exec_action = False
				if exec_action or was_out_place:
					was_out_place = False
					return place_name
				return None
		else:
			was_out_place = True
		
		return None
	
	def get_near_location_object():
		mx, my = me.x, me.y
		min_dist = character_radius * 3
		res = None
		
		for i in objects_on_location:
			if isinstance(i, Character):
				continue
			
			obj = location_objects[i.type]
			if obj['max_in_inventory_cell'] <= 0:
				continue
			
			dx, dy = i.x - mx, i.y - my
			dist = math.sqrt(dx * dx + dy * dy)
			if dist < min_dist:
				min_dist = dist
				res = i
		return res
		

