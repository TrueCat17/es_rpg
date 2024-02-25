init 2 python:
	
	set_sit_place('liaz_bench_left',   [(-16, 30, to_left), (-16, 50, to_left)])
	set_sit_place('liaz_bench_middle', [(16, 30, to_right)])
	set_sit_place('liaz_bench_right',  [(16, 30, to_right), (16, 50, to_right)])
	set_sit_place('liaz_chair_forward', [(0, 20, to_forward)])
	
	set_sit_place('bench_left',  [(18, 35, to_right), (18, 60, to_right)], over='bench_left_over')
	set_sit_place('bench_right', [(-18, 35, to_left), (-18, 60, to_left)], over='bench_right_over')
	
	set_sit_place('chair_left',   [(-14, 34, to_left)])
	set_sit_place('chair_right',   [(14, 34, to_right)])
	set_sit_place('chair_forward',  [(0, 30, to_forward)], over='chair_forward_over')
	set_sit_place('chair_backward', [(0, 40, to_back)])
	
	set_sit_place('mus_club_chair', [(0, 42, to_back)])
	set_sit_place('piano_chair', [(-15, 12, to_left), (12, 12, to_right, False), (0, 22, to_back, False)])
	
	set_sit_place('tabouret', [(14, 18, to_right)])
