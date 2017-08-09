# test_1623_

init python:
    test_1623__width = 1
    test_1623__height = 1
    test_1623__size = 16
    
    test_1623__color_field = ['green']
    
    mods['test_1623__start'] = 'test_1623'


screen test_1623__main_screen:
    image 'mods/test_1623/images/px/white.png':
        align (0.5, 0.4)
        xysize (test_1623__width * test_1623__size, test_1623__height * test_1623__size)
    
    vbox:
        align (0.5, 0.4)
        
        for i in xrange(test_1623__height):
        	# На случай, если test_1623__height поменяется прямо во время этого цикла
        	if i >= test_1623__height:
        		break
        	
            hbox:
                python:
                	test_1623__line = []
                	
                    test_1623__count = 0
	                for j in xrange(test_1623__width):
                        test_1623__count += 1
                        
                        test_1623__color = test_1623__color_field[i * test_1623__width + j]
                        
                        test_1623__is_end = j == test_1623__width - 1
                        
                        if test_1623__is_end:
                            test_1623__next_color = 'no'
                        else:
                            test_1623__next_color = test_1623__color_field[i * test_1623__width + j + 1]
                    
                        test_1623__need_draw = test_1623__color != test_1623__next_color
                    	if test_1623__need_draw:
                    		test_1623__line.append((test_1623__color, test_1623__count))
                    		test_1623__count = 0
                for test_1623__color, test_1623__count in test_1623__line:
                    image ('mods/test_1623/images/px/' + test_1623__color + '.png'):
                    	xysize (test_1623__size * test_1623__count, test_1623__size)


label test_1623__start:
    jump test_1623__main


label test_1623__main:
    $ set_fps(60)
    
    scene bg int_clubs_male_day
    show el normal pioneer far at fright
    
    window show
    el 'Выбирай игру!'
    menu:
        'Жизнь':
            jump test_1623_live__start
        'Змейка':
            jump test_1623_shake__start
        'Танчики':
            jump test_1623_tanks__start_usual
        'Упрощённые танчики':
            jump test_1623_tanks__start_simple
        ''
        'Описание':
            jump test_1623_description__start
        ''
        'Выход':
            el 'До встречи!'
