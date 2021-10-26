init 11 python:
	
	def canteen__init():
		for hour in canteen.hours:
			d, h, m, s = clock.normalize(0, hour, 0, 0 - canteen.horn_time_preparing)
			str_time = clock.time_to_str([-1, h, m, s])
			signals.add('clock-' + str_time, canteen.preparing)
			
			signals.add('clock-' + clock.time_to_str([-1, hour,  0, 0]), canteen.unlimit)
			signals.add('clock-' + clock.time_to_str([-1, hour, 10, 0]), canteen.limit)
			
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
		
		renpy.play(sfx['horn'], 'sound')
		
		canteen_hour = clock.hours + 1
		skip_chance = canteen.skip_chances[canteen_hour if canteen.skip_chances.has_key(canteen_hour) else None]
		for character in characters:
			if random.random() < skip_chance: continue
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
			
			for i in xrange(10):
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
				actions.crowding_waiting_end = get_game_time() + random.randint(5, 20) / 10.0
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
				
				near.rotate_to(character.x - near.x, character.y - near.y)
				character.rotate_to(near.x - character.x, near.y - character.y)
				
				min_conversating = 0.5
				y = rpg_locations['square'].places['canteen'].y - character.y
				max_conversating = 3.0 * max(1 - float(y) / canteen.crowding_place_ysize, 0.333)
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
			return 'moving'
		
		if state == 'moving':
			if not character.ended_move_waiting():
				return 'moving'
			if random.random() < canteen.skip_chance_after_moving:
				actions.cur_action = rpg_action_look_around
				return 'start'
			
			sitting_character = actions.canteen_chair.on[0]
			if sitting_character:
				sitting_character_actions = sitting_character.get_actions()
				if sitting_character_actions:
					sitting_character_actions.stop()
				sitting_character.stand_up()
			character.sit_down(actions.canteen_chair)
			
			d, h, m, s = clock.get()
			s += random.randint(canteen.min_time_for_eating, canteen.max_time_for_eating)
			actions.canteen_eating_end = clock.normalize(d, h, m, s)
			return 'eating'
		
		if state == 'eating':
			if clock.get() > actions.canteen_eating_end:
				return 'end'
			return 'eating'
		
		if state == 'end':
			actions.canteen_eating_end = None
			character.stand_up()
			character.move_to_place(None)
			actions.cur_action = rpg_action_interesting_place
			return 'start'
	
	
	build_object('canteen')
	canteen.hours = [8, 12, 16, 20]
	canteen.skip_chances = {
		None: 0.05,
		16: 0.20,
	}
	canteen.enable = True
	
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
	
