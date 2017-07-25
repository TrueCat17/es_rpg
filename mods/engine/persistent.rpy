init -1000 python:
	persistent_path = '../resources/persistent'
	
	persistent_updates = True
	try:
		if (not os.path.exists(persistent_path)) or os.path.getsize(persistent_path) == 0:
			persistent = Object()
		else:
			persistent_file = open(persistent_path, 'rb')
			persistent = pickle.load(persistent_file)
			persistent_file.close()
			del persistent_file
	except:
		out_msg('Ошибка при загрузке файла persistent: <' + persistent_path + '>')
		persistent = Object()
		raise

init -999 python:
	persistent_updates = False
	persistent.in_persistent = True
	
	persistent_need_save = False
	def persistent_save():
		global persistent, persistent_need_save, persistent_updates
		
		if not persistent_need_save:
			return
		persistent_need_save = False
		
		persistent_updates = True
		try:
			persistent_file = open(persistent_path, 'wb')
			pickle.dump(persistent, persistent_file)
			persistent_file.close()
		except:
			out_msg('Ошибка при сохранении файла persistent: <' + persistent_path + '>')
			persistent_updates = False
			raise
		persistent_updates = False


init -999 python:
	persistent.sprite_time = 'day'
	persistent.tint_sprite_time = im.matrix.tint(1, 1, 1)
