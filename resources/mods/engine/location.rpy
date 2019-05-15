init -1002 python:
	
	location_ext = 'png'
	
	
	location_start_time = time.time()
	location_fade_time = 0.5
	
	cur_location = None
	cur_location_name = None
	cur_place_name = None
	cur_to_place = None
	
	
	cam_object = None
	cam_object_old = None
	cam_object_start_moving = 0
	cam_object_end_moving = 0
	
	def cam_to(obj, moving_time = 1.0):
		global cam_object, cam_object_old, cam_object_start_moving, cam_object_end_moving
		if cam_object is not None:
			cam_object_old = cam_object
			cam_object_start_moving = time.time()
			cam_object_end_moving = time.time() + moving_time
		
		if isinstance(obj, str):
			if not cur_location_name:
				out_msg('cam_to', 'Current location is not defined, need to call set_location')
				return
			place = cur_location.get_place(obj)
			if not place:
				out_msg('cam_to', 'Place <' + obj + '> not found in location <' + cur_location_name + '>')
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
			if location.is_room:
				scale = min(stage_width / location.width, stage_height / location.height) # increase to width OR height
				scale = spec_floor(scale) # round to down
			else:
				scale = max(stage_width / location.width, stage_height / location.height) # increase to width AND height
				scale = spec_ceil(scale)  # round to up
			
			location_scale = max(location_scale, scale)
		
		if location_scale > 2.5:
			location_scale = 2.5
	
	
	
	locations = dict()
	objects_on_location = []	
	
	def register_location(name, path_to_images, is_room, width, height):
		location = Location(name, path_to_images, is_room, width, height)
		locations[name] = location
	
	def register_place(location_name, place_name, x, y, width, height):
		if not locations.has_key(location_name):
			out_msg('register_place', 'Location <' + location_name + '> not registered')
			return
		
		location = locations[location_name]
		if location.get_place(place_name):
			out_msg('register_place', 'Place <' + place_name + '> in location <' + self.name + '> already exists')
			return
		
		place = Place(place_name, x, y, width, height)
		location.add_place(place, place_name)
	
	def register_exit(location_name, to_location_name, to_place_name, x, y, width, height):
		if not locations.has_key(location_name):
			out_msg('register_exit', 'Location <' + location_name + '> not registered')
			return
		
		location = locations[location_name]
		exit = Exit(to_location_name, to_place_name, x, y, width, height)
		location.add_exit(exit)
	
	
	
	def set_location(location_name, place):
		if not locations.has_key(location_name):
			out_msg('set_location', 'Location <' + location_name + '> not registered')
			return
		
		if type(place) is not dict:
			if not locations[location_name].get_place(place):
				out_msg('set_location', 'Place <' + str(place) + '> in location <' + location_name + '> not found')
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
		cur_to_place = place
		
		location_start_time = time.time()
		objects_on_location = list(cur_location.objects)
		
		main = cur_location.main()
		real_width, real_height = get_image_size(main)
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
					'Location sizes on registration (' + reg_size + ') not equal to real sizes (' + real_size + ')\n' + 
					'Location: <' + cur_location_name + '>\n' + 
					'Main image: <' + main + '>')
	
	def hide_location():
		global cur_location_name, cur_to_place
		cur_location_name = None
		cur_to_place = None
	
	
	
	def get_location_image(obj, directory, name, name_postfix, ext, is_free, need = True):
		if obj.cache is None:
			obj.cache = dict()
		
		mode = times['current_name']
		key = name, name_postfix, mode
		if obj.cache.has_key(key):
			return obj.cache[key]
		
		if name_postfix:
			name_postfix = '_' + name_postfix
		file_name = name + name_postfix
		
		path = directory + file_name + '_' + mode + '.' + ext
		if not os.path.exists(path):
			path = directory + file_name + '.' + ext
			if os.path.exists(path):
				if not is_free:
					r, g, b = location_time_rgb
					path = im.recolor(path, r, g, b)
			else:
				if need:
					out_msg('get_location_image', 'File <' + path + '> not found')
				path = None
		
		obj.cache[key] = path
		return path
	
	
	class Location(Object):
		def __init__(self, name, directory, is_room, width, height):
			Object.__init__(self)
			
			self.name = name
			self.directory = directory + ('' if directory.endswith('/') else '/')
			
			self.is_room = is_room
			self.width, self.height = width, height
			
			self.places = dict()
			self.exits = []
			
			self.objects = []
		
		def main(self):
			return get_location_image(self, self.directory, 'main', '', location_ext, False)
		def over(self):
			return get_location_image(self, self.directory, 'over', '', location_ext, False, False)
		def free(self):
			return get_location_image(self, self.directory, 'free', '', location_ext, True, False)
		
		def preload(self):
			for image in self.main(), self.over(), self.free():
				if image:
					load_image(image)
		
		def add_place(self, place, place_name):
			self.places[place_name] = place
		
		def get_place(self, place_name):
			return self.places.get(place_name, None)
		
		def add_exit(self, exit):
			self.exits.append(exit)
		
		
		def update_pos(self):
			main_width, main_height = self.width * location_scale, self.height * location_scale
			stage_width, stage_height = get_stage_width(), get_stage_height()
			
			if cam_object_old is None or cam_object is None or cam_object_end_moving < time.time():
				cam_object_x = 0 if cam_object is None else cam_object['x']
				cam_object_y = 0 if cam_object is None else cam_object['y']
			else:
				from_x, from_y = cam_object_old['x'], cam_object_old['y']
				to_x, to_y = cam_object['x'], cam_object['y']
				
				time_k = (time.time() - cam_object_start_moving) / (cam_object_end_moving - cam_object_start_moving)
				cam_object_x = from_x + (to_x - from_x) * time_k
				cam_object_y = from_y + (to_y - from_y) * time_k
			
			cam_object_x *= location_scale
			cam_object_y *= location_scale
			
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
		def __init__(self, name, x, y, width, height):
			Object.__init__(self)
			self.name = name
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
	

