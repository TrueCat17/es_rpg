init -9000 python:
	
	class ImageDissolve(Object):
		for_all_scene = False
		
		def __init__(self, mask, t = 1.0, ramp = 5, reverse = False, spr = None):
			Object.__init__(self)
			
			self.start_time = time.time()
			self.mask = mask
			self.time = max(t, 0.001)
			self.ramp = max(ramp, 1)
			self.reverse = reverse
			
			self.sprite = spr
		
		def copy(self, spr):
			load_image(self.mask)
			
			res = ImageDissolve(self.mask, self.time, self.ramp, self.reverse, spr)
			return res
		
		def update(self):
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
			
			new_data, old_data = self.sprite.new_data, self.sprite.old_data
			
			if self.sprite is scene:
				if old_data:
					old_data.res_image = old_data.image
				if new_data:
					upd_spr_data(new_data, dtime / self.time, self.mask, self.ramp, self.reverse, False)
				
				if dtime >= self.time:
					self.sprite.remove_effect()
					remove_hiding_sprites()
			else:
				if old_data:
					upd_spr_data(old_data, dtime / self.time, self.mask, self.ramp, self.reverse, True)
				if new_data:
					upd_spr_data(new_data, dtime / self.time, self.mask, self.ramp, self.reverse, False)
				
				if dtime >= self.time:
					self.sprite.remove_effect()
		
		def remove(self):
			self.for_not_hiding()
		
		def for_not_hiding(self):
			if self.sprite.new_data:
				self.sprite.new_data.res_image = self.sprite.new_data.image

