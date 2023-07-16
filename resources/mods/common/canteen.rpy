init 11 python:
	
	def canteen__init():
		for hour in canteen.hours:
			d, h, m, s = clock.normalize(0, hour, 0, 0 - canteen.horn_time_preparing)
			str_time = clock.time_to_str([-1, h, m, s])
			signals.add('clock-' + str_time, canteen.preparing)
			
			signals.add('clock-' + clock.time_to_str([-1, hour, 00, -3]), canteen.unlimit)
			signals.add('clock-' + clock.time_to_str([-1, hour, 20, 0]), canteen.limit)
			
			signals.add('clock-' + clock.time_to_str([-1, hour,  0, 0]), canteen.set_full)
			signals.add('clock-' + clock.time_to_str([-1, hour, 10, 0]), canteen.set_half)
			signals.add('clock-' + clock.time_to_str([-1, hour, 13, 0]), canteen.set_empty)
	
	def canteen__limit():
		ban_exit('square', 'canteen')
	def canteen__unlimit():
		if canteen.enable:
			unban_exit('square', 'canteen')
	
	def canteen__set_full():
		if canteen.enable:
			set_location_ambience('canteen', ambience_dir + 'canteen_full.ogg')
			start_location_ambience()
	def canteen__set_half():
		if canteen.enable:
			set_location_ambience('canteen', ambience_dir + 'canteen_full.ogg', 0.5)
			start_location_ambience()
	def canteen__set_empty():
		set_location_ambience('canteen', ambience_dir + 'canteen_empty.ogg')
		start_location_ambience()
	
	
	def canteen__preparing():
		if not canteen.enable:
			return
		
		canteen.finished_characters.clear()
		renpy.play(sfx['horn'], 'sound')
		
		canteen_hour = clock.hours + 1
		skip_chance = canteen.skip_chances[canteen_hour if canteen_hour in canteen.skip_chances else None]
		for character in characters:
			skip = random.random() < skip_chance
			if character in main_characters:
				if canteen_hour in canteen.no_skip_hours:
					if character not in canteen.not_need:
						skip = False
				if character in canteen.not_eat:
					skip = True
			
			if skip: continue
			if character is me and get_rpg_control(): continue
			actions = character.get_actions()
			if not actions: continue
			
			waiting_time = random.randint(canteen.min_time_for_react, canteen.max_time_for_react)
			clock.add_signal(waiting_time, Function(actions.start, 'other_place', 'square'))
			
			crowding_time = random.randint(canteen.min_time_for_crowding, canteen.max_time_for_crowding)
			clock.add_signal(crowding_time, Function(actions.start, canteen.crowding))
			
			clock.add_signal(canteen.horn_time_preparing, Function(actions.start, canteen.inside))
	
	def canteen__crowding(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			loc = rpg_locations['square']
			place = loc.places['canteen']
			
			for i in range(10):
				res = rpg_random_free_point(['square'])
				if not res: continue
				_, x, y = res
				if x < place.x + canteen.crowding_place_xsize or x >= place.x: continue
				if y < place.y or y >= place.y + canteen.crowding_place_ysize: continue
				break # ok
			else:
				return 'start' # try later
			
			path_found = character.move_to_place(['square', {'x': x, 'y': y}])
			if not path_found:
				character.move_to_place(None)
				return 'end'
			return 'moving'
		
		if state == 'moving':
			if character.ended_move_waiting():
				return 'waiting'
			return 'moving'
		
		if state == 'waiting':
			if not actions.crowding_waiting_end:
				actions.crowding_waiting_end = get_game_time() + random.uniform(0.5, 2.0)
				character.set_direction(random.choice([to_left, to_right, to_back, to_forward]))
			if get_game_time() < actions.crowding_waiting_end:
				return 'waiting'
			actions.crowding_waiting_end = None
			return random.choice(['start', 'conversation'])
		
		if state == 'conversation':
			if not actions.crowding_conversation_end:
				dist = canteen.crowding_conversation_dist
				nears = []
				for ch in characters:
					if ch is character: continue
					ch_actions = ch.get_actions()
					if not ch_actions or ch_actions.cur_action is not actions.cur_action: continue
					if ch_actions.state == 'moving': continue
					if max(abs(ch.x - character.x), abs(ch.y - character.y)) > dist: continue
					nears.append(ch)
				if not nears:
					return 'waiting'
				near = actions.crowding_conversation_with = random.choice(nears)
				near_actions = near.get_actions()
				if near_actions.crowding_conversation_with:
					near_actions.crowding_conversation_with.state = 'waiting'
				near_actions.crowding_conversation_with = character
				actions.crowding_conversation_with = near
				
				near.rotate_to(character)
				character.rotate_to(near)
				
				min_conversating = 0.5
				y = rpg_locations['square'].places['canteen'].y - character.y
				max_conversating = max(1 - y / canteen.crowding_place_ysize, 0.333) * 3
				actions.crowding_conversation_end = get_game_time() + random.random() * (max_conversating - min_conversating) + min_conversating
				near_actions.crowding_conversation_end = actions.crowding_conversation_end
			
			if get_game_time() < actions.crowding_conversation_end:
				return 'conversation'
			
			near_actions = actions.crowding_conversation_with.get_actions()
			near_actions.crowding_conversation_end = None
			near_actions.crowding_conversation_with = None
			if near_actions.cur_action is actions.cur_action:
				near_actions.state = 'waiting'
			actions.crowding_conversation_end = None
			actions.crowding_conversation_with = None
			return 'waiting'
		
		if state == 'end':
			if actions.crowding_conversation_with:
				actions.crowding_conversation_with.state = 'waiting'
				actions.crowding_conversation_with = None
			actions.crowding_conversation_end = None
			actions.crowding_waiting_end = None
			character.move_to_place(None)
			return 'end'
	
	
	def canteen__inside(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			if not actions.canteen_chair:
				return 'end'
			character.move_to_place(['canteen', actions.canteen_chair_pre])
			actions.interruptable = False
			return 'moving'
		
		if state == 'moving':
			if not character.ended_move_waiting():
				return 'moving'
			
			can_skip = character not in main_characters or character in canteen.not_need
			if can_skip and random.random() < canteen.skip_chance_after_moving:
				actions.set('look_around')
				actions.add('interesting_place')
				return IGNORE_STATE
			
			sitting_character = actions.canteen_chair.on[0]
			if sitting_character:
				sitting_character_actions = sitting_character.get_actions()
				if sitting_character_actions:
					sitting_character_actions.stop()
				sitting_character.stand_up()
			character.sit_down(actions.canteen_chair)
			
			actions.fast_eat = character in canteen.fast_eat
			if actions.fast_eat:
				actions.canteen_eating_end = get_game_time() + canteen.fast_eat_time
			else:
				d, h, m, s = clock.get()
				s += random.randint(canteen.min_time_for_eating, canteen.max_time_for_eating)
				actions.canteen_eating_end = clock.normalize(d, h, m, s)
			return 'eating'
		
		if state == 'eating':
			if actions.fast_eat:
				if get_game_time() > actions.canteen_eating_end:
					return 'end'
			else:
				if clock.get() > actions.canteen_eating_end and character not in canteen.wait_characters:
					return 'end'
			return 'eating'
		
		if state == 'end':
			actions.fast_eat = None
			actions.canteen_eating_end = None
			canteen.finished_characters.add(character)
			character.stand_up()
			character.move_to_place(None)
			actions.set('interesting_place')
			return IGNORE_STATE
	
	
	def canteen__get_table():
		res = ''
		min_dist = 1e9
		for name, place in rpg_locations['canteen'].places.items():
			if 'table' not in name: continue
			dist = get_dist(place.x + place.xsize / 2, place.y + place.ysize / 2, me.x, me.y)
			if dist < min_dist:
				min_dist = dist
				res = name[name.index('-')+1:]
		return res
	
	def canteen__is_sit(character):
		actions = character.get_actions()
		if actions:
			chair = actions.canteen_chair
			if chair:
				return chair.on[0] is character
		return character.location.name == 'canteen' and character.get_pose() == 'sit'
	
	
	def canteen__wait(*characters, **kwargs):
		canteen.wait_characters = characters
		canteen.end_wait_time = get_game_time() + kwargs.get('timeout', 1e9)
		renpy.call('canteen_wait')
	def canteen__clear_wait():
		canteen.wait_characters = []
	
	def canteen__sit_for_table(table):
		if me.get_pose() == 'stay':
			canteen.sitting_place = rpg_locations['canteen'].places[canteen.free_place[table]]
			renpy.call('canteen_sitting')
	
	def canteen__finished(ch):
		return ch in canteen.finished_characters
	def canteen__finished_all(*characters):
		return all([ch in canteen.finished_characters for ch in characters])
	def canteen__finished_any(*characters):
		return any([ch in canteen.finished_characters for ch in characters])
	
	
	build_object('canteen')
	canteen.enable = True
	canteen.wait_characters = []
	canteen.finished_characters = set()
	
	canteen.hours = [8, 12, 16, 20]
	canteen.skip_chances = {
		None: 0.05,
		16: 0.20,
	}
	
	# for main characters
	canteen.no_skip_hours = [8, 12, 20]
	canteen.not_eat = [] # don't go to canteen
	canteen.not_need = [] # can skip canteen
	canteen.fast_eat = [] # characters
	canteen.fast_eat_time = 3.0 # in seconds, real time, not game time
	
	# in seconds, before start hour
	canteen.horn_time_preparing = 15 * 60
	
	# in seconds, after horn
	canteen.min_time_for_react = 4 * 60
	canteen.max_time_for_react = 6 * 60
	canteen.min_time_for_crowding = 9 * 60
	canteen.max_time_for_crowding = 11 * 60
	
	canteen.crowding_conversation_dist = 30
	canteen.crowding_place_xsize = -350 # to left
	canteen.crowding_place_ysize = 200
	
	canteen.skip_chance_after_moving = 0.05
	
	canteen.min_time_for_eating =  3 * 60
	canteen.max_time_for_eating = 10 * 60
	
	
	canteen.say = {
		'mt': [
			"Семён, порядочный пионер никогда не отрывается от коллектива. Садись вмесете с остальными.",
			"Семён, а почему ты отдельно ото всех сел? Негоже просто так отбиваться от коллектива.",
			"Семён, извини конечно, но мы с Виолеттой тут обсуждаем одну взрослую тему, и лишние уши нам не нужны. Не мог бы ты пересесть?",
		],
		'cs': [
			"А чего это ты, пионер, отдельно сел? Слишком активные пионерки за вашим столом, поесть не дают?",
			"А почему отдельно от пионерок сидим? Смотри какие красотки. Дерзай, Пионер.",
		],
		'stranger': [
			"Чего подслушиваешь? Не мог бы пересесть?",
			"Эй! Тут занято! Сядь на какое-нибудь другое место.",
			"Ой, а почему ты не со своим отрядом ешь?",
			"А чего не ешь за своим столом?",
		],
	}
	
	canteen.free_place = {
		'r4': 'chair_forward_pos-r4b',
		'r5': 'chair_forward_pos-r5b',
		'r6': 'chair_forward_pos-r6a',
	}


label canteen_wait:
	while get_game_time() < canteen.end_wait_time:
		if all([canteen.is_sit(ch) or canteen.finished(ch) for ch in canteen.wait_characters]):
			break
		pause 0.01

label canteen_sitting:
	if me.get_pose() == 'sit':
		return
	$ me.move_to_place({'x': canteen.sitting_place.x, 'y': canteen.sitting_place.y + 20})
	$ canteen_sit_objs = get_near_sit_objects(max_dist=50)
	$ me.sit_down(canteen_sit_objs[0][0])

label canteen_no_conversation:
	python:
		near_chars = []
		table = canteen.get_table()
		for ch in main_characters:
			if canteen.is_sit(ch):
				ch_table = ch.canteen_chair_place_name[:-1].split('-')[1]
				if table == ch_table:
					near_chars.append(ch)
		
	if not near_chars:
		"За столом никого не было."
	else:
		if len(near_chars) > 1:
			"За столом сидело несколько %s." % ('пионеров' if el in near_chars or sh in near_chars else 'пионерок', )
			"Они сосредоточенно ели, о чём-то думая."
		else:
			$ male = near_chars[0] in (el, sh)
			"За столом %s %s." % ('сидел' if male else 'сидела', near_chars[0])
			"%s сосредоточенно %s, о чём-то думая." % (('Он', 'ел') if male else ('Она', 'ела'))
	"Что ж, когда я ем - я глух и нем."
	
	$ clock.add(3 * 60)

