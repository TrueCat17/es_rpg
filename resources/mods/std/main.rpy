init 10 python:
	db_font = 'FixEx3'
	
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

init 25 python:
	limit_camp_out()
	limit_rooms()
	
	def spec_start():
		global day_num
		day_num = 1
		
		init_characters()
		
		set_rpg_control(True)
		set_location('square', {'x': 400, 'y': 450})
		me.set_dress('sport')
		
		if 0:
			characters_auto(False)
			
			show_character(mi, me)
			print mi.move_to_place([('houses_2', 'house_dv')])


label start:
	call day0_start
	#$ spec_start()
	
	call rpg_loop
