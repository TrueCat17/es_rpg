init 1 python:
	
	set_default_location_ambience({None: 'sound/ambience/camp.ogg', 'night': 'sound/ambience/camp_night.ogg'})
	
	set_location_ambience('flat', '')
	set_location_ambience('city', 'sound/ambience/cold_wind.ogg')
	set_location_ambience('station', 'sound/ambience/cold_wind.ogg')
	set_location_ambience('liaz', '')
	
	set_location_ambience('ikarus', None, 0.5)
	
	set_location_ambience('radio_club', 'sound/ambience/clubs_inside.ogg')
	set_location_ambience('radio_storeroom', 'sound/ambience/clubs_inside.ogg', 0.5)
