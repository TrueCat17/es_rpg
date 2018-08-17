init -1001 python:
	
	location_objects = dict()
	
	def register_location_object(obj_name, directory, image, free = None, 
	                               max_in_inventory_cell = 0, remove_to_location = True,
	                               frames = 1, frame_time = 1.0, frame_main = 0):
		if location_objects.has_key(obj_name):
			out_msg('register_location_object', 'Объект с именем <' + obj_name + '> уже существует')
			return
		
		location_objects[obj_name] = {
			'name': obj_name,
			'directory': directory
			'image': image,
			'free': free,
			'frames': frames,
			'frame_time': frame_time,
			'frame_main': frame_main,
			'max_in_inventory_cell': max_in_inventory_cell,
			'remove_to_location': remove_to_location
		}
	
	
	
	class LocationObject(Object):
		def __init__(self, directory, image, free, frames, main_frame):
			Object.__init__(self)
			
			self.directory = directory
			self.image, self.free = image, free
			
			self.frames, self.main_frame = frames, main_frame
		
		def add_animation()
	
	
	
	def add_location_object(location_name, place, obj_name):
		if not locations.has_key(location_name):
			out_msg('add_location_object', 'Локация <' + location_name + '> не зарегистрирована')
			return
		location = locations[location_name]
		
		if type(place) is str:
			tmp_place = location.get_place(place)
			if not tmp_place:
				out_msg('add_location_object', 'В локации <' + location_name + '> нет места с именем <' + place + '>')
				return
			place = tmp_place
			px, py = place.x + place.width / 2, place.y + place.height / 2
		else:
			px, py = place['x'], place['y'] - 1
		
		if not location_objects.has_key(obj_name):
			out_msg('', 'Объект <' + obj_name + '> не зарегистрирован')
			return
		
		obj = location_objects[obj_name]
		
		instance = Object()
		instance.type = obj_name
		instance.x, instance.y = px, py
		instance.xanchor, instance.yanchor = 0.5, 1.0
		instance.width, instance.height = get_texture_size(instance.image)
		instance.crop = (0, 0, 1.0, 1.0)
		location.objects.append(instance)
		objects_on_location.append(instance)
	
	def remove_location_object(location_name, place, obj_name, count = 1):
		if not locations.has_key(location_name):
			out_msg('remove_location_object', 'Локация <' + location_name + '> не зарегистрирована')
			return
		location = locations[location_name]
		
		if type(place) is str:
			place = location.get_place(place)
			if not place:
				out_msg('add_location_object', 'В локации <' + location_name + '> нет места с именем <' + place_name + '>')
				return
		if place:
			px, py = place['x'], place['y']
		else:
			px = py = 0
		
		to_remove = []
		for i in location.objects:
			if i.type == obj_name:
				to_remove.append(i)
		
		to_remove.sort(key = lambda o: (o.x - p.x)**2 + (o.y - p.y)**2)
		to_remove = to_remove[0:count]
		
		for i in to_remove:
			if i in location.objects:
				location.objects.remove(i)
			if i in objects_on_location:
				objects_on_location.remove(i)

