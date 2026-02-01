class Human:
    def __init__(self, v_name, v_age, v_sex = 1):
        self.name = v_name
        self.age = v_age
        self.sex = v_sex
        self.adult = True if self.age >= 18 else False
    #Взросление  на год
    def aging(self):
        self.age += 1

    def __str__(self):
        return 'Человек по имени ' + self.name + ' ' + str(self.age) + ' лет'

class Kid(Human):
    def __init__(self,v_name, v_age, v_sex, v_toys):
        super().__init__(v_name, v_age, v_sex)
        self.adult = False
        self.toys_count = v_toys
    def __str__(self):
        return 'Ребенок по имени ' + self.name + ' ' + str(self.age) + ' лет, имеет ' + str(self.toys_count) + ' игрушек'


# o_Toma = Human('Toma', 29, 0)
# print(o_Toma)
# o_Max = Kid('Max', 8, 1, 10)
# print(o_Max)

class bus:
    def __init__(self, v_sits:int = 10):
        self.kids = {k: None for k in range(1,v_sits + 1)}
        # print(self.kids.items())

    def add_kid(self, v_kids):
        # print('Хотим посадить', sum(1 for k in v_kids if k is not None))
        # print('Свободных мест', sum(1 for k in self.kids.values() if k is None))
        # Ошибка, если хотим посадить больше детей, чем есть свободных мест
        if sum(1 for k in v_kids if k is not None) > sum(1 for k in self.kids.values() if k is None):
            print('Не хватает свободных мест в автобусе')
        else:
            for v in v_kids:
                # Садим на первое свободное место
                print(v, 'садится на место', self.__first_empty_sit())
                self.mv_kid(v, self.__first_empty_sit())
                # print(self.kids.items())

    def __first_empty_sit(self):
        for k, v in self.kids.items():
            if v is None:
                return k

    def rm_kid(self, v_kid):
        for k, v in self.kids.items():
            if v == v_kid:
                self.kids[k] = None

    def kid_sit(self,v_kid):
        for k, v in self.kids.items():
            if v == v_kid:
                return k

    def kid_info(self, v_kid):
        sit = self.kid_sit(v_kid)
        if sit is not None:
            print(v_kid + ' сидит на месте ' + str(sit))
        else:
            print(v_kid, 'нет в автобусе')

    def mv_kid(self, v_kid, v_sit):
        #Проверяем, есть ли такое место вообще
        if v_sit not in self.kids.keys():
            print('Такого места в автобусе нет!')
        #Если место занято, то менять местами
        elif self.kids[v_sit] is not None:
            #Узнаем старое место v_kid и садим туда того, кто раньше сидел на указанном месте
            self.kids[self.kid_sit(v_kid)], self.kids[v_sit] = self.kids.get(v_sit), v_kid
        #Если свободно, то
        else:# Если нигде не сидел, то посадить
            if self.kid_sit(v_kid) is None:
                self.kids[v_sit] = v_kid
            else:# удалить со старого и посадить на новое
                self.kids[self.kid_sit(v_kid)] = None
                self.kids[v_sit] = v_kid

    def mv_all(self, v_kids):
        print('Пересадка всех детей!')
        for i, k in enumerate(v_kids):
            self.mv_kid(k, i + 1)
        self.bus_info()

    def bus_info(self):
        kid_count = sum(1 for k in self.kids.values() if k is not None)
        print('В автобусе ' + str(len(self.kids)) + ' мест,', str(kid_count) + ' детей')
        if kid_count > 0:
            for k, v in self.kids.items():
                print(k, ': ', v)

o_bus11 = bus()
o_bus11.bus_info()
o_bus11.add_kid(['Lera','Masha','Toma','Lola','Lina'])
o_bus11.bus_info()
# o_bus11.mv_kid('Toma',2)
# o_bus11.bus_info()
o_bus11.mv_all(['Lina', None, 'Masha', None, 'Lola', None, 'Toma', None, 'Lera'])
# o_bus11.rm_kid('Lera')
# o_bus11.bus_info()
# o_bus11.kid_info('Lera')

o_bus11.add_kid(['Lera2','Masha2','Toma2','Lola2','Lina2'])
o_bus11.bus_info()