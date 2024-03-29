init python:
	conversation.good_ends = Object()
	conversation.bad_ends = Object()
	
	
	conversation.bad_ends['common'] = [
		"Своя точка зрения - это, конечно, хорошо... Но не всегда.",
		"Ты ошибаешься.",
		"Нет, всё совсем не так.",
		"Это не интересно.",
		"Скучно.",
		"Мне уже пора идти.",
		
		"Заканчивай уже с этим.",
		"Не стоит поднимать эту тему.",
		"Не хочу об этом говорить.",
		"Не говори такого.",
		
		"О чём ты вообще?",
		"Я тебя не понимаю!",
		"Глупости!",
		"Хватит!",
		"???",
		"...",
		"Я, пожалуй, промолчу.",
		
		[
			"И вот поэтому в некоторых местах не стоит строить девятиэтажки.",
			["th", "Очевидно, мы совсем ушли от первоначальной темы разговора. Печально."],
		],
		[
			"Конечно же отдых - это важно!",
			["th", "Нить разговора оказалась утеряна полностью."],
		],
		[
			"И вот как в таких обстоятельствах учиться?",
			["th", "Эм... А разве мы об этом начинали говорить?"],
		],
		[
			"...как тебе эта история?",
			["me", "Я, пожалуй, промолчу..."],
			"Да? Ну, как знаешь.",
		],
	]
	
	conversation.good_ends['common'] = [
		"О, вот оно как.",
		"Кажется, ты прав.",
		"Хм. Вполне может быть.",
		"Интересно.",
		"Надо бы запомнить.",
		"Да, это хороший совет. Спасибо.",
		"Серьёзно? Буду знать.",
		"В самом деле? Кто бы мог подумать.",
		
		"Обязательно напомни мне об этом позже.",
		"Эх... К сожалению, мне надо идти. Поговорим потом ещё.",
		"Хм. Это стоит конкретно так обдумать. Свяжись со мной завтра.",
		"Продолжим потом с этого момента.",
		
		"Именно так!",
		"Абсолютно верно!",
		"Правильно!",
		"Это ты верно говоришь!",
		"Ахаха~. Это интересно!",
	]
	
	
	conversation.bad_ends['male'] = [
		"Не согласен.",
		"Точно уверен, что это не так.",
		"Так и знал, что ты в этом не разбираешься.",
		"Я опечален твоими знаниями.",
	]
	
	conversation.good_ends['male'] = [
		"Этого я не знал.",
		"Приятно удивлён тем, что ты разбираешься в этом вопросе.",
		"Не ожидал, что ты в курсе таких тонкостей.",
		"Рад, что мы сошлись в этом.",
		
		"Полностью согласен!",
		"Никогда бы не подумал!",
		"Именно! Будущее - за роботизацией!",
	]
	
	
	conversation.bad_ends['female'] = [
		"Ой, всё!",
		"Не согласна.",
		"Точно уверена, что это не так.",
		"Так и знала, что ты в этом не разбираешься.",
		"Я опечалена твоими знаниями.",
	]
	
	conversation.good_ends['female'] = [
		"Этого я не знала.",
		"Приятно удивлена тем, что ты разбираешься в этом вопросе.",
		"Не ожидала, что ты в курсе таких тонкостей.",
		"Рада, что мы сошлись в этом.",
		
		"Полностью согласна!",
		"Никогда бы не подумала!",
	]
