# Начало игры: возвращение домой перед выпускным
label Intro:
    nvl clear
    $ Location_name = "home"
    $ hour = 16
    "пидор ленивый"
    "тест говна"
    "тест говна"
    $ AddStats(mood, 2000)
    "тест говна"
    $ CheckTime()
    $ img = "png.png"
    "Здесь мы просто тестируем, как это будет смотреться"
    "Здесь мы просто тестируем, как это будет смотреться"

    $ img = "fon.png"  # Улица вечером
    
    $ img = "val_1.png"
    $ img = "val_2.png"
    $ img = "val_3.png"
    $ img = "val_4.png"
    "тест очка"
    return