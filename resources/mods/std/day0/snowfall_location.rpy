init -1000 python:
	
	class SnowfallLocation(Object):
		def __init__(self, xpos, ypos, xsize, ysize, **kwargs):
			Object.__init__(self)
			
			if kwargs.has_key('image'):
				self.image = kwargs['image']
			else:
				self.image = im.rect('#FFF')
			
			if kwargs.has_key('free'):
				self.free_image = kwargs['free']
			else:
				self.free_image = im.rect('#000', xsize, ysize)
			
			self.type = kwargs.get('name', 'snowfall_location')
			self.zorder = 1e7
			
			self.xsize, self.ysize = xsize, ysize
			
			self.min_dx = kwargs.get('min_dx', -0.0001)
			self.max_dx = kwargs.get('max_dx', 0.0001)
			self.min_dy = kwargs.get('min_dy', 0.0003)
			self.max_dy = kwargs.get('max_dy', 0.0010)
			self.min_size = kwargs.get('min_size', 1)
			self.max_size = kwargs.get('max_size', 2)
			
			self.objs = []
			self.set_count(kwargs.get('count', 100))
			
			self.prev_update_time = time.time()
		
		def set_count(self, count):
			rand_int = random.randint
			def rand_float(min, max):
				return random.random() * (max - min) + min
			
			old_count = len(self.objs)
			if count <= old_count:
				self.objs = self.objs[0:count]
			else:
				self.objs.extend([None] * (count - old_count))
				
				for i in xrange(count - old_count):
					x, y = rand_float(0, 1), rand_float(0, 1)
					dx, dy = rand_float(self.min_dx, self.max_dx), rand_float(self.min_dy, self.max_dy)
					size = rand_float(self.min_size, self.max_size)
					
					self.objs[old_count + i] = [x, y, dx, dy, size]
		
		def free(self):
			return None
		
		def set_direction(self, dx, dy):
			self.dx, self.dy = dx, dy
		
		def update(self):
			free = self.free_image
			
			dtime = time.time() - self.prev_update_time
			self.prev_update_time = time.time()
			
			w, h = self.xsize, self.ysize
			x, y, dx, dy = 0, 1, 2, 3
			for obj in self.objs:
				obj[x] = (obj[x] + obj[dx] * k) % 1
				obj[y] = (obj[y] + obj[dy] * k) % 1
				
				if random.random() < obj[dy] * 3:
					color = get_image_pixel(free, int(obj[x] * w), int(obj[y] * h))
					if (color & 255) == 255:
						obj[y] = 0
		
		def get_zorder(self):
			return self.zorder
		
		def get_draw_data(self):
			res = [None] * len(self.objs)
			
			w, h = self.xsize, self.ysize
			for i in xrange(len(self.objs)):
				x, y, dx, dy, size = self.objs[i]
				res[i] = {
					'image':   self.image,
					'size':    absolute(size),
					'pos':    (absolute(x * w), absolute(y * h)),
					'anchor': (0, 0),
					'crop':   (0, 0, 1.0, 1.0),
					'alpha':   1,
					'zorder':  self.get_zorder()
				}
			
			return res
		
