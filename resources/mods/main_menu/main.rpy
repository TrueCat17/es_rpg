init -2000000 python:
#	start_mod('original_es')

init python:
	set_fps(20)
	set_can_mouse_hide(False)
	set_can_auto_save(False)
	start_screens = 'main_menu'
	
	hover_matrix = im.matrix.identity()
	hover_matrix[19] = 0.01 # alpha += 0.01
	
	back_path   =                gui + 'menu/main/back.png'
	ground_path =                gui + 'menu/main/ground.png'
	hover_path  = im.MatrixColor(gui + 'menu/main/hover.png', hover_matrix)
	
	tw, th = get_texture_size(ground_path)

screen main_menu:
	image back_path:
		size (1.0, 1.0)
	
	imagemap:
		pos (get_stage_width() - tw - 50, 30)
		size (tw, th)
		
		ground  ground_path
		hover   hover_path
		
		hotspot (0,   0, tw, 45) action Function(start_mod, "std")
		hotspot (0,  45, tw, 55) action ShowMenu('load')
		hotspot (0, 100, tw, 60) action ShowMenu('settings')
		hotspot (0, 160, tw, 50) action Function(out_msg, "Не реализовано")
		hotspot (0, 210, tw, 60) action Function(out_msg, "Не реализовано")
		hotspot (0, 270, tw, 50) action exit_from_game

