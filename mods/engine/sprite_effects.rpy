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
				self.set_data_list()
		
		def copy(self, spr):
			res = Dissolve(self.time, spr)
			return res
		
		def set_data_list(self):
			self.sprite.data_list = (self.sprite.old_data, self.sprite.new_data)
		
		def for_all_scene(self):
			return False
		
		
		def update(self):
			global sprites_list
			
			now = time.time()
			dtime = now - self.start_time
			
			k = 1.8
			alpha = in_bounds(dtime / self.time * k, 0.0, 1.0)
			anti_alpha = in_bounds((1 - dtime / self.time) * k, 0.0, 1.0)
			
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


