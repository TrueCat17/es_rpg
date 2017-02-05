init python:
	
	def get_map_free():
		cs = character_xsize
		def near(x, y, width, height):
			return x - cs < me.x and me.x < x + width + cs and y - cs < me.y and me.y < y + height + cs
		
		objs = [obj for obj in objects_on_location if not isinstance(obj, Character)]
		characters = [obj for obj in objects_on_location if isinstance(obj, Character) and obj is not me]
		
		# Вычитаем 253.9/255 из каждого (rgb) канала, чтобы все цвета, кроме чисто-белого, стали чёрными
		matrix = im.matrix.identity()
		matrix.t = [i for i in matrix.t]
		matrix.t[4] = matrix.t[9] = matrix.t[14] = -253.9/255.0
		
		to_draw = [(cur_location.width, cur_location.height), (0, 0), cur_location.free]
		for obj in objs:
			if near(obj.x, obj.y - obj.height, obj.width, obj.height):
				to_draw += [(obj.x, obj.y - obj.height), im.MatrixColor(obj.free, im.matrix.invert() * matrix)]
		
		for character in characters:
			if near(character.x, character.y, 0, 0):
				to_draw += [(character.x - cs / 2, character.y - cs / 2), im.Rect('#FFFFFF', cs, cs)]
		
		if len(to_draw) != 3:
			res = im.Composite(*to_draw)
		else:
			res = cur_location.free
		return res
	
	
	def get_end_point(from_x, from_y, dx, dy):
		to_x, to_y = from_x + dx, from_y + dy
		if to_x > cur_location.width: 	to_x = cur_location.width - 1
		if to_x < 0:					to_x = 0
		if to_y > cur_location.height: 	to_y = cur_location.height - 1
		if to_y < 0:					to_y = 0
		dx, dy = to_x - from_x, to_y - from_y
		
		free = get_map_free()
		if free is None or (dx == 0 and dy == 0):
			return to_x, to_y
		
		rotations = (
			(-1, -1), # left-up: x == -1, y == -1
			( 0, -1), # up
			( 1, -1), # right-up
			( 1,  0), # ...
			( 1,  1),
			( 0,  1),
			(-1,  1),
			(-1,  0)
		)
		
		
		def sign(x):
			return -1 if x < 0 else 1 if x > 0 else 0
		
		def to_zero(x):
			return 0 if abs(x) < 1 else x + 1 if x < 0 else x - 1
		
		def part(x):
			return sign(x) if abs(x) > 1 else x
		
		black_color = 255 # r, g, b, a = 0, 0, 0, 255
		
		
		rot_index = rotations.index( (sign(dx), sign(dy)) )
		left1, right1 = rotations[(rot_index - 1) % len(rotations)], rotations[(rot_index + 1) % len(rotations)]
		left2, right2 = rotations[(rot_index - 2) % len(rotations)], rotations[(rot_index + 2) % len(rotations)]
		
		x, y = from_x, from_y
		while int(x + dx) != int(x) or int(y + dy) != int(y):
			pdx, pdy = part(dx), part(dy)
			dx, dy = to_zero(dx), to_zero(dy)
			
			dist = 0
			changed = False
			while not changed and dist <= character_radius:
				color1 = get_pixel(free, int(x + pdx + dist * left2[0]), int(y + pdy + dist * left2[1]))
				color2 = get_pixel(free, int(x + pdx + dist * right2[0]), int(y + pdy + dist * right2[1]))
				
				free1, free2 = color1 == black_color, color2 == black_color
				
				changed = True
				if free1 and free2:
					x, y = x + pdx, y + pdy
				elif free1:
					color_extra = get_pixel(free, int(x + dist * left1[0]), int(y + dist * left1[1]))
					if color_extra == black_color:
						x, y = x + left1[0], y + left1[1]
					else:
						x, y = x + left2[0], y + left2[1]
				elif free2:
					color_extra = get_pixel(free, int(x + dist * right1[0]), int(y + dist * right1[1]))
					if color_extra == black_color:
						x, y = x + right1[0], y + right1[1]
					else:
						x, y = x + right2[0], y + right2[1]
				else:
					changed = False
				dist += 1
				
			if not changed:
				dx = dy = 0
		
		return x + dx, y + dy

