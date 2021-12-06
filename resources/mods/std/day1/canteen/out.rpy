label day1__square__canteen:
	if rpg_event != 'enter':
		return
	if 'canteen_pioneers_12h' not in was:
		return
	
	$ set_rpg_control(False)
	
	mt "Ну как, поел?"
	me "Ага."
	$ mt.set_direction(to_forward)
	mt "Вкусно?"
	me "Очень вкусно!"
	mt "Ну и хорошо. До ужина ещё много времени, так что осматривайся. Только не шалить!"
	me "Хорошо."
	$ mt.get_actions().start('interesting_place')
	
	if 'library' in was:
		th "Точно, в библиотеку надо зайти."
	if 'clubs' in was:
		th "Ну, можно и в кружки заглянуть..."
	"Хотя на самом деле хочется немного пройтись и поваляться в домике."
	
	window hide
	$ set_rpg_control(True)
