label day1_start:
	scene bg black
	
	python:
		#db_set_ui('day')
		
		was = []
		
		day_num = 1
		add_location_object('enter', 'ikarus_place', 'ikarus')
		
		init_characters()
		#characters_auto(False)
		
		mt.get_actions().stop()
		show_character(mt, 'mt_bed', 'house_mt')
		mt.set_direction(to_back)
		mt.set_auto(False)
		
		un.set_auto(False)
		show_character(un, 'clubs', 'radio_club')
		us.set_auto(False)
		show_character(us, 'porch_left', 'clubs')
		
		set_rpg_control(False)
		me.set_dress('winter')
		
		set_location('ikarus', 'sit_place')
		me.set_direction(to_right)
		me.set_pose('sit')
	
	pause 1
	"Вдруг стало душно. Невыносимая жара и автобусная пыль вызвали тошноту, отчего я и проснулся."
	hide bg with dissolve2
	
	"И не было понятно, чему удивляться сильнее: то ли яркому солнечному свету за окном, то ли совершенно иному автобусу, то ли отсутствию снега на улице посреди зимы."
	window hide
	
	$ me.set_pose('stay')
	pause 1
	$ me.move_to_place('before_sit_place')
	$ me.set_direction(to_back)
	
	$ me.move_to_place('enter')
	
	$ set_rpg_control(True)

