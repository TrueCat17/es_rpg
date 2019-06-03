init 1 python:
	
	register_location_object('armchair',  'images/locations/flat/objects/', 'armchair', None)
	register_location_object('flat_keys', 'images/locations/objects/', 'flat_keys', None, 1)
	register_location_object('lighter',   'images/locations/objects/', 'lighter',   None, 1)
	register_location_object('notepad',   'images/locations/objects/', 'notepad',   None, 1)
	register_location_object('phone',     'images/locations/objects/', 'phone',     None, 1)
	
	
	register_location_object('liaz', 'images/locations/station/objects/', 'liaz', None)
	
	
	register_location_object('uv_night_prologue', 'images/locations/objects/', 'uv_night_prologue', None)
	
	register_location_object('ikarus', 'images/locations/enter/objects/', 'ikarus_main', 'ikarus_free')
	
	register_location_object('gate_left', 'images/locations/enter/objects/', 'gate_left_main', 'gate_free')
	register_location_object('gate_right', 'images/locations/enter/objects/', 'gate_right_main', 'gate_free')
	
	register_location_object_animation('gate_right', 'open',
		'images/locations/enter/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 0,
		3, 2, 2,
		-1
	)
	register_location_object_animation('gate_right', 'opening',
		'images/locations/enter/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 0,
		3, 0, 2
	)
	register_location_object_animation('gate_right', 'closing',
		'images/locations/enter/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 0,
		3, 2, 0
	)
	
	
	register_location_object('cupboard_1',  'images/locations/library/objects/', 'cupboard_1', 'cupboard_free')
	register_location_object('cupboard_2',  'images/locations/library/objects/', 'cupboard_2', 'cupboard_free')
	register_location_object('cupboard_3',  'images/locations/library/objects/', 'cupboard_3', 'cupboard_free')
	
	
	register_location_object('musclub_rails',  'images/locations/clubs/objects/', 'musclub_rails', None)
	register_location_object('musclub_column', 'images/locations/clubs/objects/', 'musclub_column', None)
	
	
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
	register_location_object('canteen_door', 'images/locations/canteen/objects/', 'door', None)
	
	
	register_location_object('musclub_microphone', 'images/locations/musclub/objects/', 'microphone', 'microphone_free')
	register_location_object('stand',              'images/locations/musclub/objects/', 'stand',      'stand_free')
	
	
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
	add_location_object("canteen", "canteen_door_pos", "canteen_door")
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
	
	add_location_object("clubs", "musclub_column_pos-1", "musclub_column")
	add_location_object("clubs", "musclub_column_pos-2", "musclub_column")
	add_location_object("clubs", "musclub_column_pos-3", "musclub_column")
	add_location_object("clubs", "musclub_column_pos-4", "musclub_column")
	add_location_object("clubs", "musclub_column_pos-5", "musclub_column")
	add_location_object("clubs", "musclub_rails_pos-1", "musclub_rails")
	add_location_object("clubs", "musclub_rails_pos-2", "musclub_rails")
	add_location_object("clubs", "musclub_rails_pos-3", "musclub_rails")
	add_location_object("clubs", "musclub_rails_pos-4", "musclub_rails")
	
	add_location_object("enter", "gate_left_pos", "gate_left")
	add_location_object("enter", "gate_right_pos", "gate_right")
	add_location_object("enter", "ikarus_pos", "ikarus")
	
	add_location_object("flat", "armchair_pos", "armchair")
	add_location_object("flat", "flat_keys_pos", "flat_keys")
	add_location_object("flat", "lighter_pos", "lighter")
	add_location_object("flat", "notepad_pos", "notepad")
	add_location_object("flat", "phone_pos", "phone")
	
	add_location_object("library", "cupboard_1_pos", "cupboard_1")
	add_location_object("library", "cupboard_2_pos", "cupboard_2")
	add_location_object("library", "cupboard_3_pos", "cupboard_3")
	
	add_location_object("musclub", "musclub_microphone_pos", "musclub_microphone")
	add_location_object("musclub", "stand_pos", "stand")
	
	add_location_object("scene", "scene_microphone_pos", "scene_microphone")
	
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
	
