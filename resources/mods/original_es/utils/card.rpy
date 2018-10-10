init python:
	card_time_koef = 1.0 / 7 * 7
	
	class Card(Object):
		def __init__(self, name, is_my):
			Object.__init__(self)
			
			self.is_my = is_my
			self.index = len(cards_my if is_my else cards_rival)
			
			self.name = name
			self.visible = is_my
			
			self.x = 0.5 - 0.5 * card_width / get_stage_width()
			self.y = 0.5 - 0.5 * card_height / get_stage_height()
			self.move()
			self.update_pos()
			self.update_view()
			
			self.interesting = False
			self.hot = False
			self.allow = False
		
		def move(self):
			self.from_x, self.from_y = self.x, self.y
			
			sw, sh = get_stage_size()
			
			self.to_x = float(card_width / 4 + card_width * self.index + card_indent * (self.index - 1)) / sw
			self.to_y = (0.93 if self.is_my else 0.07) * (1 - float(card_height) / sh)
			
			dist = get_dist(self.to_x * sw, self.to_y * sh, self.from_x * sw, self.from_y * sh)
			
			self.time_start = time.time()
			self.time_end = self.time_start + card_time_koef * (dist**0.25)
		
		def update_view(self):
			if self.visible or self.name == card_none:
				self.ground = card_img[self.name]
			else:
				self.ground = card_img["cover"]
			
			if self.is_my:
				is_button = cards_state in ("me_defend_1", "me_defend_2", "rival_select")
			else:
				is_button = cards_state == "me_select" and self.allow
			
			if is_button:
				self.hover = im.MatrixColor(self.ground, im.matrix.brightness(0.1) * im.matrix.saturation(1.5))
				self.mouse = True
				self.action = SetVariable('answer', (self.is_my, self.index))
			else:
				self.ground = self.hover = im.MatrixColor(self.ground, im.matrix.saturation(0.1))
				self.mouse = False
				self.action = None
		
		def update_pos(self):
			if self.time_end <= time.time():
				self.x, self.y = self.to_x, self.to_y
			else:
				dtime = (time.time() - self.time_start) / (self.time_end - self.time_start)
				self.x = self.from_x + (self.to_x - self.from_x) * dtime
				self.y = self.from_y + (self.to_y - self.from_y) * dtime

