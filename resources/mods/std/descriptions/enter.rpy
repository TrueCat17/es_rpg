label day0__enter__lamp_desc:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Фонарь?",
		"Не горит. Впрочем, а нужно ли это?",
		"А может ли фонарь платить налоги? Я ведь могу...",
	])
	window hide
	$ set_rpg_control(True)

label day0__enter__bench_desc:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Лавочка как лавочка.",
		"Сон скоро кончится, зачем опять садиться?",
	])
	window hide
	$ set_rpg_control(True)

label day0__enter__sign:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Сюда ходят автобусы?",
		"Знакомые цифры... Прямо как ошибка.",
	])
	window hide
	$ set_rpg_control(True)

label day0__enter__before_gates:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Это пионеры?",
		"Статуи выглядят старыми, хоть и неплохо сохранились.",
		"Никак не пойму, труба это в руке у мальчика или что-то другое. Из-за тумана не видно.",
	])
	window hide
	$ set_rpg_control(True)
