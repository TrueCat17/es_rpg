label un_good_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_square_night_ending:
		size (1.2, 1.2)
		xanchor 0.1
		linear 12 xanchor 0.0
	show un normal pioneer:
		yalign 1.0
		xpos 0.7
		linear 11 xpos 0.2
	with dissolve2
	pause 8
	
	scene cg d1_grasshopper_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene bg ext_polyana_night_ending:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	show un angry pioneer at cleft:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	show dv angry pioneer at cright:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	with dissolve2
	pause 8
	
	scene cg d3_un_dance_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene cg epilogue_un_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.0)
		linear 12 anchor (0.0, 0.1)
	pause 8
	
	scene cg d5_un_island_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene cg d6_un_evening_1_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d6_un_evening_2_ending with dissolve
	pause 4
	scene cg epilogue_un_good_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label un_bad_ending:
	scene bg black with dissolve2
	pause 1
	
	play music music_list["410"] fadein 3
	
	$ show_credits()
	
	pause 8
	scene un_ending_bad with dissolve2
	$ renpy.pause(79, hard=True)
	
	scene bg black with dissolve2
	stop music fadeout 5
	pause 4


label main_good_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	pause 2
	
	scene anim intro_1 with dissolve
	pause 0.5
	scene anim intro_2 with dissolve
	pause 0.5
	scene anim intro_3 with dissolve
	pause 0.5
	scene anim intro_4 with dissolve
	pause 0.5
	scene anim intro_5 with dissolve
	pause 0.5
	scene anim intro_6 with dissolve
	pause 0.5
	scene anim intro_8 with dissolve
	pause 0.5
	scene anim intro_7 with dissolve
	pause 0.5
	scene anim intro_9 with dissolve
	pause 0.5
	scene anim intro_10 with dissolve
	pause 0.5
	scene anim intro_11 with dissolve
	pause 0.5
	scene anim intro_13 with dissolve
	pause 0.5
	scene anim intro_14 with dissolve
	pause 0.5
	scene anim intro_15 with dissolve
	pause 0.5
	scene anim intro_16 with dissolve
	pause 0.5
	
	scene op_back with dissolve2
	pause 1
	show op_sl with dissolve2
	pause 1
	show cg d6_sl_forest_ending with dissolve
	pause 0.5
	show cg d3_sl_library_ending with dissolve
	pause 0.5
	hide cg with dissolve2
	
	show op_un with dissolve2
	pause 1
	show cg d5_un_island_ending with dissolve
	pause 0.5
	show cg epilogue_un_ending with dissolve
	pause 0.5
	hide cg with dissolve2
	
	show op_us with dissolve2
	pause 1
	show cg d2_ussr_falling_ending with dissolve
	pause 0.5
	show cg d4_us_cancer_ending with dissolve
	pause 0.5
	show cg d3_ussr_catched_ending with dissolve
	pause 0.5
	hide cg with dissolve2
	
	show op_dv with dissolve2
	pause 1
	show cg d5_dv_argue_ending with dissolve
	pause 0.5
	show cg d2_water_dan_ending with dissolve
	pause 0.5
	hide cg with dissolve2
	
	show op_mi with dissolve2
	pause 1
	show cg d2_miku_piano_ending with dissolve
	pause 0.5
	show cg d4_mi_guitar_ending with dissolve
	pause 0.5
	show cg epilogue_mi_1_ending with dissolve
	pause 0.5
	hide cg with dissolve2
	
	show op_uv with dissolve2
	pause 1
	
	scene bg ext_road_day_ending with dissolve2
	pause 1
#	show logo_day with dissolve2:
#		align (0.5, 0.5)
	
	pause 12
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label main_bad_ending:
	scene bg black with dissolve2
	pause 1
	
	play music music_list["410"] fadein 3
	
	$ show_credits()
	
	pause 8
	scene black_long with dissolve2
	pause 79
	
	scene bg black with dissolve2
	stop music fadeout 5
	pause 4


label dv_bad_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_beach_day_ending:
		size (1.2, 1.2)
		anchor (0.1, 0.0)
		linear 12 anchor (0.0, 0.1)
	show dv smile pioneer2:
		yalign 1.0
		xpos 0.1
		linear 12 xpos 0.7
	with dissolve2
	pause 8
	
	# !!! from day2
	scene cg d2_2ch_beach_ending with dissolve2:
		ypos -1920
		linear 9.0 ypos 0
		linear 3.0 ypos -250
	pause 8
	
	scene bg ext_polyana_night_ending:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	show un scared pioneer at cright:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	show dv rage pioneer at cleft:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	with dissolve2
	pause 8
	
	scene cg d3_dv_scene_1_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg d5_dv_island_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene cg d7_dv_2_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	pause 7
	
	scene cg d6_dv_fight_ending with dissolve2:
		size (1.1, 1.1)
		linear 5 size (1.0, 1.0)
	pause 3
	
	scene cg d6_dv_fight_2_ending with dissolve
	pause 3
	scene cg d6_dv_fight_3_ending with dissolve
	pause 3
	scene cg epilogue_dv_2_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label dv_good_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_beach_day_ending:
		size (1.2, 1.2)
		anchor (0.1, 0.0)
		linear 12 anchor (0.0, 0.1)
	show dv smile pioneer2:
		xpos 0.1
		linear 12 xpos 0.7
	with dissolve2
	pause 8
	
	# !!! from day2
	scene cg d2_2ch_beach_ending with dissolve2:
		pos (0,-1920)
		linear 9.0 pos (0, 0)
		linear 3.0 pos (0, -250)
	pause 8
	
	scene bg ext_polyana_night_ending:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	show un scared pioneer at cright:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	show dv rage pioneer at cleft:
		size (1.2, 1.2)
		linear 11 size (1.0, 1.0)
	with dissolve2
	pause 8
	
	scene cg d3_dv_scene_2_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg d5_dv_island_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene cg d7_dv_2_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	pause 7
	
	scene cg d5_dv_argue_ending with dissolve2:
		size (1.1, 1.1)
		linear 5 size (1.0, 1.0)
	pause 3
	
	scene cg d5_dv_argue_2_ending with dissolve
	pause 3
	scene cg d5_dv_argue_3_ending with dissolve
	pause 3
	scene cg epilogue_dv_3_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label sl_bad_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_houses_day_ending:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	show sl smile2 pioneer:
		xpos 0.2
		linear 12 xpos 0.5
	with dissolve2
	pause 8
	
	scene cg d1_sl_dinner_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d1_sl_dinner_0_ending with dissolve
	pause 4
	
	scene cg d3_sl_dance_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.1
		linear 12 xanchor 0.0
	pause 8
	
	scene cg d5_sl_sleep_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d5_sl_sleep_2_ending with dissolve
	pause 4
	
	scene cg d3_sl_evening_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg d6_sl_forest_2_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d6_sl_forest_ending with dissolve
	pause 4
	
	scene cg d3_sl_library_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene bg semen_room_window_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label sl_good_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_houses_day_ending:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	show sl smile2 pioneer:
		xpos 0.2
		linear 12 xpos 0.5
	with dissolve2
	pause 8
	
	scene cg d1_sl_dinner_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d1_sl_dinner_0_ending with dissolve
	pause 4
	
	scene cg d3_sl_dance_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.1
		linear 12 xanchor 0.0
	pause 8
	
	scene cg d5_sl_sleep_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d5_sl_sleep_2_ending with dissolve
	pause 4
	
	scene cg d3_sl_evening_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg d6_sl_forest_2_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d6_sl_forest_ending with dissolve
	pause 4
	
	scene cg d3_sl_library_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene cg epilogue_sl_ending with flash2
	pause 4
	scene cg epilogue_sl_2_ending with dissolve
	pause 4
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label us_bad_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_playground_day_ending:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	show us laugh sport:
		yalign 1.0
		xpos 0.1
		linear 12 xpos 0.8
	with dissolve2
	pause 8
	
	scene cg d2_ussr_falling_ending with dissolve2:
		size (1.2, 1.2)
		yanchor 0.1
		linear 12 yanchor 0.0
	pause 8
	
	scene cg d3_soccer_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene cg d3_us_library_1_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d3_us_library_2_ending with dissolve
	pause 4
	
	scene cg d3_ussr_catched_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg d4_catac_us_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d4_catac_us_2_ending with dissolve
	pause 4
	
	scene cg d5_us_ghost_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg epilogue_us_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label us_good_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_playground_day_ending:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	show us laugh sport:
		yalign 1.0
		xpos 0.1
		linear 12 xpos 0.8
	with dissolve2
	pause 8
	
	scene cg d2_ussr_falling_ending with dissolve2:
		size (1.2, 1.2)
		yanchor 0.1
		linear 12 yanchor 0.0
	pause 8
	
	scene cg d3_soccer_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene cg d6_us_film_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene cg d3_ussr_catched_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg d5_us_ghost_2_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.1
		linear 12 xanchor 0.0
	pause 8
	
	scene cg d5_us_kiss_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	pause 8
	
	scene cg epilogue_us_3_a_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label mi_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_musclub_day_ending:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	show mi smile pioneer:
		yalign 1.0
		xpos 0.6
		linear 12 xpos 0.2
	with dissolve2
	pause 8
	
	scene cg d2_miku_piano2_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d2_miku_piano_ending with dissolve
	pause 4
	
	scene cg d4_mi_guitar_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene cg d5_mi_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene cg d4_mi_sing_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg epilogue_mi_1_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 8
	
	scene bg int_musclub_day_ending:
		size (1.1, 1.1)
		linear 24 size (1.0, 1.0)
	show mi shy pioneer at center:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	with dissolve2
	pause 2
	
	show mi smile pioneer at center with dissolve:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 2
	
	show mi laugh pioneer at center with dissolve:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 2
	
	show mi happy pioneer at center with dissolve:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 2
	
	scene cg epilogue_mi_9_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label harem_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene cg d7_pioneers_leaving_ending with dissolve2:
		size (1.2, 1.2)
		linear 12 size (1.0, 1.0)
	pause 8
	
	scene bg ext_square_day_ending:
		size (1.1, 1.1)
		linear 12 size (1.0, 1.0)
	
	show us smile pioneer at fleft
	show mi smile pioneer at fright
	show dv smile pioneer at cleft
	show un smile pioneer at cright
	show sl smile pioneer at center
	with dissolve2
	pause 8
	
	scene cg d3_disco_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene cg d2_lineup_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene bg int_bus_people_day_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	pause 4
	
	scene bg int_bus_people_night_ending with dissolve2:
		size (1.2, 1.2)
		xanchor 0.1
		linear 12 xanchor 0.0
	pause 4
	
	scene bg ext_aidpost_day_ending            with dissolve_fast
	scene bg ext_boathouse_day_ending          with dissolve_fast
	scene bg ext_clubs_day_ending              with dissolve_fast
	scene bg ext_dining_hall_away_day_ending   with dissolve_fast
	scene bg ext_house_of_mt_day_ending        with dissolve_fast
	scene bg ext_island_day_ending             with dissolve_fast
	scene bg ext_library_day_ending            with dissolve_fast
	scene bg ext_stage_normal_day_ending       with dissolve_fast
	scene bg ext_washstand_day_ending          with dissolve_fast
	scene bg int_aidpost_day_ending            with dissolve_fast
	scene bg int_clubs_male_day_ending         with dissolve_fast
	scene bg int_dining_hall_people_day_ending with dissolve_fast
	scene bg int_house_of_dv_day_ending        with dissolve_fast
	scene bg int_house_of_mt_day_ending        with dissolve_fast
	scene bg int_house_of_sl_day_ending        with dissolve_fast
	scene bg int_house_of_un_day_ending        with dissolve_fast
	
	scene bg ext_beach_day_ending:
		size (1.1, 1.1)
		linear 12 size (1.0, 1.0)
	show us smile swim at fleft
	show mi smile swim at fright
	show dv smile swim at cleft
	show un smile swim at cright
	show sl smile swim at center
	with dissolve2
	pause 8
	
	scene cg final_all_2_ending with flash2
	pause 8
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4


label uv_ending:
	$ day_time()
	scene bg black with dissolve2
	pause 1
	
	play music music_list["opening"] fadein 3
	
	$ show_credits()
	
	scene bg ext_polyana_day_ending:
		size (1.2, 1.2)
		xanchor 0.0
		linear 12 xanchor 0.1
	show uv smile:
		yalign 1.0
		xpos 0.6
		linear 12 xpos 0.2
	with dissolve2
	pause 8
	
	scene cg d4_uv_1_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d4_uv_ending with dissolve
	pause 4
	
	scene cg d6_uv_2_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 8
	
	scene cg d5_uv_ending with dissolve2:
		size (1.1, 1.1)
		linear 6 size (1.0, 1.0)
	pause 4
	
	scene cg d5_uv_2_ending with dissolve
	pause 4
	
	scene cg d7_uv_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.1)
		linear 12 anchor (0.1, 0.0)
	pause 8
	
	scene cg epilogue_uv_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.0, 0.0)
		linear 12 anchor (0.1, 0.1)
	pause 4
	
	scene cg d1_uv_ending with dissolve2:
		size (1.2, 1.2)
		anchor (0.1, 0.1)
		linear 12 anchor (0.0, 0.0)
	pause 4
	
	scene cg epilogue_uv_dv_ending with flash2
	pause 2
	scene cg epilogue_uv_sl_ending with dissolve
	pause 2
	scene cg epilogue_uv_un_ending with dissolve
	pause 2
	scene cg epilogue_uv_us_ending with dissolve
	pause 2
	scene cg epilogue_uv_mi_ending with dissolve
	pause 2
	scene cg epilogue_uv_uv_ending with dissolve
	pause 2
	
	scene black with dissolve2
	stop music fadeout 3
	pause 4

