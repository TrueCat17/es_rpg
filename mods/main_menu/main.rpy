init python:
	mods['start_main_menu'] = 'main_menu'
	start_screens = 'main_menu'


screen main_menu:
	imagemap:
		ground	es2d_gui + 'menu/ground.png'
		hover	es2d_gui + 'menu/hover.png'
	
		hotspot (1000,  40, 325, 50) action Function(start_mod, "std")
		hotspot (1000,  90, 325, 50) action Function(out_msg, "Не реализовано")
		hotspot (1000, 140, 325, 50) action Function(out_msg, "Не реализовано")
		hotspot (1000, 190, 325, 50) action Function(out_msg, "Не реализовано")
		hotspot (1000, 240, 325, 50) action Function(out_msg, "Не реализовано")
		hotspot (1000, 290, 325, 50) action exit_from_game



label start_main_menu:
	$ set_fps(20)
	
	while True:
		pause 0.1
