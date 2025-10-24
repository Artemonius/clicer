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
    global arouse_def
    # всего отбражаемого ароуза 100, но вообще 200, просто из полного вычитается удовлетовренность.
    # т.е. чтобы возбудить полностью удовлетворенную бабу нужно набрать 200 баллов, при этом возбуждаемость работает как индес
    # т.е. если возбуждаемость 100, то любой плюс возбуждения умножается на 1, если 150, то на 1.5
    global energy  # Энергия персонажа, влияет на его активность и способность выполнять действия
    global hunger  # Голод персонажа, влияет на его настроение и здоровье
    global mood  # Настроение персонажа, влияет на его реакции и взаимодействия
    global return_label  # Метка для возвращения в домашнюю локацию
    return_label = "Home"
    global overral_handy  # Общий вид персонажа, влияет на его привлекательность и уверенность в себе
    global hairs  # Волосы персонажа, влияют на его внешний вид и уверенность в себе
    global face  # Лицо персонажа, влияет на его внешний вид и привлекательность
    global skin  # Кожа персонажа, влияет на его здоровье и внешний вид
    global body  # Тело персонажа, влияет на его физические способности и здоровье
    global fatty  # Полнота персонажа, влияет на его внешний вид и здоровье
    global physique  # Физическая форма персонажа, влияет на его физические способности и здоровье
    global cosmetic  # Косметические параметры персонажа, влияют на его внешний вид и привлекательность
    global tits  # Сиськи персонажа, влияют на его внешний вид и привлекательность
    global satisfaction    
    global lust


    global wet_panties # мокрые трусы, не от возбуждения, а после секса, типа надо подмыться.

    global alkohol
    alkohol = 0

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

    # Простая система кликера
    global img_current
    global img_max
    global img_prefix

    img_current = 0
    img_max = 0
    img_prefix = ""

    def ClearThings():
        global Location_items
        del Location_items[:]
        Location_items[:] = []

    def CanUseChange(NewCan):
        global CanUse
        CanUse = NewCan

    def AddArouse(x):  # Возбуждение
        global arouse, arouse_def, lust, satisfaction
        arouse_def += x * (lust / 100)
        arouse = arouse_def - satisfaction
        if arouse < 0:
            arouse = 0
        if arouse > 100:
            arouse = 100


    def CheckMood():
        global mood, want_fame, want_macbook, want_airpods, want_ipad, want_perfume, want_makeup, want_pizza, want_burger, want_iphone
        if mood > 100:
            mood = 100
        if mood < 0:
            mood = 0
        
        # Снижаем настроение если есть неудовлетворенные желания
        if want_fame: # хочет славы
            mood -= 8
        if want_macbook: # хочет макбук
            mood -= 15 
        if want_airpods: # хочет аирподс
            mood -= 10
        if want_ipad: # хочет айпад
            mood -= 8
        if want_perfume: # хочет духи
            mood -= 5
        if want_makeup: # хочет косметику
            mood -= 4
        if want_pizza: # хочет пиццу
            mood -= 2
        if want_burger: # хочет бургер
            mood -= 2
        if want_iphone: # хочет iphone
            mood -= 10
            
        # Проверяем еще раз после всех изменений
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

    def AddMood(x): #добавляем настроение. но можно и минусовать
        global mood 
        mood += x
        CheckMood()
    def AddLust(x): #развращенность
        global lust
        lust += x
        if lust > 100:
            lust = 100
        if lust < 0:
            lust = 0
    def AddHunger(x): #голод
        global hunger 
        hunger += x
        if hunger > 100:
            hunger = 100
        if hunger < 0:
            hunger = 0
    def AddSatisfaction(x): #удовлетворенность
        global satisfaction
        satisfaction += x
        if satisfaction > 100:
            satisfaction = 100
        if satisfaction < 0:
            satisfaction = 0
    def AddHygiene(x): #гигиена
        global hygiene
        hygiene += x
        if hygiene > 100:
            hygiene = 100
        if hygiene < 0:
            hygiene = 0
    
    def AddFatty(x): #толстота
        global fatty 
        fatty += x
        if fatty > 100:
            fatty = 100
        if fatty < 0:
            fatty = 0
    def AddCosmetic(x): #косметика
        global cosmetic
        cosmetic += x
        if cosmetic > 100:
            cosmetic = 100
        if cosmetic < 0:
            cosmetic = 0
    def AddFace(x): #красота лица
        global face
        face += x
        if face > 100:
            face = 100
        if face < 0:
            face = 0


    def CheckBody():
        global body
        body = physique - (fatty - 30)
        if skin > 60:
            body += 20
        if skin < 10:
            body -= 20
        elif skin < 20:
            body -= 15
        elif skin < 30:
            body -= 10
        if body > 100:
            body = 100
        if body < 0:
            body = 0

    def CheckFace():
        global face
        face = skin+hairs
        if cosmetic < 4 and cosmetic != 0:
            face -= 20
        if cosmetic > 8:
            face += 20
        elif cosmetic > 4:
            face += 10
        if fatty > 80:
            face = 10
        if face > 100:
            face = 100
        if face <= 0:
            face = 0

    def CheckOverralHandy():
        global overral_handy
        overral_handy = 0
        overral_handy += hairs*3
        overral_handy += body*5
        overral_handy += skin*5
        if cosmetic > 7:
            overral_handy += 20
        elif cosmetic >= 4:
            overral_handy += 10
        elif cosmetic > 0:
            overral_handy -= 20
        overral_handy = round(overral_handy*0.75)
        if overral_handy > 100:
            overral_handy = 100
        if overral_handy < 0:
            overral_handy = 0

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

    def CheckTownPolice(): #проверка наличия шерифа
        global TownSheriffWorking
        global TownDeputySheriffWorking
        if hour < 12 or hour > 16:
            TownSheriffWorking = 0
        else:
            TownSheriffWorking = 1

        if hour == 13:
            TownDeputySheriffWorking = 0
        else:
            TownDeputySheriffWorking = 1

    def CheckFatherKitchen():
        global father_kitchen
        if weekdays.index(weekday) < 6:
            if hour == 7 or hour == 20:
                father_kitchen = 1
            else:
                father_kitchen = 0
        else:
            if hour == 10 or hour == 19:
                father_kitchen = 1
            else:
                father_kitchen = 0

    def CheckMotherKitchen():
        global mother_kitchen
        if weekdays.index(weekday) < 6:
            if hour == 6 or hour == 7 or hour == 20:
                mother_kitchen = 1
            else:
                mother_kitchen = 0
        else:
            if (hour > 8 and hour < 12) or (hour >= 18 and hour <= 20):
                mother_kitchen = 1
            else:
                mother_kitchen = 0

    def CheckHallFather():
        global father_hall
        if weekdays.index(weekday) < 6:
            if hour == 20 or hour == 21:
                father_hall = 1
            else:
                father_hall = 0
        else:
            if hour > 15 and hour < 22:
                father_hall = 1
            else:
                father_hall = 0
    def CheckHallMother():
        global mother_hall
        if weekdays.index(weekday) < 6:
            if hour == 21:
                mother_hall = 1
            else:
                mother_hall = 0
        else:
            if hour >= 20 and hour <= 21:
                mother_hall = 1
            else:
                mother_hall = 0

    def CheckNewDayVariables():
        global physique
        global richgym_ticket 
        physique -= 1
        if richgym_ticket > 0:
            richgym_ticket -= 1


    def CheckSleepVariables(index):
        global cosmetic
        global energy
        global hunger
        global hygiene
        global hairs
        global arouse
        if cosmetic > 0:
            cosmetic = 1
        if index > 6:
            energy = 100
            hunger = 0
            hygiene -= 60
            if hairs == 10:
                hairs = 6
            else :
                hairs -= 2
        elif index > 4:
            energy += 60
            hunger -= 60
            hygiene -= 40
            if hairs == 10:
                hairs = 8
            else :
                hairs -= 1
        elif index > 2:
            energy += 40
            hunger -= 40
            hygiene -= 30
            if hairs == 10:
                hairs = 9
            else :
                hairs -= 1
        elif index == 1:
            energy += 15
            hunger -= 10                        
        else:
            energy += 20
            hunger -=20
            hygiene -= 20
            if hairs == 10:
                hairs = 8
            else :
                hairs -= 1
        arouse = 0
    def AddEnergy(x):
        global energy
        energy += x
        if energy > 100:
            energy = 100
        if energy < 0:
            energy = 0
    def AddMinutes(min): #чтобы добавить час нужно добавить 60 минут
        global minutes
        global energy
        minutes += min
        energy -= min*0.08
        CheckTime()

    def AddMoney(x): #деньги
        global money
        money += x
        if money < 0:
            money = 0

    def AddAlko(ind): #добавить алкоголь
        global alkohol
        alkohol += ind
        if alkohol > 100:
            alkohol = 100
        if alkohol < 0:
            alkohol = 0

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

