label lineup_reminder:
	$ set_rpg_control(False)
	if cur_location_name == 'square':
		"Судя по всему, где-то здесь скоро должна начаться линейка."
	else:
		"Если я ничего не путаю, на площади скоро должна начаться линейка."
	window hide
	$ set_rpg_control(True)



init 11 python:
	def lineup__reminder():
		if lineup.enable_reminder:
			renpy.call('lineup_reminder')
	
	def lineup__prepare():
		for ch in lineup.characters:
			if ch in lineup.skip: continue
			if not ch.get_auto(): continue
			actions = ch.get_actions()
			if not actions: continue
			actions.allow = ['other_place', 'sit', 'to_friend', 'look_around']
			actions.start('other_place', 'square')
	
	def lineup__start():
		lineup.conversation_id = set_interval(lineup.conversation, 1.0)
		
		for ch in lineup.characters:
			if ch in lineup.skip: continue
			if not ch.get_auto(): continue
			actions = ch.get_actions()
			if not actions: continue
			actions.allow = []
			actions.block = ['to_friend']
			actions.start(lineup.action)
	
	def lineup__end():
		clear_interval(lineup.conversation_id)
		
		for ch in lineup.characters:
			if ch in lineup.skip: continue
			if not ch.get_auto(): continue
			actions = ch.get_actions()
			if not actions: continue
			actions.block = []
			if actions.cur_action is not lineup.action: continue
			actions.random()
	
	
	
	def lineup__conversation():
		if cur_location_name != 'square': return
		if mt.location != cur_location: return
		if max(abs(me.x - mt.x), abs(me.y - mt.y)) > 300: return
		
		clear_interval(lineup.conversation_id)
		label_name = 'day' + str(clock.day) + '__lineup_conversation'
		if renpy.has_label(label_name):
			renpy.call(label_name)
	
	
	
	def lineup__get_place(character):
		kx = 1 if character is mt else -1
		indent_x = 30
		indent_y = 100
		dy = 20
		index = 2 if character is mt else lineup.characters.index(character)
		
		x, y = get_place_center(rpg_locations['square'].places['before_genda'])
		x += kx * indent_x
		y += indent_y + index * dy
		return x, y
	
	def lineup__action(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			x, y = lineup.get_place(character)
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
				actions.lineup_end_time = get_game_time() + random.uniform(0.5, 5.0)
				character.set_direction(random.choice([to_left, to_right, to_forward, to_back]))
			if get_game_time() < actions.lineup_end_time:
				return 'waiting'
			
			actions.lineup_end_time = None
			return 'waiting' if random.random() < 0.75 else 'conversation'
		
		if state == 'conversation':
			if not actions.lineup_end_time:
				if character is mt:
					return 'waiting'
				
				index = lineup.characters.index(character)
				tmp_list = [lineup.characters[index - 1], lineup.characters[index + 1]]
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
				actions.lineup_end_time = tmp_actions.lineup_end_time = get_game_time() + random.uniform(1.5, 5.0)
			
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
	
	
	
	build_object('lineup')
	
	lineup.enable_reminder = False
	
	lineup.characters = [dv, us, mz, un, sl, el, sh, mi, sm, mt]
	lineup.skip = []
	
	
	signals.add('clock-20:17:00', lineup.prepare)
	signals.add('clock-20:20:00', lineup.reminder)
	
	signals.add('clock-20:24:00', lineup.start)
	signals.add('clock-20:40:00', lineup.end)
	
