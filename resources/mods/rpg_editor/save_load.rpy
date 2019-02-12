init -1000 python:
	locations_path = 'images/locations/'
	location_objects_path = 'images/location_objects/'

	preview_path = 'mods/rpg_editor/cache/'
	if not os.path.exists(preview_path):
		os.mkdir(preview_path)
	
	locations_file_path = 'mods/rpg_editor/results/locations.rpy'
	location_objects_file_path = 'mods/rpg_editor/results/location_objects.rpy'
	
	
	def clear():
		global locations, locations_times
		
		locations = dict()
		locations_times = persistent.locations_times = Object()
	
	if persistent.locations_times is None:
		persistent.locations_times = Object()
	
	locations_times = persistent.locations_times


init python:
	def register_new_locations():
		ext = location_object_ext
		
		locations_dirs = [i for i in os.listdir(locations_path) if not i.startswith('_') and os.path.exists(locations_path + i + '/main.' + ext)]
		
		for name in locations_dirs:
			preview_created = False
			if not os.path.exists(preview_path + name + '.' + ext):
				preview_created = True
				make_preview(name)
			
			path = locations_path + name
			if locations_times.has_key(name):
				files_time, preview_time = locations_times[name]
				if files_time >= os.path.getmtime(path):
					continue
				del locations[name]
			
			if not preview_created:
				make_preview(name)
			
			main = path + '/main.' + ext
			register_location(name, path, False, get_image_width(main), get_image_height(main))
			
			set_save_locations()
	
	def get_preview(name):
		return preview_path + name + '.png?' + str(locations_times[name][1])
	
	def make_preview(name):
		location = locations[name]
		
		w, h = location.width, location.height
		
		if location.over:
			image = im.Composite((w, h), (0, 0), location.main(), (0, 0), location.over())
		else:
			image = location.main()
		
		to_save = preview_path + name + '.png'
		im.save(image, to_save, 128 * w / max(w, h), 128 * h / max(w, h))
		
		locations_times[name] = [
			os.path.getmtime(locations_path + name),
			os.path.getmtime(to_save)
		]
	
	def save():
		place_indent = ' ' * (len('location') - len('place'))
		exit_indent = ' ' * (len('location') - len('exit'))
		
		tmp = ['init python:', '\t']
		location_names = locations.keys()
		location_names.sort()
		for location_name in location_names:
			location = locations[location_name]
			
			location_name = '"' + location_name + '"'
			path = '"' + location.directory + '"'
			is_room = str(location.is_room)
			w, h = str(location.width), str(location.height)
			
			tmp.append('\tregister_location(' + ', '.join([location_name, path, is_room, w, h]) + ')')
			
			places = location.places.keys()
			places.sort()
			for place_name in places:
				place = location.places[place_name]
				place_name = '"' + place_name + '"'
				
				if place.side_exit is None:
					x, y = str(place.x), str(place.y)
					w, h = str(place.width), str(place.height)
					tmp.append('\tregister_place(' + place_indent + ', '.join([location_name, place_name, x, y, w, h]) + ')')
			
			for place_name in places:
				place = location.places[place_name]
				place_name = '"' + place_name + '"'
				
				if place.side_exit is not None:
					px, py = place.x, place.y
					x, y, w, h, exit_x, exit_y, exit_w, exit_h = get_place_coords(place)
					
					x += px
					y += py
					exit_x += px
					exit_y += py
					
					in_place_indent = ' ' * (len(', ') + len(location_name))
					place_args = [location_name, place_name + in_place_indent] + map(str, [x, y, w, h])
					exit_args  = [location_name, place_name, location_name   ] + map(str, [exit_x, exit_y, exit_w, exit_h])
					tmp.append('\tregister_place(' + place_indent + ', '.join(place_args) + ')')
					tmp.append('\tregister_exit(' +  exit_indent  + ', '.join(exit_args)  + ')')
			
			for exit in location.exits:
				to_location_name = '"' + exit.to_location_name + '"'
				to_place_name = '"' + exit.to_place_name + '"'
				x, y = str(exit.x), str(exit.y)
				w, h = str(exit.width), str(exit.height)
				
				tmp.append('\tregister_exit(' + ', '.join([location_name, to_location_name, to_place_name, x, y, w, h]) + ')')
			
			tmp.append('\t')
		
		tmp += ['\t', '\t']
		
		for location_name in locations:
			location = locations[location_name]
			if not location.using:
				x = y = "None"
			else:
				x, y = str(int(location.x)), str(int(location.y))
			tmp.append('\tlocations["' + location_name + '"].x, locations["' + location_name + '"].y = ' + x + ', ' + y)
		
		tmp.append('')
		
		locations_file = open(locations_file_path, 'w')
		locations_file.writelines(map(lambda s: s + '\n', tmp))
		locations_file.close()
		
		
		
		location_objects_file = open(location_objects_file_path, 'r')
		tmp = location_objects_file.readlines()
		location_objects_file.close()
		for i in xrange(len(tmp) - 1, -1, -1):
			if tmp[i].startswith('\tregister_location_object'):
				s = 0
				while i < len(tmp):
					line = tmp[i]
					i += 1
					s += line.count('(') - line.count(')')
					if s == 0:
						break
				break
		tmp = map(lambda s: '\t' if s == '\t\n' else s.rstrip(), tmp[0:i])
		tmp.append('\t')
		
		obj_names = location_objects.keys()
		location_names = locations.keys()
		location_names.sort()
		for location_name in location_names:
			location = locations[location_name]
			
			added = False
			places = location.places.keys()
			places.sort()
			for place_name in places:
				if '_pos' in place_name:
					obj_name = place_name[0:place_name.index('_pos')]
					if obj_name in obj_names:
						added = True
						args = map(lambda s: '"' + s + '"', [location_name, place_name, obj_name])
						tmp.append('\tadd_location_object(' + ', '.join(args) + ')')
			
			if added:
				tmp.append('\t')
		
		location_objects_file = open(location_objects_file_path, 'w')
		location_objects_file.writelines(map(lambda s: s + '\n', tmp))

