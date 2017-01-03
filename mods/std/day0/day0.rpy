label prologue:
	$ set_fps(30)
	
	$ me.set_dress('wn')
	
#	jump end_sleep
	
	$ make_names_unknown()
	$ set_mode_adv()
	
	scene anim prolog_1
	play music music_list["a_promise_from_distant_days_v2"] fadein 3
	
	window show
	"{i}Этот{/i} сон..."
	"Каждую ночь одно и то же."
	"Но наутро, как обычно, всё забудется."
	"Может быть, оно и к лучшему..."
	"Останутся только туманные воспоминания о приоткрытых, словно приглашающих куда-то воротах, рядом с которыми в камне застыли два пионера."
	"А ещё странная девочка...{w} которая постоянно спрашивает:"
	scene bg ext_camp_entrance_night
	dreamgirl "Ты пойдёшь со мной?"
	"Пойду?.."
	"Но куда?"
	"И зачем?.."
	"Да и где я вообще нахожусь?"
	"Конечно, случись всё на самом деле, наяву, стоило бы непременно испугаться."
	"Как же иначе!"
	"Но это – всего лишь сон.{w} Тот самый, который я вижу каждую ночь."
	"А ведь всё это неспроста!"
	"Необязательно знать {i}где{/i} и {i}почему{/i}, чтобы понять – что-то происходит."
	"Нечто, отчаянно требующее моего внимания."
	"Ведь всё окружающее меня здесь – реально!"
	"Реально настолько, насколько реальны вещи в моей квартире; я бы мог открыть ворота, услышать скрип петель, смахнуть рукой осыпающуюся ржавчину, потянуть носом свежий прохладный воздух и поёжиться от холода."
	"Мог бы, но для этого надо сдвинуться с места, сделать шаг, пошевелить рукой..."
	"А ведь это сон – я понимаю, но что дальше, что изменит моё {i}понимание{/i}?"
	"Ведь здесь – словно по ту сторону потрескавшегося экрана старого телевизора, который из последних сил борется с помехами и силится показать зрителям всё, не упустив ни малейшей детали."
	"Но вот картинка теряет чёткость...{w} Наверное, скоро просыпаться."
	"..."
	"Может быть, спросить у неё что-то?{w} У девочки."
	"Как же её зовут..."
	"Например про звёзды..."
	"Хотя почему про звёзды?"
	"Можно же спросить про ворота!{w} Да, про ворота!"
	"Вот она удивится."
	"Или лучше про букву {i}ё{/i}."
	"Хорошая была буква..."
	"Как будто её больше нет!"
	"И какое отношение буквы, ворота и звёзды имеют к этому месту?"
	"Ведь если мне каждую ночь снится {i}этот{/i} сон, который потом всё равно забудется, надо искать разгадку здесь и сейчас!"
	"А вот, если присмотреться, можно увидеть Магелланово Облако..."
	"Словно попал в южное полушарие!"
	"..."
	"Во сне всегда больше волнуют мелочи: неестественный цвет травы, невозможная кривизна прямых или своё перекошенное отражение – а реальная опасность, готовая оборвать всё здесь и сейчас, кажется пустяком."
	"Естественно, ведь {i}здесь{/i} нельзя умереть."
	"Я точно знаю – я делал это сотни раз."
	"Но если нельзя умереть, нет смысла жить?"
	"Надо будет спросить у девочки: она местная – должна знать!"
	"Да, именно!{w} Спросить, например, про сову."
	"Больно уж птица странная..."
	"А впрочем, неважно..."
	"..."
	dreamgirl "Ты пойдёшь со мной?"
	"И каждый раз надо отвечать."
	"Иначе никак, иначе сон не закончится, а я – не проснусь."
	window hide
	pause 0.5
	menu:
		"Да, я пойду с тобой":
		    $ prologue = 1
		"Нет, я останусь здесь":
		    pass
	pause 0.5
	window show
	"Каждый раз так сложно решить, что же ответить."
	"Где я, что я здесь делаю, кто она такая?"
	"И почему от ответа на этот вопрос зависит так много в моей жизни?"
	"Или не зависит?.."
	"Ведь это просто сон..."
	"Просто сон..."
	stop music fadeout 2
	
	jump end_sleep


label end_sleep:
	$ me.set_direction(forward)
	$ me.set_pose("sit")
	$ set_location("Квартира", "Кресло")
	play sound_loop sfx_keyboard_mouse_computer_noise fadein 3
	scene

	"Экран монитора смотрел на меня словно живой."
	"Иногда мне правда казалось, что он обладает сознанием, своими мыслями и желаниями, стремлениями; умеет чувствовать, любить и страдать."
	"Словно в наших отношениях инструмент не он – неодушевлённый кусок пластика и текстолита, – а я."
	"Наверное, в этом есть доля правды, ведь компьютер на 90% обеспечивает моё общение с внешним миром."
	"Анонимные имиджборды, иногда какие-то чаты, редко – аська или джаббер, ещё реже – форумы."
	window hide
	pause 2
	window show
	"А людей, сидящих по ту сторону сетевого кабеля, попросту не существует!"
	"Все они – всего лишь плод его больной фантазии, ошибка в программном коде или баг ядра, зажившего собственной жизнью."
	window hide
	pause 3
	scene anim prolog_15
	with fade
	pause 3
	scene anim prolog_3
	with fade
	pause 3
	scene anim prolog_4
	with fade
	pause 3
	stop sound_loop fadeout 4
	window show
	"Если посмотреть со стороны на моё существование, то такие мысли покажутся не столь уж бредовыми, а какой-нибудь психолог наверняка поставит мне кучу заумных диагнозов и, возможно, выпишет направление в жёлтый дом."
	window hide
	pause 3
	scene anim prolog_5
	with fade
	pause 3
	scene anim prolog_14
	with fade
	pause 3
	scene anim prolog_11
	with fade
	pause 3
	window show
	"Маленькая квартирка без следов какого бы то ни было ремонта или даже подобия порядка, и вечно одинаковый вид из окна на серый, день и ночь куда-то бегущий мегаполис, – вот условия моей жизни."
	window hide
	play music music_list["farewell_to_the_past_edit"] fadein 5
	scene anim prolog_2
	with fade
	$ set_mode_nvl()
	window show
	"Конечно, всё начиналось не так..."
	"Я родился, пошёл в школу, закончил её – всё как у людей."
	"Поступил в институт, где кое-как промучился полтора курса."
	"Работал на паре-тройке разных работ.{w} Иногда даже и неплохо, иногда даже получая за это достойные деньги."
	"Однако всё это казалось чужим, словно списанным с биографии другого человека."
	"Я не ощущал полноту жизни – она словно зациклилась и продолжала идти по кругу.{w} Как в фильме «День сурка»."
	"Только у меня не было выбора, как именно провести этот день, и каждый раз всё повторялось по одной и той же схеме.{w} Схеме пустоты, уныния и отчаяния."
	nvl clear
	window hide
	pause 2
	window show
	"Последние несколько лет я просто целыми днями сидел за компьютером."
	"Иногда подворачивались какие-то халтурки, иногда помогали родители."
	"В общем, на жизнь хватало."
	"Это и немудрено, ведь потребности у меня небольшие."
	"На улицу я практически не выхожу, а всё моё общение с людьми сводится к интернет-переписке с {i}анонимами{/i}, у которых нет ни реального имени, ни пола, ни возраста."
	"Короче говоря, достаточно типичная жизнь достаточно типичного асоциального человека своего времени.{w} Этакий Обломов XXI века."
	"Может быть, маститый писатель напишет обо мне роман, который станет классикой современной литературы.{w} Или напишу я сам..."
	"Впрочем нет, что себя обманывать – уже не раз пытался, но меня не хватало даже на короткий рассказ."
	nvl clear
	"Изучал я и множество других вещей."
	"Рисовать – не дано от природы.{w} Программирование – надоело.{w} Иностранные языки – долго и скучно..."
	"Любил я разве что читать, но даже при этом никогда бы не назвал себя эрудированным человеком."
	"Возможно, я был асом в просмотре аниме и гроссмейстером неумелых шуточек в интернете."
	"Плати мне за это деньги, я бы обрадовался (да и заработал неплохо), но вряд ли так просто можно заполнить пустоту в душе."
	nvl clear
	window hide
	scene bg semen_room_window
	with fade
	stop music fadeout 4
	play sound_loop sfx_street_traffic_outside fadein 2
	window show
	"Сегодня очередной типичный день моей типичной жизни типичного неудачника."
	"И именно сегодня мне нужно ехать на встречу институтских товарищей."
	"По правде говоря, совершенно не хотелось."
	"Да и какой смысл, если вместе с ними я отучился всего ничего?"
	"Однако меня всё же уговорил друг, бывший одногруппник, один из немногих, с кем я поддерживал контакт не только в интернете."
	window hide
	pause 4
	stop sound_loop fadeout 3
	play ambience ambience_cold_wind_loop fadein 3
	$ set_mode_adv()
	play sound sfx_intro_bus_stop_steps
	scene anim intro_1
	with fade
	pause 3
	scene anim intro_2
	with fade
	pause 3
	scene anim intro_3
	with fade
	pause 3
	scene anim intro_4
	with fade
	pause 3
	scene anim intro_5
	with fade
	pause 3
	scene anim intro_6
	with fade
	pause 3
	play sound sfx_intro_bus_stop_sigh
	scene anim intro_8
	with fade
	pause 3
	scene anim intro_7
	with fade
	pause 3
	scene bg bus_stop
	with fade
	
	jump bus_station


label bus_station:
	scene
	$ set_location("Остановка", "Начало")
	$ me.set_direction(back)
	$ me.move_to_place("Остановка", False)
	$ me.set_direction(right)
	
	window show
	"Вечер. Мороз.{w} Остановка и ожидание автобуса."
	"Я никогда не любил зиму.{w} Впрочем, и жаркое лето – тоже не моя стихия."
	"Просто не вижу смысла выделять какое-то одно время года – не столь важно, какая погода на улице, если ты целыми днями сидишь дома."
	"Автобус сегодня задерживался так сильно, что я уже был готов плюнуть на всё и потратить последнюю пару сотен на такси (совсем не ехать мне почему-то в голову не пришло)."
	"В мозгу, как всегда, роились миллионы мыслей, из которых совершенно невозможно выудить хотя бы одну стоящую."
	"Такую, которую можно закончить, привести в порядок, облечь в форму идеи и претворить в жизнь."
	"Может быть, заняться бизнесом?{w} Но откуда я возьму деньги?"
	"Или пойти опять работать в офис?{w} Нет уж!"
	"Может, стоит попробовать фриланс?{w} Да что я умею, и кому я нужен..."
	window hide
	pause 3
	scene anim prolog_2
	with fade
	pause 1
	$ set_mode_nvl()
	window show
	"Вдруг мне вспомнилось детство...{w} Или скорее юношество – 15-17 лет."
	"Почему именно это время?{w} Не знаю."
	"Наверное, потому что тогда всё было проще."
	"Было проще принимать такие сложные сейчас и такие простые тогда решения."
	"Проснувшись с утра, я чётко знал, как пройдёт мой день, а выходных ждал с нетерпением – смогу отдохнуть, заняться любимыми делами: компьютер, футбол, встречи с друзьями."
	"А потом, когда наступит новая неделя, вновь примусь за учёбу."
	"Ведь раньше не возникало этих мучительных вопросов «зачем», «кому это надо», «что изменится, если я это сделаю» или «что не изменится»."
	"Простой поток жизни, такой привычный для любого нормального человека и такой чуждый для меня теперешнего."
	nvl clear
	"Время беззаботного детства...{w} Тогда же я и встретил свою первую любовь."
	"Стёрлись из памяти её внешность, характер."
	"Как строчка из профиля в социальной сети осталось лишь имя, да те чувства, которые захлёстывали меня, когда я был с ней.{w} Теплота, нежность, желание заботиться, защитить..."
	"Жаль, что это продолжалось так недолго."
	"Сейчас я уже с трудом могу себе представить что-то подобное."
	"Наверное, и хочется познакомиться с девушкой, только не знаю, как начать диалог, о чём вообще с ней говорить, чем её заинтересовать."
	"Да и подходящих девушек я давно не встречал.{w} Хотя где мне их встретить..."
	nvl clear
	window hide
	
	play sound sfx_intro_bus_engine_start
	pause 1
	play sound_loop sfx_intro_bus_engine_loop fadein 3
	
	$ set_map_object("Лиаз", "Место автобуса")
	scene
	
	$ set_mode_adv()
	window show
	"Звук работающего двигателя вернул меня к реальности."
	"Подъехал автобус."
	"«Какой-то он не такой» – мелькнула мысль."
	"Впрочем, какая разница – по этому маршруту ходит только 410-ый."
	window hide
	pause 1
	
	$ me.move_to_place("Вход в автобус", False)
	jump liaz

label liaz:
	$ set_location("Лиаз", "Вход")
	scene
	$ me.set_direction(forward)
	$ me.move_to_place("Перед сиденьем", False)
	$ me.set_direction(right)
	$ me.move_to_place("Сиденье", False)
	$ me.set_pose("sit")
	pause 1
	
	stop sound_loop fadeout 4
	scene bg intro_xx
	with fade
	stop ambience fadeout 2
	play sound_loop sfx_bus_interior_moving fadein 4
	window show
	"Огни пролетают мимо, их холодный свет словно зажигает внутри давно погасшие чувства."
	$ volume(0.5, "music")
	play music music_list["lightness_radio_bus"] fadein 7
	"Или не зажигает, а просто пробуждает..."
	"Ведь «они» уже давно живут во мне, то затихая, то просыпаясь вновь."
	"Какая-то очень известная мелодия играла в радиоприёмнике у водителя.{w} Но я её не слушал."
	"Я смотрел в запотевшее окно автобуса на проезжающие мимо машины."
	"Ведь люди куда-то спешат, ведь им что-то нужно, и, погружённые в свои дела, они не задумываются о вопросах, мучающих меня."
	"Наверное, у них тоже есть свои серьёзные проблемы, а может, им живётся куда легче."
	"Знать наверняка нельзя, так как все люди разные.{w} Или не разные?"
	"Бывает, поступки человека легко предсказуемы, но, пытаясь заглянуть к нему в душу, видишь лишь непроглядную тьму."
	"..."
	"Автобус приближался к центру, и мои мысли прервал яркий свет огней большого города."
	"Сотни рекламных вывесок, тысячи машин, миллионы людей."
	"Я смотрел на это светопреставление, и мне почему-то безумно захотелось спать."
	window hide
	pause 1.5
	window show
	"Глаза закрылись всего на полсекунды и..."
	stop music fadeout 2
	window hide
	stop sound_loop fadeout 3
	with fade3
	pause 3
	$ volume(1.0, "music")
	
	scene
	jump day1
