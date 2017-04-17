init -1000 python:
	
	class Sprite(Object):
		def __init__(self, decl_at, at, show_at, with_at, old_sprite = None):
			Object.__init__(self)
			
			self.new = get_inited_transform()
			self.old = old_sprite.new if old_sprite and with_at is not None else get_inited_transform()
			
			self.decl_at = Transition(decl_at, self)
			self.at      = Transition(at, self)
			self.show_at = Transition(show_at, self)
			
			self.set_with_at(with_at)
		
		def set_with_at(self, with_at):
			if with_at is not None and with_at.for_all_scene():
				if self is not screen:
					screen.set_with_at(with_at)
					screen.with_at.sprite = False
					with_at = None
			
			if with_at is not None:
				self.with_at = with_at.copy(self)
			else:
				self.with_at = None
				self.new_old_ordered = (self.new, self.old)
		
		def remove_with_at(self):
			global sprites_hide_list
			
			for i in xrange(len(sprites_hide_list)):
				if sprites_hide_list[i] is self:
					sprites_hide_list = sprites_hide_list[0:i] + sprites_hide_list[i+1:]
					break
			else:
				if self.with_at:
					if self.with_at.start_time:
						self.with_at.start_time = 0
						self.with_at.update()
					self.with_at = None
				self.new_old_ordered = (self.new, )
		
		
		def update(self):
			if not sprite_can_update and self is not screen:
				return
			
			self.decl_at.update()
			self.at.update()
			self.show_at.update()
			
			
			for trans in self.new_old_ordered:
				xsize = ysize = 0
				
				if trans.xsize is not None:
					xsize = get_absolute(trans.xsize, get_stage_width())
				else:
					if self.new.xsize is None and trans.image is not None:
						xsize = get_texture_width(trans.image)
					else:
						xsize = self.new.xsize
			
				if trans.ysize is not None:
					ysize = get_absolute(trans.ysize, get_stage_height())
				else:
					if self.new.ysize is None and trans.image is not None:
						ysize = get_texture_height(trans.image)
					else:
						ysize = self.new.ysize
				
				trans.real_xsize, trans.real_ysize = xsize, ysize
			
			for spr in self.new.contains:
				spr.update()
			
			if self.with_at:
				self.with_at.update()
		
		def __str__(self):
			return str(self.call_str)


