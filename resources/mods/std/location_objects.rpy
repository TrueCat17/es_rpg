init 1 python:
	register_location_object('ikarus', 'images/locations/enter/objects/', 'ikarus_main', 'ikarus_free')
	
	register_location_object('gate_left', 'images/locations/enter/objects/', 'gate_left_main', 'gate_free')
	register_location_object('gate_right', 'images/locations/enter/objects/', 'gate_right_main', 'gate_free')
	
	register_location_object_animation(
		'gate_right', 'open',
		'images/locations/enter/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 0,
		3, 2, 2,
		-1
	)
	register_location_object_animation(
		'gate_right', 'opening',
		'images/locations/enter/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 0,
		3, 0, 2
	)
	register_location_object_animation(
		'gate_right', 'closing',
		'images/locations/enter/objects/anim/', 'gate_right_main', 'gate_right_free',
		0, 0,
		3, 2, 0
	)
	
	register_location_object('musclub_rails', 'images/locations/clubs/objects/', 'musclub_rails', None)
	register_location_object('musclub_column', 'images/locations/clubs/objects/', 'musclub_column', None)
	
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
	
