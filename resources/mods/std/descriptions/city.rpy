init python:
	city__enter = False
label city__city_enter:
	if exec_action:
		$ set_rpg_control(False)
		if not city__enter:
			"Я вроде ничего не забыл."
			$ city__enter = True
		else:
			"Мне незачем возвращаться."
		window hide
		$ set_rpg_control(True)

label city__urn-*:
	if exec_action:
		$ set_rpg_control(False)
		"Старый мусорный бак. На дне виднеются бычки и пара смятых бутылок."
		window hide
		$ set_rpg_control(True)

init python:
	city__urn_park = False
label city__urn_park-*:
	if exec_action:
		$ set_rpg_control(False)
		if not city__urn_park:
			"Пустой мусорный бак."
			$ city__urn_park = True
		else:
			"На дне виднеется снег."
		window hide
		$ set_rpg_control(True)

label city__sign:
	if exec_action:
		$ set_rpg_control(False)
		"Обычный пешеходный знак, с царапинами на металле."
		window hide
		$ set_rpg_control(True)

label city__benchs-*:
	if exec_action:
		$ set_rpg_control(False)
		"Мне некогда сидеть. Да и к тому же, она вся в снегу."
		window hide
		$ set_rpg_control(True)

label city__snow_car:
	if exec_action:
		$ set_rpg_control(False)
		narrator random.choice([
			"Чья-то машина, покрытая снегом.",
			"Если не ошибаюсь, она здесь уже почти год стоит...",
		])
		window hide
		$ set_rpg_control(True)

init python:
	city__shop = False
label city__shop-*:
	if exec_action:
		$ set_rpg_control(False)
		if not city__shop:
			"Не открываются, хотя свет внутри горит."
			"Мне казалось, что они работают без выходных..."
			"Наверно на это есть причина."
			"..."
			"Или кому-то лень рисовать ненужное помещение..."
			$ city__shop = True
		else:
			"..."
		window hide
		$ set_rpg_control(True)

init python:
	city__graffity = False
label city__graffity:
	if exec_action:
		if not city__graffity:
			"Старое граффити, которое нарисовали через неделю после открытия магазина."
			"Насколько знаю, его пытались несколько раз закрасить, но через пару дней, его снова рисовали."
			"Кто-то должен был выбыть из этой гонки, и этим кто-то оказался директор магазина."
			$ city__graffity = True
		else:
			"..."
		$ set_rpg_control(False)
		window hide
		$ set_rpg_control(True)

