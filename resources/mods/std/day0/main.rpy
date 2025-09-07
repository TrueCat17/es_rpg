init python:
	def day0_dream_set():
		night_time()
		
		set_location('enter', 'dream_start')
		me.set_dress('sport')
		
		cam_to('square_down', 0)
		
		fog_params = dict(
			name = 'fog',
			image = 'images/locations/objects/fog',
			alpha = 0.5,
			dx = 0.010,
			dy = 0.014,
		)
		add_location_object('enter', { 'x': 0, 'y': 0, 'xsize': 1.0, 'ysize': 1.0 }, ScrollObject, **fog_params)
		
		uv_dream = add_location_object('enter', 'uv_dream_place', 'uv_dream')
		uv_dream.start_animation('main', -1)
		
		add_location_object('enter', 'lamp_place', 'lamp')
		bench = add_location_object('enter', 'bench_right_place', 'bench_right')
		me.sit_down(bench)
		
		ban_exit('enter')
	
	
	def day0_dream_unset():
		day_time()
		
		remove_location_object('enter', None, 'bench_right')
		remove_location_object('enter', None, 'lamp')
		remove_location_object('enter', None, 'uv_dream')
		remove_location_object('enter', None, 'fog')
		
		unban_exit('enter')

init 10 python:
	flat_snowfall_params = dict(
		name = 'snowfall',
		background = im.rect('#68B'),
		image = im.rect('#FFF'),
		count = 100,
	)
	add_location_object('flat', 'window', ParticleFactory, **flat_snowfall_params)
	
	add_location_object('flat', 'dress_place', 'dress')
	
	flat_monitor = get_location_objects('flat', None, 'monitor')[0]
	flat_monitor.start_animation('main', -1)
	
	
	def flat_lamp_light_update(lamp_light):
		min = 0.15
		max = 0.30
		half_period = 1.5
		speed = (max - min) / half_period
		
		if 'dalpha' not in lamp_light:
			lamp_light.dalpha = speed
		
		lamp_light.alpha += lamp_light.dalpha * get_last_tick()
		
		if lamp_light.alpha >= max:
			lamp_light.alpha = max
			lamp_light.dalpha = -speed
		if lamp_light.alpha <= min:
			lamp_light.alpha = min
			lamp_light.dalpha = speed
	
	flat_lamp_light = get_location_objects('flat', None, 'lamp_light')[0]
	flat_lamp_light.user_function = flat_lamp_light_update
	
	
	dust_params = dict(
		name = 'dust',
		image = im.rect('#8888'),
		count = 20,
		zorder = 1e5,
		min_dx = -0.01,
		max_dx = 0.02,
		min_dy = 0.1,
		max_dy = 0.5,
		min_size = 0.5,
		max_size = 1,
	)
	add_location_object('flat', 'dust_place', ParticleFactory, **dust_params)
	
	
	liaz_light_far_params = dict(
		name = 'light_far',
		image = 'images/locations/liaz/objects/light_far',
		dx = 0.0,
		dy = 0.0,
		zorder = -2
	)
	liaz_light_close_params = dict(
		name = 'light_close',
		image = 'images/locations/liaz/objects/light_close',
		dx = 0.0,
		dy = 0.0,
		zorder = -1
	)
	liaz_light_far   = add_location_object('liaz', 'lights_place', ScrollObject, **liaz_light_far_params)
	liaz_light_close = add_location_object('liaz', 'lights_place', ScrollObject, **liaz_light_close_params)
	
	station_snow_free = 'images/locations/station/objects/snow_free'
	station_snowfall_params = dict(
		name = 'station_snowfall',
		free = station_snow_free,
		count = 200,
	)
	place = { 'x': 0, 'y': 0, 'xsize': get_image_width(station_snow_free), 'ysize': get_image_height(station_snow_free) }
	add_location_object('station', place, SnowfallLocation, **station_snowfall_params)


label forgot_things:
	$ set_rpg_control(False)
	narrator random.choice([
		"Кажется, я что-то забыл.",
		"Карманы ощущаются слишком лёгкими, нужно проверить, вдруг забыл что-то.",
		"Не помешает проверить карманы... Блин, чего-то не хватает.",
		"Я точно всё взял?",
	])
	window hide
	$ set_rpg_control(True)


label day0_start:
	scene bg black
	python:
		clock.day = 0
		set_run_allow(False)
		day0_dream_set()
		location_cutscene_on(0, zoom = 1, obj = 'square_down')
	
	python:
		sprites.hide('bg with Dissolve(5)'.split(' '))
		cam_to('square_center', 5, zoom = 1)
	
	"Мне опять снился сон..."
	"Я сижу на скамейке перед приоткрытыми железными воротами."
	"Странно, но в последнее время только во время этого сна я ощущаю себя живым."
	"Проснёшься - и сон забудется, но пока ещё спишь - осознаёшь своё глупое положение от того, что не сможешь удержать все эти образы в голове после пробуждения."
	"Пусть здесь и лето, из-за тумана чувствуется лёгкий озноб."
	"Но сейчас мне комфортно настолько, что даже боюсь, что усну во сне."
	"Я чуть поднимаю взгляд над воротами."
	
	$ cam_to('behind_gates', 2, zoom = 1)
	
	"«Совёнок»? Как сова, но маленькая..."
	"В любом случае, я лишь наблюдаю."
	"При всём желании взять с собой сувенир не получится."
	"Что ни говори, а ночь здесь прекрасна."
	"Прям как в сказках описывают."
	"Но не может же быть все так идеально, в самом деле?"
	"Конечно не может, ведь это - сон."
	"Всего лишь сон..."
	"Что же. Скоро просыпаться, так почему бы не осмотреться здесь получше?.."
	
	$ location_cutscene_off(1, obj = me)
	"[[Управление: WASD, шаг/бег: Shift, сесть/встать: Z]"
	$ set_rpg_control(True)
	window hide
	# Свободное время, сон заканчивается, если подойти к воротам


label day0__enter__before_gates_close:
	stop music fadeout 3
	scene bg black with dissolve2
	$ hide_location()
	$ day0_dream_unset()
	
	pause 3
	play sound_loop sfx['computer_noise'] fadein 2
	pause 1
	
	$ prologue_k = 217 / 155
	$ prologue_size = (0.2, 0.2 * get_from_hard_config('window_w_div_h', float) / prologue_k)
	
	show prologue_sleep with dissolve:
		anchor (0.5, 0.5)
		pos (0.25, 0.33)
		size prologue_size
	pause 3
	play sound sfx['mystery_movement']
	pause 1
	
	show prologue_wake with dissolve:
		anchor (0.5, 0.5)
		pos (0.50, 0.33)
		size prologue_size
	pause 3
	
	play sound_loop sfx['keyboard_mouse_computer_noise'] fadein 1
	pause 1
	show prologue_keyboard with dissolve:
		anchor (0.5, 0.5)
		pos (0.75, 0.33)
		size prologue_size
	pause 4
	
	show prologue_monitor with dissolve:
		anchor (0.5, 0.5)
		pos (0.33, 0.66)
		size prologue_size
	pause 5
	play sound sfx['message']
	show prologue_message with dissolve:
		anchor (0.5, 0.5)
		pos (0.66 - prologue_size[0] * (1.5 - 1) * 0.5, 0.66 + prologue_size[1] * (1.5 - 1) * 0.5)
		size (prologue_size[0] * 1.5, prologue_size[1] * 1.5)
	pause 8
	
	scene bg black with dissolve2
	python:
		set_rpg_control(False)
		set_location('flat', 'armchair_pos')
		me.x += 10
		me.set_direction(to_forward)
		armchair = get_near_sit_objects(me)[0][0]
		me.sit_down(armchair)
	hide bg with dissolve
	
	"Пару дней назад мне неожиданно написал бывший однокурсник."
	"Один из немногих, с кем я хоть и изредка, но поддерживал связь."
	"Он позвал меня на встречу выпускников." 
	"Мне не хотелось никуда идти, но и обижать его тоже не хотелось, поэтому я не дал чёткого ответа." 
	"Имиджборды, в каком-то плане, заменили мне друзей на некоторое время, но сейчас я понимаю, что начинаю от них уставать." 
	"Может быть, мне правда стоит сходить туда?" 
	"Другого шанса не будет, нужно решать сейчас."
	"Я пролистываю посты, и на душе становится тоскливее от осознания, что одну и ту же картину я вижу изо дня в день каждый раз." 
	"Мой распорядок дня не меняется уже пару лет." 
	"Думаю, мне правда стоит поехать, чтобы вырваться из этого «Дня Сурка»."
	"Осталось собрать вещи, одеться и выйти."
	
	$ quest_start('taking_objects')
	window hide
	
	play sound_loop sfx['computer_noise']
	$ flat_monitor.remove_animation()
	$ me.move_to_place('computer')
	$ me.move_to_place('center')
	
	$ set_rpg_control(True)
	# Свободный режим, требуется собрать необходимые предметы


label day0__flat__bed:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	if not inventory.has('phone') and not get_location_objects('flat', None, 'phone'):
		"Итак, телефон найден."
		$ inventory.add('phone', 1)
		call day0_check_items
	else:
		narrator random.choice([
			"О да, любимый портал в царство Морфея.",
			"Представляю вам мою Единственную и Неповторимую - Кровать!",
			"Пружины поскрипывают уже, ну да ладно.",
		])
	window hide
	$ set_rpg_control(True)

label day0__flat__computer:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	if not inventory.has('lighter') and not get_location_objects('flat', None, 'lighter'):
		"Зажигалка. Может, взять её?"
		$ inventory.add('lighter', 1)
		call day0_check_items
	else:
		narrator random.choice([
			"Хм. И зачем мне этот старый монитор на столе?",
			"Сотни и тысячи часов последних лет моей жизни проведены именно здесь.",
			'"Добро пожаловать. Снова."',
		])
	window hide
	$ set_rpg_control(True)

label day0__flat__table:
	if rpg_event != 'action':
		return
	
	$ set_rpg_control(False)
	$ has_flat_keys = inventory.has('flat_keys') or get_location_objects('flat', None, 'flat_keys')
	$ has_notepad   = inventory.has('notepad')   or get_location_objects('flat', None, 'notepad')
	if not has_flat_keys and not has_notepad:
		"Вот и ключи. И блокнот. Возьму его на всякий случай, вместе с ручкой."
	if not has_flat_keys:
		$ inventory.add('flat_keys', 1)
	if not has_notepad:
		$ inventory.add('notepad', 1)
	call day0_check_items
	window hide
	$ set_rpg_control(True)

label day0__flat__*:
	if rpg_event == 'take':
		call day0_check_items

label day0_check_items:
	if quest_started('taking_objects') and inventory.has('phone') and inventory.has('flat_keys') and inventory.has('notepad'):
		$ quest_end('taking_objects')


label day0__flat__to_dress:
	if rpg_event != 'action':
		return
	
	if quest_started('taking_objects'):
		call forgot_things
		return
	
	if me.get_dress() != 'winter':
		scene bg black with dissolve
		$ me.set_dress('winter')
		$ remove_location_object('flat', None, 'dress')
		hide bg with dissolve
	else:
		$ set_rpg_control(False)
		"В принципе, выбор что надеть был невелик."
		"Хоть есть что-то по погоде - и на том спасибо."
		window hide
		$ set_rpg_control(True)

label day0__flat__exit:
	if rpg_event != 'action' or not me.get_dress() == 'winter':
		return
	if not inventory.has('phone') or not inventory.has('flat_keys') or not inventory.has('notepad'):
		call forgot_things
		return
	
	scene bg black with dissolve
	stop sound_loop fadeout 1
	pause 1
	play sound sfx['close_door']
	pause 1
	$ set_location('station', 'station_enter')
	hide bg with dissolve

label day0__station__before_stop:
	$ set_rpg_control(False)
	$ me.set_direction(to_right)
	
	"Осталось дождаться автобуса."
	"Пока сюда шёл, успел замёрзнуть."
	"Даже промелькнула мысль развернуться обратно, и никуда не ехать."
	"Но я тут же откинул её, ведь я уже на полпути."
	"Было бы глупо, что-то начать, и не довести до конца."
	"Хотя я столько раз так делал..."
	window hide
	
	scene bg black with dissolve2
	$ add_location_object('station', 'liaz_place', 'liaz')
	play sound sfx['bus_door_open']
	hide bg with dissolve
	
	$ me.move_to_place('liaz_enter')
	$ set_location('liaz', 'liaz_enter')
	$ set_rpg_control(True)
	play sound_loop sfx['bus_idle'] fadein 1

label day0__liaz__*:
	if rpg_event != 'sit_down':
		return
	
	$ set_rpg_control(False)
	$ set_run_allow(True)
	
	play sound sfx['bus_door_close']
	pause 1
	play sound_loop sfx['bus_interior_moving'] fadein 1
	
	$ liaz_light_far.set_direction(-0.1, 0)
	$ liaz_light_close.set_direction(-0.5, 0)
	
	"Выбрав, наверно, самое тёплое место в автобусе, я начал поглядывать на мелькающие огни за заснеженным окном."
	"Зима уже не близко - она уже здесь."
	"И особенно хорошо это проявляется в этом старом Лиазе, где об обогревателях, наверно, можно только грезить."
	"Если честно, думал их уже давно сняли со всех маршрутов, но оказывается - нет, парочка осталась."
	"Через несколько лет этот автобус, наверно, станет достоянием любителей автомобильной археологи."
	"..."
	window hide
	
	scene bg black with dissolve
	hide bg with dissolve
	
	"Интересно, кто сидел на этом месте до меня?"
	"Может какая-нибудь милая красивая девушка? {w}Не, не думаю."
	"Милые и особенно красивые девушки не ездят на автобусах."
	"На автобусах ездим мы - студенты, работяги, старушки и наркоманы."
	"И как ни странно, я не отношусь ни к какой из этих групп. {w}Я ведь уже не студент."
	"Хотя если бы не ленился, то может быть и получил бы высшее образование, а не был бы выгнан за прогулы."
	"..."
	window hide
	
	scene bg black with dissolve
	hide bg with dissolve
	
	"Я заметил, что у меня начинают слипаться глаза."
	"Вроде проспал весь день, но все ещё хочется."
	"Странная штука организм."
	"Ехать ещё долго, так что можно и вздремнуть несколько минут."
	"Я прикрываю глаза..."
	"..."
	window hide
	
	scene bg black with dissolve2
	stop sound_loop fadeout 2
	pause 2
	$ show_presents()
	$ hide_presents()
	stop music fadeout 1
	pause 2
	
	call day1_start
