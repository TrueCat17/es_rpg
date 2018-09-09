init -1001 python:
	
	location_object_ext = 'png'
	
	
	location_objects = dict()
	
	def register_location_object(obj_name, directory, main_image, free_image,
	                               max_in_inventory_cell = 0, remove_to_location = True,
	                               frames = 1, animation_time = 1.0, main_frame = 0):
		if location_objects.has_key(obj_name):
			out_msg('register_location_object', 'Объект с именем <' + obj_name + '> уже существует')
			return
		
		if main_frame >= frames:
			out_msg('register_location_object',
				'Объект <' + obj_name + '> содержит кадров: ' + str(frames) + ', но основным кадром ставится ' + str(main_frame))
			main_frame = frames - 1
		
		location_objects[obj_name] = {
			'name': obj_name,
			'directory': directory,
			'main_image': main_image,
			'free_image': free_image,
			'max_in_inventory_cell': max_in_inventory_cell,
			'remove_to_location': remove_to_location,
			'frames': frames,
			'animation_time': animation_time,
			'main_frame': main_frame
		}
	
	def register_location_object_animation(obj_name, img_path, frames, animation_time = 1.0):
		pass
	
	
	class LocationObject(Object):
		def __init__(self, name):
			Object.__init__(self)
			
			self.type = name
			self.animation_start_time = None
			
			for key, value in location_objects[name].iteritems():
				self[key] = value
			
			self.xanchor, self.yanchor = 0.5, 1.0
			self.xsize, self.ysize = 0, 0
			self.loaded = False
		
		def set_frame(self, frame):
			self.crop = (int(frame) * self.xsize, 0, self.xsize, self.ysize)
		def set_main_frame(self):
			self.set_frame(self.main_frame)
		
		def main(self):
			res = get_location_image(self, self.directory, self.main_image, '', location_object_ext, False)
			if not self.loaded:
				self.loaded = True
				self.xsize, self.ysize = get_texture_size(res)
				self.xsize = math.ceil(self.xsize / self.frames)
				self.set_frame(self.main_frame)
			return res
		def free(self):
			if self.free_image is None:
				return None
			return get_location_image(self, self.directory, self.free_image, '', location_object_ext, True, False)
		
		def start_animation(self):
			self.animation_start_time = time.time()
		def stop_animation(self):
			self.animation_start_time = None
		
		def update(self):
			if self.frames > 1 and self.animation_start_time is not None:
				dtime = time.time() - self.animation_start_time
				frame = min(self.frames * dtime / self.animation_time, self.frames - 1)
				self.set_frame(frame)
	
	
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
		
		instance = LocationObject(obj_name)
		instance.x, instance.y = px, py
		
		location.objects.append(instance)
		objects_on_location.append(instance)
	
	def remove_location_object(location_name, place, obj_name, count = 1):
		if not locations.has_key(location_name):
			out_msg('remove_location_object', 'Локация <' + location_name + '> не зарегистрирована')
			return
		location = locations[location_name]
		
		if type(place) is str:
			tmp_place = location.get_place(place)
			if tmp_place is None:
				out_msg('remove_location_object', 'В локации <' + location_name + '> нет места с именем <' + place + '>')
				return
			place = tmp_place
		
		px, py = place['x'], place['y']
		
		to_remove = []
		for i in location.objects:
			if i.type == obj_name:
				to_remove.append(i)
		
		def dist_sqr(obj):
			dx, dy = obj.x - px, obj.y - py
			return dx*dx + dy*dy
		
		to_remove.sort(key = dist_sqr)
		to_remove = to_remove[0:count]
		
		for i in to_remove:
			if i in location.objects:
				location.objects.remove(i)
			if i in objects_on_location: # ???
				objects_on_location.remove(i) # ???

