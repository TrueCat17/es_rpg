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
	
	
	locations = dict()
	map_objects = dict()
	
	objects_on_location = []
	
	
	def register_location(name, path_to_images, no_pictures):
		location = Location(name, path_to_images, no_pictures)
		locations[name] = location
	
	def set_location(location_name, place_name):
		if not locations.has_key(location_name):
			out_msg('set_location', 'Локация <' + location_name + '> не найдена')
			return
		if not locations[location_name].get_place(place_name):
			out_msg('set_location', 'Локация <' + location_name + '> не содержит места <' + place_name + '>')
			return
		
		global cur_location, cur_location_name, cur_place_name, objects_on_location
		cur_location = locations[location_name]
		
		cur_location_name = location_name
		cur_place_name = place_name
		
		objects_on_location = []
		show_character(me, place_name)
	
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
		
		map_object = Object()
		map_object.image = map_objects[obj_name]
		map_object.x, map_object.y = place.x, place.y
		map_object.xanchor, map_object.yanchor = 0, 0
		objects_on_location.append(map_object)
	
	def hide_map_object(obj_name):
		if not map_objects.has_key(obj_name):
			out_msg('set_map_object', 'Объект <' + obj_name + '> не найден')
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
		def __init__(self, name, path_to_images, no_pictures):
			Object.__init__(self)
			self.name = name
			
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
			main_width, main_height = get_texture_width(self.main), get_texture_height(self.main)
			stage_width, stage_height = get_stage_width(), get_stage_height()
			
			dx, dy = main_width - stage_width, main_height - stage_height
			cx, cy = main_width / 2, main_height / 2
			
			if dx < 0 or cam_object is None:
				self.x = -dx / 2
			else:
				if cam_object.x <= cx - dx / 2:
					self.x = 0
				elif cam_object.x >= cx + dx / 2:
					self.x = -dx
				else:
					self.x = cx - cam_object.x
			
			if dy < 0 or cam_object is None:
				self.y = -dy / 2
			else:
				if cam_object.y <= cy - dy / 2:
					self.y = 0
				elif cam_object.y >= cy + dy / 2:
					self.y = -dy
				else:
					self.y = cy - cam_object.y
	
	
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
