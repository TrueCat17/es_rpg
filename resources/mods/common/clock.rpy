init python:
	
	def clock__parse_time(time):
		"""'2-00:01:30' -> [2, 0, 1, 30]"""
		if '-' not in time or time.count(':') != 2:
			out_msg('clock.parse_time', 'time expected in format day-hh:mm:ss, got <' + time + '>')
			return [-1, -1, -1, -1]
		day, time = time.split('-')
		h, m, s = time.split(':')
		return [int(day), int(h), int(m), float(s)]
	
	def clock__normalize(d, h, m, s):
		m += int(s) // 60
		s %= 60
		
		h += m // 60
		m %= 60
		
		d += h // 60
		h %= 24
		
		return d, h, m, s
	
	def clock__normalize_self():
		clock.day, clock.hours, clock.minutes, clock.seconds = clock.normalize(clock.day, clock.hours, clock.minutes, clock.seconds)
	
	def clock__time_to_str(l):
		"""
		[2, 18, 0, 30.7] -> '2-18:00:30'
		[-1, 7, 30, 0] -> '7:30:00'
		"""
		
		d, h, m, s = clock.normalize(*l)
		
		res = '' if d < 0 else (str(d) + '-')
		for i in (h, m, s):
			res += '%02i:' % i
		return res[:-1]
	
	def clock__send_signal(time_str):
		signals.send('clock-' + time_str)                           # clock-d-hh:mm:ss
		signals.send('clock-' + time_str[time_str.index('-') + 1:]) # clock-hh:mm:ss
	
	def clock__add(time):
		if type(time) not in (int, float):
			if '-' not in time:
				time = '0-' + time
			d, h, m, s = clock.parse_time(time)
			time = 3600 * 24 * d + 3600 * h + 60 * m + s
		
		d, h, m, s = clock.get()
		nd, nh, nm, ns = clock.normalize(d, h, m, s + time)
		
		while time:
			prev_s = clock.seconds
			if time >= 1:
				clock.seconds += 1
				time -= 1
			else:
				clock.seconds += time
				time = 0
			
			if clock.seconds >= 60:
				clock.normalize_self()
			if int(prev_s) != int(clock.seconds):
				time_str = clock.time_to_str(clock.get())
				clock.send_signal(time_str)
	
	def clock__set(time):
		clock.day, clock.hours, clock.minutes, clock.seconds = clock.parse_time(time)
		clock.normalize_self()
		time_str = clock.time_to_str(clock.get())
		clock.send_signal(time_str)
	
	def clock__get():
		return clock.day, clock.hours, clock.minutes, clock.seconds
	
	def clock__add_signal(after, function, priority = 0):
		d1, h1, m1, s1 = clock.get()
		
		times = -1
		if type(after) in (int, float):
			d2 = h2 = m2 = 0
			s2 = after
			times = 1
		else:
			if '-' in after:
				times = 1
			else:
				after = '0-' + after
			d2, h2, m2, s2 = clock.parse_time(after)
		
		d, h, m, s = clock.normalize(d1 + d2, h1 + h2, m1 + m2, s1 + s2)
		signals.add('clock-' + clock.time_to_str([d, h, m, s]), function, priority=priority, times=times)
	
	def clock__on_tick():
		if has_screen('pause') or clock.pause or db.visible:
			return
		
		clock.add(clock.acceleration * get_last_tick())
	
	def clock__on_location_change():
		if clock.pause or db.visible:
			return
		if clock.first_location_show:
			clock.first_location_show = False
			return
		
		clock.add(clock.location_change_time)
	
	
	build_object('clock')
	clock.first_location_show = True
	
	clock.day = 0
	clock.hours = 0
	clock.minutes = 0
	clock.seconds = 0.0
	
	clock.pause = True
	clock.acceleration = 6
	clock.location_change_time = 60 * 3


init 11 python:
	signals.add('enter_frame', clock.on_tick)
	signals.add('rpg-location', clock.on_location_change)
	
	# change location lighting
	signals.add('clock-07:00:00', sunset_time)
	signals.add('clock-09:00:00', day_time)
	signals.add('clock-19:00:00', sunset_time)
	signals.add('clock-21:00:00', night_time)
	
	
	signals.add('clock-07:30:00', Function(signals.send, 'wake_up'))
	signals.add('clock-21:30:00', Function(signals.send, 'go_to_sleep'))
	
	signals.add('wake_up',     Play(sfx['horn'], 'sound'))
	signals.add('go_to_sleep', Play(sfx['horn'], 'sound'))


screen clock:
	zorder 100
	
	image im.rect('#eee'):
		size (250, 50)
		
		text clock.time_to_str(clock.get()):
			align 0.5
			text_size 40
			color 0
