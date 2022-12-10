label *__closed*:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Закрыто.",
		"Заперто.",
		"Не открывается.",
		"Вообще, заглядывать в рандомные двери - плохая идея. Могут ведь и открыть, и что тогда?",
		"И зачем мне туда идти?",
	])
	window hide
	$ set_rpg_control(True)

label *__toilet*:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Я не хочу в туалет.",
		"Нет, не сейчас.",
		"Зачем?",
		"Для чего?",
	])
	window hide
	$ set_rpg_control(True)


# side_characters, with -
label houses_?__house-??:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Лучше не лезть в чужой домик.",
		"Этот домик не мой, и даже не моего отряда.",
	])
	window hide
	$ set_rpg_control(True)

# main_characters, with _
label houses_?__house_??:
	if cur_place_name == 'house_sh':
		if rpg_event != 'action':
			return
	else:
		if rpg_event != 'no_exit':
			return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Думаю, лучше не лезть в чужой домик.",
		"Зачем мне заходить в чей-то домик?",
		"Это не мой домик, и меня сюда не звали.",
		"Мы не настолько хорошо знакомы, чтобы ходить в гости без приглашения.",
	])
	window hide
	$ set_rpg_control(True)

label *__washbasin*:
	$ place_name = cur_place_name
	
	if rpg_event != 'action':
		return
	
	if clock.hours < 21:
		return
	
	$ set_rpg_control(False)
	
	if has_in_inventory('tooth_paste_and_brush'):
		if '_' in place_name:
			$ me.move_to_place(place_name)
			$ me.rotate_in_place(place_name)
		
		narrator random.choice([
			"И вот, настало время чистить зубы.",
			"Итак, \"пришла пора чистить зубки и ложиться спать\" - правильно?",
			"Быстрее бы уже под одеяло!",
		])
		$ was.append('tooth_cleaning')
		
		if clock.day == 1:
			"Бр-р. После такой \"прохладной\" водички стоит только начинать день, но никак не идти спать."
			"А придётся..."
	else:
		narrator "У меня нет зубных пасты и щётки, поэтому я не могу почистить зубы."
	
	window hide
	$ set_rpg_control(True)
