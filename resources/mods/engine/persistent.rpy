init -1002 python:
	def load_object(path):
		try:
			if (not os.path.exists(path)) or os.path.getsize(path) == 0:
				res = dict()
				out_msg('Файл <' + path + '> не существует или пуст')
			else:
				tmp_file = open(path, 'rb')
				res = pickle.load(tmp_file)
				tmp_file.close()
			return res
		except:
			out_msg('Ошибка при загрузке объекта из файла <' + path + '>')
			raise
	
	def save_object(path, obj):
		global persistent_updates
		
		try:
			persistent_updates = True
			
			tmp_file = open(path, 'wb')
			pickle.dump(obj, tmp_file)
			tmp_file.close()
			
			persistent_updates = False
		except:
			persistent_updates = False
			out_msg('Ошибка при сохранении объекта в файл <' + path + '>')
			raise
	
	def load_global_vars(path):
		g = globals()
		obj = load_object(path)
		for k in obj.keys():
			g[k] = obj[k]
	
	def save_global_vars(path):
		g = globals()
		obj = dict()
		
		class TmpClass: pass
		tmp_instance = TmpClass()
		
		safe_types = [bool, int, float, long, str, list, tuple, set, dict, type(None), type(TmpClass), type(tmp_instance)]
		
		for k in g.keys():
			o = g[k]
			
			# renpy contains module <random>, modules can't saves
			# reference to globals() too
			if o is not renpy and o is not g:
				if type(o) in safe_types:
					obj[k] = o
		
		save_object(path, obj)



init -1001 python:
	persistent_path = 'saves/persistent'
	
	try:
		if (not os.path.exists(persistent_path)) or os.path.getsize(persistent_path) == 0:
			persistent = Object()
		else:
			persistent = load_object(persistent_path)
	except:
		persistent = Object()
		raise


init -1000 python:
	persistent_updates = False
	persistent.in_persistent = True
	
	if not persistent.has_attr('config'):
		persistent.config = Object()
	
	persistent_need_save = False
	def persistent_save():
		global persistent_need_save
		
		if persistent_need_save:
			persistent_need_save = False
			save_object(persistent_path, persistent)


init -999 python:
	persistent.st_r = 255
	persistent.st_g = 255
	persistent.st_b = 255
	
	persistent.sprite_time = 'day'

