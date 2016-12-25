init python:
	mods['test_label'] = 'test'

label test_label:
	scene bg bus_stop
	
	me "Музыку!"
	play music music_list["a_promise_from_distant_days_v2"]
	
	me "Спрайт!"
	show dv laugh swim far at left
	me "Ещё!"
	show dv laugh swim close as dv2 behind dv
	me "И ещё один!"
	show dv laugh pioneer2 far
	
	mt "Поздравляю!"
	extend " Спрайты отображаются нормально!!!"
	
	"..."
