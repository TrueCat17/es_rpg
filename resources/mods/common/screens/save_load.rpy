# sl = save_load
init -2 python:
	save_dir = 'saves/'
	
	sl_cur_table = '0'
	sl_cur_save  = '0'
	
	sl_inited = False
	def init_sl():
		global sl_inited
		global sl_btn_hover, sl_btn_selected
		
		sl_inited = True
		
		sl_btn_hover    = get_back_with_color('images/gui/save_load/hover.png')
		sl_btn_selected = get_back_with_color('images/gui/save_load/selected.png')
	
	
	def sl_get_dirs(path):
		if not os.path.exists(path):
			return []
		dirs_files = os.listdir(path)
		dirs = [name for name in dirs_files if os.path.isdir(os.path.join(path, name))]
		return dirs
	
	def sl_get_tables():
		res = list(str(i) for i in xrange(12)) + ['auto']
		dirs = sl_get_dirs(save_dir)
		for i in dirs:
			if i not in res:
				res.append(i)
		return res
	def sl_get_table_saves(table):
		res = list(str(i) for i in xrange(12))
		dirs = sl_get_dirs(os.path.join(save_dir, table))
		for i in dirs:
			if i not in res:
				res.append(i)
		return res
	
	def sl_get_screenshot(table, save, save_exists):
		selected = sl_cur_save == save
		over = sl_btn_selected if selected else sl_btn_hover
		
		if save_exists:
			screenshot = os.path.join(save_dir, table, save, 'screenshot.png')
			screenshot += "?" + str(os.path.getmtime(screenshot))
			w, h = get_texture_width(screenshot), get_texture_height(screenshot)
			return im.Composite((w, h), (0, 0), screenshot, (0, 0), im.Scale(over, w, h))
		
		return over
	
	def sl_save(table, save):
		global save_table, save_name, need_save
		save_table, save_name = table, save
		need_save = True
		
	
	def sl_delete_save(table, save):
		shutil.rmtree(os.path.join(save_dir, table, save))
		sl_update_table_saves()
	
	def sl_update_table_saves():
		global sl_tables, sl_table_saves, sl_table_saves_exists
		
		sl_tables = sl_get_tables()
		sl_table_saves = sl_get_table_saves(sl_cur_table)
		
		sl_table_saves_exists = {}
		for save_name in sl_table_saves:
			sl_table_saves_exists[save_name] = os.path.exists(os.path.join(save_dir, sl_cur_table, save_name, 'screenshot.png'))
	sl_update_table_saves()
	

