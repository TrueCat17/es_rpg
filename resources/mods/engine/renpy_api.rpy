init -999 python:
	
	pause_end = 0
	def pause(sec):
		global pause_end
		pause_end = time.time() + sec
	
	
	class Music:
		@staticmethod
		def register_channel(name, mixer, loop):
			_register_channel(name, mixer, loop, get_filename(1), get_numline(1))
		@staticmethod
		def has_channel(name):
			return _has_channel(name)
		
		@staticmethod
		def play(file_names, channel, depth = 0, **kwargs):
			fadein = kwargs.get('fadein', 0)
			file_name = file_names if isinstance(file_names, str) else file_names[0]
			_play(channel + ' "' + file_name + '" fadein ' + str(float(fadein)), get_filename(depth + 1), get_numline(depth + 1))
		@staticmethod
		def stop(channel, depth = 0, **kwargs):
			fadeout = kwargs.get('fadeout', 0)
			_stop(channel + ' fadeout ' + str(float(fadeout)), get_filename(depth + 1), get_numline(depth + 1))
		
		@staticmethod
		def set_volume(vol, channel, depth = 0):
			_set_volume(in_bounds(vol, 0, 1), channel, get_filename(depth + 1), get_numline(depth + 1))
		@staticmethod
		def set_mixer_volume(vol, mixer, depth = 0):
			vol = in_bounds(round(vol, 2), 0.0, 1.0)
			config[mixer + '_volume'] = vol
			_set_mixer_volume(vol, mixer, get_filename(depth + 1), get_numline(depth + 1))
		@staticmethod
		def add_mixer_volume(d, mixer):
			Music.set_mixer_volume(config[mixer + '_volume'] + d, mixer)
	
	
	class Easy:
		@staticmethod
		def color(c):
			if isinstance(c, tuple) or isinstance(c, list):
				r, g, b = c[0], c[1], c[2]
				if len(c) == 4:
					a = c[3]
				else:
					a = 255
			
			elif isinstance(c, basestring):
				if c[0] == '#':
					c = c[1:]
				elif c[0:2] == '0x':
					c = c[2:]
				
				if len(c) == 6:
					r = int(c[0]+c[1], 16)
					g = int(c[2]+c[3], 16)
					b = int(c[4]+c[5], 16)
					a = 255
				elif len(c) == 8:
					r = int(c[0]+c[1], 16)
					g = int(c[2]+c[3], 16)
					b = int(c[4]+c[5], 16)
					a = int(c[6]+c[7], 16)
				elif len(c) == 3:
					r = int(c[0], 16) * 0x11
					g = int(c[1], 16) * 0x11
					b = int(c[2], 16) * 0x11
					a = 255
				elif len(c) == 4:
					r = int(c[0], 16) * 0x11
					g = int(c[1], 16) * 0x11
					b = int(c[2], 16) * 0x11
					a = int(c[3], 16) * 0x11
				else:
					out_msg('renpy.ease.color', 'Неожидаемый размер строки (ожидалось: 3, 4, 6 или 8; получено: ' + str(len(c)) + ', c = "' + c + '")')
					r = g = b = 0
					a = 255
			else:
				out_msg('renpy.ease.color', 'Неожидаемый тип аргумента (ожидалось: list, tuple или basestring; получено: ' + str(type(c)) + ')')
				r = g = b = 0
				a = 255
			
			return r, g, b, a
	
	
	class Renpy:
		config = persistent.config
		
		music = Music
		easy = Easy
		
		# prop = module
		random = random
		
		
		@staticmethod
		def pause(sec):
			pause(sec)
		
		@staticmethod
		def say(who, what):
			if who is None:
				who = narrator
			
			if isinstance(who, str):
				g = globals()
				if g.has_key(who):
					who = g[who]
				else:
					out_msg('renpy.say', 'Персонаж <' + who + '> не существует')
					return
			who(what)
		
		@staticmethod
		def play(file_names, channel, **kwargs):
			Renpy.music.play(file_name, channel, 1, **kwargs)
		@staticmethod
		def stop(channel, **kwargs):
			Renpy.music.stop(channel, 1, **kwargs)
		
		@staticmethod
		def has_label(label):
			return _has_label(label)
		
		@staticmethod
		def call_screen(screen_name, ret_name, **kwargs):
			global call_screen_choosed, call_screen_name, call_ret_name
			
			call_screen_choosed = False
			call_screen_name, call_ret_name = screen_name, ret_name
			
			show_screen(screen_name)
	
	
	
	renpy = Renpy
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel, depth = 1)

