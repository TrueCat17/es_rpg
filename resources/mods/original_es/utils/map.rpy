init -51 python:
	map_pics = {
		"bg":        "images/maps/bg.png",
		"available": "images/maps/available.png",
		"selected":  "images/maps/selected.png"
	}
	
	map_zones = {
		"me_mt_house":   { "position":( 825,  47, 1005, 230) },
		"estrade":       { "position":(1039,  47, 1288, 230) },
		"music_club":    { "position":( 541, 231,  711, 356) },
		"square":        { "position":( 825, 357, 1005, 665) },
		"dining_hall":   { "position":(1006, 457, 1159, 665) },
		"sport_area":    { "position":(1160, 457, 1578, 665) },
		"beach":         { "position":(1160, 666, 1578, 871) },
		"boat_station":  { "position":( 825, 666, 1005, 871) },
		"clubs":         { "position":( 418, 357,  711, 665) },
		"library":       { "position":(1160, 231, 1288, 456) },
		"medic_house":   { "position":(1039, 231, 1159, 456) },
		"camp_entrance": { "position":( 278, 357,  417, 665) },
		"forest":        { "position":( 541,  47,  711, 230) }
	}

init -50 python:
	global_map_result = "error"
	
	def disable_all_zones():
		for zone in map_zones.values():
			zone["label"] = "nothing_here"
			zone["available"] = False
	def enable_all_zones():
		for zone in map_zones.values():
			zone["label"] = "nothing_here"
			zone["available"] = True
	disable_all_zones()
	
	def set_zone(name, label):
		map_zones[name]["label"] = label
		map_zones[name]["available"] = True
	def reset_zone(name):
		map_zones[name]["available"] = False
	
	def disable_current_zone():
		reset_zone(global_map_result)
	def zone_click(name):
		global global_map_result
		global_map_result = name
		hide_map()
		renpy.jump(map_zones[name]["label"])


screen map:
	python:
		if map_hide_time > map_show_time:
			map_alpha = 1 - (time.time() - map_hide_time) / map_fade_time
			if map_alpha <= 0:
				hide_screen('map')
		elif time.time() - map_show_time < map_fade_time:
			map_alpha = (time.time() - map_show_time) / map_fade_time
		else:
			if map_alpha != 1:
				sprites_list = []
			map_alpha = 1
		
		bg = map_pics['bg']
		bgw, bgh = get_texture_width(bg), get_texture_height(bg)
		
		map_ground_args = [(bgw, bgh), (0, 0), bg]
		map_hover_args  = [(bgw, bgh)]
		map_hotspots = []
		for name, zone in map_zones.iteritems():
			if zone["available"]:
				pos = zone["position"]
				x, y, w, h = pos[0], pos[1], pos[2]-pos[0], pos[3]-pos[1]
				map_hotspots.append([name, x, y, w, h])
				
				ground = im.Crop(map_pics["available"], (x, y, w, h))
				hover  = im.Crop(map_pics["selected"],  (x, y, w, h))
				
				map_ground_args += [(x, y), ground]
				map_hover_args  += [(x, y), get_back_with_color(hover, color = '#888', alpha = 1.0/255)]
		map_ground = im.Composite(*map_ground_args)
		map_hover  = im.Composite(*map_hover_args)
		
		if map_hide_time > map_show_time:
			map_hotspots = []
	
	imagemap:
		ground map_ground
		hover  map_hover
		
		alpha map_alpha
		size (1.0, 1.0)
		
		for name, x, y, w, h in map_hotspots:
			hotspot (x, y, w, h) action zone_click(name)


init python:
	map_show_time = 0
	map_hide_time = 0
	map_fade_time = 0.5
	
	def show_map():
		global map_show_time
		map_show_time = time.time()
		
		show_screen('map')
		renpy.jump('map_waiting')
	
	def hide_map():
		global map_hide_time
		map_hide_time = time.time()

label map_waiting:
	while True:
		pause 0.1

label nothing_here:
	python:
		r = random.choice([
			"Тут ничего нет.",
			"Мне нечего тут делать.",
			"Пойду-ка я лучше еще куда-нибудь."
		])
	narrator r
	$ show_map()

