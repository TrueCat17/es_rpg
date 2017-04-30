init -1001 python:
	
	location_start_time = time.time()
	location_fade_time = 0.5
	
	cur_location = None
	cur_location_name = None
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
		
		global location_scale
		location_scale = 1
		
		for location_name in locations.keys():
			location = locations[location_name]
			if location.is_room:  # Помещение (комната, автобус...)?
				scale = min(stage_width / location.width, stage_height / location.height) # Увеличение до одной из сторон экрана
				scale = int(scale)  # Округление в меньшую сторону
			else:
				scale = max(stage_width / location.width, stage_height / location.height) # Увеличение до обоих сторон экрана
				scale = ceil(scale) # Округление в большую сторону
			
			location_scale = max(location_scale, scale)
		
		if location_scale > 3:
			location_scale = 3
	
	
	
	locations = dict()
	map_objects = dict()
	
	objects_on_location = []
	
	
	def register_location(name, path_to_images, no_pictures, is_room, width, height):
		location = Location(name, path_to_images, no_pictures, is_room, width, height)
		locations[name] = location
	
	def set_location(location_name, place_name):
		if not locations.has_key(location_name):
			out_msg('set_location', 'Локация <' + location_name + '> не найдена')
			return
		if not locations[location_name].get_place(place_name):
			out_msg('set_location', 'Локация <' + location_name + '> не содержит места <' + place_name + '>')
			return
		
		global cur_location, cur_location_name, cur_to_place
		global objects_on_location, location_start_time
		
		objects_on_location = []
		location_start_time = time.time()
		
		cur_location = locations[location_name]
		cur_location_name = location_name
		cur_to_place = place_name
		
		main = cur_location.main
		real_width, real_height = get_texture_width(main), get_texture_height(main)
		reg_width, reg_height = cur_location.width, cur_location.height
		if reg_width != real_width or reg_height != real_height:
			reg_size = str(reg_width) + 'x' + str(reg_height)
			real_size = str(real_width) + 'x' + str(real_height)
			out_msg('set_location', 
					'Размер локации при регистрации (' + reg_size + ') не соответствует реальному размеру (' + real_size + ')\n' + 
					'Локация: <' + cur_location_name + '>\n' + 
					'Основное изображение: <' + main + '>')
	
	def show_character(character, place_name):
		if not character:
			out_msg('show_character', 'character == None')
			return
		if not cur_location_name:
			out_msg('show_character', 'Текущая локация не установлена, сначала следует вызвать set_location')
			return
		place = cur_location.get_place(place_name)
		if not place:
			out_msg('show_character', 'В локации <' + cur_location_name + '> нет места с именем <' + str(place_name) + '>')
			return
		
		character.x, character.y = place.x + place.width / 2, place.y + place.height / 2
		objects_on_location.append(character)
	
	def hide_character(character):
		if not character:
			out_msg('hide_character', 'character == None')
			return
		
		global objects_on_location
		for i in xrange(len(objects_on_location)):
			obj = objects_on_location[i]
			if obj is character:
				objects_on_location = objects_on_location[0:i] + objects_on_location[i + 1:]
				break
		else:
			out_msg('hide_character', 'Персонаж <' + character.real_name + ', ' + character.unknow_name + '> не добавлен в список отображаемых')
	
	def hide_location():
		global cur_location_name, cur_to_place
		
		cur_location_name = None
		cur_to_place = None
	
	
	def set_map_object(obj_name, place_name):
		if not cur_location_name:
			out_msg('set_map_object', 'Текущая локация не установлена, сначала следует вызвать set_location')
			return
		place = cur_location.get_place(place_name)
		if not place:
			out_msg('set_map_object', 'В локации <' + cur_location_name + '> нет места с именем <' + place_name + '>')
			return
		if not map_objects.has_key(obj_name):
			out_msg('set_map_object', 'Объект <' + obj_name + '> не найден')
			return
		
		
		images = map_objects[obj_name]
		
		map_object = Object()
		map_object.image = images['main']
		map_object.free = images['free']
		map_object.x, map_object.y = place.x, place.y
		map_object.xanchor, map_object.yanchor = 0, 1.0
		map_object.width, map_object.height = get_texture_width(map_object.image), get_texture_height(map_object.image)
		map_object.crop = (0, 0, 1.0, 1.0)
		objects_on_location.append(map_object)
	
	def hide_map_object(obj_name):
		if not map_objects.has_key(obj_name):
			out_msg('hide_map_object', 'Объект <' + obj_name + '> не найден')
			return
		image = map_objects[obj_name]
		
		global objects_on_location
		for i in xrange(len(objects_on_location)):
			obj = objects_on_location[i]
			if obj.image == image:
				objects_on_location = objects_on_location[0:i] + objects_on_location[i + 1:]
				break
	
	
	def register_place(location_name, place_name, x, y, width, height):
		if not locations.has_key(location_name):
			out_msg('register_place', 'Локация <' + location_name + '> не найдена')
			return
		
		location = locations[location_name]
		if location.get_place(place_name):
			out_msg('register_place', 'Место <' + place_name + '> в локации <' + self.name + '> уже существует')
			return
		
		place = Place(x, y, width, height)
		location.add_place(place, place_name)
	
	def register_map_object(obj_name, main, free):
		if map_objects.has_key(obj_name):
			out_msg('register_map_object', 'Объект с именем <' + obj_name + '> уже существует')
			return
		map_object = {
			'main': main,
			'free': free
		}
		map_objects[obj_name] = map_object
	
	def register_exit(location_name, to_location_name, to_place_name, x, y, width, height):
		if not locations.has_key(location_name):
			out_msg('register_exit', 'Локация <' + location_name + '> не найдена')
			return
		
		location = locations[location_name]
		exit = Exit(to_location_name, to_place_name, x, y, width, height)
		location.add_exit(exit)
	
	
	class Location(Object):
		def __init__(self, name, path_to_images, no_pictures, is_room, width, height):
			Object.__init__(self)
			self.name = name
			
			self.is_room = is_room
			self.width, self.height = width, height
			
			self.main = path_to_images + 'main.png'
			self.over = None if 'o' in no_pictures else path_to_images + 'over.png'
			self.free = None if 'f' in no_pictures else path_to_images + 'free.png'
			
			self.places = dict()
			self.exits = []
		
		def add_place(self, place, place_name):
			self.places[place_name] = place
		
		def get_place(self, place_name):
			if self.places.has_key(place_name):
				return self.places[place_name]
			return None
		
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
				if was_out_exit and can_exit_to(exit.to_location_name, exit.to_place_name):
					was_out_exit = False
					was_out_place = True
					return exit
				return None
		else:
			was_out_exit = True
		
		return None
	
	def get_location_place():
		global was_out_place
		
		for place_name in cur_location.places.keys():
			place = cur_location.places[place_name]
			if place.inside(me.x, me.y):
				if exec_action or was_out_place:
					was_out_place = False
					return place_name
				return None
		else:
			was_out_place = True
		
		return None

