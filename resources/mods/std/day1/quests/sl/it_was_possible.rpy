init python:
	sl_it_was_possible__name = 'А так можно было?'

label sl_it_was_possible__start:
	$ me.get_actions().start('follow', sl)
	$ sl.move_to_place(['square', 'canteen', (-90, 10)])
	$ sl.set_direction(to_right)
	$ me.get_actions().update('rewind_to_max')
	
	# добавить затемнённый спрайт Алисы
	sl "Эй, стоять!"
	"Впрочем, это было бессмысленно. Злодей сбежал."
	sl "Бесполезно... Ладно, не будем забивать голову. Я сейчас."
	
	# (сл подходит к двери, звук связки ключей и поворота замка.)
	# (так же как и во "взломе", в кустах, куда спрыгнула алиса, будет лежать "инструмент взлома", который алиса выронила, когда убегала. Его можно забрать, но только в тот же вечер)
	sl "Заходи!"
	
	$ me.allow_exit('square', 'canteen')
	
	$ sl.move_to_place(['canteen', 'chair_forward_pos-r3a', (30, 30)])
	$ me.get_actions().update('rewind_to_min')
	$ me.set_auto(False)
	
	$ me.disallow_exit('square', 'canteen')
	
	$ sl.set_direction(to_left)
	sl "Ты садись, я сейчас посмотрю, что там есть."
	me "Эм... может, мне тоже поискать?"
	sl "Ой, да брось ты! Сиди."
	
	python:
		sl.move_to_place(['canteen', 'canteen_door_pos', (0, 20)])
		me.move_to_place(['canteen', 'chair_forward_pos-r3a', (0, 20)])
	$ me.sit_down(get_near_sit_objects()[0][0])
	$ hide_character(sl)
	
	th "Это очень необычно."
	th "Если так подумать, то этот \"сон\", или что бы там ни было, очень даже хорош."
	th "Красивая природа, красивые девушки, лето в разгаре... да ещё и обслуживают, словно важную персону. А ведь я для них никто!"
	$ show_character(sl)
	$ sl.set_dress('pioneer_food')
	$ sl.move_to_place(['canteen', 'chair_backward_pos-r3b', (0, -20)])
	$ sl.set_direction(to_back)
	"Славя вернулась с двумя треугольниками кефира и несколькими булочками."
	$ sl.set_dress('pioneer')
	$ sl.sit_down(get_near_sit_objects(sl)[0][0])
	sl "Угощайся."
	"..."
	
	"Было немного неловко не только от того, что на меня смотрела Славя, но и от того, что мне всё предоставили, как ребёнку."
	"Впрочем, голод заставил забыть о стеснении."
	"Только укусив эти на вид, казалось бы, обычные булочки, я растаял. Хотя уже и полдня прошло, на вкус они были, будто только выскочили из печи."
	th "Видимо, легенды о советских продуктах и еде не такие уж и легенды"
	me "Больфое шпашибо..."
	"Славя заливисто рассмеялась."
	sl "Не за что. Не говори, а то подавишься ещё."
	"..."
	
	me "Очень вкусно. Ещё раз спасибо."
	sl "Ну, не я же готовила, так что спасибо пекарям. Пойдем?"
	me "А-ага."
	
	show bg black with dissolve
	$ hide_location()
	hide bg
	"Славя хотела было и пустые треугольники забрать, но тут даже я смог твёрдо отказаться от помощи и выкинул их сам. Боже, это всё так нелепо..."
	window hide
	$ show_character(sl, 'canteen', 'square')
	$ sl.x -= 100
	$ sl.set_direction(to_right)
	$ set_location('square', 'canteen')
	$ me.x -= 65
	$ me.set_direction(to_left)
	
	me "Большое спасибо за всё."
	sl "Ой, да хватит тебе уже благодарить... Но мне, всё же, приятно. На здоровье!"
	sl "Ладненько, пора расходиться уже. До завтра!"
	me "Спокойной ночи."
	sl "Спокойной."
	window hide
	
	$ sl.set_auto(True)
	$ set_rpg_control(True)
	
	$ quest_end('sl_it_was_possible')
