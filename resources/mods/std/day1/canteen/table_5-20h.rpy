label day1__canteen__table-5-time20h:
	$ canteen.wait([sl, mi])
	
	if 'mi_meet' in was:
		"На этот раз напротив Слави сидела Мику."
		th "Видимо, обед она просто пропустила. Что же, буду знать, что она здесь сидит."
		"Хотя Мику и активно обсуждала что-то со Славей, заметив меня, она сразу прервалась."
		mi "Хочешь сидеть тут? Это хорошо! Всегда садись тут..."
		me "А, да. Ладно."
		"Успел вставить я."
		mi "Зайдёшь после ужина?"
		me "Может быть."
		"Мику быстро сказала \"хорошо\" и продолжила оживлённую беседу со Славей. Впрочем, больше я не вслушивался."
	else:
		"За вторым столиком появилась девочка с длинными волосами."
		th "Вообще я её вроде как видел пару раз в течение дня. Скорее всего, она тоже из моего... кхм, нашего отряда."
		"Стоило заметить, что она очень оживлённо обсуждала что-то со Славей, но я всё равно позволил себе встрять в их разговор."
		me "Ничего, если я присяду?"
		sl "А? Да, конечно, садись."
		"Больше на меня внимания не обращали."
	
	$ clock.add(5 * 60)
