init -10000 python:
	es2d_gui = 'images/gui/'
	
	alphabet = tuple(map(chr, xrange(ord('a'), ord('z') + 1))) # a-z
	numbers = tuple(xrange(10)) # 0-9

init -998 python:
	checkboxes_inited = False
	def init_checkboxes():
		global checkboxes_inited, checkbox_yes, checkbox_no
		checkboxes_inited = True
		
		checkbox_yes = get_back_with_color(es2d_gui + 'std/checkbox/yes.png')
		checkbox_no  = get_back_with_color(es2d_gui + 'std/checkbox/no.png')
	
	
	bar_ground = es2d_gui + 'std/bar/ground.png'
	bar_hover  = es2d_gui + 'std/bar/hover.png'
	
	vbar_ground = im.Rotozoom(bar_ground, 90, 1)
	vbar_hover  = im.Rotozoom(bar_hover , 90, 1)



init -1100000000 python:
	def get_traceback(tb):
		import traceback
		l = traceback.format_tb(tb)
		return ''.join(l)

init -1000000 python:
	def get_numline(depth):
		s = inspect.stack()
		frame = s[1 + depth]
		return frame[2]
	def get_filename(depth):
		s = inspect.stack()
		frame = s[1 + depth]
		return frame[1]


init -100000 python:
	def quick_load():
		path = os.path.join(save_dir, config.quick_save_table, config.quick_save_name, 'py_globals')
		if os.path.exists(path):
			load(config.quick_save_table, config.quick_save_name)
	def quick_save():
		sl_save(config.quick_save_table, config.quick_save_name)
	
	def ceil(n):
		res = int(n)
		if res != n and n > 0:
			res += 1
		return res
	
	def in_bounds(v, vmin, vmax):
		return vmin if v < vmin else vmax if v > vmax else v
	
	def get_absolute(value, max_value):
		if (value > 0 and value < 1) or (value == 1.0 and type(value) is float):
			return int(value * max_value)
		return int(value)
	
	def get_dist(x1, y1, x2, y2):
		return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
	
	def get_mods():
		# name : directory
		res = {}
		
		mods_path = 'mods/'
		fs_and_ds = os.listdir(mods_path)
		for path in fs_and_ds:
			if path[-1] in ('/', '\\'):
				path = path[:-1]
			
			if os.path.isdir(mods_path + path):
				path_to_name = mods_path + path + '/name'
				if os.path.exists(path_to_name) and os.path.getsize(path_to_name):
					f = open(path_to_name)
					
					name = f.db_read()
					f.close()
					if name and name[-1] == '\n':
						name = name[:-1]
					
					if name:
						res[name] = path
		return res
	
	def get_from_hard_config(param, ret_type):
		res = _get_from_hard_config(str(param))
		if ret_type is bool:
			return res == "True"
		return ret_type(res)
	
	def load(table, num):
		_load(str(table), str(num))
	
	def out_msg(msg, err = ''):
		_out_msg(str(msg), str(err))
	
	def get_image(name):
		if image_was_registered(name):
			code = get_image_code(name)
			res = ([code] if code else []) + get_image_decl_at(name)
		else:
			out_msg('get_image', 'Изображение <' + name + '> не зарегистрировано')
			res = [im.Rect('#000', 256, 256)]
		return res
	
	def can_exec_next_command():
		return (db_read) and (call_screen_choosed) and (characters_moved()) and (sprites_effects_ended())
	
