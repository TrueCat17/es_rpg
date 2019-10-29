init -1002 python:
	
	location_ext = 'png'
	
	
	location_start_time = 0
	location_fade_time = 0.5
	
	
	location_was_show = True
	def location_showed():
		return location_was_show
	can_exec_next_check_funcs.append(location_showed)
	
	def location_show():
		global location_start_time
		location_start_time = time.time() - location_fade_time * 2
	can_exec_next_skip_funcs.append(location_show)
	
	
	cur_location = None
	cur_location_name = None
	cur_place_name = None
	cur_to_place = None
	
	
	location_zoom = 1.0
	
	
	locations = dict()
	
	def register_location(name, path_to_images, is_room, xsize, ysize):
		if locations.has_key(name):
			out_msg('register_location', 'Location <' + name + '> already registered')
		else:
			location = Location(name, path_to_images, is_room, xsize, ysize)
			locations[name] = location
	
	def register_place(location_name, place_name, x, y, xsize, ysize, to_side = None):
		if not locations.has_key(location_name):
			out_msg('register_place', 'Location <' + location_name + '> not registered')
			return
		
		location = locations[location_name]
		if location.get_place(place_name):
			out_msg('register_place', 'Place <' + place_name + '> in location <' + self.name + '> already exists')
			return
		
		place = Place(place_name, x, y, xsize, ysize, to_side)
		location.add_place(place, place_name)
	
	def register_exit(location_name, to_location_name, to_place_name, x, y, xsize, ysize):
		if not locations.has_key(location_name):
			out_msg('register_exit', 'Location <' + location_name + '> not registered')
			return
		
		location = locations[location_name]
		exit = Exit(to_location_name, to_place_name, x, y, xsize, ysize)
		location.add_exit(exit)
	
	
	def set_location(location_name, place):
		if not locations.has_key(location_name):
			out_msg('set_location', 'Location <' + location_name + '> not registered')
			return
		
		if type(place) is str:
			if not locations[location_name].get_place(place):
				out_msg('set_location', 'Place <' + place + '> in location <' + location_name + '> not found')
				return
		
		if not has_screen('location'):
			show_screen('location')
			show_screen('inventory')
		
		global location_start_time, location_was_show
		location_start_time = time.time()
		location_was_show = False
		
		global cur_location, cur_location_name, cur_to_place
		cur_location = locations[location_name]
		cur_location_name = location_name
		cur_to_place = place
		
		end_location_ambience(cur_location)
		
		main = cur_location.main()
		real_width, real_height = get_image_size(main)
		reg_width, reg_height = cur_location.xsize, cur_location.ysize
		
		global location_changed, draw_location
		global was_out_exit, cam_object
		if draw_location is None:
			location_start_time -= location_fade_time
			
			location_changed = True
			draw_location = cur_location
			
			start_location_ambience()
			
			was_out_exit = False
			cam_object = me
		else:
			cam_object = {'x': me.x, 'y': me.y}
		
		show_character(me, cur_to_place)
		
		if reg_width != real_width or reg_height != real_height:
			reg_size = str(reg_width) + 'x' + str(reg_height)
			real_size = str(real_width) + 'x' + str(real_height)
			out_msg('set_location', 
					'Location sizes on registration (' + reg_size + ') not equal to real sizes (' + real_size + ')\n' + 
					'Location: <' + cur_location.name + '>\n' + 
					'Main image: <' + main + '>')
	
	def hide_location():
		global cur_location, cur_location_name, cur_to_place
		cur_location = cur_location_name = None
		cur_to_place = None
		
		global draw_location
		draw_location = None
		end_location_ambience()
	
	
	
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
		def __init__(self, name, directory, is_room, xsize, ysize):
			Object.__init__(self)
			
			self.name = name
			self.directory = directory + ('' if directory.endswith('/') else '/')
			
			self.is_room = is_room
			self.xsize, self.ysize = xsize, ysize
			
			self.places = dict()
			self.exits = []
			
			self.objects = []
			
			self.ambience_paths = None
			self.ambience_volume = 1.0
		
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
			self.x, self.y = get_camera_params(self)
	
	
	class Place(Object):
		def __init__(self, name, x, y, xsize, ysize, to_side):
			Object.__init__(self)
			self.name = name
			self.x, self.y = x, y
			self.xsize, self.ysize = xsize, ysize
			self.to_side = to_side
		
		def inside(self, x, y):
			return self.x <= x and x <= self.x + self.xsize and self.y <= y and y <= self.y + self.ysize
	
	class Exit(Object):
		def __init__(self, to_location_name, to_place_name, x, y, xsize, ysize):
			Object.__init__(self)
			self.to_location_name = to_location_name
			self.to_place_name = to_place_name
			self.x, self.y = x, y
			self.xsize, self.ysize = xsize, ysize
		
		def inside(self, x, y):
			return self.x <= x and x <= self.x + self.xsize and self.y <= y and y <= self.y + self.ysize
	
	
	def get_place_center(place, align = (0.5, 0.5)):
		x, y = place['x'], place['y']
		
		w = place['xsize'] if place.has_key('xsize') else 0
		h = place['ysize'] if place.has_key('ysize') else 0
		
		xa = get_absolute(place['xanchor'], w) if place.has_key('xanchor') else 0
		ya = get_absolute(place['yanchor'], h) if place.has_key('yanchor') else 0
		
		return (x - xa + align[0] * w), (y - ya + align[1] * h)
	
	
	exec_action = False
	was_out_exit = False
	was_out_place = False
	
	def get_location_exit():
		global was_out_exit, was_out_place
		
		if not exec_action and cur_location.is_room:
			was_out_exit = True
			return None
		
		for exit in cur_location.exits:
			if not exit.inside(me.x, me.y):
				continue
			
			if not exec_action and locations[exit.to_location_name].is_room:
				break
			if not was_out_exit:
				break
			
			if globals().has_key('can_exit_to') and not can_exit_to(exit.to_location_name, exit.to_place_name):
				continue
			
			was_out_exit = False
			was_out_place = True
			return exit
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

