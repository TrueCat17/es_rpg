init python:
	
	def day1_sl_escort(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			character.move_to_place(['house_mt', 'houses_1'])
			return 'moving'
		
		if state == 'moving':
			if character.ended_move_waiting():
				return 'end'
			
			# ???
			return 'moving'
		
		if state == 'end':
			character.move_to_place(None)
			return 'end'
		
