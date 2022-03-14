# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:  # Вода
    def __init__(self):
        self.water = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):  # Воздух
            return Storm()  # Шторм
        if isinstance(other, Fire):  # Огонь
            return Steam()  # Пар
        if isinstance(other, Earth):  # Земля
            return Mud()  # Пыль
        else:
            return None

    def __str__(self):
        return '{}'.format(self.water)


class Air:  # Воздух
    def __init__(self):
        self.air = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):  # Вода
            return Storm()  # Шторм

        if isinstance(other, Fire):  # Огонь
            return Lightning()  # Молния

        if isinstance(other, Earth):  # Земля
            return Dust()  # Пыль
        else:
            return None

    def __str__(self):
        return '{}'.format(self.air)


class Fire:  # Огонь
    def __init__(self):
        self.fire = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):  # Вода
            return Steam()  # Пар

        if isinstance(other, Air):  # Вода
            return Lightning()  # Пар

        if isinstance(other, Earth):
            return Lava()  # Лава

    def __str__(self):
        return '{}'.format(self.fire)


class Earth:  # Земля
    def __init__(self):
        self.earth = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):  # Вода
            return Mud()  # Грязь

        if isinstance(other, Air):  # Воздух
            return Dust()  # Пыль

        if isinstance(other, Fire):  # Огонь
            return Lava()  # Лава

    def __str__(self):
        return '{}'.format(self.earth)


class Storm:  # Шторм
    def __init__(self):
        self.storm = 'Шторм'

    def __str__(self):
        return '{}'.format(self.storm)


class Steam:  # Пар
    def __init__(self):
        self.steam = 'Пар'

    def __str__(self):
        return '{}'.format(self.steam)


class Mud:  # Грязь
    def __init__(self):
        self.mud = 'Грязь'

    def __str__(self):
        return '{}'.format(self.mud)


class Lightning:  # Молния
    def __init__(self):
        self.lightning = 'Молния'

    def __str__(self):
        return '{}'.format(self.lightning)


class Dust:  # Пыль
    def __init__(self):
        self.dust = 'Пыль'

    def __str__(self):
        return '{}'.format(self.dust)


class Lava:  # Лава
    def __init__(self):
        self.lava = 'Лава'

    def __str__(self):
        return '{}'.format(self.lava)


print(Water(), '+', Air(), '=', Air() + Water())
print(Air(), '+', Water(), '=', Air() + Water())

print(Water(), '+', Fire(), '=', Water() + Fire())
print(Fire(), '+', Water(), '=', Fire() + Water())

print(Water(), '+', Earth(), '=', Water() + Earth())
print(Earth(), '+', Water(), '=', Earth() + Water())

print(Air(), '+', Fire(), '=', Air() + Fire())
print(Fire(), '+', Air(), '=', Fire() + Air())

print(Air(), '+', Earth(), '=', Air() + Earth())
print(Earth(), '+', Air(), '=', Earth() + Air())

print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Earth(), '+', Fire(), '=', Earth() + Fire())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# Зачёт!
