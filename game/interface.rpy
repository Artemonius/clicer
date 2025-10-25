# Трансформация - влево вверх (energy, arouse)
transform balls_fly_left_up:
    xpos 512
    ypos 868
    alpha 1.0
    parallel:
        linear 0.6 xpos 200
    parallel:
        linear 0.6 ypos 200
    linear 0.2 alpha 0.0

# Трансформация - прямо вверх (hunger, mood)
transform balls_fly_up:
    xpos 512
    ypos 868
    alpha 1.0
    linear 0.6 ypos 200
    linear 0.2 alpha 0.0

# Трансформация - вправо вверх (hygiene, new_value_test)
transform balls_fly_right_up:
    xpos 512
    ypos 868
    alpha 1.0
    parallel:
        linear 0.6 xpos 824
    parallel:
        linear 0.6 ypos 200
    linear 0.2 alpha 0.0

# Screen для анимации изменения статов
screen stat_animation(stat_name, change_value):
    zorder 200
    tag stat_animation

    # Выбираем картинку
    if change_value > 0:
        $ ball_image = "images/balls2.png"
    else:
        $ ball_image = "images/balls.png"

    # Выбираем траекторию и показываем анимацию
    if stat_name in ["hunger", "mood"]:
        add ball_image at balls_fly_up
    elif stat_name in ["energy", "arouse"]:
        add ball_image at balls_fly_left_up
    elif stat_name in ["hygiene", "new_value_test"]:
        add ball_image at balls_fly_right_up
    else:
        add ball_image at balls_fly_up

    timer 0.8 action Hide("stat_animation")

# Screen для отображения изменений статов (+ и -)
screen stat_changes_display():
    zorder 99

    # Отображаем изменения
    for stat_name, change_val in stat_changes.items():
        $ x_pos = 300
        $ y_pos = 50

        # Позиции справа от баров
        if stat_name == "energy":
            $ x_pos = 300
            $ y_pos = 50
        elif stat_name == "hunger":
            $ x_pos = 570
            $ y_pos = 50
        elif stat_name == "hygiene":
            $ x_pos = 840
            $ y_pos = 50
        elif stat_name == "arouse":
            $ x_pos = 300
            $ y_pos = 110
        elif stat_name == "mood":
            $ x_pos = 570
            $ y_pos = 110
        elif stat_name == "new_value_test":
            $ x_pos = 840
            $ y_pos = 110

        if change_val > 0:
            text "+" xpos x_pos ypos y_pos size 40 color "#00ff00" at fade_in_out
        elif change_val < 0:
            text "-" xpos x_pos ypos y_pos size 40 color "#ff0000" at fade_in_out

        timer 2.0 action Function(clear_stat_change, stat_name)

# Трансформация для плавного появления и исчезновения текста
transform fade_in_out:
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 1.6
    linear 0.2 alpha 0.0

# Функция для очистки изменений статов
init python:
    def clear_stat_change(stat_name):
        if stat_name in stat_changes:
            del stat_changes[stat_name]

screen my_overlay:
    # Белый фон
    add Solid("#FFFFFF")

    # Основная подложка игры
    add "images/game_fon.png" xalign 0.5 yalign 0.5

    frame:
        xsize 450
        ysize 1080
        background None
        xpos 0
        ypos 0

    frame:
        xsize 450
        ysize 1080
        background None
        xpos 1920-450
        ypos 0

    frame:
        xsize 3
        ysize 1080
        background Solid("#000000")
        xpos 447
        yalign 0

    frame:
        xsize 3
        ysize 1080
        background Solid("#000000")
        xpos 1920-449
        yalign 0

    #frame:
    #    xsize 1920-450-450
    #    xpos 450
    #    ypos 650
    #    ysize 1
    #    background Solid("#000000")
        

    #frame:
    #    xsize 300
    #    ysize 1
    #    background Solid("#ffffff")
    #    xalign 0.05
    #    yalign 0.24

    #frame:
    #    xsize 300
    #    ysize 1
    #    background Solid("#ffffff")
    #    xalign 0.05
    #    yalign 0.73

    #frame:
    #    xsize 330
    #    ysize 1
    #    background Solid("#ffffff")
    #    xalign 0.97
    #    yalign 0.06


    add "UI/LeftBlockFull.png" xalign 0
    add "UI/RightBlockFull.png" xalign 1.0
    #add "UI/RightBlockLine.png" xalign 0.999 yalign 0.06
    add "UI/CenterBlock.png" xalign 0.5
    vbox:
        yalign 0.02
        xalign 0.999
        spacing 5
        text "[Location_name]" line_spacing 10 xalign 0.5 xanchor 0.5 xmaximum 350 size 44 font "fonts/LocationName.ttf"
        add "UI/RightBlockLine.png" xalign 1.0
    vbox:

        xmaximum 500
        ymaximum 500
        xalign 0.15
        yalign 0.03
        xanchor 0.5
        spacing 1
        #text "[Location_name]" line_spacing 10 size 44  font "fonts/LocationName.ttf" #color "#373737"
    #    text "[Location_description]" size 24 font "fonts/LocationDescription.ttf" ypos 10 xpos 10
    #    if renpy.get_screen("choice"):
    #        for i in Location_items:
    #            textbutton i.name action Jump(i.Label) style "ThingButtonWindow" text_style "ThingButtonText"
    #    else:
    #        for i in Location_items:
    #            textbutton i.name style "ThingButtonWindow" text_style "ThingButtonText"

    # Навигация по левой плашке
    #vbox:
    #    xalign 1.0
    #    yalign 0.85
    #    spacing 10
    #    if character == 1:
    #        imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("character", 1), SetVariable("inventory", 0), SetVariable("relationship", 0)]
    #    else :
    #        imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("character", 1), SetVariable("inventory", 0), SetVariable("relationship", 0)]
    #    if inventory == 1:
    #        imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("inventory", 1), SetVariable("character", 0), SetVariable("relationship", 0)]
    #    else:
    #        imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("inventory", 1), SetVariable("character", 0), SetVariable("relationship", 0)]
    #    if relationship == 1:
    #        imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("relationship", 1), SetVariable("inventory", 0), SetVariable("character", 0)]
    #    else:
    #        imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("relationship", 1), SetVariable("inventory", 0), SetVariable("character", 0)]
#
    #vbox:
    #    xalign 0.99
    #    yalign 0.84
    #    spacing 34
    #    text "Персонаж" font "fonts/LocationName.ttf" size 50 color "#373737" 
    #    text "Инвентарь" font "fonts/LocationName.ttf" size 50 color "#373737"
    #    text "Отношения" font "fonts/LocationName.ttf" size 50 color "#373737"

    # Статы

    # vbox:
    #     xalign 0.06
    #     yalign 0.95
    #     spacing 0
    #     textbutton "ПЕРСОНАЖ" text_font "fonts/spectral.ttf" text_size 40 action [SetVariable("character_menu", "1"), SetVariable("inventory_menu", "0"), SetVariable("journal_menu", "0")]
    #     textbutton "ИНВЕНТАРЬ" text_font "fonts/spectral.ttf" text_size 40 action [SetVariable("inventory_menu", "1"), SetVariable("character_menu", "0"), SetVariable("journal_menu", "0")]
    #     textbutton "ЗАМЕТКИ" text_font "fonts/spectral.ttf" text_size 40 action [SetVariable("journal_menu", "1"), SetVariable("character_menu", "0"), SetVariable("inventory_menu", "0")]

    # Статы наверху - выровнены в 3 колонки, 2 строки
    vbox:
        xpos 50
        ypos 30
        spacing 30

        # Первая строка - 3 бара
        hbox:
            spacing 20

            # Энергия (колонка 1)
            hbox:
                spacing 10
                xsize 250
                add "images/energy.png" yalign 0.5
                bar value VariableValue("energy", 100):
                    yalign 0.5
                    xmaximum 200
                    ymaximum 40
                    left_bar "UI/Bars/green.png"
                    right_bar "UI/Bars/Background.png"
                    thumb None
                    thumb_shadow None

            # Голод (колонка 2)
            hbox:
                spacing 10
                xsize 250
                add "images/hungry.png" yalign 0.5
                bar value VariableValue("hunger", 100):
                    yalign 0.5
                    xmaximum 200
                    ymaximum 40
                    left_bar "UI/Bars/green.png"
                    right_bar "UI/Bars/Background.png"
                    thumb None
                    thumb_shadow None

            # Гигиена (колонка 3)
            hbox:
                spacing 10
                xsize 250
                add "images/hygiene.png" yalign 0.5
                bar value VariableValue("hygiene", 100):
                    yalign 0.5
                    xmaximum 200
                    ymaximum 40
                    left_bar "UI/Bars/green.png"
                    right_bar "UI/Bars/Background.png"
                    thumb None
                    thumb_shadow None

        # Вторая строка - 2 бара (выровнены по колонкам 1 и 2)
        hbox:
            spacing 20

            # Возбуждение (колонка 1)
            hbox:
                spacing 10
                xsize 250
                add "images/arouse.png" yalign 0.5
                bar value VariableValue("arouse", 100):
                    yalign 0.5
                    xmaximum 200
                    ymaximum 40
                    left_bar "UI/Bars/green.png"
                    right_bar "UI/Bars/Background.png"
                    thumb None
                    thumb_shadow None

            # Настроение (колонка 2)
            hbox:
                spacing 10
                xsize 250
                add "images/mood.png" yalign 0.5
                bar value VariableValue("mood", 100):
                    yalign 0.5
                    xmaximum 200
                    ymaximum 40
                    left_bar "UI/Bars/green.png"
                    right_bar "UI/Bars/Background.png"
                    thumb None
                    thumb_shadow None

            # Тестовый бар (колонка 3)
            hbox:
                spacing 10
                xsize 250
                add "images/energy.png" yalign 0.5
                bar value VariableValue("new_value_test", 100):
                    yalign 0.5
                    xmaximum 200
                    ymaximum 40
                    left_bar "UI/Bars/green.png"
                    right_bar "UI/Bars/Background.png"
                    thumb None
                    thumb_shadow None

    # Отображение текущей локации справа от баров
    if Location_name == "home":
        text "Дом" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "bedroom":
        text "Спальня" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "kitchen":
        text "Кухня" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "bathroom":
        text "Ванная" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "street":
        text "Улица" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "shop":
        text "Магазин" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "park":
        text "Парк" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    elif Location_name == "school":
        text "Школа" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"
    else:
        text "[Location_name]" xpos 900 ypos 50 size 48 font "fonts/LocationName.ttf"

    # Время и дата под барами - одной строкой
    hbox:
        xpos 50
        ypos 170
        spacing 15

        # Время
        hbox:
            spacing 2
            if hour < 10:
                text hour_show size 36 font "fonts/serreg.ttf"
            else:
                text hour_show size 36 font "fonts/serreg.ttf"
            if minutes > 9:
                text minutes_show size 36 font "fonts/serreg.ttf"
            else:
                text minutes_show size 36 font "fonts/serreg.ttf"

        # День недели
        text "[weekday]" size 24 font "fonts/serreg.ttf" yalign 0.5

        # Дата
        text "[date].[month].[year]" size 20 font "fonts/serreg.ttf" yalign 0.5

        # Деньги
        text "Наличность: [money]$" size 24 font "fonts/serreg.ttf" yalign 0.5

    # Отображение изменений статов (+ и -)
    use stat_changes_display

    # Описание персонажа
    
    # Инвентарь

    # Кнопки

    #vbox:
    #    xalign 0
    #    yalign 0.98
    #    spacing 10
    #    if character == 1:
    #        imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("character", 1), SetVariable("inventory", 0), SetVariable("relationship", 0)]
    #    else :
    #        imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("character", 1), SetVariable("inventory", 0), SetVariable("relationship", 0)]
    #    if inventory == 1:
    #        imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("inventory", 1), SetVariable("character", 0), SetVariable("relationship", 0)]
    #    else:
    #        imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("inventory", 1), SetVariable("character", 0), SetVariable("relationship", 0)]
    #    if relationship == 1:
    #        imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("relationship", 1), SetVariable("inventory", 0), SetVariable("character", 0)]
    #    else:
    #        imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("relationship", 1), SetVariable("inventory", 0), SetVariable("character", 0)]

    #    imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [MainMenu(confirm=True)]               


    #vbox:
    #    xalign 0.04
    #    yalign 0.97
    #    spacing 34
    #    text "Персонаж" font "fonts/LocationName.ttf" size 50 color "#373737" 
    #    text "Инвентарь" font "fonts/LocationName.ttf" size 50 color "#373737"
    #    text "Отношения" font "fonts/LocationName.ttf" size 50 color "#373737"
    #    text "Меню" font "fonts/LocationName.ttf" size 50 color "#373737"

    

style ThingButtonWindow:
    ypos 10
    xpos 20
    background "UI/ItemButton.png" 
    hover_background "UI/ItemButtonHover.png"
    xpadding 100

style ThingButtonText:
    size 40
    idle_color "#000000"
    hover_color "#ffffff"
    xanchor  0.5
    xcenter 0.5
    font "fonts/ChoiceText.ttf"
    

screen main_UI:
    add DynamicImage("images/1.png") xalign 0.5 yalign 0 # бэкграунд
    add "UI/overlay.png"
    text "[LocationCurrent]" xalign 0.5 yalign 0.69  size 40 font "fonts/LocationName.ttf" xanchor 0.5
    # Описание локации
    vbox:
        xmaximum 350
        ymaximum 500
        xalign 0.97
        yalign 0.03
        spacing 10
        text "[Location_name]:"  size 44  font "fonts/LocationName.ttf" color "#373737"
        # text "[Location_description]" size 24 font "fonts/LocationDescription.ttf" ypos 10 xpos 10
        if len(Location_chars) > 0:
            text "Персонажи:" size 24
        
        if renpy.get_screen("choice"):
            for i in Location_chars:
                textbutton i.name action Jump(i.Label) style "ThingButtonWindow" text_style "ThingButtonText"
        else:
            for i in Location_items:
                textbutton i.name style "ThingButtonWindow" text_style "ThingButtonText"

        if len(Location_items) > 0:
            text "Предметы:" size 24

        if renpy.get_screen("choice"):
            for i in Location_items:
                textbutton i.name action Jump(i.Label) style "ThingButtonWindow" text_style "ThingButtonText"
        else:
            for i in Location_items:
                textbutton i.name style "ThingButtonWindow" text_style "ThingButtonText"

    # Навигация по левой плашке
    vbox:
        xalign 1.0
        yalign 0.85
        spacing 10
        if character == 1:
            imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("character", 1), SetVariable("inventory", 0), SetVariable("relationship", 0)]
        else :
            imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("character", 1), SetVariable("inventory", 0), SetVariable("relationship", 0)]
        if inventory == 1:
            imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("inventory", 1), SetVariable("character", 0), SetVariable("relationship", 0)]
        else:
            imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("inventory", 1), SetVariable("character", 0), SetVariable("relationship", 0)]
        if relationship == 1:
            imagebutton idle "UI/GreenButton.png" hover "UI/GreenButton.png"  action [SetVariable("relationship", 1), SetVariable("inventory", 0), SetVariable("character", 0)]
        else:
            imagebutton idle "UI/RedButton.png" hover "UI/GreenButton.png"  action [SetVariable("relationship", 1), SetVariable("inventory", 0), SetVariable("character", 0)]

    vbox:
        xalign 0.99
        yalign 0.84
        spacing 34
        text "Персонаж" font "fonts/LocationName.ttf" size 50 color "#373737" 
        text "Инвентарь" font "fonts/LocationName.ttf" size 50 color "#373737"
        text "Отношения" font "fonts/LocationName.ttf" size 50 color "#373737"

    # Статы

    #text "[hour]:[minutes]" xalign 0.09 yalign 0.03 size 90  xanchor 0.5 font "fonts/LocationName.ttf"
    if hour < 10:
        text "0[hour]:" xalign 0.06 yalign 0.03 size 90  xanchor 0.5 font "fonts/LocationName.ttf"
    else :
        text "[hour]:" xalign 0.06 yalign 0.03 size 90  xanchor 0.5 font "fonts/LocationName.ttf"
    if minutes > 9:
        text "[minutes]" xalign 0.12 yalign 0.03 size 90  xanchor 0.5 font "fonts/LocationName.ttf"
    else:
        text "0[minutes]" xalign 0.12 yalign 0.03 size 90  xanchor 0.5 font "fonts/LocationName.ttf"
    text "[weekday]" xalign 0.09 yalign 0.1  xanchor 0.5 font "fonts/ChoiceText.ttf" size 34
    text "[date].[month].[year]" xalign 0.09 yalign 0.155 xanchor 0.5 font "fonts/LocationDescription.ttf"

    text "Наличность: [money]$" xalign 0.09 yalign 0.19 xanchor 0.5 font "fonts/LocationDescription.ttf"
