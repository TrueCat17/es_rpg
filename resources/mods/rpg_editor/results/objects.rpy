init 1 python:
	
	register_location_object('flat_keys', 'images/locations/objects/', 'flat_keys', None, 1)
	register_location_object('lighter',   'images/locations/objects/', 'lighter',   None, 1)
	register_location_object('notepad',   'images/locations/objects/', 'notepad',   None, 1)
	register_location_object('phone',     'images/locations/objects/', 'phone',     None, 1)
	
	register_location_object('armchair',   'images/locations/flat/objects/', 'armchair', None)
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
	
	register_location_object('snow_car', 'images/locations/city/objects/', 'snow_car', 'snow_car_free')
	register_location_object('city_lamp_left', 'images/locations/city/objects/', 'lamp_left', 'lamp_left_free')
	register_location_object('city_lamp_right', 'images/locations/city/objects/', 'lamp_right', 'lamp_right_free')
	register_location_object('city_sign', 'images/locations/city/objects/', 'sign', 'sign_free')
	
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
	
	
	register_location_object('cupboard_1',  'images/locations/library/objects/', 'cupboard_1', 'cupboard_free')
	register_location_object('cupboard_2',  'images/locations/library/objects/', 'cupboard_2', 'cupboard_free')
	register_location_object('cupboard_3',  'images/locations/library/objects/', 'cupboard_3', 'cupboard_free')
	
	
	register_location_object('mus_club_rails',  'images/locations/clubs/objects/', 'mus_club_rails', None)
	register_location_object('mus_club_column', 'images/locations/clubs/objects/', 'mus_club_column', None)
	
	
	register_location_object('bench_left',  'images/locations/objects/', 'bench_left',  'bench_free')
	register_location_object('bench_right', 'images/locations/objects/', 'bench_right', 'bench_free')
	register_location_object('lamp', 'images/locations/objects/', 'lamp', 'lamp_free')
	
	
	register_location_object('chair_left',     'images/locations/canteen/objects/', 'chair_left', 'chair_free')
	register_location_object('chair_right',    'images/locations/canteen/objects/', 'chair_right', 'chair_free')
	register_location_object('chair_backward', 'images/locations/canteen/objects/', 'chair_backward', 'chair_backward_free')
	register_location_object('chair_forward',  'images/locations/canteen/objects/', 'chair_forward', 'chair_forward_free')
	register_location_object('table_h', 'images/locations/canteen/objects/', 'table_h', 'table_h_free')
	register_location_object('table_v', 'images/locations/canteen/objects/', 'table_v', 'table_v_free')
	register_location_object('canteen_column',      'images/locations/canteen/objects/', 'column', 'column_free')
	register_location_object('canteen_column_back', 'images/locations/canteen/objects/', 'column_back', 'column_free')
	
	
	register_location_object('mus_club_microphone', 'images/locations/mus_club/objects/', 'microphone', 'microphone_free')
	register_location_object('stand',              'images/locations/mus_club/objects/', 'stand',      'stand_free')
	
	
	register_location_object('scene_microphone', 'images/locations/scene/objects/', 'microphone', 'microphone_free')
	
	
	register_location_object('car', 'images/locations/square/objects/', 'car', 'car_free')
	register_location_object('washbasin_left',  'images/locations/square/objects/', 'washbasin_left',  'washbasin_free')
	register_location_object('washbasin_right', 'images/locations/square/objects/', 'washbasin_right', 'washbasin_free')
	
	
	register_location_object('stadium_rails', 'images/locations/stadium/objects/', 'rails', None)
	
	
	register_location_object('separator', 'images/locations/tennis/objects/', 'separator', 'separator_free')
	
	
	register_location_object('bath_rails_left',  'images/locations/bath/objects/', 'rails_left',  None)
	register_location_object('bath_rails_right', 'images/locations/bath/objects/', 'rails_right', None)
	
	add_location_object("admin", "bench_left_pos", "bench_left")
	add_location_object("admin", "lamp_pos-1", "lamp")
	add_location_object("admin", "lamp_pos-2", "lamp")
	add_location_object("admin", "lamp_pos-3", "lamp")
	add_location_object("admin", "lamp_pos-4", "lamp")
	add_location_object("admin", "lamp_pos-5", "lamp")
	
	add_location_object("bath", "bath_rails_left_pos", "bath_rails_left")
	add_location_object("bath", "bath_rails_right_pos", "bath_rails_right")
	
	add_location_object("canteen", "canteen_column_back_pos-1", "canteen_column_back")
	add_location_object("canteen", "canteen_column_back_pos-2", "canteen_column_back")
	add_location_object("canteen", "canteen_column_back_pos-3", "canteen_column_back")
	add_location_object("canteen", "canteen_column_pos-1", "canteen_column")
	add_location_object("canteen", "canteen_column_pos-2", "canteen_column")
	add_location_object("canteen", "canteen_column_pos-3", "canteen_column")
	add_location_object("canteen", "chair_backward_pos-01", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-02", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-03", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-04", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-05", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-06", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-07", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-08", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-09", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-10", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-11", "chair_backward")
	add_location_object("canteen", "chair_backward_pos-12", "chair_backward")
	add_location_object("canteen", "chair_forward_pos-01", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-02", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-03", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-04", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-05", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-06", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-07", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-08", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-09", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-10", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-11", "chair_forward")
	add_location_object("canteen", "chair_forward_pos-12", "chair_forward")
	add_location_object("canteen", "table_h_pos-1", "table_h")
	add_location_object("canteen", "table_h_pos-2", "table_h")
	add_location_object("canteen", "table_h_pos-3", "table_h")
	add_location_object("canteen", "table_h_pos-4", "table_h")
	add_location_object("canteen", "table_h_pos-5", "table_h")
	add_location_object("canteen", "table_h_pos-6", "table_h")
	
	add_location_object("city", "city_lamp_left_pos-1", "city_lamp_left")
	add_location_object("city", "city_lamp_left_pos-2", "city_lamp_left")
	add_location_object("city", "city_lamp_left_pos-3", "city_lamp_left")
	add_location_object("city", "city_lamp_left_pos-4", "city_lamp_left")
	add_location_object("city", "city_lamp_left_pos-5", "city_lamp_left")
	add_location_object("city", "city_lamp_left_pos-6", "city_lamp_left")
	add_location_object("city", "city_lamp_right_pos-1", "city_lamp_right")
	add_location_object("city", "city_lamp_right_pos-2", "city_lamp_right")
	add_location_object("city", "city_lamp_right_pos-3", "city_lamp_right")
	add_location_object("city", "city_lamp_right_pos-4", "city_lamp_right")
	add_location_object("city", "city_lamp_right_pos-5", "city_lamp_right")
	add_location_object("city", "city_lamp_right_pos-6", "city_lamp_right")
	add_location_object("city", "city_sign_pos", "city_sign")
	add_location_object("city", "snow_car_pos", "snow_car")
	
	add_location_object("clubs", "mus_club_column_pos-1", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-2", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-3", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-4", "mus_club_column")
	add_location_object("clubs", "mus_club_column_pos-5", "mus_club_column")
	add_location_object("clubs", "mus_club_rails_pos-1", "mus_club_rails")
	add_location_object("clubs", "mus_club_rails_pos-2", "mus_club_rails")
	add_location_object("clubs", "mus_club_rails_pos-3", "mus_club_rails")
	add_location_object("clubs", "mus_club_rails_pos-4", "mus_club_rails")
	
	add_location_object("enter", "gate_left_pos", "gate_left")
	add_location_object("enter", "gate_right_pos", "gate_right")
	
	add_location_object("flat", "armchair_pos", "armchair")
	add_location_object("flat", "lamp_light_pos", "lamp_light")
	add_location_object("flat", "monitor_pos", "monitor")
	
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
	
	add_location_object("library", "cupboard_1_pos", "cupboard_1")
	add_location_object("library", "cupboard_2_pos", "cupboard_2")
	add_location_object("library", "cupboard_3_pos", "cupboard_3")
	
	add_location_object("mus_club", "mus_club_microphone_pos", "mus_club_microphone")
	add_location_object("mus_club", "stand_pos", "stand")
	
	add_location_object("square", "bench_left_pos-1", "bench_left")
	add_location_object("square", "bench_left_pos-2", "bench_left")
	add_location_object("square", "bench_left_pos-3", "bench_left")
	add_location_object("square", "bench_right_pos-1", "bench_right")
	add_location_object("square", "bench_right_pos-2", "bench_right")
	add_location_object("square", "bench_right_pos-3", "bench_right")
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
	
	add_location_object("stadium", "stadium_rails_pos", "stadium_rails")
	
	add_location_object("tennis", "separator_pos", "separator")
	
