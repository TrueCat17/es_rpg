label mus_club_meet:
	# (стук)
	
	$ mus_club.move_miku_to_piano()
	$ mus_club.show_miku_at_piano(2)
	mi "Заходите-заходите!"
	
	$ set_location('mus_club', 'clubs')
	$ me.set_direction(to_forward)
	
	mi "А, это ты! Можешь не стучать в следующий раз, знакомы ведь уже как-никак."
	$ me.allow_exit('clubs', 'mus_club')
	th "Она так каждому знакомому доверяет?"
	
	me "Кхм. Так что, начинаем играть?"
	mi "Конечно, бери гитару и садись!"
	
	$ mus_club.prepare()
	pause 1
	$ mus_club.show_miku_at_piano(1)
	pause 1
	$ mus_club.play()
	
	mi "Будем ещё?"
	me "Ну-у, честно говоря..."
	mi "Хорошо, продолжаем!"
	mi "Шучу, хватит пока."
	me "Спасибо."
	"Мику мило хихикнула."
	
	mi "А ты вообще как за гитару взялся? Как я понимаю, недавно начал?"
	th "Недавно, хах... настолько недавно, что даже не в твоем времени."
	me "Ну... если честно, я начал пару лет назад. Сначала более-менее занимался, что-то началось получаться, а потом энтузиазм пропал. Ну и время от времени только бренчал, что умел."
	"Мику немного задумалась."
	mi "Жаль... Нет, это ничего, ты не подумай. Тем более за смену ты сможешь хорошо подтянуть игру. Ну, ещё смотря как ходить будешь, конечно, но всё же... я выложусь на все сто, чтобы помочь тебе!"
	"Эти слова, хотя и пахнущие наивностью, словно пробили меня. Я ведь уже и забыл, что такое забота и чувство, когда кто-то хочет тебе от всей души помочь."
	me "Спасибо. Мне давно...кхм..."
	mi "Что?"
	me "Да нет, ничего."
	
	mi "Точно? Н-ну ладно. А, так вот. Просто раз уж разговор зашёл, я могла бы рассказать, как сама с гитарой познакомилась. Ты же никуда не спешишь?"
	me "Нет... Конечно нет. Рассказывай."
	mi "Ну вообще я с самого детства любила разные музыкальные инструменты. Еще в Японии я..."
	th "Вот это поворот. Она из Японии?"
	me "Извини, что перебиваю, но ты из Японии?"
	mi "А? Я разве не говорила?"
	
	mi "Хм. А, точно, я же обещала рассказать! Ну, на самом деле, всё не так сложно. Мой отец - инженер, и познакомился с моей мамой, когда строил в Японии станцию. Атомную."
	extend " Или не атомную... В общем, неважно."
	mi "До шести лет я с ними жила в Японии, но после, по некоторым причинам, переехала в Россию. Такая история."
	th "Теперь понятно. Да. Всё так просто, хах..."
	
	me "Понял. Так что ты говорила про инструменты?"
	mi "Так вот, на гитаре я еще с пяти лет начала играть. А потом и на пианино. И на барабанах. И вообще ещё на много чём: флейта, немного скрипка, даже саксофон..."
	mi "Нет, ну лучше всего у меня гитара и фортепиано получаются, но и на остальных неплохо тоже. Как говорят, слушать можно."
	th "...девочка-оркестр, да?"
	th "Может я бы и не поверил, но вот я смотрю сейчас в эти глаза и у меня почти ни капли сомнения, что это всё правда..."
	me "Ого. Это очень сложно, наверное?"
	mi "Ой, да не особо. Мне это нравится, да и всегда нравилось. Да, часто надо было постараться... Но это была моя жизнь. И есть. Живу музыкой!"
	"Мику рассмеялась."
	me "Понятно... Ну, это действительно круто. Такого учителя ещё поискать надо."
	mi "Спасибо..."
	"..."
	
	"Несколько секунд мы посидели в тишине."
	me "Ну... Я пойду тогда?"
	mi "Да. Приходи ещё вечером, поиграем!"
	$ me.stand_up()
	me "Если получится."
	
	$ mi.rp += 1
	$ mi.get_actions().start('interesting_place')
