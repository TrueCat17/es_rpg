screen choose_menu:
	modal True
	zorder -1
	
	vbox:
		align (0.5, 0.5)
		spacing 10
		
		for i in xrange(len(choose_menu_variants)):
			if choose_menu_variants[i]:
				textbutton choose_menu_variants[i] action Return(i):
					text_size 20
					size (300, 35)
			elif choose_menu_variants[i] is not None:
				null ysize 35
	
	
	key 'Q' action [
		SetVariable('save_table', 1),
		SetVariable('save_num', 1),
		SetVariable('need_save', True)]
	
	key 'ESCAPE' action show_pause
	
	
	button:
		ground 	db_menu_btn

		anchor (0.5, 0.5)
		pos    (get_stage_width() - db_menu_btn_indent - db_menu_btn_size / 2, db_menu_btn_indent + db_menu_btn_size / 2)
		size   (db_menu_btn_size, db_menu_btn_size)
		action show_pause
		
		rotate (int(time.time() * 10) % 360)
	
