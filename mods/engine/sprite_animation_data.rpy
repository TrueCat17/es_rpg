init -9000 python:
	
	class SpriteAnimationData(Object):
		def __init__(self):
			Object.__init__(self)
			
			self.xpos, self.ypos = 0, 0
			self.xanchor, self.yanchor = 0, 0
			self.xsize, self.ysize = None, None
			self.xcrop, self.ycrop, self.xsizecrop, self.ysizecrop = 0, 0, 1.0, 1.0
			self.alpha = 1.0
			self.rotate = 0
			
			self.contains = []
			self.image = None
		
		
		def get_all_data(self):
			sw, sh = get_stage_width(), get_stage_height()
			
			self.real_xpos    = get_absolute(self.xpos, sw)
			self.real_ypos    = get_absolute(self.ypos, sh)
			self.real_xanchor = get_absolute(self.xanchor, self.real_xsize)
			self.real_yanchor = get_absolute(self.yanchor, self.real_ysize)
			self.real_alpha   = self.alpha
			self.real_rotate  = self.rotate
			
			res = [self]
			
			for spr in self.contains:
				for spr_data in spr.data_list:
					for data in spr_data.get_all_data():
						data.real_xpos    += self.real_xpos
						data.real_ypos    += self.real_ypos
						data.real_xanchor += self.real_xanchor
						data.real_yanchor += self.real_yanchor
						data.real_alpha   *= self.real_alpha
						data.real_rotate  += self.real_rotate
						res.append(data)
			
			return res
	
	
