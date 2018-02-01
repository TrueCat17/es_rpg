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
		
		$ cur_quests_labels = quest_get_labels(cur_location_name, cur_place_name)
		if len(cur_quests_labels) == 1:
			$ window_showed = db_visible
			if not window_showed:
				window show
			$ control = False
			call expression cur_quests_labels[0][1]
			$ control = True
			if not window_showed:
				window hide
		elif len(cur_quests_labels) > 1:
			$ control = False
			$ me.set_pose("stance")
			window show
			"В этом месте пересекаются несколько активных квестов (" + str(len(cur_quests_labels)) + ")."
			
			$ choose_menu_variants = [name for name, label in cur_quests_labels]
			$ renpy.call_screen('choose_menu', 'choose_menu_result')
			while not call_screen_choosed:
				pause 0.1
			$ name, label = cur_quests_labels[choose_menu_result]
			call expression label
			
			window hide
			$ control = True
	
	$ exec_action = False

