label day1__square__canteen:
	if rpg_event != 'enter':
		return
	
	if 'canteen_pioneers_12h' in was and clock.hours == 12:
		if 'canteen_out_12h' in was:
			return
		$ was.append('canteen_out_12h')
		
		$ set_rpg_control(False)
		
		mt "Ну как, поел?"
		me "Ага."
		$ mt.set_direction(to_forward)
		mt "Вкусно?"
		me "Очень вкусно!"
		mt "Ну и хорошо. До ужина ещё много времени, так что осматривайся. Только не шалить!"
		me "Хорошо."
		$ mt.get_actions().start('interesting_place')
		
		if 'library' in was:
			th "Точно, в библиотеку надо зайти."
		if 'clubs' in was:
			th "Ну, можно и в кружки заглянуть..."
		"Хотя на самом деле хочется немного пройтись и поваляться в домике."
		
		window hide
		$ set_rpg_control(True)
		return
	
	if 'canteen_pioneers_20h' in was and clock.hours == 20:
		if 'canteen_out_20h' in was:
			return
		$ was.append('canteen_out_20h')
		
		$ set_rpg_control(False)
		
		mt "Семён!"
		$ me.set_direction(to_forward)
		"Окликнула меня вожатая из столовой."
		mt "Сейчас сразу будет линейка, так что иди на площадь."
		mt "Со всем отрядом я тебя ещё не знакомила, но кое-кого ты уже знаешь, так что как увидишь - подходи к ним."
		me "Хорошо."
		$ me.set_direction(to_left)
		th "Вечерняя линейка... интересно увидеть это вживую."
		
		window hide
		$ set_rpg_control(True)
		return
