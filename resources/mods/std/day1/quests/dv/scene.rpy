init python:
	def day1__dv_scene_actions(character, state):
		if state == 'start':
			character.get_actions().interruptable = False
			
			show_character(character, 'before_microphone', 'scene')
			character.start_animation('guitar', -1)
			return 'playing'
		
		if state == 'playing':
			if (clock.hours, clock.minutes) >= (11, 30):
				return 'end'
			return 'playing'
		
		if state == 'end':
			character.remove_animation()
			return 'end'
	
	def day1__dv_start():
		if characters_inited:
			dv.get_actions().start(day1__dv_scene_actions)
	signals.add('clock-day_1', day1__dv_start)
	
	def day1__dv_return_music_volume():
		if cur_location_name == 'scene':
			renpy.music.set_volume(1.0, delay = 1.0, channel = 'music')
		else:
			renpy.music.stop('music', fadeout = 2.0)
			set_timeout(Function(renpy.music.set_volume, 1.0, channel = 'music'), 2.0)


label day1__library_and_hospital__before_scene:
	if 'dv_scene' in was:
		return
	$ was.append('dv_scene')
	
	$ set_rpg_control(False)
	$ me.set_direction(to_forward)
	
	$ renpy.music.set_volume(0.2, channel = 'music')
	play music music_list['blow_with_the_fires']
	$ signals.add('rpg-location', day1__dv_return_music_volume, times = 1)
	
	$ cam_to('scene', align = (0.5, 0.0))
	"Проходя мимо большого деревянного амфитеатра, скорее всего, являющегося сценой, я услышал звуки электрогитары."
	$ cam_to(me, align = 'center')
	
	menu:
		"Не обращать внимания":
			th "Гитара и гитара. Ничего необычного."
			window hide
			
			$ dv.get_actions().start('home')
			
			stop music fadeout 3.0
			$ set_timeout(Function(renpy.music.set_volume, 1.0, channel = 'music'), 3.0)
			
			$ set_rpg_control(True)
			return
		
		"Подойти ближе":
			pass
	
	me "Интересно, кто там..."
	$ me.move_to_place(['scene', 'before_scene_left'])
	$ me.set_direction(to_right)
	
	"На сцене была рыжеволосая девушка, которая играла так воодушевлённо, что даже не замечала меня."
	$ renpy.music.set_volume(0.5, delay = 1.0, channel = 'music')
	$ dv.set_auto(False)
	$ dv.set_direction(to_left)
	"И только когда её \"партия\" была окончена, она бросила на меня взгляд."
	"Хотя в моей голове всё ещё продолжала играть её мелодия."
	dv "Что уставился?"
	
	menu:
		"Оправдаться":
			me "Извини, я не хотел."
			th "И что я не хотел?"
			"Девушка хмыкнула и ушла."
			$ dv.set_auto(True)
			$ dv.get_actions().start('home')
		
		"Похвалить":
			me "Ну... я просто слушал. Круто играешь!"
			"Девушка широко и слегка хитро улыбнулась."
			dv "А то. Сам мечтаешь так играть?"
			"И, не дожидаясь ответа, продолжила:"
			dv "Захочешь поучиться - дам пару уроков."
			dv "Но не сейчас, сейчас я ухожу. Бывай!"
			"Напоследок она подмигнула и, спрыгнув со сцены с гитарой в руках, куда-то умчалась."
			python:
				dv.set_auto(True)
				dv.get_actions().start('home', run = True, force = True)
				dv.get_actions().interruptable = False
	
	stop music fadeout 2.0
	$ set_timeout(Function(renpy.music.set_volume, 1.0, channel = 'music'), 2.0)
	
	window hide
	$ set_rpg_control(True)
