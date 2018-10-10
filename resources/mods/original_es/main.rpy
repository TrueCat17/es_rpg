init python:
	set_fps(60)
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel, depth = 1)

label start:
#	jump day1
#	jump day2_main1
	jump prologue

