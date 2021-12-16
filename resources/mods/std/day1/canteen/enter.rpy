init python:
	def day1_set_eaters_12h():
		canteen.not_eat = [mi, mz, mt]
		canteen.fast_eat = [us]
	
	def day1_set_eaters_20h():
		canteen.not_eat = []
		canteen.fast_eat = [un]
	
	signals.add('clock-1-11:00:00', day1_set_eaters_12h, times=1)
	signals.add('clock-1-19:00:00', day1_set_eaters_20h, times=1)
	
	signals.add('clock-1-11:45:10', Function(renpy.call, 'first_horn'), times=1)

label first_horn:
	python:
		mt.set_auto(False)
		place = rpg_locations['canteen'].places['square']
		mt.move_to_place(['canteen', {'x': place.x + 100, 'y': place.y}], run=True, wait_time=0)
	$ set_rpg_control(False)
	me "Судя по всему, это сигнал к скорому обеду."
	window hide
	$ set_rpg_control(True)


label day1__canteen__square:
	if clock.hours != 12:
		return
	
	if 'canteen' in was:
		return
	$ was.append('canteen')
	
	$ mt.set_direction(to_left)
	$ set_rpg_control(False)
	$ location_cutscene_on(align='down')
	
	mt "Семён..."
	
	$ me.move_to_place({'x': mt.x, 'y': mt.y - 30})
	$ me.set_direction(to_back)
	$ mt.set_direction(to_forward)
	
	mt "Так, на наш отряд у нас во-он те столы... хотя ладно, пошли."
	window hide
	python:
		place = rpg_locations['canteen'].places['table_h_pos-r4']
		mt.move_to_place({'x': place.x - 60, 'y': place.y - 20}, wait_time=1.5)
	python:
		place = rpg_locations['canteen'].places['table_h_pos-r4']
		me.move_to_place({'x': place.x - 60, 'y': place.y + 20})
	
	$ mt.move_to_end()
	$ mt.set_direction(to_back)
	mt "Свободных мест тут достаточно, так что садись куда хочешь."
	window hide
	$ me.set_direction(to_right)
	
	$ location_cutscene_off()
	$ set_rpg_control(True)
	
	$ mt.get_actions().start(canteen.inside)

label day1__canteen__*:
	if rpg_event != 'sit_down':
		return
	if 'canteen_pioneers_' + str(clock.hours) + 'h' in was:
		return
	if clock.hours not in canteen.hours:
		return
	
	$ set_rpg_control(False)
	
	$ table = canteen.get_table()
	if table.startswith('r'):
		$ table_num = int(table[1:])
		if table_num >= 4 and table_num <= 6:
			$ canteen_name = 'canteen_pioneers_' + str(clock.hours) + 'h'
			$ canteen_label = 'day1__canteen__table-' + str(table_num) + '-time' + str(clock.hours) + 'h'
			if renpy.has_label(canteen_label):
				if canteen_name not in was:
					$ canteen_id = set_interval(Function(canteen.sit_for_table, table), 0.5)
					$ renpy.call(canteen_label)
					$ clear_interval(canteen_id)
					python:
						if clock.hours == 12:
							mt.set_auto(False)
							x, y = get_place_center(rpg_locations['square'].places['canteen'])
							mt.move_to_place(['square', {'x': x, 'y': y + 30}], run=True, wait_time=0)
		elif table_num < 4:
			$ chars = [ch for ch in [mt, cs] if canteen.is_sit(ch)]
			if chars:
				$ canteen_name = 'canteen_mt_' + str(clock.hours) + 'h'
				if canteen_name not in was:
					$ ch = random.choice(chars)
					ch random.choice(canteen.say[ch.rpg_name])
			else:
				$ canteen_name = None
		else:
			$ canteen_name = 'canteen_window_' + str(clock.hours) + 'h'
			if canteen_name not in was:
				me "У окна, конечно, хорошо."
				me "Вот только порций здесь нет."
				$ me.stand_up()
	elif table.startswith('c'):
		$ canteen_name = 'canteen_center_' + str(clock.hours) + 'h'
		if canteen_name not in was:
			me "Как-то не уютно сидеть за этими столами по центру столовой - в одиночестве и у всех на виду."
			$ me.stand_up()
	else:
		$ canteen_name = 'canteen_strangers_' + str(clock.hours) + 'h'
		if canteen_name not in was:
			"Вдруг я услышал чей-то незнакомый голос."
			voice random.choice(canteen.say['stranger'])
			$ me.stand_up()
	
	if canteen_name and canteen_name not in was:
		$ was.append(canteen_name)
	
	window hide
	$ set_rpg_control(True)
