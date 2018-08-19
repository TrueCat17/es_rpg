init -10000 python:
	gui = 'images/gui/'
	
	alphabet = list(map(chr, xrange(ord('a'), ord('z') + 1))) # a-z
	numbers = range(10) # 0-9


init -998 python:
	checkboxes_inited = False
	def init_checkboxes():
		global checkboxes_inited, checkbox_yes, checkbox_no
		checkboxes_inited = True
		
		checkbox_yes = get_back_with_color(gui + 'std/checkbox/yes.png')
		checkbox_no  = get_back_with_color(gui + 'std/checkbox/no.png')
	
	
	bar_ground = gui + 'std/bar/ground.png'
	bar_hover  = gui + 'std/bar/hover.png'
	
	vbar_ground = im.Rotozoom(bar_ground, 90, 1)
	vbar_hover  = im.Rotozoom(bar_hover , 90, 1)


init -1000000 python:
	def get_numline(depth):
		frame = inspect.currentframe().f_back
		while depth:
			depth -= 1
			frame = frame.f_back
		return inspect.getlineno(frame)
	def get_filename(depth):
		frame = inspect.currentframe().f_back
		while depth:
			depth -= 1
			frame = frame.f_back
		return inspect.getfile(frame)
	def get_file_and_line(depth):
		frame = inspect.currentframe().f_back
		while depth:
			depth -= 1
			frame = frame.f_back
		return inspect.getfile(frame), inspect.getlineno(frame)


init -100000 python:
	def quick_load():
		path = os.path.join(save_dir, config.quick_save_table, config.quick_save_name, 'py_globals')
		if os.path.exists(path):
			load(config.quick_save_table, config.quick_save_name)
	def quick_save():
		sl_save(config.quick_save_table, config.quick_save_name)
	
	def make_screenshot(width = None, height = None):
		global need_screenshot, screenshot_width, screenshot_height
		need_screenshot = True
		screenshot_width, screenshot_height = width or get_stage_width(), height or get_stage_height()
	
	
	def in_bounds(v, vmin, vmax):
		return vmin if v < vmin else vmax if v > vmax else v
	def get_absolute(value, max_value):
		if type(value) is float and value > 0 and value <= 1.0:
			value *= max_value
		return int(value)
	def get_dist(x1, y1, x2, y2):
		dx, dy = x1 - x2, y1 - y2
		return math.sqrt(dx*dx + dy*dy)
	
	def get_texture_size(texture):
		return get_texture_width(texture), get_texture_height(texture)
	def get_stage_size():
		return get_stage_width(), get_stage_height()
	
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
			res = ["im.Rect('#000', 256, 256)"]
		return res


init -1000000 python:
	can_exec_next_vars = []
	can_exec_next_funcs = []
	
	def can_exec_next_command():
		for obj, var in can_exec_next_vars:
			if obj is None:
				obj = globals()
			if not obj[var]:
				return False
		
		for func in can_exec_next_funcs:
			if not func():
				return False
		
		return True

