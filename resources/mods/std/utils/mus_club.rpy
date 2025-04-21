init python:
	def mus_club__move_miku_to_piano():
		mi.set_auto(False)
		if me.location is not mi.location:
			show_character(mi, 'piano_chair_pos', 'mus_club')
			mi.y += 10
		else:
			mi.move_to_place(['mus_club', 'piano_chair_pos', (0, +10)], run = True)
	
	def mus_club__show_miku_at_piano(place_index = -1):
		piano_chair = get_location_objects('mus_club', 'piano_chair_pos', 'piano_chair')[0]
		mi.sit_down(piano_chair, place_index)
	
	def mus_club__prepare():
		renpy.call('mus_club__take_guitar_and_sit')
	
	def mus_club__play(need_play = None, no_more = False):
		mus_club.need_play = need_play if need_play is not None else mus_club.need_play_by_default
		mus_club.no_more = no_more
		mus_club.miku_text = ''
		renpy.call('mus_club__playing')
	
	
	def mus_club__start_playing():
		me.start_animation('guitar', -1)
	def mus_club__stop_playing():
		me.start_animation('guitar_stop', -1)
	
	def mus_club__end():
		me.remove_animation()
		add_location_object(cur_location.name, 'guitar_pos', 'guitar')
	
	
	def mus_club__calc_res(quality, difficulty):
		if quality < 0.1 and mus_club.enable_miku_reaction:
			mus_club.miku_text = 'Решил прерваться?'
			return
		
		res = 0.0
		
		if difficulty == 0:
			if quality > 0.80:
				res = 0.05
			if quality > 0.94:
				res = 0.10
			if quality == 1:
				res = 0.125
		
		if difficulty == 1:
			if quality > 0.75:
				res = 0.10
			if quality > 0.90:
				res = 0.15
			if quality == 1:
				res = 0.175
		
		if difficulty == 2:
			if quality > 0.75:
				res = 0.15
			if quality > 0.85:
				res = 0.20
			if quality > 0.90:
				res = 0.25
			if quality == 1:
				res = 0.275
		
		mi.rp += res
		
		exprs = {
			0.275: 'Ого! Круто! Ни единой ошибки на таком сложном уровне!',
			0.175: 'Ого! Круто! Ни единой ошибки на таком уровне!',
			0.125: 'Ты ни разу не ошибся! Поздравляю!',
			
			0.25: 'Ого! Круто!',
			0.20: 'Отлично!',
			0.15: 'Хорошо сыграл!',
			0.10: 'Неплохо, неплохо.',
			0.05: 'Для начала неплохо.',
			0.00: 'Ну... Тебе ещё многому предстоит научиться.',
		}
		if mus_club.enable_miku_reaction:
			mus_club.miku_text = exprs[res]
		
		mus_club.played += 1
	
	
	build_object('mus_club')
	mus_club.need_play_by_default = 3
	mus_club.enable_miku_reaction = True


label mus_club__take_guitar_and_sit:
	$ me.move_to_place('before_guitar')
	$ remove_location_object('mus_club', me, 'guitar')
	$ me.sit_down(get_near_sit_objects()[0][0])
	$ mus_club.stop_playing()

label mus_club__playing:
	$ db.skip_tab = False
	window hide
	
	$ mus_club.played = 0
	if mus_club.need_play > 0:
		$ guitar_hero.close_btn = False
	
	$ guitar_hero.show()
	
	$ prev_playing = False
	while has_screen('guitar_hero'):
		$ playing = guitar_hero.playing()
		
		if playing and not prev_playing:
			$ mus_club.start_playing()
		
		if not playing and prev_playing:
			$ mus_club.stop_playing()
			$ mus_club.calc_res(guitar_hero.last_game_quality, guitar_hero.difficulty)
			
			if canteen.preparing_started:
				$ guitar_hero.close_btn = True
			
			if mus_club.played >= mus_club.need_play:
				$ guitar_hero.close_btn = True
				
				if mus_club.no_more:
					$ guitar_hero.hide()
					pause guitar_hero.disappearance_time
			
			if mus_club.miku_text:
				$ guitar_hero.block_playing = True
				mi mus_club.miku_text
				window hide
				$ guitar_hero.block_playing = False
		
		$ prev_playing = playing
		
		pause 0.1
	
	$ guitar_hero.hide()
	$ mus_club.end()
