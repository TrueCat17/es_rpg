init -1000 python:
	music_list = {}
	
	def add_music(name, filename = None, path = 'sound/music/', ext = '.ogg'):
		music_list[name] = path + (filename or name) + ext
	
	add_music('blow_with_the_fires')
	add_music('everlasting_summer')
	add_music('star_called_sun')
