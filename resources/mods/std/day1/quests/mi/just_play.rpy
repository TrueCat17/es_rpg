label day1__mus_club__clubs:
	if not joined_mus_club or joined_mus_club_hours >= 12:
		return
	if (clock.hours, clock.minutes) < (20, 15):
		return
	if (clock.hours, clock.minutes) > (21, 15):
		return
	
	if 'just_play' in was:
		return
	$ was.append('just_play')
	
	$ set_rpg_control(False)
	
	$ mus_club.move_miku_to_piano()
	$ mus_club.show_miku_at_piano(2)
	
	me "Привет. Я уже без стука, ничего?"
	mi "Конечно, я же сама говорила. Сразу начнём?"
	me "Ага."
	
	$ mus_club.prepare()
	pause 1
	$ mus_club.show_miku_at_piano(1)
	pause 1
	$ mus_club.play()
	
	me "Уф, я уже все."
	mi "Ну, по итогам первого дня - неплохо. Если продолжим так и дальше, к концу смены что-то толковое точно выйдет!"
	me "Хех, надеюсь. Кстати, спасибо за занятия и за день."
	mi "Ой, да брось. Это же я тебя изначально затащила..."
	me "Ну... всё равно."
	"Мику хихикнула."
	mi "И тебе спасибо."
	me "..."
	me "Поздновато уже. Пойду, наверное."
	mi "Эх, ладно. Спокойной ночи."
	$ me.stand_up()
	me "Добрых снов. До завтра?"
	mi "Конечно, приходи когда хочешь и на сколько хочешь!"
	me "Обязательно. Ну всё, я пойду. Пока."
	mi "Пока."
	
	$ mi.rp += 1
	$ mi.get_actions().start('interesting_place')
	
	window hide
	$ set_rpg_control(True)
