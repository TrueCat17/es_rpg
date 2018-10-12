init python:
	set_fps(60)
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel, depth = 1)

label start:
	scene stars with dissolve
	play music music_list["waltz_of_doubts"] fadein 3
	window show
	"Я сидел в шезлонге и смотрел на звёзды."
#	jump day1
#	jump day2_main1
#	jump day3_main4
	jump day4_main2
	jump prologue

