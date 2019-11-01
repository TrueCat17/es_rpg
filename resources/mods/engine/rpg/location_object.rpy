init -1001 python:
	
	location_object_ext = 'png'
	
	
	location_objects = dict()
	
	
	def location_objects_animations_ended():
		if cur_location:
			for obj in cur_location.objects:
				if not isinstance(obj, LocationObject):
					continue
				
				animation = obj.animation
				if animation.start_frame != animation.end_frame and obj.repeat >= 0:
					if animation.time > 0 and time.time() - obj.animation_start_time < animation.time:
						return False
		return True
	can_exec_next_check_funcs.append(location_objects_animations_ended)
	
	def location_objects_animations_to_end():
		if cur_location:
			for obj in cur_location.objects:
				if not isinstance(obj, LocationObject):
					continue
				
				animation = obj.animation
				if animation.start_frame != animation.end_frame and obj.repeat >= 0 and animation.time > 0:
					obj.animation_start_time = time.time() - obj.animation.time
					obj.repeat = 0
	can_exec_next_skip_funcs.append(location_objects_animations_to_end)
	
	
	def register_location_object(obj_name, directory, main_image, free_image,
	                             max_in_inventory_cell = 0, remove_to_location = True):
		if location_objects.has_key(obj_name):
			out_msg('register_location_object', 'Object <' + obj_name + '> already exists')
			return
		
		location_objects[obj_name] = {
			'name': obj_name,
			'max_in_inventory_cell': max_in_inventory_cell,
			'remove_to_location': remove_to_location,
			'animations': Object()
		}
		register_location_object_animation(obj_name, None, directory, main_image, free_image, 0, 0, 1, 0, 0)
	
	def register_location_object_animation(obj_name, anim_name,
	                                       directory, main_image, free_image,
	                                       xoffset, yoffset,
	                                       count_frames, start_frame, end_frame, time = 1.0):
		if not location_objects.has_key(obj_name):
			out_msg('register_location_object_animation', 'Object <' + str(obj_name) + '> not registered')
			return
		
		if type(xoffset) is not int or type(yoffset) is not int:
			out_msg('register_location_object_animation',
			        'On registration of animation <' + str(anim_name) + '> of object <' + str(obj_name) + '>\n' +
			        'set invalid pos: <' + str(xoffset) + ', ' + str(yoffset) + '>, expected ints')
			return
		
		if count_frames <= 0 or not (0 <= start_frame < count_frames) or not (0 <= end_frame < count_frames):
			out_msg('register_location_object_animation',
			        'On registration of animation <' + str(anim_name) + '> of object <' + str(obj_name) + '>\n' +
			        'set invalid frames:\n' +
			        'count, start, end = ' + str(count_frames) + ', ' + str(start_frame) + ', ' + str(end_frame))
			return
		
		obj = location_objects[obj_name]
		
		animations = obj['animations']
		if animations.has_key(anim_name):
			out_msg('register_location_object_animation', 'Animation <' + str(anim_name) + '> of object <' + str(obj_name) + '> already exists')
			return
		
		animation = animations[anim_name] = Object(
			directory    = directory,
			main_image   = main_image,
			free_image   = free_image,
			
			count_frames = count_frames,
			start_frame  = start_frame,
			end_frame    = end_frame,
			time         = float(time),
		
			xoffset = xoffset,
			yoffset = yoffset,
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
			self.xoffset, self.yoffset = 0, 0
			
			self.xanchor, self.yanchor = 0.5, 1.0
			self.xsize, self.ysize = 0, 0
			
			self.remove_animation()
			self.update()
		
		def set_frame(self, frame):
			self.crop = (int(frame) * self.xsize, 0, self.xsize, self.ysize)
		
		def set_animation(self, anim_name):
			if not self.animations.has_key(anim_name):
				out_msg('set_animation', 'Animation <' + str(anim_name) + '> not found in object <' + str(self.type) + '>')
				return False
			
			self.anim_name = anim_name
			self.animation = self.animations[anim_name]
			self.animation.first_update = True
			return True
		
		def main(self):
			return get_location_image(self.animation, self.animation.directory, self.animation.main_image, '', location_object_ext, False)
		
		def free(self):
			if self.animation.free_image is None:
				return None
			res = get_location_image(self.animation, self.animation.directory, self.animation.free_image, '', location_object_ext, True, False)
			if self.animation.count_frames != 1:
				res = im.crop(res, self.crop)
			return res
		
		def start_animation(self, anim_name, repeat = 0):
			if not self.set_animation(anim_name):
				return
			
			self.animation_start_time = time.time()
			self.repeat = int(repeat)
		
		def remove_animation(self):
			self.start_animation(None)
		
		def update(self):
			animation = self.animation
			
			dtime = time.time() - self.animation_start_time
			time_k = 1
			if animation.time > 0:
				if dtime > animation.time:
					if self.repeat:
						self.animation_start_time = time.time()
						time_k = 0
					if self.repeat > 0:
						self.repeat -= 1
				else:
					time_k = dtime / animation.time
			
			if animation.first_update:
				animation.first_update = False
				
				if not animation.loaded:
					animation.loaded = True
					animation.xsize, animation.ysize = get_image_size(self.main())
					animation.xsize = int(math.ceil(animation.xsize / animation.count_frames))
				
				self.xsize, self.ysize = animation.xsize, animation.ysize
				self.xoffset, self.yoffset = animation.xoffset, animation.yoffset
			
			start_frame = animation.start_frame
			end_frame = animation.end_frame
			if end_frame < start_frame:
				frame = start_frame - int((start_frame - end_frame + 1) * time_k)
				frame = in_bounds(frame, end_frame, start_frame)
			else:
				frame = start_frame + int((end_frame - start_frame + 1) * time_k)
				frame = in_bounds(frame, start_frame, end_frame)
			
			self.set_frame(frame)
	
	
	def add_location_object(location_name, place, obj_name):
		if not locations.has_key(location_name):
			out_msg('add_location_object', 'Location <' + location_name + '> not registered')
			return
		location = locations[location_name]
		
		if type(place) is str:
			tmp_place = location.get_place(place)
			if not tmp_place:
				out_msg('add_location_object', 'Place <' + place + '> not found in location <' + location_name + '>')
				return
			place = tmp_place
			px, py = place.x + place.xsize / 2, place.y + place.ysize / 2
		else:
			px, py = place['x'], place['y'] - 1
		
		if not location_objects.has_key(obj_name):
			out_msg('', 'Object <' + obj_name + '> not registered')
			return
		
		instance = LocationObject(obj_name, px, py)
		location.objects.append(instance)
	
	
	def get_location_objects(location_name, place, obj_type, count = -1):
		if not locations.has_key(location_name):
			out_msg('get_location_objects', 'Location <' + location_name + '> not registered')
			return
		location = locations[location_name]
		
		if type(place) is str:
			tmp_place = location.get_place(place)
			if not tmp_place:
				out_msg('get_location_objects', 'Place <' + place + '> not found in location <' + location_name + '>')
				return
			place = tmp_place
			px, py = place.x + place.xsize / 2, place.y + place.ysize / 2
		else:
			px, py = place['x'], place['y']
		
		res = []
		for obj in location.objects:
			if not isinstance(obj, LocationObject):
				continue
			
			if obj_type is not None and obj_type != obj.type:
				continue
			
			dx, dy = obj.x - px, obj.y - py
			dist = math.sqrt(dx * dx + dy * dy)
			res.append((dist, obj))
		
		res.sort(key = lambda (dist, obj): dist)
		if count >= 0:
			res = res[:count]
		return [obj for dist, obj in res]
	
	def get_near_location_object():
		mx, my = me.x, me.y
		min_dist = character_radius * 5
		res = None
		
		for i in cur_location.objects:
			if not isinstance(i, LocationObject):
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
	
	
	def remove_location_object(location_name, place, obj_name, count = 1):
		if not locations.has_key(location_name):
			out_msg('remove_location_object', 'Location <' + location_name + '> not registered')
			return
		location = locations[location_name]
		
		if type(place) is str:
			tmp_place = location.get_place(place)
			if tmp_place is None:
				out_msg('remove_location_object', 'Place <' + place + '> in location <' + location_name + '> not found')
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
	
