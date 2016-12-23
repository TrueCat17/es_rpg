init -1000 python:
	renpy.music.register_channel("ambience", "ambience", True)
	renpy.music.register_channel("music", "music", True)
	
	renpy.music.register_channel("sound", "sfx", False)
	renpy.music.register_channel("sound2", "sfx", False)
	renpy.music.register_channel("sound3", "sfx", False)
	
	renpy.music.register_channel("sound_loop", "voice", True)
	renpy.music.register_channel("sound_loop2", "voice", True)
	renpy.music.register_channel("sound_loop3", "voice", True)
		
