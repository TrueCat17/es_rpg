init python:
	set_fps(20)
	start_screens = 'main_menu'
	
	hover_matrix = im.matrix.identity()
	hover_matrix[19] = 0.01 # alpha += 0.01
	
	back_path   =				gui + 'menu/main/back.png'
	ground_path =				gui + 'menu/main/ground.png'
	hover_path  = im.MatrixColor(gui + 'menu/main/hover.png', hover_matrix)
	
	tw, th = get_texture_width(ground_path), get_texture_height(ground_path)
	
	if 0:
		bus = 'images/bg/bus_stop.jpg'
		get_texture_height(bus)
		
		N = 15
		st = time.time()
		for i in xrange(N):
			args = [(1920 + N, 1080)]
			for j in xrange(300):
				args += [(i, j), bus]
			get_texture_height(im.composite(*args))
		print (time.time() - st) / N
	


screen main_menu:
	image back_path:
		size (1.0, 1.0)
	
	imagemap:
		pos (get_stage_width() - tw - 50, 30)
		size (tw, th)
		
		ground  ground_path
		hover   hover_path
		
		hotspot (0,   0, tw, 45) action Function(start_mod, "rpg_editor")
		hotspot (0,  45, tw, 55) action ShowMenu('load')
		hotspot (0, 100, tw, 60) action ShowMenu('settings')
		hotspot (0, 160, tw, 50) action Function(out_msg, "Не реализовано")
		hotspot (0, 210, tw, 60) action Function(out_msg, "Не реализовано")
		hotspot (0, 270, tw, 50) action exit_from_game


label start:
	while True:
		pause 0.1

