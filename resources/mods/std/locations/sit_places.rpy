init 2 python:
	
	set_sit_place('armchair', [(1, 30, to_forward)], over = 'armchair')
	set_sit_place('flat_bed', [(-30, 60, to_left)])
	
	set_sit_place('liaz_bench_left',   [(-16, 30, to_left), (-16, 50, to_left)])
	set_sit_place('liaz_bench_middle', [(16, 30, to_right)])
	set_sit_place('liaz_bench_right',  [(16, 30, to_right), (16, 50, to_right)])
	set_sit_place('liaz_chair_forward', [(0, 20, to_forward)])
	
	set_sit_place('admin_bench', [(-27, 25, to_back), (0, 25, to_back), (28, 25, to_back)])
	
	set_sit_place('boat_station_bench', [(-5, 20, to_back), (20, 20, to_back)])
	set_sit_place('boat_station_tabouret', [(0, 25, to_back)])
	
	set_sit_place('clubs_bench', [(-27, 25, to_back), (0, 25, to_back), (27, 25, to_back)])
	
	set_sit_place('crossroad_bench', [(-25, 25, to_back), (5, 25, to_back), (35, 25, to_back)])
	
	set_sit_place('bench_left',  [(18, 35, to_right), (18, 60, to_right)], over = 'bench_left_over')
	set_sit_place('bench_right', [(-18, 35, to_left), (-18, 60, to_left)], over = 'bench_right_over')
	set_sit_place('canteen_bench', [(-30, 16, to_forward), (-10, 16, to_forward), (10, 16, to_forward), (30, 16, to_forward)], over = 'canteen_bench')
	
	set_sit_place('chair_left',   [(-14, 34, to_left)])
	set_sit_place('chair_right',   [(14, 34, to_right)])
	set_sit_place('chair_forward',  [(0, 30, to_forward)], over = 'chair_forward_over')
	set_sit_place('chair_backward', [(0, 40, to_back)])
	
	set_sit_place('mus_club_chair', [(0, 42, to_back)])
	set_sit_place('piano_chair', [(-15, 12, to_left), (12, 12, to_right, False), (0, 22, to_back, False)])
	
	set_sit_place('storage_tabouret', [(14, 18, to_right)])
	
	set_sit_place('sm_bed', [(23, 60, to_right)])
	
	set_sit_place('houses_1_bench_forward',    [(-25, 16, to_forward), (0, 16, to_forward), (25, 16, to_forward)], over = 'bench_over')
	set_sit_place('houses_1_bench_backward',   [(-25, 22, to_back), (0, 22, to_back), (25, 22, to_back)])
	set_sit_place('houses_1_bench_with_book',  [(0, 22, to_back), (25, 22, to_back)])
	set_sit_place('houses_1_bench_with_chess', [(-25, 22, to_back), (25, 22, to_back)])
	set_sit_place('houses_1_bench_with_paper', [(-25, 22, to_back), (0, 22, to_back)])
	
	set_sit_place('bench_forward',  [(-21, 16, to_forward), (0, 16, to_forward), (21, 16, to_forward)], over = 'bench_over')
	set_sit_place('bench_backward', [(-21, 22, to_back), (0, 22, to_back), (21, 22, to_back)])
	
	set_sit_place('library_armchair',   [(0, 50, to_back)])
	set_sit_place('library_chair_left', [(-16, 27, to_left)])
	
	set_sit_place('library_and_hospital_bench', [(-16, 35, to_back), (16, 35, to_back)])
	
	set_sit_place('radio_club_tabouret',      [(0, 16, to_forward)], over = 'tabouret_over')
	set_sit_place('radio_storeroom_tabouret', [(0, 27, to_back)])
	
	# 615 - bench width
	# 16 - count of sit places
	scene_bench_sit_places = [(int(615 / 16 * i + 615 / 16 / 2 - 615 / 2), 16, to_forward) for i in range(16)]
	scene_bench_sit_places1 = scene_bench_sit_places[:-1]
	scene_bench_sit_places3 = scene_bench_sit_places[:5] + scene_bench_sit_places[6:]
	
	set_sit_place('scene_bench_1', scene_bench_sit_places1, over = 'bench_1_over')
	set_sit_place('scene_bench_2', scene_bench_sit_places , over = 'bench_2_over')
	set_sit_place('scene_bench_3', scene_bench_sit_places3, over = 'bench_3_over')
	set_sit_place('scene_bench_4', scene_bench_sit_places , over = 'bench_4_over')
	set_sit_place('scene_bench_5', scene_bench_sit_places , over = 'bench_5_over')
	
	set_sit_place('stadium_bench_left',  [(-17, 19, to_left), (-17, 41, to_left), (-17, 63, to_left), (-17, 85, to_left)])
	
	set_sit_place('bench_backward', [(-13, 23, to_back), (13, 23, to_back)])
	set_sit_place('bench_forward',  [(-13, 15, to_forward), (13, 15, to_forward)], over = 'bench_forward_over')
	set_sit_place('tennis_bench_left', [(-14, 20, to_left), (-14, 46, to_left)])
	set_sit_place('tennis_bench_right', [(14, 20, to_right), (14, 46, to_right)])
