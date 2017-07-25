init python:
	
	def get_map_free():
		cs = character_xsize
		def near(x, y, width, height):
			return x - cs < me.x and me.x < x + width + cs and y - cs < me.y and me.y < y + height + cs
		
		objs = [obj for obj in objects_on_location if not isinstance(obj, Character)]
		characters = [obj for obj in objects_on_location if isinstance(obj, Character) and obj is not me]
		
		# Вычитаем 253.9/255 из каждого (rgb) канала, чтобы все цвета, кроме чисто-белого, стали чёрными
		matrix = im.matrix.identity()
		matrix.t = [i for i in matrix.t] # tuple -> list
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
		
		black_color = 255 # r, g, b, a = 0, 0, 0, 255
		map_width, map_height = get_texture_width(free), get_texture_height(free)
		
		def is_black(x, y):
			x, y = int(x), int(y)
			if x < 0 or x >= map_width or y < 0 or y >= map_height:
				return False
			return get_pixel(free, x, y) == black_color
		
		s2 = 1 / (2 ** 0.5)
		rotations = (
			(-s2, -s2), # left-up: x == -1, y == -1
			(  0, -1 ), # up
			( s2, -s2), # right-up
			(  1,  0 ), # ...
			( s2,  s2),
			(  0,  1 ),
			(-s2,  s2),
			( -1,  0 )
		)
		
		
		def sign(x):
			return -1 if x < 0 else 1 if x > 0 else 0
		
		def to_zero(x):
			return 0 if abs(x) < 1 else x + 1 if x < 0 else x - 1
		
		def part(x):
			return sign(x) if abs(x) > 1 else x
		
		sdx, sdy = sign(dx), sign(dy)
		if sdx and sdy:
			sdx, sdy = sdx * s2, sdy * s2
		
		rot_index = rotations.index( (sdx, sdy) )
		left1, right1 = rotations[(rot_index - 1) % len(rotations)], rotations[(rot_index + 1) % len(rotations)]
		left2, right2 = rotations[(rot_index - 2) % len(rotations)], rotations[(rot_index + 2) % len(rotations)]
		
		x, y = from_x, from_y
		while int(x + dx) != int(x) or int(y + dy) != int(y):
			pdx, pdy = part(dx), part(dy)
			
			dist = 0
			changed = False
			while not changed and dist <= character_radius:
				free1 = is_black(x + pdx + dist * left2[0], y + pdy + dist * left2[1])
				free2 = is_black(x + pdx + dist * right2[0], y + pdy + dist * right2[1])
				
				changed = True
				if free1 and free2:
					dpoint = (pdx, pdy)
				elif free1:
					free_extra = is_black(x + dist * left1[0], y + dist * left1[1])
					dpoint = left1 if free_extra else left2
				elif free2:
					free_extra = is_black(x + dist * right1[0], y + dist * right1[1])
					dpoint = right1 if free_extra else right2
				else:
					changed = False
				dist += 1
				
			if not changed:
				dx = dy = 0
			else:
				dx, dy = to_zero(dx), to_zero(dy)
				x, y = x + dpoint[0], y + dpoint[1]
		
		return x + dx, y + dy

