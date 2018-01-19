init -9000 python:
	
	class Fade(Object):
		def __init__(self, out_time, hold_time = 0, in_time = None, color = '000', spr = None):
			Object.__init__(self)
			
			if in_time is None:
				in_time = out_time
			
			if out_time <= 0:
				out_time = 0.001
			if hold_time <= 0:
				hold_time = 0.001
			if in_time <= 0:
				in_time = 0.001
			
			self.out_time, self.hold_time, self.in_time = out_time, hold_time, in_time
			self.start_time = time.time()
			
			self.color = color
			
			self.sprite = spr
			if spr:
				self.set_data_list()
				
				global sprite_can_update
				sprite_can_update = False
		
		def copy(self, spr):
			res = Fade(self.out_time, self.hold_time, self.in_time, self.color, spr)
			return res
		
		def set_data_list(self):
			screen.background = SpriteAnimationData()
			screen.background.alpha = 0
			screen.background.image = im.Rect(self.color, 1, 1)
			
			screen.new_data.alpha = 0
			
			if self.sprite:
				screen.data_list = [self.sprite.old_data, self.sprite.new_data, self.sprite.background]
		
		def for_all_scene(self):
			return True
		
		
		def update(self):
			now = time.time()
			dtime = now - self.start_time
			
			screen.background.real_xsize = screen.new_data.real_xsize
			screen.background.real_ysize = screen.new_data.real_ysize
			
			if dtime < self.out_time + self.hold_time:
				screen.background.alpha = in_bounds(dtime / self.out_time, 0.0, 1.0)
			else:
				global sprite_can_update
				
				if not sprite_can_update:
					to_delete = [] if self.sprite is not False else [spr for spr in sprites_list if spr.hiding]
					for spr in to_delete:
						spr.remove_effect()
					
					screen.new_data.alpha = 1.0
					screen.data_list = [screen.new_data, screen.background]
				
				sprite_can_update = True
				
				screen.background.alpha = 1 - in_bounds((dtime - self.out_time - self.hold_time) / self.out_time, 0.0, 1.0)
				if screen.background.alpha == 0:
					if self.sprite:
						self.sprite.remove_effect()
					elif self is screen.effect:
						screen.remove_effect()
	
	
	
	fade = Fade(0.5)
	fade2 = Fade(1)
	fade3 = Fade(1.5)
	
	flash = Fade(1, color="#FFF")
	flash2 = Fade(2, 2, 2, color="#FFF")
	flash_red = Fade(1, color="#E11")
	
	
	
	
	class Dissolve(Object):
		def __init__(self, t, spr = None):
			Object.__init__(self)
			
			if t <= 0:
				t = 0.001
			
			self.time = t
			self.start_time = time.time()
			
			self.sprite = spr
			if spr:
				spr.old_data.except_state_props.add('alpha')
				spr.new_data.except_state_props.add('alpha')
				
				spr.data_list = [spr.old_data, spr.new_data]
				spr.update()
				self.set_data_list()
		
		def copy(self, spr):
			res = Dissolve(self.time, spr)
			return res
		
		def set_data_list(self):
			def rotate_point(x, y, xcenter, ycenter, angle):
				sina, cosa = _sin(angle), _cos(angle)
				tx, ty = x - xcenter, y - ycenter
				rx, ry = tx * cosa - ty * sina, tx * sina + ty * cosa
				return rx + xcenter, ry + ycenter
			def rotate_rect(xmin, ymin, xmax, ymax, xcenter, ycenter, angle):
				points = (rotate_point(xmin, ymin, xcenter, ycenter, angle),
				          rotate_point(xmin, ymax, xcenter, ycenter, angle),
				          rotate_point(xmax, ymin, xcenter, ycenter, angle),
				          rotate_point(xmax, ymax, xcenter, ycenter, angle)
				)
				xmin = min(points, key = lambda point: point[0])[0]
				ymin = min(points, key = lambda point: point[1])[1]
				xmax = max(points, key = lambda point: point[0])[0]
				ymax = max(points, key = lambda point: point[1])[1]
				return xmin, ymin, xmax, ymax
			
			cache = {}
			def get_rect(data):
				if cache.has_key(data):
					return cache[data]
				
				xanchor, yanchor = data.real_xanchor, data.real_yanchor
				x, y, xsize, ysize = data.real_xpos - xanchor, data.real_ypos - yanchor, data.real_xsize, data.real_ysize
				xmin, ymin, xmax, ymax = x, y, x + xsize, y + ysize
				
				rotate = int(data.real_rotate) % 360
				if rotate:
					res = rotate_rect(xmin, ymin, xmax, ymax, x + xanchor, y + yanchor, rotate)
				else:
					res = xmin, ymin, xmax, ymax
				
				cache[data] = res
				return res
			
			def intersection_rects(xmin1, ymin1, xmax1, ymax1, xmin2, ymin2, xmax2, ymax2):
				return xmax1 > xmin2 and xmax2 > xmin1 and ymax1 > ymin2 and ymax2 > ymin1
			
			new_datas = self.sprite.new_data.get_all_data()
			old_datas = self.sprite.old_data.get_all_data()
			
			make_common = False
			if self.sprite is not screen:
				for new_data in new_datas:
					if not new_data.image:
						continue
					
					xmin1, ymin1, xmax1, ymax1 = get_rect(new_data)
					
					for old_data in old_datas:
						if not old_data.image:
							continue
						
						xmin2, ymin2, xmax2, ymax2 = get_rect(old_data)
						
						if intersection_rects(xmin1, ymin1, xmax1, ymax1, xmin2, ymin2, xmax2, ymax2):
							make_common = True
							break
					if make_common:
						break
			
			if not make_common:
				self.sprite.data_list = (self.sprite.old_data, self.sprite.new_data)
			else:
				all_rects = [get_rect(data) for data in new_datas + old_datas if data.image is not None]
				
				xmin = min(all_rects, key = lambda rect: rect[0])[0]
				ymin = min(all_rects, key = lambda rect: rect[1])[1]
				xmax = max(all_rects, key = lambda rect: rect[2])[2]
				ymax = max(all_rects, key = lambda rect: rect[3])[3]
				
				width, height = xmax - xmin, ymax - ymin
				if width <= 0 or height <= 0:
					self.sprite.data_list = (self.sprite.old_data, self.sprite.new_data)
				else:
					new_image_args, old_image_args = [(width, height)], [(width, height)]
					for args, datas in ((new_image_args, new_datas), (old_image_args, old_datas)):
						for data in datas:
							image = data.image
							if not image:
								continue
							
							image_xsize, image_ysize = get_texture_width(data.image), get_texture_height(data.image)
							res_xsize, res_ysize = data.real_xsize, data.real_ysize
							if (res_xsize, res_ysize) != (image_xsize, image_ysize):
								image = im.Scale(image, res_xsize, res_ysize)
							
							crop = [data.xcrop, data.ycrop, data.xsizecrop, data.ysizecrop]
							if crop != [0, 0, 1, 1] and crop != [0, 0, image_xsize, image_ysize]:
								for i in xrange(4):
									prop = crop[i]
									if (prop > 0 and prop < 1) or (prop == 1.0 and type(prop) is float):
										crop[i] = get_absolute(prop, image_ysize if i % 2 else image_xsize)
								image = im.Crop(image, crop)
							
							if data.real_alpha == 10:
								image = im.Alpha(image, data.real_alpha)
							
							rotate = int(data.real_rotate) % 360
							if rotate:
								image = im.Rotozoom(image, -rotate, 1)
							
							_xmin, _ymin, _xmax, _ymax = get_rect(data)
							args.append((_xmin - xmin, _ymin - ymin))
							args.append(image)
					
					new_image, old_image = im.Composite(*new_image_args), im.Composite(*old_image_args)
					
					common_data = SpriteAnimationData()
					common_data.image = im.Mask(new_image, old_image, 128, 'a', 'ge', 'a', 1)
					common_data.xpos, common_data.ypos = xmin, ymin
					
					self.sprite.data_list = (common_data, self.sprite.old_data, self.sprite.new_data)
					
					self.state_num = sum(data.state_num for data in new_datas + old_datas if data.image)
		
		def for_all_scene(self):
			return False
		
		
		def update(self):
			global sprites_list
			
			if self.sprite and len(self.sprite.data_list) == 3:
				new_datas = self.sprite.new_data.get_all_data()
				old_datas = self.sprite.old_data.get_all_data()
				
				state_num = sum(data.state_num for data in new_datas + old_datas if data.image)
				if self.state_num != state_num:
					self.set_data_list()
					self.sprite.update_data_size()
			
			now = time.time()
			dtime = now - self.start_time
			
			alpha = in_bounds(dtime / self.time, 0.0, 1.0)
			anti_alpha = in_bounds(1 - dtime / self.time, 0.0, 1.0)
			
			if self.sprite:
				self.sprite.new_data.alpha = alpha
				self.sprite.old_data.alpha = anti_alpha
				
				if alpha == 1:
					self.sprite.remove_effect()
			elif self.sprite is False:
				for spr in sprites_list:
					for data in spr.data_list:
						data.alpha = alpha if not spr.hiding else anti_alpha
				
				if alpha == 1:
					i = 0
					while i < len(sprites_list):
						if sprites_list[i].hiding:
							sprites_list = sprites_list[0:i] + sprites_list[i+1:]
						else:
							spr.remove_effect()
							i += 1
	
	
	dspr = Dissolve(0.2)
	dissolve = Dissolve(0.5)
	dissolve2 = Dissolve(1)
	
	
	
	class Punch(Object):
		def __init__(self, prop, dist, time_one, time_all):
			Object.__init__(self)
			
			self.prop, self.dist, self.time_one, self.time_all = prop, dist, time_one, time_all
			self.start_time = time.time()
		
		def for_all_scene(self):
			return True
		
		def copy(self, spr = None):
			return Punch(self.prop, self.dist, self.time_one, self.time_all)
		
		
		def update(self):
			global sprites_list
			i = 0
			for spr in sprites_list:
				if spr.hiding and spr.effect is None:
					sprites_list = sprites_list[0:i] + sprites_list[i+1:]
				else:
					i += 1
			
			now = time.time()
			dtime = now - self.start_time
			
			if dtime > self.time_all:
				screen.new_data[self.prop] = 0
				screen.remove_effect()
			else:
				t = (dtime % self.time_one) / self.time_one # 0.0 -> 1.0
				
				if True:                      # Дёргано, резко
					t = 1 if t > 0.5 else -1
				else:                         # Плавно
					if t > 0.5:
						t = 1 - t
					t *= 2
				
				m = 1 if int(dtime / self.time_one) % 2 else -1
				
				screen.new_data[self.prop] = round(t * m * self.dist)
	
	
	hpunch = Punch('xpos', 10, 0.1, 0.5)
	vpunch = Punch('ypos',  7, 0.1, 0.5)
	
	
	
	class ImageDissolve(Object):
		def __init__(self, mask, t = 1.0, ramp = 5, reverse = False, spr = None):
			Object.__init__(self)
			
			if t <= 0:
				t = 0.001
			if ramp < 1:
				ramp = 1
			
			self.mask, self.time, self.ramp, self.reverse = mask, t, ramp, reverse
			self.start_time = time.time()
			
			self.sprite = spr
			if spr:
				self.set_data_list()
		
		def copy(self, spr):
			res = ImageDissolve(self.mask, self.time, self.ramp, self.reverse, spr)
			return res
		
		def set_data_list(self):
			self.sprite.data_list = (self.sprite.old_data, self.sprite.new_data)
		
		def for_all_scene(self):
			return False
		
		
		def update(self):
			global sprites_list
			
			now = time.time()
			dtime = now - self.start_time
			
			def upd_spr_data(data, k_time, mask, ramp, reverse, hiding):
				if not data.image:
					data.res_image = data.image = None
					return
				
				if hiding:
					reverse = not reverse
					mask = im.MatrixColor(mask, im.matrix.invert())
				
				sw, sh = get_stage_width(), get_stage_height()
				w, h = get_texture_width(data.image), get_texture_height(data.image)
				if w > sw or h > sh:
					kw = float(sw) / w
					kh = float(sh) / h
					k = max(kw, kh)
					w, h = int(w * k), int(h * k)
					image = im.Scale(data.image, w, h)
				else:
					image = data.image
				mask = im.Scale(mask, w, h)
				
				value = in_bounds(int(k_time * 255), 0, 255)
				if reverse:
					value = 255 - value
				if value != 255:
					value = int(value / ramp) * ramp
				data.res_image = im.Mask(image, mask, value, 'r', 'le', 'a', 1)
			
			
			scene = sprites_list[0] if sprites_list else None
			
			if self.sprite:
				if self.sprite is scene:
					scene.old_data.res_image = scene.old_data.image
				else:
					upd_spr_data(self.sprite.old_data, dtime / self.time, self.mask, self.ramp, self.reverse, True)
				upd_spr_data(self.sprite.new_data, dtime / self.time, self.mask, self.ramp, self.reverse, False)
				
				if dtime >= self.time:
					self.sprite.remove_effect()
			elif self.sprite is False:
				for spr in sprites_list:
					if spr is not scene:
						for data in spr.data_list:
							upd_spr_data(data, dtime / self.time, self.mask, self.ramp, self.reverse, spr.hiding)
				
				if scene:
					scene.old_data.res_image = scene.old_data.image
					upd_spr_data(scene.new_data, dtime / self.time, self.mask, self.ramp, self.reverse, False)
				
				if dtime >= self.time:
					i = 0
					while i < len(sprites_list):
						if sprites_list[i].hiding:
							sprites_list = sprites_list[0:i] + sprites_list[i+1:]
						else:
							spr.remove_effect()
							i += 1
	
