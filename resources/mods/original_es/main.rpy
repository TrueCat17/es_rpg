init python:
	set_fps(60)
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel, depth = 1)

label start:
#	jump day1
#	jump day2_main1
#	jump day3_main4
	jump day4_main2
	jump prologue

