init 10 python:
	odn     = Character('Одногруппник',      color = 0xFFFFFF)
	lk      = Character('Луркмор-кун',       color = 0xFFFFFF)
	message = Character('Сообщение',         color = 0xFFFFFF)
	dy      = Character('Голос из динамика', color = 0xFF0000)
	bush    = Character('Голос',             color = 0x808080)
	voice   = Character('Голос',             color = 0x808080)
	voices  = Character('Голоса',            color = 0x808080)
	all     = Character('Пионеры',           color = 0xFF0000)
	kids    = Character('Малышня',           color = 0xFFFF00)
	
	mt_voice = Character('Голос',  color = 0x00EE33)
	pi       = Character('Пионер', color = 0xFF0000)
	
	sm        = Character('Семён', color = 0xEEEEAA)
	dreamgirl = Character('...',   color = 0xFFFFFF)
	
	dv = Character('Алиса',            unknown_name = 'Пионерка',         color = 0xDD9900)
	un = Character('Лена',             unknown_name = 'Пионерка',         color = 0xBB55FF)
	sl = Character('Славя',            unknown_name = 'Пионерка',         color = 0xEEEE00)
	mi = Character('Мику',             unknown_name = 'Пионерка',         color = 0x00DDFF)
	us = Character('Ульяна',           unknown_name = 'Пионерка',         color = 0xFF3300)
	
	cs = Character('Виола',            unknown_name = 'Медсестра',        color = 0x9999EE)
	mz = Character('Женя',             unknown_name = 'Пионерка',         color = 0x4488FF)
	mt = Character('Ольга Дмитриевна', unknown_name = 'Вожатая',          color = 0x00EE33)
	sh = Character('Шурик',            unknown_name = 'Пионер',           color = 0xEEEE00)
	el = Character('Электроник',       unknown_name = 'Пионер',           color = 0xEEEE00)
	uv = Character('Юля',              unknown_name = 'Странная девочка', color = 0xFFFF00)
	
	pm = Character('Пионер',   color = 0xFFFFFF)
	pf = Character('Пионерка', color = 0xFFFFFF)
	
	
	sm.make_rpg('images/characters/', 'sm', 'pioneer')
	me = sm
	
	
	std_actions = get_std_rpg_actions()
	std_actions.interesting_places = [
		'square',
		'houses_1',
		'houses_2',
		'beach',
		'boat_station',
		'stadium',
		'washbasins',
	]
	
	main_characters = set()
	side_characters = set()
	
	main_character_names = ' '.join([
		'dv un sl mi us',
		'cs mz mt sh el uv',
	]).split(' ')
	
	def init_main_character_actions():
		start_dress = {
			'cs': 'work',
			'uv': 'dress',
			'dv': 'dissolute',
			'us': 'sport',
		}
		
		roommates_list = [('mt', 'sm'), ('un', 'mi'), ('dv', 'us'), ('sl', 'mz'), ('sh', 'el')]
		
		canteen = rpg_locations['canteen']
		canteen_places = {
			'dv': 'chair_backward_pos-r4a',
			'us': 'chair_backward_pos-r4b',
			
			'mi': 'chair_backward_pos-r5a',
			'un': 'chair_backward_pos-r5b',
			'sl': 'chair_forward_pos-r5a',
			
			'mz': 'chair_backward_pos-r6a',
			'el': 'chair_backward_pos-r6b',
			'sh': 'chair_forward_pos-r6b',
			
			'mt': 'chair_backward_pos-r2a',
			'cs': 'chair_forward_pos-r2a',
		}
		
		g = globals()
		for name in main_character_names:
			g['rp_' + name] = 0 # [relationship points] to player
			
			character = g[name]
			character.make_rpg('images/characters/', name, start_dress.get(name, 'pioneer'))
			
			if name == 'uv': continue
			
			character_actions = character.set_actions(std_actions)
			character_actions.start('spawn')
			character.set_auto(True)
			main_characters.add(character)
			
			for roommates in roommates_list:
				if name not in roommates: continue
				
				character_actions.friends = [g[roommate] for roommate in roommates if roommate != name]
				
				if name in ('sh', 'el'):
					character_actions.home = ('houses_1', 'house_sh') # fake location
				else:
					home = 'house_' + roommates[0]
					character_actions.home = home
					
					loc_with_home = 'houses_' + ('2' if name in ('dv', 'us') else '1')
					ban_exit(loc_with_home, home)
					character.allow_exit(loc_with_home, home)
				break
			
			# canteen:
			if name not in canteen_places: continue
			chair_place_name = canteen_places[name]
			del canteen_places[name]
			if chair_place_name not in canteen.places:
				out_msg('init_main_character_actions', 'Place <' + chair_place_name + '> not found in canteen')
				return index
			
			near_objs = get_location_objects('canteen', chair_place_name, None, 1)
			if not near_objs:
				out_msg('init_main_character_actions', 'Needed <chair> object not found in canteen')
				return index
			
			near_obj = near_objs[0]
			dy = (-1 if 'backward' in chair_place_name else 1) * 20
			character_actions.canteen_chair_pre = {'x': near_obj.x, 'y': near_obj.y + dy}
			character_actions.canteen_chair = near_obj
		
		if canteen_places:
			out_msg('init_main_character_actions', 'Canteen places for %s are not installed' % tuple(canteen_places.keys()))
		
		mt.get_actions().friends = [cs, sl]
		cs.get_actions().friends = [mt, un]
		sl.get_actions().friends += [mt]
		un.get_actions().friends += [cs]
		
		mi.get_actions().friends += [dv]
		dv.get_actions().friends += [mi]
		
		sm.allow_exit('houses_1', 'house_mt')
	
	
	def init_side_character_actions(location_name, index):
		location = rpg_locations[location_name]
		canteen = rpg_locations['canteen']
		
		for place in location.places:
			if not (place.startswith('house-') and place[-1].isdigit()):
				continue
			
			name, skin = ('Пионер', 'boy') if random.random() < 0.4 else ('Пионерка', 'girl')
			
			roommates = [Character(name) for i in xrange(2)]
			for character in roommates:
				side_characters.add(character)
				
				character.make_rpg('images/characters/', skin, 'pioneer')
				character.set_auto(True)
				
				character_actions = character.set_actions(std_actions)
				character_actions.start('spawn')
				
				character_actions.home = (location_name, place)
				character_actions.friends = [roommate for roommate in roommates if roommate is not character]
				
				# canteen:
				side = 'left' if (index % 4) < 2 else 'right'
				num = str(index / 4 + 1)
				if len(num) == 1:
					num = '0' + num
				symbol = 'a' if index % 2 else 'b'
				chair_place_name = 'chair_' + side + '_pos-e' + num + symbol
				if chair_place_name not in canteen.places:
					out_msg('init_side_character_actions', 'Place <' + chair_place_name + '> not found in canteen')
					return index
				
				near_objs = get_location_objects('canteen', chair_place_name, None, 1)
				if not near_objs:
					out_msg('init_side_character_actions', 'Needed <chair> object not found in canteen')
					return index
				
				near_obj = near_objs[0]
				dx = (-1 if side == 'right' else 1) * 30
				character_actions.canteen_chair_pre = {'x': near_obj.x + dx, 'y': near_obj.y}
				character_actions.canteen_chair = near_obj
				
				index += 1
		return index
	
	def init_characters():
		uninit_main_characters()
		uninit_side_characters()
		
		init_main_character_actions()
		index = 0
		index = init_side_character_actions('houses_1', index)
		index = init_side_character_actions('houses_2', index)
	
	
	def characters_auto(value):
		for character in main_characters | side_characters:
			character.set_auto(value)
	
	
	def uninit_main_characters():
		for character in main_characters:
			character.set_actions(None)
			if character.location:
				hide_character(character)
		main_characters.clear()
	
	def uninit_side_characters():
		for character in side_characters:
			character.set_actions(None)
			forget_character(character)
		side_characters.clear()


init 11 python:
	register_character_animation(dv, 'node',         'images/characters/anim/dv_node',         0, 0, 34, 0, 33, 8.5)
	register_character_animation(dv, 'punch',        'images/characters/anim/dv_punch',        0, 0,  5, 0,  4, 1.25)
	register_character_animation(sl, 'hello',        'images/characters/anim/sl_hello',        0, 0,  4, 0,  3, 1.0)
	register_character_animation(un, 'book_full',    'images/characters/anim/un_book_full',    0, 0,  6, 0,  5, 1.5)
	register_character_animation(un, 'ruffle',       'images/characters/anim/un_ruffle',       0, 0, 34, 0, 33, 8.5)
	register_character_animation(un, 'trample',      'images/characters/anim/un_trample',      0, 0,  4, 0,  3, 1.0)
	register_character_animation(us, 'salute',       'images/characters/anim/us_salute',       0, 0,  4, 0,  3, 1.0)
	register_character_animation(us, 'cricket',      'images/characters/anim/us_cricket',      0, 0,  6, 0,  5, 1.5)
	register_character_animation(us, 'sport_salute', 'images/characters/anim/us_sport_salute', 0, 0,  4, 0,  3, 1.0)
	register_character_animation(us, 'waves',        'images/characters/anim/us_waves',        0, 0,  3, 0,  2, 0.75)

