label wi_loop:
	$ words_invaders_fail = False
	while len(wi_phrases) and not words_invaders_fail:
		$ wi_add_words(wi_phrases[0])
		$ wi_phrases.pop(0)


init python:
	wi_size = 600
	
	wi_attack_time = 1
	wi_attack_start = 2
	wi_attack_last = 0
	wi_symbol_attack_speed = 30
	
	wi_symbol_xspeed = 20
	wi_symbol_xsize = 18
	wi_symbol_ysize = 30
	wi_max_line_size = wi_symbol_xsize * 30
	
	wi_to_left = False
	
	wi_player_acceleration = 4000
	wi_player_friction = 0.85
	wi_player_speed = 0
	wi_player_xpos = 0
	wi_player_ypos = 450
	wi_player_size = (100, 100)
	
	wi_player_symbol_ypos = wi_player_ypos + wi_player_size[1] + 20
	
	wi_bullet_speed = 2000
	wi_bullet_xsize = 10
	wi_bullet_ysize = 20
	
	wi_dir = os.path.dirname(get_filename(0))
	wi_player_image = wi_dir + '/ship.webp'
	wi_bullet_image = wi_dir + '/bullet.webp'
	
	
	wi_gaming = False
	def words_invaders_finished():
		return not wi_gaming
	can_exec_next_check_funcs.append(words_invaders_finished)
	
	def words_invaders(phrases):
		global wi_phrases
		wi_phrases = list(phrases)
		
		global wi_player_symbols
		wi_player_symbols = wi_get_array_symbols('Стабильная психика', 1.5, 1e9)
		xmin = wi_player_symbols[0]['x']
		xmax = wi_player_symbols[-1]['x']
		xsize = xmax - xmin
		dx = (wi_size - xsize) / 2
		for symbol in wi_player_symbols:
			symbol['x'] += dx
			symbol['y'] = wi_player_symbol_ypos
		
		renpy.call('wi_loop')
	
	
	def wi_get_array_symbols(symbols, kx, xmax):
		res = []
		symbol = ''
		x = wi_symbol_xsize / 2
		y = wi_symbol_ysize / 2
		for byte in symbols:
			if is_first_byte(byte):
				if symbol and symbol != ' ':
					res.append({
						'symbol': symbol,
						'x': x,
						'y': y,
						'attack': False,
					})
					x += wi_symbol_xsize * kx
					if x >= xmax:
						x = wi_symbol_xsize / 2
						y += wi_symbol_ysize
				symbol = ''
			symbol += byte
		if symbol and symbol != ' ':
			res.append({
				'symbol': symbol,
				'x': x,
				'y': y,
				'attack': False,
			})
		return res
	
	wi_symbols = []
	wi_bullets = []
	wi_player_symbols = []
	def wi_add_words(phrase):
		if not renpy.has_screen('words_invaders'):
			renpy.show_screen('words_invaders')
			save_rpg_control()
			set_rpg_control(False)
		
		global wi_gaming, wi_symbols, wi_bullets
		wi_gaming = True
		wi_symbols = wi_get_array_symbols(phrase, 3, wi_max_line_size)
		wi_bullets = []
		
		global wi_to_left
		wi_to_left = False
		
		global wi_player_xpos, wi_player_speed
		wi_player_xpos = wi_size / 2
		wi_player_speed = 0
		
		global wi_attack_last
		wi_attack_last = get_game_time() + wi_attack_start
	
	
	def wi_update():
		global wi_to_left
		
		dtime = get_last_tick()
		i = 0
		while i < len(wi_bullets):
			bullet_props = wi_bullets[i]
			bullet_props['y'] -= wi_bullet_speed * dtime
			if bullet_props['y'] < 0:
				wi_bullets.pop(i)
				continue
			
			bx = bullet_props['x'] - wi_bullet_xsize / 2
			by = bullet_props['y'] - wi_bullet_ysize / 2
			
			for j in xrange(len(wi_symbols)):
				symbol = wi_symbols[j]
				sx = symbol['x'] - wi_symbol_xsize / 2
				sy = symbol['y'] - wi_symbol_ysize / 2
				
				if rects_intersects(bx, by, wi_bullet_xsize, wi_bullet_ysize, sx, sy, wi_symbol_xsize, wi_symbol_ysize):
					wi_symbols.pop(j)
					wi_bullets.pop(i)
					i -= 1
					break
			
			i += 1
		
		global wi_attack_last
		if get_game_time() - wi_attack_last > wi_attack_time:
			indeces = range(len(wi_symbols))
			
			while indeces:
				index = random.choice(indeces)
				indeces.remove(index)
				
				attacker = wi_symbols[index]
				if attacker['attack']:
					continue
				
				for symbol in wi_symbols:
					if abs(symbol['x'] - attacker['x']) > wi_symbol_xsize:
						continue
					if symbol['y'] > attacker['y']:
						attacker = None
						break
				if not attacker:
					continue
				
				ok = False
				for symbol in wi_player_symbols:
					if abs(symbol['x'] - attacker['x']) < wi_symbol_xsize / 2:
						ok = True
						break
				if ok:
					attacker['attack'] = True
					wi_attack_last = get_game_time()
					break
		
		if wi_symbols:
			dy = 0
			
			if wi_to_left:
				xmin = wi_symbols[0]['x']
				for symbol in wi_symbols:
					xmin = min(xmin, symbol['x'])
				
				new_xmin = xmin - wi_symbol_xspeed * dtime
				if new_xmin < 0:
					new_xmin = 0
					dy = wi_symbol_ysize
					wi_to_left = not wi_to_left
				dx = new_xmin - xmin
			else:
				xmax = wi_symbols[0]['x']
				for symbol in wi_symbols:
					xmax = max(xmax, symbol['x'])
				
				new_xmax = xmax + wi_symbol_xspeed * dtime
				if new_xmax > wi_size:
					new_xmax = wi_size
					dy = wi_symbol_ysize
					wi_to_left = not wi_to_left
				dx = new_xmax - xmax
			
			for symbol in wi_symbols:
				if symbol['attack']:
					symbol['y'] += wi_symbol_attack_speed * dtime
				else:
					symbol['x'] += dx
					symbol['y'] += dy
		
		
		global wi_player_xpos, wi_player_speed
		wi_player_xpos = in_bounds(wi_player_xpos + wi_player_speed * dtime, 0, wi_size)
		wi_player_speed *= wi_player_friction
		
		i = 0
		while i < len(wi_symbols):
			symbol = wi_symbols[i]
			sx = symbol['x'] - wi_symbol_xsize / 2
			sy = symbol['y'] - wi_symbol_ysize / 2
			
			if symbol['y'] > wi_size:
				wi_symbols.pop(i)
				continue
			
			for j in xrange(len(wi_player_symbols)):
				psymbol = wi_player_symbols[j]
				px = psymbol['x'] - wi_symbol_xsize / 2
				py = psymbol['y'] - wi_symbol_ysize / 2
				
				if rects_intersects(sx, sy, wi_bullet_xsize, wi_bullet_ysize, px, py, wi_symbol_xsize, wi_symbol_ysize):
					wi_player_symbols.pop(j)
					wi_symbols.pop(i)
					i -= 1
					break
			
			i += 1
		
		global words_invaders_fail, wi_gaming
		if not wi_player_symbols:
			renpy.hide_screen('words_invaders')
			return_prev_rpg_control()
			words_invaders_fail = True
			wi_gaming = False
		elif not wi_symbols:
			renpy.hide_screen('words_invaders')
			return_prev_rpg_control()
			words_invaders_fail = False
			wi_gaming = False
	
	
	def wi_left():
		global wi_player_speed
		wi_player_speed -= wi_player_acceleration * get_last_tick()
	def wi_right():
		global wi_player_speed
		wi_player_speed += wi_player_acceleration * get_last_tick()
	
	def wi_make_bullet():
		wi_bullets.append({
			'x': wi_player_xpos,
			'y': wi_player_ypos,
		})


screen words_invaders:
	$ wi_update()
	
	size wi_size
	align 0.5
	
	image im.rect('#000'):
		size wi_size + 20
		align 0.5
		alpha 0.3
	
	for symbol in wi_symbols:
		text symbol['symbol']:
			anchor       0.5
			xpos         absolute(symbol['x'])
			ypos         absolute(symbol['y'])
			font        'Consola'
			text_size    wi_symbol_ysize
			color        0xFFFFFF
			outlinecolor 0
	
	for symbol in wi_player_symbols:
		text symbol['symbol']:
			anchor       0.5
			xpos         absolute(symbol['x'])
			ypos         absolute(symbol['y'])
			font        'Consola'
			text_size    wi_symbol_ysize
			color        0x00FF00
			outlinecolor 0x008000
	
	image wi_player_image:
		xanchor 0.5
		xpos absolute(wi_player_xpos)
		ypos wi_player_ypos
		size wi_player_size
	
	for bullet in wi_bullets:
		image wi_bullet_image:
			anchor 0.5
			xpos   absolute(bullet['x'])
			ypos   absolute(bullet['y'])
			size   (wi_bullet_xsize, wi_bullet_ysize)
	
	
	key 'LEFT'  first_delay 0 action wi_left
	key 'RIGHT' first_delay 0 action wi_right
	key 'a'     first_delay 0 action wi_left
	key 'd'     first_delay 0 action wi_right
	
	key 'SPACE' first_delay 1 delay 1 action wi_make_bullet











