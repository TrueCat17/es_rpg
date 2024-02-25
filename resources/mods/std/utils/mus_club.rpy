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
	
	def mus_club__play():
		renpy.call('mus_club__playing')
	
	
	def mus_club__start():
		me.start_animation('guitar', -1)
	
	def mus_club__end():
		me.remove_animation()
		add_location_object(cur_location.name, 'guitar_pos', 'guitar')
	
	build_object('mus_club')


label mus_club__take_guitar_and_sit:
	$ me.move_to_place('before_guitar')
	$ remove_location_object('mus_club', me, 'guitar')
	$ me.sit_down(get_near_sit_objects()[0][0])
	$ me.start_animation('guitar_stop', -1)

label mus_club__playing:
	$ mus_club.start()
	"..."
	$ mus_club.end()
