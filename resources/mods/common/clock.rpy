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
		m += int(s) / 60
		s %= 60
		
		h += m / 60
		m %= 60
		
		d += h / 60
		h %= 24
		
		return d, h, m, s
	
	def clock__normalize_self():
		clock.day, clock.hours, clock.minutes, clock.seconds = clock.normalize(clock.day, clock.hours, clock.minutes, clock.seconds)
	
	def clock__time_to_str(l):
		"""[1, 8, 0, 30.7] -> '1-08:00:30'"""
		l = map(int, l)
		l = map(str, l)
		day = l[0]
		l = map(lambda s: (2 - len(s)) * '0' + s, l[1:])
		return day + '-' + ('%s:%s:%s') % tuple(l)
	
	def clock__send_signal():
		signals.send('clock-' + clock.time_to_str(clock.get()))
	
	def clock__add(time):
		prev_time = clock.get()
		
		if type(time) not in (int, float):
			if '-' not in time:
				time = '0-' + time
			d, h, m, s = clock.parse_time(time)
			time = 3600 * 24 * d + 3600 * h + 60 * m + s
		
		clock.seconds += time
		clock.normalize_self()
		
		d, h, m, s = prev_time
		while time:
			prev_s = s
			if time >= 1:
				s += 1
				time -= 1
			else:
				s += time
				time = 0
			
			if s >= 60:
				d, h, m, s = clock.normalize(d, h, m, s)
			if int(prev_s) != int(s):
				time_str = clock.time_to_str([d, h, m, s])
				signals.send('clock-' + time_str)                           # clock-d-hh:mm:ss
				signals.send('clock-' + time_str[time_str.index('-') + 1:]) # clock-hh:mm:ss
	
	def clock__set(time):
		clock.day, clock.hours, clock.minutes, clock.seconds = clock.parse_time(time)
		clock.normalize_self()
		clock.send_signal()
	
	def clock__get():
		return clock.day, clock.hours, clock.minutes, clock.seconds
	
	def clock__add_signal(after, function, priority = 0):
		d1, h1, m1, s1 = clock.get()
		
		if type(time) in (int, float):
			d2 = h2 = m2 = 0
			s2 = time
		else:
			if '-' not in time:
				time = '0-' + time
			d2, h2, m2, s2 = clock.parse_time(after)
		
		d, h, m, s = clock.normalize([d1 + d2, h1 + h2, m1 + m2, s1 + s2])
		signals.add('clock-' + clock.time_to_str([d, h, m, s]), function, priority=priority)
	
	def clock__on_tick():
		if clock.pause or has_screen('pause'):
			return
		
		clock.add(clock.acceleration * get_last_tick())
	
	def clock__on_location_change():
		clock.add(clock.location_change_time)
	
	
	build_object('clock')
	
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
	
	# canteen
	for hour in [8, 12, 16, 20]:
		prev_hour = str(hour - 1)
		if len(prev_hour) == 1:
			prev_hour = '0' + prev_hour
		signals.add('clock-' + prev_hour + ':45:00', canteen_preparing)

screen clock:
	zorder 100
	
	image im.rect('#eee'):
		size (250, 50)
		
		text clock.time_to_str(clock.get()):
			align 0.5
			text_size 40
			color 0
