# Пример использования системы кликера для последовательной смены картинок

# Этот label показывает, как использовать кликер
label clicker_test:

    # Инициализируем последовательность картинок от 1_1 до 1_20
    # Картинки должны находиться в папке game/images/ и называться:
    # 1_1.png, 1_2.png, 1_3.png ... 1_20.png
    $ update_img("1_1", "1_20")

    # Показываем экран кликера - каждый клик будет менять картинку
    # После 1_20.png экран автоматически закроется
    call screen image_clicker

    # После завершения кликера продолжаем сценарий
    "Последовательность картинок завершена!"

    return


# Более сложный пример с несколькими последовательностями
label clicker_multiple:

    "Сейчас будет первая сцена..."

    # Первая последовательность
    $ update_img("scene1_1", "scene1_10")
    call screen image_clicker

    "Первая сцена завершена! Теперь вторая..."

    # Вторая последовательность
    $ update_img("scene2_1", "scene2_15")
    call screen image_clicker

    "Все сцены завершены!"

    return


# Пример с текстом между картинками
label clicker_with_text:

    "Это начало сцены..."

    $ update_img("intro_1", "intro_5")
    call screen image_clicker

    "Середина сцены - что-то произошло!"

    $ update_img("middle_1", "middle_8")
    call screen image_clicker

    "И финал!"

    $ update_img("end_1", "end_3")
    call screen image_clicker

    "Сцена завершена!"

    return
