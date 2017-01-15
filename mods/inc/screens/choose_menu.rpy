screen choose_menu:
	modal True
	
	vbox:
		align (0.5, 0.5)
		spacing 10
		
		for i in xrange(len(choose_menu_variants)):
			if choose_menu_variants[i]:
				textbutton choose_menu_variants[i] action Return(i):
					size 20
					xysize (300, 35)
			elif choose_menu_variants[i] is not None:
				null ysize 35
