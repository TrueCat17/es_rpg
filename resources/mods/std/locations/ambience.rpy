init 1 python:
	
	ambience_dir = 'sound/ambience/'
	
	set_default_location_ambience({
		None: ambience_dir + 'camp.ogg',
		'sunset': ambience_dir + 'camp_sunset.ogg',
		'night': ambience_dir + 'camp_night.ogg'
	})
	
	set_location_ambience('flat', '')
	set_location_ambience('station', ambience_dir + 'cold_wind.ogg')
	set_location_ambience('liaz', '')
	
	set_location_ambience('ikarus', None, 0.5)
	
	
	for name in ('scene', 'bath', 'washbasins', 'crossroad'):
		set_location_ambience(name, None, 0.7)
	
	for name in ('dv', 'sl', 'un'):
		set_location_ambience('house_' + name, None, 0.3)
	
	
	set_location_ambience('radio_club', ambience_dir + 'clubs_inside.ogg')
	set_location_ambience('radio_storeroom', ambience_dir + 'clubs_inside.ogg', 0.5)
	
	
	for name in ('house_mt', 'mus_club', 'hospital'):
		set_location_ambience(name, {
			None: ambience_dir + 'room_clock.ogg',
			'sunset': ambience_dir + 'room_clock_sunset.ogg',
			'night': ambience_dir + 'room_clock_night.ogg',
		})
	
	
	set_location_ambience('canteen', ambience_dir + 'canteen_empty.ogg')
	
	set_location_ambience('library', {
		None: ambience_dir + 'library.ogg',
		'night': ''
	})
	set_location_ambience('stadium', {
		None: ambience_dir + 'stadium.ogg',
		'night': ambience_dir + 'camp_night.ogg'
	})
	
	
	for i in range(10):
		name = 'forest_path-' + str(i)
		if i in (0, 4, 5, 9):
			sound_name = 'road'
			if i == 0:
				name = 'enter'
		else:
			sound_name = 'forest'
		
		set_location_ambience(name, {
			None: ambience_dir + sound_name + '.ogg',
			'sunset': ambience_dir + sound_name + '_sunset.ogg',
			'night': ambience_dir + sound_name + '_night.ogg'
		})
	
	for name in ('boat_station', 'beach'):
		set_location_ambience(name, {
			None: ambience_dir + 'boat_station.ogg',
			'night': ambience_dir + 'boat_station_night.ogg'
		}, 0.5 if name == 'beach' else 1)
	
	
	set_location_ambience('old_camp', {
		'day': ambience_dir + 'forest.ogg',
		None: ambience_dir + 'old_camp.ogg'
	})
	
	for name in ('bunker', 'bunker_enter'):
		set_location_ambience(name, ambience_dir + 'catacombs.ogg')
	
	
