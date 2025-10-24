init python:

    def move(where):
        global curloc, prevloc, outside #Объявляем глобальную переменную курлок, которая явлеется объектом текущей локации
        if isinstance(where, basestring):
            for x in allLocs:
                if x.id == where:
                    where = x
                    break
        prevloc = curloc # Сохраняем предыдущую локацию
        curloc = where # Присваиваем курлоку текущее назначение
        # curloc.move(player)
        player.normalize()
        
        renpy.scene(layer='master') # Сброс картинок
        renpy.scene(layer='screens') # Сброс скринов
        renpy.show('black') # Базовый фон
        renpy.retain_after_load()
        checkEvents(curloc)
        renpy.jump('location_label') #Прыгаем на наш костыль для вызовы скрина локации



    def checkEvents(curloc):
        # это все примеры из чужого проекта
        if curloc == getLocation('juliaRoom'):
            pass
            # renpy.jump('julia_test')
        if curloc == getLocation('plaza') and trigger[10] == 0:
            renpy.jump('no_intro_return')
            
        if curloc == getLocation('tavern') and day_time == 1:
            renpy.jump('tavern_early')
            
        if curloc == getLocation('juliaRoom') and day_time == 3 and trigger[11] in [9]:
            renpy.jump('julia_mastur_select')

        #


    class Location:
        def __init__(self, id, name, description, image, type, doors = None, reputation = 0):
            self.id = id # Для удобства определения, что за локация. Мало ли. пригодится.
            self.name = name # Отображаемое имя
            self.description = description # Массив описаний.
            self.image = image # Картиинка для показа
            self.items = [] # Массив предметов в локации
            if doors == None:
                self.doors = [] # Массив дверей в локации
            self.dos = [] # Массив возможных эвентов в локации
            self.type = type # Тип локации
            self.people = [] # Массив людей в локации
            self.navigation = [] # Массив локаций, в которые можно перейти
            self.events = []
        
        # Функция добавления возможной локации для перехода.
        def addNav(self, locObj):
            if self != locObj and locObj not in self.navigation:
                self.navigation.append(locObj)
                if self not in locObj.navigation:
                    locObj.navigation.append(self)
            
        def genNavigation(self, where, investigation):
            if rand(1,2) == 0:
                self.addNav(where)
            else:
                self.genDoor(self.getLevel(), where, investigation)
                
        def move(self, char):
            if isinstance(char, basestring):
                for x in allChars:
                    if x.id == char:
                        char = x
                        break
            for loc in allLocs:
                if char in loc.people:
                    loc.people.remove(char)
            char.location = self
            self.people.append(char)


    def getLocation(id = ''):
        for x in allLocs:
            if x.id == id:
                return x
        return 'WRONG LOCATION!!!'
                
    def appendEvents():
        _locs = renpy.get_all_labels()
        for x in allLocs:
            x.events = []
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'event_': # находим тот, что с евентом
                for location in allLocs: # начинаем перебирать локации
                    if location.id in eventLabel and eventLabel not in location.events: # Если имя локации содержится в имени эвента
                        location.events.append(eventLabel) # добавляем его в массив эвентов локации



    def genLocs():
# Генерация локаций
        allLocs = []
        mainRoom = Location(
            id = 'mainRoom',
            name = _('Моя комната'),
            description = [_('Комната пастора.'), 
                _('Всё обставлено довольно скромно и аскетично. У каменного камина стоят два кресла, в которых удобно беседовать вечерами.'),
                _('Слева стоит небольшой стол с фруктами, а старая, но удобная кровать покрыта зелёным пледом.')],
            type = ['private','inside'],
            image = 'mainRoom_im')
        allLocs.append(mainRoom)