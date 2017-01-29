label set_day1_morning_sl_actions:
	actions sl:
		dress sl in "pioneer"    									# Установить Славе пионерскую форму
		tp sl to "Ворота" in "Клубы"								# Поместить её к месту "Ворота" в локации "Клубы"
		wait person_in_place(me, "Ворота", "Ворота")				# Ждать, пока Семён не подойдёт к воротам в локации "Ворота"
		
		move sl to me            									# Подойти к Семёну 
		jump start_dialog											# Перейти на метку сценария start_dialog (где начальный разговор)
		wait text_ended()											# Ждать (т. е. стоять и ничего не делать), пока не закончится диалог
		
		anim sl is "Славя машет рукой"      						# Показать анимацию махания рукой
		pause 1.0					    							# А через секунду
		anim sl is None												# Убрать её (анимацию)
		
		move sl to "Переодевалка" in "Лодочная станция"     		# Идти в переодевалку в локации "Берег"
		pause 5.0   												# Ждать 5 секунд
		dress sl in "swim"  										# Сменить форму на купальник
		move sl to "Место купания-1" in "Лодочная станция"      	# Зайти в воду
		
		wait person_in_location(me, "Лодочная станция")				# Ждать, пока Семён не придёт в локацию "Берег"
		
		# Если Семён вообще не придёт сюда,
		#  то дальнейший код так и не будет достигнут
		
		jump fix_first_error										# "Ой, так тебе не сюда...Я Славя...Погоди, я переоденусь..."
		wait text_ended()
		
		$ control = False											# Запретить игроку управлять Семёном
		move me to "Мост" in "Лодочная станция" without waiting:    # Отправить Семёна к мосту без ожидания окончания ходьбы для текущих действий
    		anim me is "Семён плескает ноги в воде"                 # После того, как Семён подойдёт, включить анимацию
		
		move sl to "Переодевалка" in "Лодочная станция"
		pause 5.0
		dress sl in "pioneer"
		move sl to me
		
		jump fix_first_error_2      								# "Пошли?"
		wait textEnded()
		
		anim me is None
		aim me is sl  												# Семён следует за Славей
		
		move sl to "Генда" in "Площадь"
		if see(sl, dv) and see(sl, us):								# Если Славя видит Алису и Ульяну на площади
			jump must_not_run										# "Ульяна, не бегать!...Есть, гржднин начник!"
			wait text_ended()
		
		move sl to "Домик ОД" in "Домики 1-17"
		$ control = True											# Возврат контроля Семёном игроку
		aim me is None     											# Никого не преследовать
		jump meet_mt
		wait textEnded()
		
		move sl to "Переодевалка" in "Лодочная станция"
		pause 5.0
		dress sl in "swim"
		move sl to "Место купания-1" in "Лодочная станция"
	
	
	pre_canteen_actions sl:											# Действия при горне (сигнал к приёму пищи)
		move sl to "Переодевалка" in "Лодочная станция"
		pause 5.0
		dress sl in "pioneer"
	
	canteen_actions sl:												# Действия после предыдущих приготовлений
		move sl to "Место Слави" in "Столовая"
		rotation sl is sl_canteen_rotation
