init python:
	credits_text = [
		"Команда Soviet Games (IIchan Eroge Team) благодарит вас за время, уделённое игре!",
		"Благодарности:",
		"PyTom'у за движок Ren'Py.",
		"Сайту freesounds.org за бесплатные звуки.",
		"Сайтам iichan.hk и 2ch.hk.",
		"Всем, кто помогал работать над игрой.",
		"Всем, кто нас поддерживал все эти годы, ждал и верил!",
		" ",
		" ",
		"КОНЕЦ."
	]

label final_credits:
	scene bg black with dissolve2
	pause 1
	play music music_list["opening"] fadein 3
	$ show_credits()
	scene black with dissolve2
	stop music fadeout 3
	pause 4
label final_credits_410:
	scene bg black with dissolve2
	pause 1
	play music music_list["410"] fadein 3
	show credits credits_text:
		xalign 0.5
		ypos 1.3
		linear 87.0 ypos -1.0
	pause 87
	scene black with dissolve2
	stop music fadeout 3
	pause 4

