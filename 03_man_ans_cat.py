# -*- coding: utf-8 -*-
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.home = home
        self.cat = cat

    def __str__(self):
        return '{}, сытость {}'.format(self.name, self.fullness, )

    def go_to_the_house(self):
        self.home.house.append(self.name)  # Бифис заехал в дом
        cprint('{} вьехал в дом'.format(self.name), color='cyan')
        cprint('В доме проживают {}'.format(self.home.house), color='green')
        self.take_cat()  # Бифис подобрал кота
        cprint('В доме проживают {}'.format(self.home.house), color='green')
        self.fullness -= 10  # при переезде расходовал энергию

    def take_cat(self):  # подобрать кота
        self.home.house.append(cat.name_cat)
        cprint('{}, подобрал кота'.format(self.name), color='blue')

    def eat(self):
        if self.home.food > 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.home.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        if self.fullness >= 10:
            cprint('{} сходил на работу'.format(self.name), color='blue')
            self.home.money += 150
            self.fullness -= 10

    def shopping(self):
        if self.home.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.home.money -= 50
            self.home.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat(self):  # сходить за едой коту
        if self.home.money >= 50:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.home.money -= 50
            self.home.cat_food += 50
            self.fullness -= 10

    def clean_the_house(self):  # убраться в доме
        if self.fullness > 10:
            cprint('{} убрался в доме'.format(self.name), color='green')
            self.home.cat_dirt -= 100  # степень грязи в доме уменьшается
            self.fullness -= 10

    def pet_the_cat(self):  # гладит кота
        if self.fullness > 10:
            cprint('{} погладил кота'.format(self.name), color='green')
            self.fullness -= 5
            self.cat.number_of_labels += 20  # мурлыков увеличивается

    def watch_mtv(self):  # смотреть телевизор
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return

        if self.fullness <= 10:  # если сытость меньше 10
            self.eat()  # то Бифис ест

        elif self.home.money <= 50:  # если денег меньше 20
            self.work()  # то на работу

        elif self.home.food <= 20:  # если в доме еда уменьшается, то Бивис идет в магазин
            self.shopping()

        elif self.home.cat_food <= 10:  # если еды для кота осталось меньше 10, то в магазин
            self.shopping_cat()

        elif self.home.cat_dirt >= 100:  # если грязи в доме  100
            self.clean_the_house()  # то уборка

        elif self.cat.number_of_labels < 50:  # если мурлыков уменьшается, то Бивис его гладит
            self.pet_the_cat()  # погладил кота

        else:
            self.watch_mtv()


class Cat:
    def __init__(self, name_cat):
        self.well_fed_cat = 10  # Сытость кота
        self.name_cat = name_cat
        self.number_of_labels = 50  # количество мурлыков
        self.home = home

    def __str__(self):
        return '{}, сытость {}, осталось мурлыков {}'.format(self.name_cat, self.well_fed_cat, self.number_of_labels)

    def cat_eating(self):  # кот ест
        if self.home.cat_food >= 10:  # если еды в доме больше 10
            cprint('{} поел'.format(self.name_cat), color='cyan')
            self.well_fed_cat += 20  # сытость увеличивается
            self.home.cat_food -= 10  # еда уменьшается

    def the_cat_purrs(self):  # кот мырлычит
        cprint('{} мырлычит'.format(self.name_cat), color='grey')
        self.number_of_labels -= 5

    def the_cat_sleeping(self):  # кот спит
        if self.number_of_labels >= 50:
            cprint('{} спит'.format(self.name_cat), color='blue')
            self.well_fed_cat -= 10  # сытость уменьшается

    def cat_tears_wallpaper(self):  # кот дерет обои
        if self.well_fed_cat > 10:
            cprint('{} дерет обои'.format(self.name_cat), color='red')
            self.well_fed_cat -= 10  # сытость уменьшается
            self.home.cat_dirt += 5  # грязь увеличивается

    def act(self):
        if self.well_fed_cat < 0:
            cprint('{} умер...'.format(self.name_cat), color='red')
            return

        if self.number_of_labels < 0:  # если мурлыков меньшу нуля, то кот заболел
            cprint('{} заболел...'.format(self.name_cat), color='red')
            return

        if self.well_fed_cat <= 10:  # если сытости меньше 10
            self.cat_eating()  # то кот ест

        if self.well_fed_cat >= 20:  # если сытости у кота больше 10
            self.the_cat_sleeping()  # то кот спит

        if self.home.cat_dirt < 100:  # если грязи в доме меньше 100
            self.cat_tears_wallpaper()  # то кот дерет обои

        if self.number_of_labels > 40:  # если мурлыков больше 40
            self.the_cat_purrs()  # то спит


class House:

    def __init__(self):
        self.food = 50  # еда человека
        self.cat_food = 0  # еда кота
        self.cat_dirt = 0  # грязь от кота
        self.money = 0
        self.house = []

    def __str__(self):
        return 'В доме еды осталось для Бифиса = {}, еды для Кота осталось = {}, ' \
               'денег осталось = {}, грязи в доме накопилось {} ' \
            .format(self.food, self.cat_food, self.money, self.cat_dirt)


home = House()
cat = Cat(name_cat='Кот')  # Кто живет в доме
man = Man(name='Бивис')
citizens = [man, cat]
man.go_to_the_house()  # переезд   в дом

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()  # на каждый  citisen то есть каждому жителю говорим -"Действуй" citisen.act()
    print('--- в конце дня ---')

    for citizen in citizens:
        print(citizen)  # Каждый citisen то есть житель выведет свое состояние
    print(home)  # Выведет что произошло в доме

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# Зачёт!
