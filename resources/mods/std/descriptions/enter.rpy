label enter__lamp_desc:
	if exec_action:
		$ set_rpg_control(False)
		narrator random.choice([
			"Фонарь?",
			"Не горит. Впрочем, а нужно ли это?",
			"А может ли фонарь платить налоги? Я ведь могу...",
		])
		window hide
		$ set_rpg_control(True)

label enter__bench_desc:
	if exec_action:
		$ set_rpg_control(False)
		narrator random.choice([
			"Лавочка как лавочка.",
			"Сон скоро кончится, зачем опять садиться?",
		])
		window hide
		$ set_rpg_control(True)

label enter__sign:
	if exec_action:
		$ set_rpg_control(False)
		narrator random.choice([
			"Сюда ходят автобусы?",
			"Знакомые цифры… Прямо как ошибка.",
		])
		window hide
		$ set_rpg_control(True)

label enter__before_gates:
	if exec_action:
		$ set_rpg_control(False)
		narrator random.choice([
			"Это пионеры?",
			"Статуи выглядят старыми, хоть и неплохо сохранились.",
			"Никак не пойму, труба это в руке у мальчика или что-то другое. Из-за тумана не видно.",
		])
		window hide
		$ set_rpg_control(True)
