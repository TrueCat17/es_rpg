label day1_start:
	scene bg black
	
	python:
		#db_set_ui('day')
		
		day_num = 1
		add_location_object('enter', 'ikarus_place', 'ikarus')
		
		set_rpg_control(False)
		me.set_dress('winter')
		
		set_location('ikarus', 'sit_place')
		me.set_direction(to_right)
		me.set_pose('sit')
	
	pause 1
	hide bg with dissolve2
	
	"Лето. Икарус."
	"Ясно-понятно."
	window hide
	
	$ me.set_pose('stay')
	pause 1
	$ me.move_to_place('before_sit_place')
	$ me.set_direction(to_back)
	
	$ me.move_to_place('enter')
	
	$ set_rpg_control(True)

