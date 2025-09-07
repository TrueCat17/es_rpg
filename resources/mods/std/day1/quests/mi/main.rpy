init python:
	joined_mus_club = False
	joined_mus_club_hours = 0


label day1__clubs__mus_club:
	if rpg_event != 'no_exit' or (clock.hours, clock.minutes) > (21, 15):
		return
	
	# сначала Мику уговаривает вступить в клуб, а уже потом они знакомятся друг с другом более обстоятельно
	# т. е. по хронологии сначала идёт join, потом meet
	# (а потом just_play, но это уже не через эту метку, т. к. вход свободен, т. е. события no_exit не будет)
	
	if 'mus_club_join' not in was:
		$ set_rpg_control(False)
		
		if me.get_dress() != 'pioneer':
			"Лучше сначала сходить и переодеться."
		else:
			$ was.append('mus_club_join')
			call mus_club_join
		
		window hide
		$ set_rpg_control(True)
		return
	
	if 'mus_club_meet' not in was and joined_mus_club:
		$ set_rpg_control(False)
		
		if clock.hours - joined_mus_club_hours >= 3:
			$ was.append('mus_club_meet')
			call mus_club_meet
		else:
			"Для повторного занятия пока слишком рано."
		
		window hide
		$ set_rpg_control(True)
