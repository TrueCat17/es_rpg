label day1__canteen__table-6-time12h:
	$ canteen.wait([el, sh])
	$ el.get_actions().canteen_eating_end = None
	$ sh.get_actions().canteen_eating_end = None
	"Из-за некоторых особенностей моего характера меня потянуло за дальний стол. К тому же, женских особ тут не наблюдалось."
	
	if 'clubs' in was or 'el_washbasins_help' in was:
		me "Не занято?"
		el "Хм? Садись конечно, Семён! Не занято."
		if 'clubs' not in was:
			extend " Кстати, знакомься: это Шурик."
			sh "Саша."
			me "Семён."
			"Мы пожали руки."
		$ clock.add(2 * 60)
		el "Кстати, Женя говорила, что не придёт, так что можешь брать её порцию."
		"Что за Женя - мне было не особо интересно, да и почему-то мне казалось, что мы ещё пересечёмся."
		"..."
		window hide
		show bg black with dissolve
		$ clock.add(2 * 60)
		pause 2
		hide bg with dissolve
		"Когда я доел борщ, Сергей с Шуриком встали из-за стола."
		$ el.stand_up()
		$ sh.stand_up()
		$ clock.add(2 * 60)
		el "В общем, мы пойдем робота делать. Если хочешь, заходи к нам."
		me "Хорошо."
		sh "Ну и приятного аппетита."
		me "А... спасибо."
#		"Получен доступ к квесту \"Технологии и светлое будущее\"."
	else:
		me "Можно с вами?"
		el "Да, если хочешь."
		if "el_washbasins_refusal" in was:
			"И только сейчас я понял, что я спрашивал того самого парня, которого проигнорировал возле умывальников."
			th "Чёрт, лишь бы не узнал."
			"К счастью, он лишь недоумённо взглянул на меня и продолжил есть."
		$ clock.add(2 * 60)
		"На столе стояла как раз лишняя порция, и я уже было потянулся за ней, но вспомнил о правилах приличиях. Внезапно."
		th "А если и спрашивать про порцию, то нужно хотя бы имена знать..."
		me "Меня, кстати, Семён зовут, а вас?"
		sh "Шурик."
		$ meet('sh', 'Шурик')
		el "Сергей. Можно Электроник."
		$ meet('sh', 'Электроник')
		$ clock.add(3 * 60)
		me "Приятно познакомиться... а порция это ничья?"
		el "Это девочки одной, но она, похоже, не придет. Так что можешь брать."
		me "Спасибо."
		el "Да не за что."
		"..."
		window hide
		show bg black with dissolve
		$ clock.add(2 * 60)
		pause 2
		hide bg with dissolve
		"Когда я доел борщ, Сергей с Шуриком встали из-за стола."
		el "Ну, до скорого, Семён."
	
	$ el.get_actions().start('other_place', 'clubs')
	$ sh.get_actions().start('other_place', 'clubs')
	"..."
	"Со вторым в виде котлеты с макаронами я управился быстро."
