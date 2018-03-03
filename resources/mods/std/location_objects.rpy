init 1 python:
	register_location_object('liaz', 'images/location_objects/liaz_main.png', None)
	register_location_object('ikarus', 'images/location_objects/ikarus_main.png', 'images/location_objects/ikarus_free.png')
	
	add_location_object('enter', 'bus_pos', 'ikarus')
	
