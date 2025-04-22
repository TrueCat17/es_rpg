init -2000000 python:
	start_mod('std')
#	start_mod('rpg_editor')

init python:
	set_fps(20)
	set_can_mouse_hide(False)
	config.has_autosave = False
	
	pause_screen.disable = True
	start_screens = ['hotkeys', 'main_menu']
	
	hover_matrix = im.matrix.identity()
	hover_matrix[19] = 0.01 # alpha += 0.01
	
	back_path   =                'images/gui/menu/main/back.png'
	ground_path =                'images/gui/menu/main/ground.png'
	hover_path  = im.MatrixColor('images/gui/menu/main/hover.png', hover_matrix)
	
	tw, th = get_image_size(ground_path)

screen main_menu:
	image back_path:
		size 1.0
	
	imagemap:
		pos (get_stage_width() - tw - 50, 30)
		size (tw, th)
		
		ground  ground_path
		hover   hover_path
		
		hotspot (0,   0, tw, 45) action Function(start_mod, 'std')
		hotspot (0,  45, tw, 55) action ShowMenu('load')
		hotspot (0, 100, tw, 60) action ShowMenu('preferences')
		hotspot (0, 160, tw, 50) action Notify('Не реализовано')
		hotspot (0, 210, tw, 60) action Notify('Не реализовано')
		hotspot (0, 270, tw, 50) action exit_from_game

