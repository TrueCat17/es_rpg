init 10 python:
	db_font = 'FixEx3'
	
	dreamgirl = Character('...', color='#FFFFFF')
	
	day_num = 0
	
	def can_exit_to(to_location_name, to_place_name):
		day_func = globals()['day' + str(day_num) + '_can_exit_to']
		return day_func(to_location_name, to_place_name)
	
	def check_exist_label_glob(name):
		if renpy.has_label(name):
			return name
		
		labels = [label[:-1] for label in renpy.get_all_labels() if label[-1] == "*"]
		
		while name:
			for label in labels:
				if label == name:
					return label + '*'
			name = name[:-1]
		return None
	
	def get_place_label():
		const = cur_location_name + '__' + (cur_place_name or 'unknown')
		res = 'day' + str(day_num) + '__' + const
		
		res = check_exist_label_glob(res)
		if res:
			return res
		res = check_exist_label_glob(const)
		if res:
			return res
		return const
	
	fog_params = dict(
		name='fog',
		image='images/locations/objects/fog.' + location_object_ext,
		alpha=0.5,
		dx=0.010,
		dy=0.014,
	)
	
	gate_right = get_location_objects('enter', None, 'gate_right')[0]
	gate_right.start_animation('open')


label start:
	call day0_start
	
	call rpg_loop
