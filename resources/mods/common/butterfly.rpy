init -10 python:
	
	def add_butterflies(min, max):
		for name, location in rpg_locations.iteritems():
			if location.is_room: continue
			
			count = random.randint(min, max)
			for i in xrange(count):
				x = random.randint(0, location.xsize - 1)
				y = random.randint(0, location.ysize - 1)
				add_location_object(name, {'x': x, 'y': y}, Butterfly)
	
	class Butterfly(Object):
		
		standart_image = 'images/misc/butterfly.png'
		
		def __init__(self, xpos, ypos, xsize, ysize, **kwargs):
			Object.__init__(self)
			self.xpos, self.ypos = xpos + xsize / 2, ypos + ysize / 2
			
			self.count_frames = 5
			self.frame = random.randint(0, self.count_frames - 1)
			self.fps = 10
			
			self.xsize, self.ysize = get_image_size(Butterfly.standart_image)
			self.xsize /= self.count_frames
			
			self.rotate = random.randint(0, 359)
			self.xspeed = 0.0
			self.yspeed = 0.0
			
			self.rotate_chance = 10.0 # ~updates/sec
			self.rotate_max = 10 # degrees
			
			self.speed = random.randint(40, 70) # px/sec
			self.alarm_dist = 100
			self.fast_k = 1.7  # for speed and framerate
			
			self.set_color()
			self.update_frame()
		
		def set_color(self, color = None):
			if color is None:
				r = random.randint( 64, 255)
				g = random.randint(128, 255)
				b = random.randint(128, 255)
				a = random.randint(192, 255)
			else:
				r, g, b, a = renpy.easy.color(color)
			self.image = im.recolor(Butterfly.standart_image, r, g, b, a)
		
		def update_frame(self):
			frame = int(self.frame) % self.count_frames
			self.crop = (frame * self.xsize, 0, self.xsize, self.ysize)
		
		def get_draw_data(self):
			return {
				'image':  self.image,
				'crop':   self.crop,
				'pos':    (absolute(self.xpos), absolute(self.ypos)),
				'size':   (self.xsize, self.ysize),
				'rotate': self.rotate,
			}
		
		
		def get_dist(self, x, y, w, h, chs):
			dist = min(self.alarm_dist, x, y, w - 1 - x, h - 1 - y)
			for character in chs:
				dist = min(dist, get_dist(x, y, character.x, character.y))
			return dist
		
		def get_next_pos(self, x, y, rotate, speed):
			# - 90, because not rotated = to up, not to right
			return x + _cos(rotate - 90) * speed, y + _sin(rotate - 90) * speed
		
		def update(self):
			if has_screen('pause'):
				return
			
			x, y = self.xpos, self.ypos
			location = self.location
			w, h = location.xsize, location.ysize
			chs = [character for character in characters if character.location is location and get_dist(x, y, character.x, character.y) < self.alarm_dist]
			
			k = get_last_tick()
			
			if 0 <= x < w and 0 <= y < h:
				dist = self.get_dist(x, y, w, h, chs)
				if dist < self.alarm_dist:
					k *= self.fast_k
					if random.random() < self.rotate_chance * k:
						max_dist, need_rotate = 0, 0
						for angle in (-7, 0, 7):
							rotate = self.rotate + angle
							nx, ny = self.get_next_pos(x, y, rotate, self.speed * k)
							dist = self.get_dist(nx, ny, w, h, chs)
							if dist > max_dist:
								max_dist = dist
								need_rotate = rotate
						self.rotate = need_rotate
				else:
					if random.random() < self.rotate_chance * k:
						self.rotate += random.randint(-self.rotate_max, +self.rotate_max)
			else:
				dx, dy = w / 2 - x, h / 2 - y
				self.rotate = int(math.atan2(dy, dx) * 180 / math.pi) + 90
			
			self.frame += self.fps * k
			self.update_frame()
			self.xpos, self.ypos = self.get_next_pos(x, y, self.rotate, self.speed * k)
		
