init 1 python:
	register_location_object('ikarus', 'images/location_objects/', 'ikarus_main', 'ikarus_free')
	
	register_location_object('left_gate', 'images/location_objects/', 'left_gate_main', 'left_gate_free')
	register_location_object('right_gate', 'images/location_objects/', 'right_gates_main', 'right_gates_free', frames = 3, main_frame = 2)
	
	register_location_object('musclub_rails', 'images/location_objects/', 'musclub_rails', None)
	register_location_object('musclub_column', 'images/location_objects/', 'musclub_column', None)
	
