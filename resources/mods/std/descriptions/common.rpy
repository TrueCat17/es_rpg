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

