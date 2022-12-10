label house_mt__sm_bed:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	
	if 'tooth_reminder' not in was and 'tooth_cleaning' not in was:
		$ was.append('tooth_reminder')
		mt "Ты хоть зубы почисти перед сном. Больше напоминать не буду, не маленький уже."
	elif clock.hours >= 7 and clock.hours <= 21:
		"Спать ещё рано."
		$ me.set_direction(to_right)
	else:
		python:
			set_location('house_mt', 'sm_bed_sleep')
			me.start_animation('sleep')
		
		show bg black with dissolve
		$ hide_location()
		hide bg
		
		if 'first_dream' not in was:
			$ was.append('first_dream')
			"События сегодняшнего дня пролетали у меня перед глазами. Казалось, что за последние несколько лет моей жизни произошло всякого разного меньше, чем за один сегодняшний день."
			"Хотя я мог бы судорожно думать о том, как отсюда выбраться или бояться ночи в этом месте, но усталость и перенасыщение сегодняшним днём сделали своё дело. Я впал в сон."
		else:
			"Итак, пора спать."
		window hide
		
		python:
			while clock.hours != 7:
				clock.add(60 * 5)
			
			me.y = -100 # dont draw old image in bed without sleep animation
			me.remove_animation()
			me.set_direction(to_right)
			set_location('house_mt', 'sm_bed')
	
	$ set_rpg_control(True)
	window hide
