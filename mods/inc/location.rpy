init -1001 python:
	cur_location = None
	
	cur_location_name = None
	cur_place_name = None
	
	next_location_name = None
	next_place_name = None
	
	
	cam_object = None
	def cam_to_character(character):
		global cam_object
		cam_object = character
	def cam_to_point(x, y):
		global cam_object
		cam_object = Object()
		cam_object.x, cam_object.y = x, y
	
	
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
			if location.is_room: # Помещение (комната, автобус...)?
				scale = min(stage_width / location.width, stage_height / location.height) # Увеличение до одной из сторон экрана
				scale = int(scale) # Округление в меньшую сторону
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
		
		global cur_location, cur_location_name, cur_place_name, objects_on_location, cam_object
		cur_location = locations[location_name]
		
		main = cur_location.main
		real_width, real_height = get_texture_width(main), get_texture_height(main)
		reg_width, reg_height = cur_location.width, cur_location.height
		if reg_width != real_width or reg_height != real_height:
			reg_size = str(reg_width) + 'x' + str(reg_height)
			real_size = str(real_width) + 'x' + str(real_height)
			out_msg('set_location', 
					'Размер локации при регистрации (' + reg_size + ') не соответствует реальному размеру (' + real_size + ')\n' + 
					'Локация: <' + cur_location.name + '>\n' + 
					'Основное изображение: <' + main + '>')
		
		cur_location_name = location_name
		cur_place_name = place_name
		
		objects_on_location = []
		show_character(me, place_name)
		cam_object = me
	
	def show_character(character, place_name):
		if not character:
			out_msg('show_character', 'character == None')
			return
		if not cur_location_name:
			out_msg('show_character', 'Текущая локация не установлена, сначала следует вызвать set_location')
			return
		place = cur_location.get_place(place_name)
		if not place:
			out_msg('show_character', 'В локации <' + cur_location_name + '> нет места с именем <' + place_name + '>')
			return
		
		character.x, character.y = place.x, place.y
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
		global cur_location_name, cur_place_name
		
		cur_location_name = None
		cur_place_name = None
	
	
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
		
		image = map_objects[obj_name]
		
		map_object = Object()
		map_object.image = image
		map_object.x, map_object.y = place.x, place.y
		map_object.xanchor, map_object.yanchor = 0, 0
		map_object.width, map_object.height = get_texture_width(image), get_texture_height(image)
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
	
	
	def register_place(location_name, place_name, x, y):
		if not locations.has_key(location_name):
			out_msg('register_place', 'Локация <' + location_name + '> не найдена')
			return
		
		location = locations[location_name]
		if location.get_place(place_name):
			out_msg('register_place', 'Место <' + place_name + '> в локации <' + self.name + '> уже существует')
			return
		
		place = Place(x, y)
		location.add_place(place, place_name)
	
	def register_map_object(obj_name, path_to_image):
		if map_objects.has_key(obj_name):
			out_msg('register_map_object', 'Объект с именем <' + obj_name + '> уже существует')
			return
		map_objects[obj_name] = path_to_image
	
	def register_exit(location_name, to_location_name, to_place_name, x, y):
		if not locations.has_key(location_name):
			out_msg('register_exit', 'Локация <' + location_name + '> не найдена')
			return
		
		location = locations[location_name]
		exit = Exit(to_location_name, to_place_name, x, y)
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
		
		def in_exit(self, x, y):
			for exit in self.exits:
				if exit.inside(x, y):
					return exit
			return None
		
		
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
		def __init__(self, x, y):
			Object.__init__(self)
			self.x, self.y = x, y
	
	class Exit(Object):
		def __init__(self, to_location_name, to_place_name, x, y):
			Object.__init__(self)
			self.to_location_name = to_location_name
			self.to_place_name = to_place_name
			self.x, self.y = x, y
			
			self.radius = 50 # px
		
		def inside(self, x, y):
			dx = self.x - x
			dy = self.y - y
			s = (dx*dx + dy*dy) ** 0.5
			return s < self.radius
