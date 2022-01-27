init python:
	enable_lineup_reminder = False
	def lineup_reminder():
		if enable_lineup_reminder:
			renpy.call('lineup_reminder')

label lineup_reminder:
	$ set_rpg_control(False)
	if cur_location_name == 'square':
		"Судя по всему, где-то здесь скоро должна начаться линейка."
	else:
		"Если я ничего не путаю, на площади скоро должна начаться линейка."
	window hide
	$ set_rpg_control(True)



init 11 python:
	lineup_characters = [dv, us, mz, un, sl, el, sh, mi, sm, mt]
	
	def prepare_to_lineup():
		for ch in lineup_characters:
			if not ch.get_auto(): continue
			actions = ch.get_actions()
			if not actions: continue
			actions.allow = ['other_place', 'sit', 'to_friend', 'look_around']
			actions.start('other_place', 'square')
	
	def start_lineup():
		global lineup_conversation_id
		lineup_conversation_id = set_interval(lineup_conversation, 1.0)
		
		for ch in lineup_characters:
			if not ch.get_auto(): continue
			actions = ch.get_actions()
			if not actions: continue
			actions.allow = []
			actions.block = ['to_friend']
			actions.start(lineup)
	
	def end_lineup():
		clear_interval(lineup_conversation_id)
		
		for ch in lineup_characters:
			if not ch.get_auto(): continue
			actions = ch.get_actions()
			if not actions: continue
			actions.block = []
			if actions.cur_action is not lineup: continue
			actions.random()
	
	signals.add('clock-20:17:00', prepare_to_lineup)
	signals.add('clock-20:20:00', lineup_reminder)
	
	signals.add('clock-20:24:00', start_lineup)
	signals.add('clock-20:40:00', end_lineup)
	
	
	def lineup_conversation():
		if cur_location_name != 'square': return
		if mt.location != cur_location: return
		if max(abs(me.x - mt.x), abs(me.y - mt.y)) > 300: return
		
		clear_interval(lineup_conversation_id)
		label_name = 'day' + str(clock.day) + '__lineup_conversation'
		if renpy.has_label(label_name):
			renpy.call(label_name)
	
	
	
	def get_lineup_place(character):
		kx = 1 if character is mt else -1
		indent_x = 30
		indent_y = 100
		dy = 20
		index = 2 if character is mt else lineup_characters.index(character)
		
		x, y = get_place_center(rpg_locations['square'].places['before_genda'])
		x += kx * indent_x
		y += indent_y + index * dy
		return x, y
	
	def lineup(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			x, y = get_lineup_place(character)
			character.move_to_place(['square', {'x': x, 'y': y}])
			return 'moving'
		
		if state == 'moving':
			if character.ended_move_waiting():
				return 'waiting'
			return 'moving'
		
		if state == 'waiting':
			if (clock.hours, clock.minutes) >= (20, 30):
				return 'start_event'
			if not actions.lineup_end_time:
				actions.lineup_end_time = get_game_time() + random.randint(5, 50) / 10.0
				character.set_direction(random.choice([to_left, to_right, to_forward, to_back]))
			if get_game_time() < actions.lineup_end_time:
				return 'waiting'
			
			actions.lineup_end_time = None
			return 'waiting' if random.random() < 0.75 else 'conversation'
		
		if state == 'conversation':
			if not actions.lineup_end_time:
				if character is mt:
					return 'waiting'
				
				index = lineup_characters.index(character)
				tmp_list = [lineup_characters[index - 1], lineup_characters[index + 1]]
				ready_list = []
				for tmp in tmp_list:
					if tmp is mt: continue
					tmp_actions = tmp.get_actions()
					if not tmp_actions: continue
					if tmp_actions.cur_action is not lineup: continue
					if tmp_actions.state not in ('waiting', 'conversation'): continue
					if abs(tmp.y - character.y) > 25: continue
					ready_list.append(tmp)
				if not ready_list:
					return 'waiting' 
				tmp = random.choice(ready_list)
				tmp_actions = tmp.get_actions()
				
				tmp_actions.cur_state = 'conversation'
				tmp.rotate_to(character)
				character.rotate_to(tmp)
				actions.lineup_end_time = tmp_actions.lineup_end_time = get_game_time() + random.randint(15, 50) / 10.0
			
			if get_game_time() < actions.lineup_end_time:
				return 'conversation'
			actions.lineup_end_time = None
			return 'waiting'
		
		if state == 'start_event':
			character.set_direction(to_left if character is mt else to_right)
			return 'event'
		
		if state == 'event': # see end_lineup()
			return 'event'
		
		if state == 'end':
			actions.lineup_end_time = None
			return 'end'
