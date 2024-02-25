init 10 python:
	was = []
	
	escape_choice = 0
	
	
	def get_place_labels():
		usual_label = cur_location_name + '__' + (cur_place_name or 'unknown')
		
		res = []
		for quest in get_started_quests():
			res.extend(get_glob_labels(quest + '__' + usual_label))
		res.extend(get_glob_labels('day' + str(clock.day) + '__' + usual_label))
		res.extend(get_glob_labels(usual_label))
		return res
	
	gate_right = get_location_objects('enter', None, 'gate_right')[0]
	gate_right.start_animation('open')
	gate_right.update_location_paths()


init 25 python:
	limit_camp_out()
	limit_rooms()
	canteen.init()
	
	add_butterflies(min=1, max=2)
	remove_location_object('station', None, Butterfly, count = -1)
	
	def spec_start():
		clock.pause = False
		clock.set('1-20:46:45')
		clock.acceleration = 6
		show_screen('clock')
		
		day1_set_eaters_20h()
		
		init_characters()
#		characters_auto(False)
		cloud.init()
		
		lineup.enable_reminder = True
		set_rpg_control(True)
#		unlimit_all(me)
#		set_location('square', 'admin')
		set_location('clubs', {'x': 990, 'y': 430})

label start:
#	$ make_names_unknown()
#	call day0_start
#	call day1_start
	$ spec_start()
	
	call rpg_loop
