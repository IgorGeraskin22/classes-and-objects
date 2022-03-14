import simple_draw as sd

sd.resolution = (1000, 700)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


# class Snowflake:
#
#     def __init__(self):
#         self.x = sd.random_number(50, 950)
#         print('X-randint = ', self.x)
#         self.y = sd.random_number(500, 600)
#         print('Y - randint = ', self.y)
#         self.beam_length = sd.random_number(7, 25)
#         print('Длина снежинки = ', self.beam_length)
#
#     def move(self):
#         print('--------------------Перемещение-------------------------------')
#         print('Y на входе = ', self.y)
#         self.y -= 30
#         print('Y - 10  на входе = ', self.y)
#         print('-' * 100)
#
#     def draw(self, color):
#         print('--------------------Рисование-------------------------------')
#         point = sd.get_point(self.x, self.y)
#         print('point = ', point)
#         sd.snowflake(point, length=self.beam_length, color=color)
#         print('-' * 100)
#
#     def can_fall(self):
#         print('--------------------Функция def can_fall(self): -------------------------------')
#         print('self.y = ', self.y)
#         while self.y > 100:
#             print('-' * 100)
#             return True
#
#
# flake = Snowflake()
#
##
# while True:
#
#     flake.draw(sd.background_color)
#     flake.move()
#     if not flake.can_fall():
#         flake = Snowflake()
#     flake.draw(sd.COLOR_WHITE)
#     print('-' * 100)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         print('-' * 100)
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
N = 5


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(50, 950)
        print('---------------------Вызов class Snowflake-----------------------------------------')
        print('X-randint = ', self.x)
        self.y = sd.random_number(500, 700)
        print('Y - randint = ', self.y)
        self.beam_length = sd.random_number(7, 25)
        print('Длина снежинки = ', self.beam_length)
        print('-' * 100)

    def draw(self, color):
        print('--------------------Метод рисование-------------------------------')
        point = sd.get_point(self.x, self.y)
        print('point = ', point)
        print('Цвет', color)
        print('Какой объект - ', flake)
        sd.snowflake(point, length=self.beam_length, color=color)
        print('-' * 100)

    def move(self):
        print('--------------------Метод перемещение-------------------------------')
        print('Y на входе = ', self.y)
        self.y -= 10
        print('Y - 10  на выходе = ', self.y)
        print('Какой объект - ', flake)
        print('-' * 100)

    def can_fall(self):
        print('--------------------Метод проверки def can_fall(self): -------------------------------')
        print('self.y = ', self.y)
        print('Какой объект - ', flake)
        return self.y > 10


def get_flakes(count):
    snowflake = []
    for _ in range(count):
        snowflake.append(Snowflake())
    print('---------------------------------Функция создания объктов -------------------------------------')
    print('Добавлено в список snowflake объектов = [] - ', snowflake)
    return snowflake


flakes = get_flakes(N)


def get_fallen_flakes():
    fallen_snowflakes = []
    if not flake.can_fall():
        fallen_snowflakes.append(flake)
        number = len(fallen_snowflakes)
        print('---------------------------------Функция проверки -------------------------------------')
        print('Добавлено в список  snowf_l объектов  =  ', fallen_snowflakes)
        print('Количество добавленных объектов', number)
        print('-' * 100)
        return number


def append_flakes(number, snowflake):
    for _ in range(number):
        snowflake.append(Snowflake())

    print('---------------------------------Функция добавления append_flakes -------------------------------------')
    print('Добавлен в список snowflake - ', snowflake)


while True:
    for flake in flakes:
        flake.draw(sd.background_color)
        if flake.can_fall():
            flake.move()
            flake.draw(sd.COLOR_WHITE)
            fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало

            if fallen_flakes:
                append_flakes(fallen_flakes, flakes)  # добавить еще сверху

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# Зачёт!
