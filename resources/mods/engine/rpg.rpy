label rpg_update:
	$ exit = get_location_exit()
	if exit:
		$ set_location(exit.to_location_name, exit.to_place_name)
		
		if renpy.has_label('on__' + cur_location_name):
			call expression 'on__' + cur_location_name
	
	$ cur_place_name = get_location_place()
	if cur_place_name:
		$ cur_exec_label = cur_location_name + '__' + cur_place_name
		if exec_action and renpy.has_label(cur_exec_label):
			call expression cur_exec_label
		else:
			$ cur_label = get_place_label() if globals().has_key('get_place_label') else (cur_location_name + '__' + cur_place_name)
			if renpy.has_label(cur_label):
				call expression cur_label
	
	$ exec_action = False

