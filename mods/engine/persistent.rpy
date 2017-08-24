init -1001 python:
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
		
		safe_types = ['bool', 'int', 'float', 'long', 'str', 'list', 'tuple', 'NoneType', 'classobj', 'instance']
		for i in xrange(len(safe_types)):
			safe_types[i] = "<type '" + safe_types[i] + "'>"
		
		for k in g.keys():
			# renpy contains module <random>, modules can't saves
			if k != 'renpy':
				str_type = str(type(g[k]))
				if str_type in safe_types:
					obj[k] = g[k]
		
		save_object(path, obj)



init -1000 python:
	persistent_path = '../resources/saves/persistent'
	
	persistent_updates = True
	
	try:
		if (not os.path.exists(persistent_path)) or os.path.getsize(persistent_path) == 0:
			persistent = Object()
		else:
			persistent = load_object(persistent_path)
	except:
		persistent = Object()
		raise


init -999 python:
	persistent_updates = False
	persistent.in_persistent = True
	
	persistent_need_save = False
	def persistent_save():
		global persistent_need_save
		
		if persistent_need_save:
			persistent_need_save = False
			save_object(persistent_path, persistent)


init -999 python:
	persistent.sprite_time = 'day'
	persistent.tint_sprite_time = im.matrix.tint(1, 1, 1)
	
