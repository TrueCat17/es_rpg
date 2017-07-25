init -1001 python:
	mods_last_key = None
	mods_last_value = None
	
	class Mods:
		def __setitem__(self, key, value):
			global mods_last_key, mods_last_value
			mods_last_key, mods_last_value = key, value

init -1000 python:
	mods = Mods()
