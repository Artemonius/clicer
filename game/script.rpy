init python:

    menu = nvl_menu

    style.nvl_window.xalign = 0
    style.nvl_window.ypadding = 2
    global year
    global hour
    global minutes
    global hour_text
    global minutes_text
    global weekday
    global date
    weekdays = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]
    global month
    months = [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь"
    ]
    def timeshowing():
        global minutes_show
        global hour_show
        global minutes
        global hour
        if hour < 10:
            hour_show = "0[hour]:"
        else:
            hour_show = "[hour]:"
        if minutes < 10:
            minutes_show = "0[minutes]"
        else:
            minutes_show = "[minutes]"

    global Location_items
    Location_items = []
    global Location_chars
    Location_chars = []
    global Location_name
    Location_name = "Название Локации"
    global Location_description
    Location_description = "Ваша старая комната, в которой вы прожили всю жизнь."
    global LocationCurrent
    LocationCurrent = ""

    # Статы перса
    global money
    global luck
    global arouse
    # всего отбражаемого ароуза 100, но вообще 200, просто из полного вычитается удовлетовренность.
    # т.е. чтобы возбудить полностью удовлетворенную бабу нужно набрать 200 баллов, при этом возбуждаемость работает как индес
    # т.е. если возбуждаемость 100, то любой плюс возбуждения умножается на 1, если 150, то на 1.5
    global energy  # Энергия персонажа, влияет на его активность и способность выполнять действия
    global hunger  # Голод персонажа, влияет на его настроение и здоровье
    global mood  # Настроение персонажа, влияет на его реакции и взаимодействия
    global return_label  # Метка для возвращения в домашнюю локацию
    return_label = "Home"

    global lust

    global TownSheriffWorking
    global TownDeputySheriffWorking

    global CanUse
    CanUse = False

    global richgym_work
    global richgym_ticket

    # Relationships

    global TroyWilson_rel
    global Sheriff_rel

    # +++++

    global mother_kitchen
    global father_kitchen

    global father_hall
    global mother_hall

    # Система отслеживания изменений статов для анимации
    global stat_changes
    stat_changes = {}

    # Активные анимации шаров
    global active_ball_animations
    active_ball_animations = []

    # Счетчик для уникальных ID анимаций
    global anim_counter
    anim_counter = 0

    def ClearThings():
        global Location_items
        del Location_items[:]
        Location_items[:] = []

    def CanUseChange(NewCan):
        global CanUse
        CanUse = NewCan





    def CheckMood():
        global mood
        if mood > 100:
            mood = 100
        if mood < 0:
            mood = 0
            
    def Sleep():
        global hour
        if hour >= 18:
            AddMinutes(360)
        hour = 8
        minutes = 0
        CheckTime()
        if hunger > 0:
            AddEnergy(100)
        AddMood(20)
        AddHunger(-30)

    def AddStats(stat_name, value):
        """
        Универсальная функция для изменения всех статов с анимацией
        """
        global energy, mood, hunger, hygiene, arouse, arouse_def, lust, satisfaction
        global stat_changes

        # Обновляем значение стата
        if stat_name == "energy":
            energy += value
            if energy > 100: energy = 100
            if energy < 0: energy = 0
        elif stat_name == "mood":
            mood += value
            CheckMood()
        elif stat_name == "hunger":
            hunger += value
            if hunger > 100: hunger = 100
            if hunger < 0: hunger = 0
        elif stat_name == "hygiene":
            hygiene += value
            if hygiene > 100: hygiene = 100
            if hygiene < 0: hygiene = 0
        elif stat_name == "arouse":
            arouse += value
            if arouse < 0: arouse = 0
            if arouse > 100: arouse = 100
        elif stat_name == "lust":
            lust += value
            if lust > 100: lust = 100
            if lust < 0: lust = 0
        elif stat_name == "new_value_test":
            new_value_test += value
            if new_value_test > 100: new_value_test = 100
            if new_value_test < 0: new_value_test = 0

        # Сохраняем изменение для отображения +/-
        if value != 0:
            stat_changes[stat_name] = value

            # Добавляем анимацию в список активных
            global anim_counter, active_ball_animations
            import time
            anim_counter += 1

            # Выбираем картинку
            if value > 0:
                ball_img = "images/balls2.png"
            else:
                ball_img = "images/balls.png"

            # Выбираем transform
            if stat_name in ["hunger", "mood"]:
                transform_name = "balls_fly_up"
            elif stat_name in ["energy", "arouse"]:
                transform_name = "balls_fly_left_up"
            elif stat_name in ["hygiene", "new_value_test"]:
                transform_name = "balls_fly_right_up"
            else:
                transform_name = "balls_fly_up"

            # Добавляем в список активных анимаций
            active_ball_animations.append({
                'id': anim_counter,
                'image': ball_img,
                'transform': transform_name,
                'start_time': time.time()
            })

    def CheckMagic():
        global magic_roll, magic_chance
        # Увеличиваем шанс каждый раз при проверке
        if renpy.random.randint(0, 100) < magic_chance:
            magic_roll = True
        else:
            magic_roll = False
            # Увеличиваем шанс на следующую проверку
            magic_chance += 10
        if magic_chance == 100 or magic_chance == 90:
            magic_chance = 0
                
    def ResetMagic():
        global magic_roll
        magic_roll = False



    def CheckNewDayVariables():
        global physique
        global richgym_ticket 
        physique -= 1
        if richgym_ticket > 0:
            richgym_ticket -= 1

    def AddMinutes(min): #чтобы добавить час нужно добавить 60 минут
        global minutes
        global energy
        minutes += min
        energy -= min*0.08
        CheckTime()



    def CheckTime():
        global minutes
        global hour
        global weekday
        global date
        global month
        while minutes >= 60:
            minutes -= 60
            hour += 1
        if hour > 23:
            hour -= 24
            CheckNewDayVariables()
            if weekdays.index(weekday) > 7:
                weekday = weekdays[0]
            else:
                weekday = weekdays[weekdays.index(weekday) + 1]
            date += 1
            if date > 30:
                month = months[months.index(month) + 1]
                date = 1
        timeshowing()
        #if weekday.index > 7:
        #    weekday = weekday[1]


    class UseThing(object):
        def __init__(self, name, Label):
            self.name = name
            self.Label = Label
            
        def action():
            renpy.jump(self.Label)

    
    
define shower = UseThing("Душ", "TakingShower")
define HomeBath = UseThing("Ванна", "TakingBath")
define HomeFridge = UseThing("Холодильник", "HomeFridge")
define HomeBathMirror = UseThing("Зеркало", "HomeMirrorBath")
define HomePC = UseThing("Компьютер", "HomePc")
define HomeBed = UseThing("", "")
define HallSofa = UseThing("", "")
define HallTv = UseThing("", "")


screen main_screen3:
    zorder 10
    add "images/mainscreen.png"
    text "[location]" xalign 0.38 ypos 740 color "#ffffff" size 26

screen main_screen:
    add "images/[scim].png"
    vbox:
        xalign 0.05 
        yalign 0.95
        text "text text {a=jump:ss1} jump {/a}" color "#ffffff"
        text "text text text {a=jump:ss2} jump {/a}" color "#ffffff"
        text "[sctext]" color "#ffffff"

screen main_screen2:
    add "images/[scim].png"
    vbox:
        xalign 0.55 
        yalign 0.5
        text "text text {a=jump:ss1} jump {/a}" color "#ffffff"
        text "text text text {a=jump:ss2} jump {/a}" color "#ffffff"
        text "[sctext]" color "#ffffff"
# Изображения для анимации статов
# Простые круглые шары для анимации (можно заменить на свои изображения)
image balls_placeholder = Solid("#FF0000", xysize=(30, 30))  # Красный круг для убавления
image balls2_placeholder = Solid("#00FF00", xysize=(30, 30))  # Зеленый круг для прибавления

# Если у вас есть свои изображения, раскомментируйте строки ниже и закомментируйте выше:
# image balls = "images/balls.png"
# image balls2 = "images/balls2.png"

#здесь лежат image и можно добавлять видео
image minet_bar = Movie(play="blowjob_bar_1.webm")
image minet_bar_2 = Movie(play="blowjob_bar_2.webm")
image minet_bar_3 = Movie(play="blowjob_bar_3.webm")
image minet_bar_4 = Movie(play="blowjob_bar_4.webm")
image minet_in_car = Movie(play="Minet_in_car.webm")
image minet_in_motel = Movie(play="minet_in_motel.webm")
image minet_in_bar_podsob = Movie(play="minet_in_bar_podsob.webm")
image minet_in_pikap = Movie(play="minet_in_pikap.webm")
image minet_in_pikap_2 = Movie(play="minet_in_pikap_2.webm")
image minet_in_forest = Movie(play="minet_in_forest.webm")
image pikap_1 = Movie(play="pikap_1.webm")
image pikap_2 = Movie(play="pikap_2.webm")
image pikap_3 = Movie(play="pikap_3.webm")


define e = Character("Eileen")
define narrator = nvl_narrator
define img = "fon.png"
# The game starts here.

label start:
    $ character = 1
    $ character_menu = 0
    $ inventory_menu = 0
    $ journal_menu = 0
    $ money = 500
    $ relationship = 0
    $ physique = 50
    default new_value_test = 50
    default gym_membership = 0
    #CityCenter
    default CityCenter_Bar_waiterjob = 0 #доступность работы официанткой в баре
    default BigCityCenter_NightClub_waiterjob = 0 #доступность работы официанткой в ночном клубе
    default CityCenter_Bar_waiterjob_salary_raise = 1 #повышение зарплаты
    default CityCenter_Bar_waiterjob_worked_shifts = 0 #счетчик смен в баре
    default CityCenter_Bar_waiterjob_salary = 50  # Базовая зарплата
    default bar_boss_description_revealed = False # Показано ли описание начальницы бара в баре
    default skill_administrator = 0 # Навык администратора салона красоты
    default skill_manicurist = 0 # Навык маникюрщицы
    default skill_hairdresser = 0 # Навык парикмахерши
    default skill_depilator = 0 # Навык депиляторши
    default salon_administrator_job = False # Работа администратором салона красоты
    default salon_manicurist_job = False # Работа маникюрщицей
    default salon_hairdresser_job = False # Работа парикмахершей
    default salon_depilator_job = False # Работа депиляторшей
    default win_chance = 0
    default win_amount = 0
    default met_girl_in_bar = False
    default strip_dancer_job = 0 # работа стриптизершей в центре города
    default strip_waiter_job = 0 # работа официанткой в стрипбаре
    #CityPoorDistrict
    default BigCityPoorDistrict_Gym_Subscription = 0
    default BigCityPoorDistrict_MyApartament = 0
    default BigCityPoorDistrict_MyApartamentRent = 0
    default LittleTown_Cinema_Ticket = False #типа хрень для билета в кино в пригороде
    default Poor_District_Cinema_Ticket = False
    #CityEntrance
    default BigCityEntrance_Bar_waiterjob = False
    default BigCityEntrance_CarCenter_AddJob = 0
    default BigCityEntrance_Motel_CleanerJob = False
    default BigCityEntrance_Motel_RoomRent = 0
    default Job_Entrance_CarCenter = False
    #CityOffices
    default BigCityOffices_CallCenter_CallJob = 0
    default BigCityOffices_Cafe_WaiterWork = False
    default officer_Poor_District = False
    default blacker = False
    default RichApartments = 0
    default met_zhir = 0 #короче если будем развивать ветку наркоты то это скорее всего будут отношения с наркбоссом
    default hasCityCenterApartment = False
    #CityRich
    # Home
    default check_bar_minet = 0
    default party_event_home = 0
    # Добавляем переменные для отслеживания знакомств в баре
    default bar_rick_known = 0  # 0 - не знакомы, 1 - знакомы, 2 - был интим
    default bar_mike_known = 0  # 0 - не знакомы, 1 - знакомы, 2 - был интим
    default bar_alex_known = 0  # 0 - не знакомы, 1 - знакомы, 2 - был интим
    default bar_toni_known = 0  # 0 - не знакомы, 1 - знакомы, 2 - был интим
    default bar_frank_known = 0  # 0 - не знакомы, 1 - знакомы, 2 - был интим
    default bar_mark_dave_known = 0  # 0 - не знакомы, 1 - знакомы, 2 - был интим
    default cole_dead = False #жив ли коул
    #want
    default want_fame = False # хочет славы
    default want_macbook = False # хочет макбук
    default want_airpods = False # хочет аирподс
    default want_ipad = False # хочет айпад
    default want_perfume = False # хочет духи
    default want_makeup = False # хочет косметику
    default want_pizza = False # хочет пиццу
    default want_burger = False # хочет бургер
    default want_iphone = False # хочет iphone
    # time 
    $ year = 2020
    $ hour_show = "08:"
    $ minutes_show = "00"
    $ hour = 8
    $ minutes = 0
    $ weekday = weekdays[1]
    $ month = months[6]
    $ date = 11
    
    # stats
    
    $ energy = 70 # энергия 
    $ mood = 80 # настроение
    $ hunger = 60 # голод
    $ hygiene = 100 # прямо сейчас воняет от нее или нет
    

    $ arouse = 0 # именно непосредственно возбужденность
    $ arouse_def = 0
    $ satisfaction = 0 # удовлетворенность, т.е. как давно у нее был секс
    
    $ lust = 0 # развращенность. Влияет на то, что она готова сделать.
    $ blowjob_master = 0 # ее уменя в минете
    $ sex_master = 0 # ее уменя в сексе
    $ v_size = 1 # размер вагины 0 - 10
    $ an_size = 0 # вместимость анала 0 - 10
    $ magic_roll = False
    $ magic_chance = 0 # начальный шанс случайного события
    # attributies
    
    $ overall_handy = 40 # 0-100, где 100 - супершикарная баба, а 35 - обычная заурядная баба, т.е. тут много уровней топовсти внешности
    $ skin = 30 # качество кожи 0 - 100
    $ face = 50 # красота лица 0 - 100
    $ hairs = 10 # качество волос 0 - 30
    $ body = 30 # привлекательность тела 0-100
    $ phisique = 30 # физическая форма 0-100
    $ fatty = 30 # толстота 0 - 100
    $ cosmetic = 0 # меньше 4 - размытая косметика, которая уменьшает красивость. Ничто не может свести косметику к 0, кроме как умыться самой или смысть косметику.
    $ alkohol = 0 # степерь набуханности 0 - 100
    # locations

    $ town_cafe_work = 0

    $ richgym_work = 0
    $ richgym_ticket = 0

    $ richbrothel_work = 0 # 0 - не знает 1 - знает 2 - работает

    # inventory

    $ simplefood = 0 # не приготовленная еда
    $ cosmetics_items = 0 # косметика
    $ iphone = 0
    $ condoms = 0
    $ salfetki = 0
    default webcamera = 0
    default outfit = 1
    #одежда; допустим 
    #0 голая
    #1 это повседнев
    #2 спортивная
    #3 платье
    #4 деловой костюм (допустим в офис)
    default laptop = 0 #ноутбук
    $ chips = 0
    $ meetfood = 0
    $ vegfood = 0
    $ snack = 0
    $ icecream = 0
    $ cake = 0
    $ junkfood = 0
    default vitamins = 0 #витамины
    $ Location_items = []
    show screen my_overlay


    # Relations

    $ TroyWilson_rel = 0

    $ Cole_he = 70 # Коул считает ее своей девушкой
    $ Cole_you = 50 # Она не против Коула, но не видит с ним будущего

    #jump NVLTest
    jump Intro




label NVLTest:
    
    "Тест текста в нвл режиме. Мне хочется понять как он будет выглядеть, если нужно будет сделать две строчки, а не одну"
    "Мне кажется, что это не сработает, но нужно попробовать."
    "Работает?"

    

    "{a=jump:place1}Поехали дальше{/a}{fast}{nw}"

    "{a=jump:place2}Дальше!{/a}{fast}{nw}"

    menu: 
        "Как это будет выглядеть?":
            "Я хочу знать что это будет"
            "Надеюсь, что оно будет работать нормально"

        "Очень интересно":
            "Это было бы отлично"
            "Если бы это работало хорошо"


    $ ui.interact()

label place1:

    nvl clear

    "Это должно было очистить страницу."
    "Надеюсь, что оно сработало."
    "Или нет?"

label place2:
    nvl clear
    "А это второе место"

    "{a=jump:place1}Ну и отлично{/a}{fast}{nw}"




# Простой label для смены картинки с кликом
label i(name):
    $ img = name
    pause
    return
