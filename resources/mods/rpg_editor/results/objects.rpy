init 1 python:
	
	register_location_object('flat_keys',             'images/locations/objects/', 'flat_keys',             None, 1)
	register_location_object('lighter',               'images/locations/objects/', 'lighter',               None, 1)
	register_location_object('notepad',               'images/locations/objects/', 'notepad',               None, 1)
	register_location_object('phone',                 'images/locations/objects/', 'phone',                 None, 1)
	register_location_object('tooth_paste_and_brush', 'images/locations/objects/', 'tooth_paste_and_brush', None, 1)
	register_location_object('soap',                  'images/locations/objects/', 'soap',                  None, 1)
	register_location_object('towel',                 'images/locations/objects/', 'towel',                 None, 1)
	register_location_object('broom',         'images/locations/storage/objects/', 'broom',         'broom_free', 1)
	register_location_object('shovel',        'images/locations/storage/objects/', 'shovel',       'shovel_free', 1)
	
	register_location_object('armchair',   'images/locations/flat/objects/', 'armchair', None)
	register_location_object('flat_bed',   'images/locations/flat/objects/', 'bed', None)
	register_location_object('dress',      'images/locations/flat/objects/', 'dress', None)
	register_location_object('lamp_light', 'images/locations/flat/objects/', 'lamp_light', None)
	register_location_object('monitor',    'images/locations/flat/objects/', 'monitor', None)
	register_location_object_animation('monitor', 'main',
		'images/locations/flat/objects/', 'monitor_scroll', None,
		0, 0,
		7, 0, 6,
		2
	)
	
	register_location_object('uv_dream', 'images/locations/enter/objects/', 'uv_dream', None)
	register_location_object_animation('uv_dream', 'main',
		'images/locations/enter/objects/', 'uv_dream_anim', None,
		0, 0,
		8, 0, 7,
		6
	)
	
	register_location_object('liaz', 'images/locations/station/objects/', 'liaz', None)
	
	register_location_object('liaz_bench_left',    'images/locations/liaz/objects/', 'bench_left', None)
	register_location_object('liaz_bench_middle',  'images/locations/liaz/objects/', 'bench_middle', None)
	register_location_object('liaz_bench_right',   'images/locations/liaz/objects/', 'bench_right', None)
	register_location_object('liaz_chair_forward', 'images/locations/liaz/objects/', 'chair_forward', None)
	
	register_location_object('ikarus', 'images/locations/enter/objects/', 'ikarus_main', 'ikarus_free')
	
	register_location_object('gate_left', 'images/locations/objects/', 'gate_left_main', 'gate_free')
	register_location_object('gate_right', 'images/locations/objects/', 'gate_right_main', 'gate_free')
	
	register_location_object_animation('gate_right', 'open',
		'images/locations/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 34,
		3, 2, 2,
		-1
	)
	register_location_object_animation('gate_right', 'opening',
		'images/locations/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 34,
		3, 0, 2
	)
	register_location_object_animation('gate_right', 'closing',
		'images/locations/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 34,
		3, 2, 0
	)
	
	
	register_location_object('bench_backward', 'images/locations/objects/', 'bench_forward', 'bench_forward_free')
	register_location_object('bench_forward',  'images/locations/objects/', 'bench_forward', None)
	register_location_object('bench_left',  'images/locations/objects/', 'bench_left',  'bench_left_right_free')
	register_location_object('bench_right', 'images/locations/objects/', 'bench_right', 'bench_left_right_free')
	register_location_object('chair_left',     'images/locations/objects/', 'chair_left', 'chair_left_right_free')
	register_location_object('chair_right',    'images/locations/objects/', 'chair_right', 'chair_left_right_free')
	register_location_object('chair_backward', 'images/locations/objects/', 'chair_backward', 'chair_forward_backward_free')
	register_location_object('chair_forward',  'images/locations/objects/', 'chair_forward', 'chair_forward_backward_free')
	register_location_object('lamp', 'images/locations/objects/', 'lamp', 'lamp_free')
	
	
	register_location_object('admin_bench',  'images/locations/admin/objects/', 'bench', None)
	
	register_location_object('boat_station_bench',  'images/locations/boat_station/objects/', 'bench', None)
	register_location_object('boat_station_tabouret',  'images/locations/boat_station/objects/', 'tabouret', None)
	
	register_location_object('clubs_bench',  'images/locations/clubs/objects/', 'bench', None)
	
	register_location_object('crossroad_bench',  'images/locations/crossroad/objects/', 'bench', None)
	
	register_location_object('library_cupboard_1', 'images/locations/library/objects/', 'cupboard_1', 'cupboard_free')
	register_location_object('library_cupboard_2', 'images/locations/library/objects/', 'cupboard_2', 'cupboard_free')
	register_location_object('library_cupboard_3', 'images/locations/library/objects/', 'cupboard_3', 'cupboard_free')
	
	register_location_object('mus_club_rails',  'images/locations/clubs/objects/', 'mus_club_rails', None)
	register_location_object('mus_club_column', 'images/locations/clubs/objects/', 'mus_club_column', None)
	
	register_location_object('table_h', 'images/locations/canteen/objects/', 'table_h', 'table_h_free')
	register_location_object('table_v', 'images/locations/canteen/objects/', 'table_v', 'table_v_free')
	register_location_object('canteen_column',      'images/locations/canteen/objects/', 'column', 'column_free')
	register_location_object('canteen_column_back', 'images/locations/canteen/objects/', 'column_back', 'column_free')
	register_location_object('canteen_door', 'images/locations/canteen/objects/', 'door', None)
	
	register_location_object('mus_club_chair',      'images/locations/mus_club/objects/', 'chair',         'chair_free')
	register_location_object('mus_club_microphone', 'images/locations/mus_club/objects/', 'microphone',    'microphone_free')
	register_location_object('piano',               'images/locations/mus_club/objects/', 'piano',         'piano_free')
	register_location_object('piano_chair',         'images/locations/mus_club/objects/', 'piano_chair',   'piano_chair_free')
	register_location_object('stand',               'images/locations/mus_club/objects/', 'stand',         'stand_free')
	register_location_object('cymbal',              'images/locations/mus_club/objects/', 'cymbal',        'cymbal_free')
	register_location_object('drum',                'images/locations/mus_club/objects/', 'drum',          'drum_free')
	register_location_object('drum_and_tube',       'images/locations/mus_club/objects/', 'drum_and_tube', 'drum_and_tube_free')
	register_location_object('guitar',              'images/locations/mus_club/objects/', 'guitar',        'guitar_free')
	register_location_object('blue_guitar',         'images/locations/mus_club/objects/', 'blue_guitar',   'blue_guitar_free')
	register_location_object('mus_club_left_cupboard', 'images/locations/mus_club/objects/', 'left_cupboard', 'left_cupboard_free')
	register_location_object('mus_club_far_cupboard',  'images/locations/mus_club/objects/', 'far_cupboard', 'far_cupboard_free')
	
	register_location_object('radio_club_table', 'images/locations/radio_club/objects/', 'table', None)
	register_location_object('radio_club_cupboards', 'images/locations/radio_club/objects/', 'cupboards', None)
	
	register_location_object('scene_microphone', 'images/locations/scene/objects/', 'microphone', 'microphone_free')
	
	register_location_object('car', 'images/locations/square/objects/', 'car', 'car_free')
	register_location_object('canteen_bench', 'images/locations/square/objects/', 'canteen_bench', None)
	register_location_object('washbasin_left',  'images/locations/square/objects/', 'washbasin_left',  'washbasin_free')
	register_location_object('washbasin_right', 'images/locations/square/objects/', 'washbasin_right', 'washbasin_free')
	
	register_location_object('bath_rails_left',  'images/locations/bath/objects/', 'rails_left',  None)
	register_location_object('bath_rails_right', 'images/locations/bath/objects/', 'rails_right', None)
	
	register_location_object('sm_bed', 'images/locations/house_mt/objects/', 'bed', None)
	
	register_location_object('houses_1_bench_backward',   'images/locations/houses_1/objects/', 'bench', 'bench_free')
	register_location_object('houses_1_bench_forward',    'images/locations/houses_1/objects/', 'bench', 'bench_free')
	register_location_object('houses_1_bench_with_book',  'images/locations/houses_1/objects/', 'bench_with_book', 'bench_free')
	register_location_object('houses_1_bench_with_chess', 'images/locations/houses_1/objects/', 'bench_with_chess', None)
	register_location_object('houses_1_bench_with_paper', 'images/locations/houses_1/objects/', 'bench_with_paper', None)
	
	register_location_object('library_armchair',   'images/locations/library/objects/', 'armchair', None)
	register_location_object('library_chair_left', 'images/locations/library/objects/', 'chair_left', 'chair_free')
	
	register_location_object('library_and_hospital_bench', 'images/locations/library_and_hospital/objects/', 'bench', 'bench_free')
	
	register_location_object('radio_club_tabouret',      'images/locations/radio_club/objects/',      'tabouret', 'tabouret_free')
	register_location_object('radio_storeroom_tabouret', 'images/locations/radio_storeroom/objects/', 'tabouret', None)
	
	register_location_object('scene_bench_1', 'images/locations/scene/objects/', 'bench', 'bench_free')
	register_location_object('scene_bench_2', 'images/locations/scene/objects/', 'bench', 'bench_free')
	register_location_object('scene_bench_3', 'images/locations/scene/objects/', 'bench', 'bench_free')
	register_location_object('scene_bench_4', 'images/locations/scene/objects/', 'bench', 'bench_free')
	register_location_object('scene_bench_5', 'images/locations/scene/objects/', 'bench', 'bench_free')
	register_location_object('scene_anti_fire', 'images/locations/scene/objects/', 'anti_fire', 'anti_fire_free')
	register_location_object('scene_sound',     'images/locations/scene/objects/', 'sound', None)
	register_location_object('scene_table',     'images/locations/scene/objects/', 'table', 'table_free')
	
	register_location_object('stadium_bench_left', 'images/locations/stadium/objects/', 'bench_left', None)
	register_location_object('stadium_gates', 'images/locations/stadium/objects/', 'gates', 'gates_free')
	register_location_object('stadium_rails', 'images/locations/stadium/objects/', 'rails', None)
	register_location_object('stadium_turniks', 'images/locations/stadium/objects/', 'turniks', 'turniks_free')
	
	register_location_object('storage_cupboard',       'images/locations/storage/objects/', 'cupboard',       'cupboard_free')
	register_location_object('storage_left_cupboards', 'images/locations/storage/objects/', 'left_cupboards', 'left_cupboards_free')
	register_location_object('storage_tabouret',       'images/locations/storage/objects/', 'tabouret',       'tabouret_free')
	
	register_location_object('tennis_bench_left',  'images/locations/tennis/objects/', 'bench_left', None)
	register_location_object('tennis_bench_right', 'images/locations/tennis/objects/', 'bench_left', None)
	register_location_object('tennis_cluster_1', 'images/locations/tennis/objects/', 'cluster_1', None)
	register_location_object('tennis_cluster_2', 'images/locations/tennis/objects/', 'cluster_2', None)
	register_location_object('tennis_separator', 'images/locations/tennis/objects/', 'separator', 'separator_free')
	
	add_location_object("admin", "admin_bench_pos", "admin_bench")
	add_location_object("admin", "bench_left_pos", "bench_left")
	add_location_object("admin", "lamp_pos-1", "lamp")
	add_location_object("admin", "lamp_pos-2", "lamp")
	add_location_object("admin", "lamp_pos-3", "lamp")
	add_location_object("admin", "lamp_pos-4", "lamp")
	add_location_object("admin", "lamp_pos-5", "lamp")
	
	add_location_object("bath", "bath_rails_left_pos", "bath_rails_left")
	add_location_object("bath", "bath_rails_right_pos", "bath_rails_right")
	
	add_location_object("boat_station", "boat_station_bench_pos", "boat_station_bench")
	add_location_object("boat_station", "boat_station_tabouret_pos", "boat_station_tabouret")
	
	add_location_object("canteen", "canteen_column_back_pos-1", "canteen_column_back")
	add_location_object("canteen", "canteen_column_back_pos-2", "canteen_column_back")
	add_location_object("canteen", "canteen_column_back_pos-3", "canteen_column_back")
	add_location_object("canteen", "canteen_column_pos-1", "canteen_column")
	add_location_object("canteen", "canteen_column_pos-2", "canteen_column")
	add_location_object("canteen", "canteen_column_pos-3", "canteen_column")
	add_location_object("canteen", "canteen_door_pos", "canteen_door")
	add_location_object("canteen", "chair_backward_pos-r1a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r1b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r2a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r2b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r3a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r3b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r4a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r4b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r5a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r5b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r6a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r6b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r7a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r7b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r8a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r8b", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r9a", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-r9b", "chair_backward")
	add_location_object("canteen", "chair_forward_pos-r1a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r1b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r2a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r2b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r3a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r3b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r4a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r4b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r5a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r5b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r6a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r6b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r7a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r7b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r8a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r8b", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r9a", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-r9b", "chair_forward")
	add_location_object("canteen", "chair_left_pos-c1a", "chair_left")
	add_location_object("canteen", "chair_left_pos-c1b", "chair_left")
	add_location_object("canteen", "chair_left_pos-c2a", "chair_left")
	add_location_object("canteen", "chair_left_pos-c2b", "chair_left")
	add_location_object("canteen", "chair_left_pos-c3a", "chair_left")
	add_location_object("canteen", "chair_left_pos-c3b", "chair_left")
	add_location_object("canteen", "chair_left_pos-c4a", "chair_left")
	add_location_object("canteen", "chair_left_pos-c4b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e01a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e01b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e02a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e02b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e03a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e03b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e04a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e04b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e05a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e05b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e06a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e06b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e07a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e07b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e08a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e08b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e09a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e09b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e10a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e10b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e11a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e11b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e12a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e12b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e13a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e13b", "chair_left")
	add_location_object("canteen", "chair_left_pos-e14a", "chair_left")
	add_location_object("canteen", "chair_left_pos-e14b", "chair_left")
	add_location_object("canteen", "chair_right_pos-c1a", "chair_right")
	add_location_object("canteen", "chair_right_pos-c1b", "chair_right")
	add_location_object("canteen", "chair_right_pos-c2a", "chair_right")
	add_location_object("canteen", "chair_right_pos-c2b", "chair_right")
	add_location_object("canteen", "chair_right_pos-c3a", "chair_right")
	add_location_object("canteen", "chair_right_pos-c3b", "chair_right")
	add_location_object("canteen", "chair_right_pos-c4a", "chair_right")
	add_location_object("canteen", "chair_right_pos-c4b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e01a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e01b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e02a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e02b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e03a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e03b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e04a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e04b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e05a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e05b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e06a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e06b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e07a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e07b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e08a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e08b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e09a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e09b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e10a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e10b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e11a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e11b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e12a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e12b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e13a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e13b", "chair_right")
	add_location_object("canteen", "chair_right_pos-e14a", "chair_right")
	add_location_object("canteen", "chair_right_pos-e14b", "chair_right")
	add_location_object("canteen", "table_h_pos-r1", "table_h")
	add_location_object("canteen", "table_h_pos-r2", "table_h")
	add_location_object("canteen", "table_h_pos-r3", "table_h")
	add_location_object("canteen", "table_h_pos-r4", "table_h")
	add_location_object("canteen", "table_h_pos-r5", "table_h")
	add_location_object("canteen", "table_h_pos-r6", "table_h")
	add_location_object("canteen", "table_h_pos-r7", "table_h")
	add_location_object("canteen", "table_h_pos-r8", "table_h")
	add_location_object("canteen", "table_h_pos-r9", "table_h")
	add_location_object("canteen", "table_v_pos-c1", "table_v")
	add_location_object("canteen", "table_v_pos-c2", "table_v")
	add_location_object("canteen", "table_v_pos-c3", "table_v")
	add_location_object("canteen", "table_v_pos-c4", "table_v")
	add_location_object("canteen", "table_v_pos-e01", "table_v")
	add_location_object("canteen", "table_v_pos-e02", "table_v")
	add_location_object("canteen", "table_v_pos-e03", "table_v")
	add_location_object("canteen", "table_v_pos-e04", "table_v")
	add_location_object("canteen", "table_v_pos-e05", "table_v")
	add_location_object("canteen", "table_v_pos-e06", "table_v")
	add_location_object("canteen", "table_v_pos-e07", "table_v")
	add_location_object("canteen", "table_v_pos-e08", "table_v")
	add_location_object("canteen", "table_v_pos-e09", "table_v")
	add_location_object("canteen", "table_v_pos-e10", "table_v")
	add_location_object("canteen", "table_v_pos-e11", "table_v")
	add_location_object("canteen", "table_v_pos-e12", "table_v")
	add_location_object("canteen", "table_v_pos-e13", "table_v")
	add_location_object("canteen", "table_v_pos-e14", "table_v")
	
	add_location_object("clubs", "bench_right_pos", "bench_right")
	add_location_object("clubs", "clubs_bench_pos", "clubs_bench")
	add_location_object("clubs", "mus_club_column_pos-1", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-2", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-3", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-4", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-5", "mus_club_column")
	add_location_object("clubs", "mus_club_rails_pos-1", "mus_club_rails")
	add_location_object("clubs", "mus_club_rails_pos-2", "mus_club_rails")
	add_location_object("clubs", "mus_club_rails_pos-3", "mus_club_rails")
	add_location_object("clubs", "mus_club_rails_pos-4", "mus_club_rails")
	
	add_location_object("crossroad", "crossroad_bench_pos", "crossroad_bench")
	
	add_location_object("enter", "gate_left_pos", "gate_left")
	add_location_object("enter", "gate_right_pos", "gate_right")
	
	add_location_object("flat", "armchair_pos", "armchair")
	add_location_object("flat", "flat_bed_pos", "flat_bed")
	add_location_object("flat", "lamp_light_pos", "lamp_light")
	add_location_object("flat", "monitor_pos", "monitor")
	
	add_location_object("hospital", "chair_forward_pos-1", "chair_forward")
	add_location_object("hospital", "chair_forward_pos-2", "chair_forward")
	
	add_location_object("house_mt", "sm_bed_pos", "sm_bed")
	
	add_location_object("houses_1", "houses_1_bench_backward_pos-1", "houses_1_bench_backward")
	add_location_object("houses_1", "houses_1_bench_backward_pos-2", "houses_1_bench_backward")
	add_location_object("houses_1", "houses_1_bench_backward_pos-3", "houses_1_bench_backward")
	add_location_object("houses_1", "houses_1_bench_backward_pos-4", "houses_1_bench_backward")
	add_location_object("houses_1", "houses_1_bench_backward_pos-5", "houses_1_bench_backward")
	add_location_object("houses_1", "houses_1_bench_forward_pos-1", "houses_1_bench_forward")
	add_location_object("houses_1", "houses_1_bench_forward_pos-2", "houses_1_bench_forward")
	add_location_object("houses_1", "houses_1_bench_forward_pos-3", "houses_1_bench_forward")
	add_location_object("houses_1", "houses_1_bench_forward_pos-4", "houses_1_bench_forward")
	add_location_object("houses_1", "houses_1_bench_with_book_pos", "houses_1_bench_with_book")
	add_location_object("houses_1", "houses_1_bench_with_chess_pos", "houses_1_bench_with_chess")
	add_location_object("houses_1", "houses_1_bench_with_paper_pos", "houses_1_bench_with_paper")
	
	add_location_object("houses_2", "bench_backward_pos-1", "bench_backward")
	add_location_object("houses_2", "bench_backward_pos-2", "bench_backward")
	add_location_object("houses_2", "bench_backward_pos-3", "bench_backward")
	add_location_object("houses_2", "bench_backward_pos-4", "bench_backward")
	add_location_object("houses_2", "bench_backward_pos-5", "bench_backward")
	add_location_object("houses_2", "bench_backward_pos-6", "bench_backward")
	add_location_object("houses_2", "bench_backward_pos-7", "bench_backward")
	add_location_object("houses_2", "bench_forward_pos-1", "bench_forward")
	add_location_object("houses_2", "bench_forward_pos-2", "bench_forward")
	add_location_object("houses_2", "bench_forward_pos-3", "bench_forward")
	add_location_object("houses_2", "bench_forward_pos-4", "bench_forward")
	add_location_object("houses_2", "bench_forward_pos-5", "bench_forward")
	add_location_object("houses_2", "bench_forward_pos-6", "bench_forward")
	
	add_location_object("liaz", "liaz_bench_left_pos1", "liaz_bench_left")
	add_location_object("liaz", "liaz_bench_left_pos2", "liaz_bench_left")
	add_location_object("liaz", "liaz_bench_left_pos3", "liaz_bench_left")
	add_location_object("liaz", "liaz_bench_middle_pos", "liaz_bench_middle")
	add_location_object("liaz", "liaz_bench_right_pos1", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos10", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos11", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos12", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos2", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos3", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos4", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos5", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos6", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos7", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos8", "liaz_bench_right")
	add_location_object("liaz", "liaz_bench_right_pos9", "liaz_bench_right")
	add_location_object("liaz", "liaz_chair_forward_pos", "liaz_chair_forward")
	
	add_location_object("library", "library_armchair_pos-1", "library_armchair")
	add_location_object("library", "library_armchair_pos-2", "library_armchair")
	add_location_object("library", "library_chair_left_pos-1", "library_chair_left")
	add_location_object("library", "library_chair_left_pos-2", "library_chair_left")
	add_location_object("library", "library_chair_left_pos-3", "library_chair_left")
	add_location_object("library", "library_cupboard_1_pos", "library_cupboard_1")
	add_location_object("library", "library_cupboard_2_pos", "library_cupboard_2")
	add_location_object("library", "library_cupboard_3_pos", "library_cupboard_3")
	
	add_location_object("library_and_hospital", "library_and_hospital_bench_pos-1", "library_and_hospital_bench")
	add_location_object("library_and_hospital", "library_and_hospital_bench_pos-2", "library_and_hospital_bench")
	
	add_location_object("mus_club", "blue_guitar_pos", "blue_guitar")
	add_location_object("mus_club", "cymbal_pos", "cymbal")
	add_location_object("mus_club", "drum_and_tube_pos", "drum_and_tube")
	add_location_object("mus_club", "drum_pos", "drum")
	add_location_object("mus_club", "guitar_pos", "guitar")
	add_location_object("mus_club", "mus_club_chair_pos-1", "mus_club_chair")
	add_location_object("mus_club", "mus_club_chair_pos-2", "mus_club_chair")
	add_location_object("mus_club", "mus_club_chair_pos-3", "mus_club_chair")
	add_location_object("mus_club", "mus_club_far_cupboard_pos", "mus_club_far_cupboard")
	add_location_object("mus_club", "mus_club_left_cupboard_pos", "mus_club_left_cupboard")
	add_location_object("mus_club", "mus_club_microphone_pos", "mus_club_microphone")
	add_location_object("mus_club", "piano_chair_pos", "piano_chair")
	add_location_object("mus_club", "piano_pos", "piano")
	add_location_object("mus_club", "stand_pos", "stand")
	
	add_location_object("radio_club", "radio_club_cupboards_pos", "radio_club_cupboards")
	add_location_object("radio_club", "radio_club_table_pos", "radio_club_table")
	add_location_object("radio_club", "radio_club_tabouret_pos-1", "radio_club_tabouret")
	add_location_object("radio_club", "radio_club_tabouret_pos-2", "radio_club_tabouret")
	add_location_object("radio_club", "radio_club_tabouret_pos-3", "radio_club_tabouret")
	
	add_location_object("radio_storeroom", "radio_storeroom_tabouret_pos", "radio_storeroom_tabouret")
	
	add_location_object("scene", "scene_anti_fire_pos", "scene_anti_fire")
	add_location_object("scene", "scene_bench_1_pos", "scene_bench_1")
	add_location_object("scene", "scene_bench_2_pos", "scene_bench_2")
	add_location_object("scene", "scene_bench_3_pos", "scene_bench_3")
	add_location_object("scene", "scene_bench_4_pos", "scene_bench_4")
	add_location_object("scene", "scene_bench_5_pos", "scene_bench_5")
	add_location_object("scene", "scene_microphone_pos", "scene_microphone")
	add_location_object("scene", "scene_sound_pos-1", "scene_sound")
	add_location_object("scene", "scene_sound_pos-2", "scene_sound")
	add_location_object("scene", "scene_table_pos", "scene_table")
	
	add_location_object("square", "bench_left_pos-1", "bench_left")
	add_location_object("square", "bench_left_pos-2", "bench_left")
	add_location_object("square", "bench_left_pos-3", "bench_left")
	add_location_object("square", "bench_right_pos-1", "bench_right")
	add_location_object("square", "bench_right_pos-2", "bench_right")
	add_location_object("square", "bench_right_pos-3", "bench_right")
	add_location_object("square", "canteen_bench_pos", "canteen_bench")
	add_location_object("square", "car_pos", "car")
	add_location_object("square", "lamp_pos-1", "lamp")
	add_location_object("square", "lamp_pos-10", "lamp")
	add_location_object("square", "lamp_pos-11", "lamp")
	add_location_object("square", "lamp_pos-2", "lamp")
	add_location_object("square", "lamp_pos-3", "lamp")
	add_location_object("square", "lamp_pos-4", "lamp")
	add_location_object("square", "lamp_pos-5", "lamp")
	add_location_object("square", "lamp_pos-6", "lamp")
	add_location_object("square", "lamp_pos-7", "lamp")
	add_location_object("square", "lamp_pos-8", "lamp")
	add_location_object("square", "lamp_pos-9", "lamp")
	add_location_object("square", "washbasin_left_pos-1", "washbasin_left")
	add_location_object("square", "washbasin_left_pos-2", "washbasin_left")
	add_location_object("square", "washbasin_right_pos-1", "washbasin_right")
	add_location_object("square", "washbasin_right_pos-2", "washbasin_right")
	
	add_location_object("stadium", "stadium_bench_left_pos-1", "stadium_bench_left")
	add_location_object("stadium", "stadium_bench_left_pos-2", "stadium_bench_left")
	add_location_object("stadium", "stadium_bench_left_pos-3", "stadium_bench_left")
	add_location_object("stadium", "stadium_bench_left_pos-4", "stadium_bench_left")
	add_location_object("stadium", "stadium_gates_pos", "stadium_gates")
	add_location_object("stadium", "stadium_rails_pos", "stadium_rails")
	add_location_object("stadium", "stadium_turniks_pos", "stadium_turniks")
	
	add_location_object("storage", "broom_pos", "broom")
	add_location_object("storage", "shovel_pos", "shovel")
	add_location_object("storage", "storage_cupboard_pos", "storage_cupboard")
	add_location_object("storage", "storage_left_cupboards_pos", "storage_left_cupboards")
	add_location_object("storage", "storage_tabouret_pos", "storage_tabouret")
	
	add_location_object("tennis", "bench_backward_pos-1", "bench_backward")
	add_location_object("tennis", "bench_backward_pos-2", "bench_backward")
	add_location_object("tennis", "bench_forward_pos", "bench_forward")
	add_location_object("tennis", "tennis_bench_left_pos-1", "tennis_bench_left")
	add_location_object("tennis", "tennis_bench_left_pos-2", "tennis_bench_left")
	add_location_object("tennis", "tennis_bench_right_pos-1", "tennis_bench_right")
	add_location_object("tennis", "tennis_bench_right_pos-2", "tennis_bench_right")
	add_location_object("tennis", "tennis_cluster_1_pos", "tennis_cluster_1")
	add_location_object("tennis", "tennis_cluster_2_pos", "tennis_cluster_2")
	add_location_object("tennis", "tennis_separator_pos", "tennis_separator")
	
