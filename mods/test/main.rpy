init python:
	mods['test_label'] = 'test'

label test_label:
	scene bg bus_stop
	play music music_list["a_promise_from_distant_days_v2"]
	
	me "Вывод текста работает!"
	
	mt "Поздравляю!"
	extend "\nЕщё пару багов исправить, и можно приступать к отображению спрайтов"
	extend " вместе с анимациями!!!"
	
	menu:
		"123":
			uv "123"
		"234":
			uv "234"
		"345":
			uv "345"
	
	"..."
