label forest_path*:
	if 'us_running' not in was:
		return
	if 'forest_running' in was:
		return
	$ was.append('forest_running')
	
	$ set_rpg_control(False)
	$ me.move_to_place({'x': me.x + 200, 'y': me.y}, run=True, wait_time=0.5)
	th "Чёрт, не вижу её."
	me "Э-эй! Ты где?"
	$ me.set_direction(to_forward)
	pause 0.5
	$ me.set_direction(to_back)
	pause 0.5
	$ me.set_direction(to_right)
	pause 0.5
	th "Как сквозь землю провалилась."
	window hide
	
	show bg black with dissolve
	$ set_location('forest_path-7', 'up')
	$ me.set_direction(to_back)
	hide bg with dissolve
	
	$ me.move_to_place('forest_path-8', run=True, wait_time=1)
	
	show bg black with dissolve
	$ set_location('forest_path-6', 'left')
	$ me.set_direction(to_right)
	hide bg with dissolve
	$ me.move_to_place('forest_path-7', wait_time=2)
	
	if clock.hours < 21:
		show bg black with dissolve
		while clock.hours < 21:
			$ clock.add(60)
		hide bg with dissolve
	th "Просто замечательно. Уже дважды обвела меня вокруг пальца."
	$ me.move_to_place(None)
	th "И о чём я только думал, когда побежал за ней? Будто в пятом классе."
	window hide
	show bg black with dissolve
	$ set_location('forest_path-4', 'forest_path-5')
	$ me.set_direction(to_back)
	hide bg with dissolve
	
	me "Наконец-то!"
	$ me.move_to_place(['enter', 'forest_path-9'], wait_time=1)
	me "Теперь хоть вернуться смогу."
	th "Так, значит этой дорогой я сюда приехал? Совсем ничего не помню."
	window hide
	
	$ me.move_to_place(None)
	$ set_rpg_control(True)
