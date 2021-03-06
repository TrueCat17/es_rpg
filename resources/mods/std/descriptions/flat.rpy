label flat__books:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Наверное, в слое пыли на книгах уже целая империя всякой мелкой живности.",
		"Надо бы разобрать эти книги... Когда-нибудь.",
		"Вроде как из этой кучи я все книги прочитал. Ну или по крайней мере начинал читать...",
	])
	window hide
	$ set_rpg_control(True)

label flat__before_window:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	narrator random.choice([
		"Классно сидеть дома, пока за окном валит снег.{w}\nУвы, не в этот раз."
		"Один и тот же вид на панельки. Можно сказать, давно уже стал родным."
		"Один из плюсов жизни на высоком этаже - неплохой вид из окна...{w}\nХотя с моим образом жизни это - единственное, что я наблюдаю абсолютно каждый день."
	])
	window hide
	$ set_rpg_control(True)
