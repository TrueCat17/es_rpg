init python:
	dissolve_fast = Dissolve(0.5)
	
	if persistent.endings is None:
		persistent.endings = Object()
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel, depth = 1)

label start:
#	jump day1
#	jump day2_main1
#	jump day2_cardgame
#	jump day3_main4
#	jump main_good_ending
	jump prologue

