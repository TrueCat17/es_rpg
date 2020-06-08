init 2 python:
	
	set_sit_place('liaz_bench_left',   [(-16, 30, to_left), (-16, 50, to_left)])
	set_sit_place('liaz_bench_middle', [(16, 30, to_right)])
	set_sit_place('liaz_bench_right',  [(16, 30, to_right), (16, 50, to_right)])
	set_sit_place('liaz_chair_forward', [(0, 20, to_forward)])
	
	set_sit_place('bench_left',  [(18, 35, to_right), (18, 60, to_right)], over='bench_left_over')
	set_sit_place('bench_right', [(-18, 35, to_left), (-18, 60, to_left)], over='bench_right_over')
