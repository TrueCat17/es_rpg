init -1000 python:
	
	class SnowfallLocation(SimpleObject):
		def __init__(self, xpos, ypos, xsize, ysize, **kwargs):
			SimpleObject.__init__(self)
			
			self.image = kwargs.get('image', im.rect('#FFF'))
			self.free_image = kwargs.get('free', im.rect('#000', xsize, ysize))
			
			self.type = kwargs.get('name', 'snowfall_location')
			self.zorder = 1e7
			
			self.xsize, self.ysize = xsize, ysize
			
			self.min_dx = kwargs.get('min_dx', -0.002)
			self.max_dx = kwargs.get('max_dx', 0.002)
			self.min_dy = kwargs.get('min_dy', 0.006)
			self.max_dy = kwargs.get('max_dy', 0.020)
			self.min_size = kwargs.get('min_size', 1)
			self.max_size = kwargs.get('max_size', 2)
			
			self.objs = []
			self.set_count(kwargs.get('count', 100))
		
		def set_count(self, count):
			old_count = len(self.objs)
			if count <= old_count:
				self.objs = self.objs[:count]
			else:
				self.objs.extend([None] * (count - old_count))
				
				for i in range(count - old_count):
					x, y = random.uniform(0, 1), random.uniform(0, 1)
					dx, dy = random.uniform(self.min_dx, self.max_dx), random.uniform(self.min_dy, self.max_dy)
					size = random.uniform(self.min_size, self.max_size)
					
					self.objs[old_count + i] = [absolute(v) for v in (x, y, dx, dy, size)]
		
		def update(self):
			free = self.free_image
			dtime = get_last_tick()
			
			w, h = self.xsize, self.ysize
			x, y, dx, dy = 0, 1, 2, 3
			for obj in self.objs:
				obj[x] = (obj[x] + obj[dx] * dtime) % 1
				obj[y] = (obj[y] + obj[dy] * dtime) % 1
				
				if random.random() < obj[dy] * 0.1:
					color = get_image_pixel(free, int(obj[x] * w), int(obj[y] * h))
					if (color & 255) == 255:
						obj[y] = 0
		
		def get_draw_data(self):
			res = [None] * len(self.objs)
			
			image = self.image
			zorder = self.zorder
			w, h = self.xsize, self.ysize
			
			for i, obj in enumerate(self.objs):
				x, y, dx, dy, size = obj
				obj = res[i] = SimpleObject()
				
				obj.image = image
				obj.size = size
				obj.pos = (x * w, y * h)
				obj.anchor = (0, 0)
				obj.zorder = zorder
			
			return res
		
		def free(self):
			return None
