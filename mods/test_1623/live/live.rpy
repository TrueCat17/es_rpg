# test_1623_live__

init python:
    test_1623_live__pause = False
    test_1623_live__exit = False
    
    test_1623_live__rect_x = 0
    test_1623_live__rect_y = 0
    
    
    def test_1623_live__init():
        global test_1623_live__field, test_1623__color_field, test_1623_live__pause, test_1623_live__exit
        global test_1623__width, test_1623__height
        
        set_fps(20)
        
        test_1623__width = 50
        test_1623__height = 25
        
        test_1623_live__pause = False
        test_1623_live__exit = False
        test_1623_live__field = [renpy.random.random() < 0.3 for i in xrange(test_1623__width * test_1623__height)]
        test_1623__color_field = ['white' for i in xrange(test_1623__width * test_1623__height)]
        test_1623_live__render()
    
    
    def test_1623_live__update():
        global test_1623_live__field
        
        next_field = []
        
        for y in xrange(test_1623__height):
            for x in xrange(test_1623__width):
                v = test_1623_live__get_next_value(test_1623_live__field, x, y)
                next_field.append(v)
        
        test_1623_live__field = next_field
        
        test_1623_live__render()
    
    def test_1623_live__render():
        for y in xrange(test_1623__height):
            for x in xrange(test_1623__width):
                index = y * test_1623__width + x
                if test_1623_live__field[index]:
                    test_1623__color_field[index] = 'black'
                else:
                    test_1623__color_field[index] = 'white'
        
        rect_index = test_1623_live__rect_y * test_1623__width + test_1623_live__rect_x
        if test_1623__color_field[rect_index] == 'black':
            test_1623__color_field[rect_index] = 'black_rect'
        else:
            test_1623__color_field[rect_index] = 'rect'
    
    
    def test_1623_live__get_next_value(field, x, y):
        count_nears = 0
        
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                if i == 0 and j == 0:
                    continue
                
                realX = (x + j) % test_1623__width
                realY = (y + i) % test_1623__height
                if field[realY * test_1623__width + realX]:
                    count_nears += 1
        
        if count_nears < 2 or count_nears > 3:
            return False
        
        is_live = test_1623_live__field[y * test_1623__width + x]
        return is_live or count_nears == 3
    
    
    def test_1623_live__change_cell_state():
        index = test_1623_live__rect_y * test_1623__width + test_1623_live__rect_x
        test_1623_live__field[index] = not test_1623_live__field[index]
    
    
    def test_1623_live__clear():
        global test_1623_live__field
        test_1623_live__field = [False for i in xrange(test_1623__width * test_1623__height)]
    
    
    def test_1623_live__change_pause_state():
        global test_1623_live__pause
        test_1623_live__pause = not test_1623_live__pause
    
    
    def test_1623_live__to_exit():
        global test_1623_live__exit
        test_1623_live__exit = True
    
    
    def test_1623_live__make_planer():
        test_1623_live__clear()
        
        start_x = int(test_1623__width / 2) - 1
        start_y = int(test_1623__height / 2) - 1
        
        start_indent = start_y * test_1623__width + start_x
        test_1623_live__field[start_indent] = True
        test_1623_live__field[start_indent + 1] = True
        test_1623_live__field[start_indent + 2] = True
        test_1623_live__field[start_indent + test_1623__width + 2] = True
        test_1623_live__field[start_indent + test_1623__width * 2 + 1] = True
        
        test_1623_live__render()
    
    
    def test_1623_live__make_r_pentamino():
        test_1623_live__clear()
        
        start_x = int(test_1623__width / 2) - 1
        start_y = int(test_1623__height / 2) - 1
        
        start_indent = start_y * test_1623__width + start_x
        test_1623_live__field[start_indent + 1] = True
        test_1623_live__field[start_indent + 2] = True
        test_1623_live__field[start_indent + test_1623__width] = True
        test_1623_live__field[start_indent + test_1623__width + 1] = True
        test_1623_live__field[start_indent + test_1623__width * 2 + 1] = True
        
        test_1623_live__render()
    
    
    def test_1623_live__make_space_ship():
        test_1623_live__clear()
        
        start_x = int(test_1623__width / 2) - 1
        start_y = int(test_1623__height / 2) - 1
        
        start_indent = start_y * test_1623__width + start_x
        test_1623_live__field[start_indent + 1] = True
        test_1623_live__field[start_indent + 2] = True
        test_1623_live__field[start_indent + 3] = True
        test_1623_live__field[start_indent + 4] = True
        test_1623_live__field[start_indent + test_1623__width] = True
        test_1623_live__field[start_indent + test_1623__width + 4] = True
        test_1623_live__field[start_indent + test_1623__width * 2 + 4] = True
        test_1623_live__field[start_indent + test_1623__width * 3 + 0] = True
        test_1623_live__field[start_indent + test_1623__width * 3 + 3] = True
        
        test_1623_live__render()
    
    
    def test_1623_live__on_left_press():
        global test_1623_live__rect_x
        test_1623_live__rect_x = (test_1623_live__rect_x - 1) % test_1623__width
    def test_1623_live__on_right_press():
        global test_1623_live__rect_x
        test_1623_live__rect_x = (test_1623_live__rect_x + 1) % test_1623__width
    def test_1623_live__on_up_press():
        global test_1623_live__rect_y
        test_1623_live__rect_y = (test_1623_live__rect_y - 1) % test_1623__height
    def test_1623_live__on_down_press():
        global test_1623_live__rect_y
        test_1623_live__rect_y = (test_1623_live__rect_y + 1) % test_1623__height


screen test_1623_live__screen:
    key 'K_LEFT' action test_1623_live__on_left_press
    key 'K_RIGHT' action test_1623_live__on_right_press
    key 'K_UP' action test_1623_live__on_up_press
    key 'K_DOWN' action test_1623_live__on_down_press
    key 'K_SPACE' action test_1623_live__change_cell_state
    key 'K_RETURN' action test_1623_live__change_cell_state
    key 'a' action test_1623_live__on_left_press
    key 'd' action test_1623_live__on_right_press
    key 'w' action test_1623_live__on_up_press
    key 's' action test_1623_live__on_down_press
    key 'p' action test_1623_live__change_pause_state
    
    use test_1623__main_screen
    
    
    if not test_1623_live__pause:
        $ test_1623_live__update()
    else:
        $ test_1623_live__render()
    
    vbox:
        align (0.5, 0.98)
	    spacing 5
	    
	    hbox:
	        xalign 0.5

	        textbutton 'ReStart (Init Random)' action test_1623_live__init
	        textbutton 'Clear' action test_1623_live__clear
	        
	        textbutton ('Continue' if test_1623_live__pause else 'Pause'):
	        	action test_1623_live__change_pause_state
	        
	        textbutton 'Exit' action test_1623_live__to_exit
	    
	    hbox:
	        xalign 0.5
	        
	        text 'Make: ' text_size 20
	        textbutton 'Planer' action test_1623_live__make_planer
	        textbutton 'SpaceShip' action test_1623_live__make_space_ship
	        textbutton 'R-Pentamino' action test_1623_live__make_r_pentamino


label test_1623_live__start:
    $ test_1623_live__init()
    
    window hide
    scene black
    show screen test_1623_live__screen
    
    while not test_1623_live__exit:
        pause 0.1
    
    hide screen test_1623_live__screen
    
    jump test_1623__main

