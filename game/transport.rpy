label walk_menu:
    nvl clear
    "Выберите, куда пойти дальше:{nw}"
    menu:
        "Гетто" if return_label != "CityGhetto":
            $ AddMinutes(40)
            jump CityGhetto
        "Центр города" if return_label != "CityCenter":
            $ AddMinutes(40)
            jump CityCenter
        "Богатый район" if return_label != "CityRich":
            $ AddMinutes(40)
            jump CityRich
        "Офисный квартал" if return_label != "CityOffices":
            $ AddMinutes(40)
            jump CityOffices
        "Спальный район" if return_label != "CityPoor":
            $ AddMinutes(40)
            jump CityPoor
        "Окраина" if return_label != "CityEnterance":
            $ AddMinutes(40)
            jump CityEnterance
        #"Дом{nw}" if return_label != "Porch_main":
        #    $ AddMinutes(40)
        #    jump Porch_main
        "Пригород" if return_label != "LittleTown":
            $ AddMinutes(40)
            jump LittleTown
        "Назад":
            jump expression return_label
#++++++++++++++++++++++++++++++++++++++++++++++++
label taxi_menu:
    nvl clear
    if money <= 30:
        "Недостаточно денег"
        jump expression return_label
    "Вы поймали такси и отправились до...{nw}"
    menu:
        "Гетто" if return_label != "CityGhetto":
            $ money -= 30
            $ AddMinutes(25)
            jump CityGhetto
        "Центр города" if return_label != "CityCenter":
            $ money -= 30
            $ AddMinutes(25)
            jump CityCenter
        "Богатый район" if return_label != "CityRich":
            $ money -= 30
            $ AddMinutes(25)
            jump CityRich
        "Офисный квартал" if return_label != "CityOffices":
            $ money -= 30
            $ AddMinutes(25)
            jump CityOffices
        "Спальный район" if return_label != "CityPoor":
            $ money -= 30
            $ AddMinutes(25)
            jump CityPoor
        "Окраина" if return_label != "CityEnterance":
            $ money -= 30
            $ AddMinutes(25)
            jump CityEnterance
        #"Дом{nw}" if return_label != "Porch_main":
        #    $ money -= 30
        #    $ AddMinutes(25)
        #    $ CheckTime()
        #    jump Porch_main
        "Пригород" if return_label != "LittleTown":
            $ money -= 30
            $ AddMinutes(25)
            jump LittleTown
        "Назад":
            jump expression return_label
#++++++++++++++++++++++++++++++++++++++++++++++++
label bus_menu:
    nvl clear
    if money < 1:
        "У вас не хватает денег."
        jump expression return_label
    "Вы сели в автобус до...{nw}"
    menu:
        "Гетто" if return_label != "CityGhetto":
            $ money -= 1
            $ AddMinutes(25)
            jump CityGhetto
        "Центра города" if return_label != "CityCenter":
            $ money -= 1
            $ AddMinutes(25)
            jump CityCenter
        "Богатого района" if return_label != "CityRich":
            $ money -= 1
            $ AddMinutes(25)
            jump CityRich
        "Офисного квартала" if return_label != "CityOffices":
            $ money -= 1
            $ AddMinutes(25)
            jump CityOffices
        "Спального района" if return_label != "CityPoor":
            $ money -= 1
            $ AddMinutes(25)
            jump CityPoor
        "Окраины" if return_label != "CityEnterance":
            $ money -= 1
            $ AddMinutes(25)
            jump CityEnterance
        #"Дом{nw}" if return_label != "Porch_main":
        #    $ money -= 1
        #    $ AddMinutes(25)
        #    $ CheckTime()
        #    jump Porch_main
        "Пригород" if return_label != "LittleTown":
            $ AddMinutes(40)
            jump LittleTown
        "Назад":
            jump expression return_label

#++++++++++++++++++++++++++++++++++++++++++++++++