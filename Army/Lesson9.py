class Human:
    def __init__(self):
        self.__name = 'Ivan'
        self.__age = 30
        self.__location = 'Moscow'

    def info(self):
        print('Name:', self.__name, ', age:', self.__age, ', location:', self.__location)

    def set_name(self, v_name):
        self.__name = v_name

    def get_name(self):
        return self.__name

    def set_age(self, v_age):
        self.__age = v_age

    def get_age(self):
        return self.__age

    def set_location(self, v_location):
        self.__location = v_location

    def get_location(self):
        return self.__location


class Rota:
    __next_id = 1

    def __init__(self):
        self.__humans = []
        self.__human_count = 0
        self.__location = None
        self.__id = Rota.__next_id
        Rota.__next_id += 1

    def get_id(self):
        return self.__id

    def get_human_count(self):
        return self.__human_count

    def add_human(self, v_human: list):
        for human in v_human:
            if human not in self.__humans:
                self.__humans += v_human
        self.__set_human_count()

    def rm_human(self, v_human: list):
        for human in v_human:
            if human in self.__humans:
                self.__humans.remove(human)
        self.__set_human_count()

    def __set_human_count(self):
        self.__human_count = len(self.__humans)

    def get_location(self):
        return self.__location

    def set_location(self, v_location):
        self.__location = v_location
        for human in self.__humans:
            human.set_location(v_location)

    def info(self):
        print('Рота #', self.__id, self.__human_count, 'человек')
        for human in self.__humans:
            human.info()

    def human_list(self):
        return self.__humans


class Polk:
    __polk_id = 1

    def __init__(self):
        self.__id = Polk.__polk_id
        self.__rota_list = []
        self.__humans = []
        self.__location = None
        Polk.__polk_id += 1

    def get_location(self):
        return self.__location

    def set_location(self, v_location):
        self.__location = v_location
        for rota in self.__rota_list:
            rota.set_location(v_location)

    def add_rota(self, v_rota_list):
        for rota in v_rota_list:
            if rota not in self.__rota_list:
                self.__rota_list.append(rota)
                rota.set_location(self.__location)
                self.__add_human_of_rota(rota)

    def __add_human_of_rota(self, v_rota):
        for human in v_rota.human_list():
            if human not in self.__humans:
                self.__humans.append(human)

    def rm_rota(self, v_rota_list):
        for rota in v_rota_list:
            if rota in self.__rota_list:
                self.__rota_list.remove(rota)
                self.__rm_human(rota)

    def __rm_human(self, v_rota):
        for human in v_rota.human_list():
            if human in self.__humans:
                self.__humans.remove(human)

    def info(self):
        print('Полк #', self.__id, 'находится в', self.__location)
        for rota in self.__rota_list:
            rota.info()

    def rota_100_info(self):
        try:
            self.__rota_list[100].info()
        except IndexError:
            print('Нет такой роты в Полк #', self.__id)
