init python:
	set_fps(20)
	
	start_screens = 'main_menu'
	
	hover_matrix = im.matrix.identity()
	hover_matrix.t[19] += 0.01 # alpha += 0.01
	
	back_path   =                es2d_gui + 'menu/main/back.png'
	ground_path =                es2d_gui + 'menu/main/ground.png'
	hover_path  = im.MatrixColor(es2d_gui + 'menu/main/hover.png', hover_matrix)

screen main_menu:
	python:
		sw, sh = get_stage_width(), get_stage_height()
		tw, th = get_texture_width(ground_path), get_texture_height(ground_path)
		
		ix, iy = sw - 50, 30
		
		ground = im.Composite((sw, sh),
		                      (0, 0), im.Scale(back_path, sw, sh),
		                      (ix - tw, iy), ground_path)
		hover  = im.Composite((sw, sh),
		                      (ix - tw, iy), hover_path,
		                      (ix - tw, iy), im.Rect("00000040", tw, 45))
	
	imagemap:
		ground  ground
		hover   hover
		
		hotspot (ix - tw, iy +   0, tw, 45) action Function(start_mod, "std")
		hotspot (ix - tw, iy +  45, tw, 55) action ShowMenu('load')
		hotspot (ix - tw, iy + 100, tw, 60) action Function(out_msg, "Не реализовано")
		hotspot (ix - tw, iy + 160, tw, 50) action Function(out_msg, "Не реализовано")
		hotspot (ix - tw, iy + 210, tw, 60) action Function(out_msg, "Не реализовано")
		hotspot (ix - tw, iy + 270, tw, 50) action exit_from_game


label start:
	while True:
		pause 0.1

