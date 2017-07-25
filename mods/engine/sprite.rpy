init -9000 python:
	
	class Sprite(Object):
		def __init__(self, decl_at, at, show_at, effect, old_sprite = None):
			Object.__init__(self)
			
			self.hiding = False
			
			self.new_data = SpriteAnimationData()
			self.old_data = old_sprite.new_data if (old_sprite and effect) else SpriteAnimationData()
			
			self.new_animations = [SpriteAnimation(decl_at, self), SpriteAnimation(at, self), SpriteAnimation(show_at, self)]
			self.old_animations = old_sprite.new_animations if old_sprite else []
			
			self.set_effect(effect)
		
		def set_effect(self, effect):
			if effect and effect.for_all_scene():
				if self is not screen:
					screen.set_effect(effect)
					screen.effect.sprite = False
					effect = None
			
			if effect:
				self.effect = effect.copy(self)
			else:
				self.effect = None
				self.data_list = [self.old_data, self.new_data]
		
		def remove_effect(self):
			global sprites_list
			
			if self.hiding:
				for i in xrange(len(sprites_list)):
					if sprites_list[i] is self:
						sprites_list = sprites_list[0:i] + sprites_list[i+1:]
						break
			else:
				if self.effect:
					if self.effect.start_time:
						self.effect.start_time = 0
						self.effect.update()
					self.effect = None
				self.data_list = [self.new_data]
		
		
		def update(self):
			if not sprite_can_update and self is not screen:
				return
			
			for animation in self.old_animations + self.new_animations:
				animation.update()
			
			
			for data in self.data_list:
				xsize = ysize = 0
				
				if data.xsize is not None:
					xsize = get_absolute(data.xsize, get_stage_width())
				else:
					if self.new_data.xsize is None and data.image:
						xsize = get_texture_width(data.image)
					else:
						xsize = self.new_data.xsize
			
				if data.ysize is not None:
					ysize = get_absolute(data.ysize, get_stage_height())
				else:
					if self.new_data.ysize is None and data.image:
						ysize = get_texture_height(data.image)
					else:
						ysize = self.new_data.ysize
				
				data.real_xsize, data.real_ysize = xsize, ysize
			
			if self.effect:
				self.effect.update()
			
			
			for data in self.data_list:
				for spr in data.contains:
					spr.update()
		
		def __str__(self):
			return str(self.call_str)


