init -1001 python:
	
	location_object_ext = 'png'
	
	
	location_objects = dict()
	
	def register_location_object(obj_name, directory, main_image, free_image,
	                             max_in_inventory_cell = 0, remove_to_location = True):
		if location_objects.has_key(obj_name):
			out_msg('register_location_object', 'Объект с именем <' + obj_name + '> уже существует')
			return
		
		location_objects[obj_name] = {
			'name': obj_name,
			'max_in_inventory_cell': max_in_inventory_cell,
			'remove_to_location': remove_to_location,
			'animations': Object()
		}
		register_location_object_animation(obj_name, None, 0, 0, directory, main_image, free_image, 1, 0, 0)
	
	def register_location_object_animation(obj_name, anim_name, xalign, yalign,
	                                       directory, main_image, free_image,
	                                       count_frames, start_frame, end_frame, time = 1.0):
		if xalign < 0 or xalign > 1:
			out_msg('register_location_object_animation',
			        'При регистрации анимации <' + str(anim_name) + '> объекта <' + str(obj_name) + '>\n' +
			        'Указан некорректный xalign: ' + str(xalign) + '\n' +
			        'Ожидалось значение от 0.0 до 1.0')
			return
		if yalign < 0 or yalign > 1:
			out_msg('register_location_object_animation',
			        'При регистрации анимации <' + str(anim_name) + '> объекта <' + str(obj_name) + '>\n' +
			        'Указан некорректный yalign: ' + str(yalign) + '\n' +
			        'Ожидалось значение от 0.0 до 1.0')
			return
		
		if count_frames <= 0 or not (0 <= start_frame < count_frames) or not (0 <= end_frame < count_frames):
			out_msg('register_location_object_animation',
			        'При регистрации анимации <' + str(anim_name) + '> объекта <' + str(obj_name) + '>\n' +
			        'Указаны некорректные кадры:\n' +
			        'count, start, end = ' + str(count_frames) + ', ' + str(start_frame) + ', ' + str(end_frame))
			return
		
		if not location_objects.has_key(obj_name):
			out_msg('register_location_object_animation', 'Объект <' + str(obj_name) + '> не существует')
			return
		
		obj = location_objects[obj_name]
		
		animations = obj['animations']
		if animations.has_key(anim_name):
			out_msg('register_location_object_animation', 'Анимация <' + str(anim_name) + '> объекта <' + str(obj_name) + '> уже существует')
			return
		
		animation = animations[anim_name] = Object(
			directory    = directory,
			main_image   = main_image,
			free_image   = free_image,
			
			count_frames = count_frames,
			start_frame  = start_frame,
			end_frame    = end_frame,
			time         = float(time),
		
			xalign = xalign,
			yalign = yalign,
			xsize = 0,
			ysize = 0,
			loaded = False
		)
	
	
	class LocationObject(Object):
		def __init__(self, name, x, y):
			Object.__init__(self)
			
			self.type = name
			for key, value in location_objects[name].iteritems():
				self[key] = value
			
			self.x, self.y = x, y
			self.orig_x, self.orig_y = x, y
			
			self.xanchor, self.yanchor = 0.5, 1.0
			self.xsize, self.ysize = 0, 0
			
			self.stop_animation()
		
		def set_frame(self, frame):
			self.crop = (int(frame) * self.xsize, 0, self.xsize, self.ysize)
		
		def set_animation(self, anim_name):
			if not self.animations.has_key(anim_name):
				out_msg('set_animation', 'Объект <' + str(self.type) + '> не содержит анимации <' + str(anim_name) + '>')
				return False
			
			self.anim_name = anim_name
			self.animation = self.animations[anim_name]
			self.animation.first_update = True
			return True
		
		def set_animation_frame(self, anim_name, frame):
			self.set_animation(anim_name)
			self.set_frame(frame)
		
		def main(self):
			return get_location_image(self.animation, self.animation.directory, self.animation.main_image, '', location_object_ext, False)
		
		def free(self):
			if self.animation.free_image is None:
				return None
			res = get_location_image(self.animation, self.animation.directory, self.animation.free_image, '', location_object_ext, True, False)
			if self.animation.count_frames != 1:
				res = im.crop(res, self.crop)
			return res
		
		def start_animation(self, anim_name, then_reverse = False, repeat = 0):
			if not self.set_animation(anim_name):
				return
			
			self.animation_start_time = time.time()
			self.then_reverse = then_reverse
			self.repeat = int(repeat)
		
		def remove_animation(self):
			self.start_animation(None)
		
		def update(self):
			animation = self.animation
			if animation.first_update:
				animation.first_update = False
				
				if not animation.loaded:
					animation.loaded = True
					animation.xsize, animation.ysize = get_image_size(self.main())
					animation.xsize = int(math.ceil(animation.xsize / animation.count_frames))
				
				self.xsize, self.ysize = animation.xsize, animation.ysize
			
				main_frame = self.animations[None]
				self.x = self.orig_x + (1 - animation.xalign) * (animation.xsize - main_frame.xsize)
				self.y = self.orig_y + (1 - animation.yalign) * (animation.ysize - main_frame.ysize)
			
			dtime = time.time() - self.animation_start_time
			if self.then_reverse and dtime > animation.time:
				dtime = 2 * animation.time - dtime
			
			frame = (animation.end_frame + 1 - animation.start_frame) * dtime / animation.time
			frame = in_bounds(frame, 0, animation.count_frames - 1)
			self.set_frame(frame + animation.start_frame)
	
	
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
		
		instance = LocationObject(obj_name, px, py)
		
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
			if i in objects_on_location:
				objects_on_location.remove(i)

