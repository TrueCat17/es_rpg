init python:
	set_fps(60)
	
	if persistent.endings is None:
		persistent.endings = Object()
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel, depth = 1)

label start:
#	jump day1
#	jump day2_main1
#	jump day3_main4
	jump day4_us
	jump prologue

