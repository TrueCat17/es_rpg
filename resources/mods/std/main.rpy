init 10 python:
	was = []
	
	escape_choice = 0
	
	def my_interface_bg():
		iw, ih = int(inventory.xsize), int(inventory.ysize)
		cache = my_interface_bg.__dict__
		key = (iw, ih)
		if key in cache:
			return cache[key]
		
		back = 'images/gui/menu/pause/back.png'
		leaf = 'images/gui/menu/pause/leaf.png'
		x, y = 5, 15
		w, h = get_image_size(leaf)
		k = 0.07
		w, h = int(k * iw), int(k * ih * (float(iw) / ih) / (float(w) / h))
		
		args = [
			(iw + x * 2, ih + y * 2),
			(x, y), im.scale(back, iw, ih),
			(iw - w + x * 2, ih - h + y * 2), im.scale(leaf, w, h),
		]
		cache[key] = im.composite(*args)
		return cache[key]
	gui.inventory_bg = my_interface_bg
	gui.inventory_edge_spacing = 60
	
	def get_borders(w, h, border, color):
		cache = get_borders.__dict__
		key = (w, h, border, color)
		if key in cache:
			return cache[key]
		
		color = im.rect(color)
		args = [
			(w, h),
			(0, 0), im.scale(color, w, border),
			(0, h - border), im.scale(color, w, border),
			(0, border), im.scale(color, border, h),
			(w - border, border), im.scale(color, border, h),
		]
		cache[key] = im.composite(*args)
		return cache[key]
	def my_interface_cell_usual():
		return get_borders(int(inventory.cell_xsize), int(inventory.cell_ysize), int(inventory.cell_xsize) / 15, '#333')
	def my_interface_cell_selected():
		return get_borders(int(inventory.cell_xsize), int(inventory.cell_ysize), int(inventory.cell_xsize) / 15, '#A42')
	gui.inventory_cell_usual_over = my_interface_cell_usual
	gui.inventory_cell_selected_over = my_interface_cell_selected
	
	
	def get_place_labels():
		usual_label = cur_location_name + '__' + (cur_place_name or 'unknown')
		
		res = []
		for quest in get_started_quests():
			res.extend(get_glob_labels(quest + '__' + usual_label))
		res.extend(get_glob_labels('day' + str(clock.day) + '__' + usual_label))
		res.extend(get_glob_labels(usual_label))
		return res
	
	
	gate_right = get_location_objects('enter', None, 'gate_right')[0]
	gate_right.start_animation('open')
	gate_right.update_location_paths()


init 25 python:
	limit_camp_out()
	limit_rooms()
	canteen.init()
	
	add_butterflies(min=1, max=2)
	remove_location_object('station', None, Butterfly, count = -1)
	
	def spec_start():
		clock.pause = False
		clock.set('1-17:14:45')
		clock.acceleration = 6
		show_screen('clock')
		
		day1_set_eaters_20h()
		
		init_characters()
		cloud.init()
		
		lineup.enable_reminder = True
		set_rpg_control(True)
		unlimit_all(me)
		set_location('square', 'admin')# {'x': 250, 'y': 250})
#		me.x -= 200
#		me.y += 300
		me.set_dress('sport')
		
		if 0:
			characters_auto(False)
			
			show_character(mi, me)
			print mi.move_to_place(['clubs', 'enter'])

label start:
	#call day0_start
	#call day1_start
	$ spec_start()
	
	call rpg_loop
