import random

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Dot):
            return self.x == other.x and self.y == other.y
        return False

class Ship:
    def __init__(self, length, bow_dot, ship_direction, life_quantity):
        self.length = length
        self.bow_dot = bow_dot
        self.ship_direction = ship_direction
        self.life_quantity = life_quantity

    def dots(self):
        dot_list = []

        for i in range(self.length):
            if self.ship_direction == 'vertical':
                dot = Dot(self.bow_dot.x + i, self.bow_dot.y)
            else:
                dot = Dot(self.bow_dot.x, self.bow_dot.y + i)
            dot_list.append(dot)
        return dot_list


class Board:
    def __init__(self, hid, live_ships):
        self.field = [['0'] * 6 for _ in range(6)]
        self.ship_lst = []
        self.hid = hid
        self.live_ships = live_ships

    def add_ship(self, ship):
        ship.dots()
        for dot in ship.dots:
            if self.out(dot):
                raise Exception
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (dot.x + i, dot.y + j):
                    raise Exception
            if dot.x and dot.y in self.ship_lst:
                self.ship_lst.append(ship)
                print("■")

    def out(self, dot):
        if dot.x < 0 or dot.y < 0 or dot.x >= 6 or dot.y >= 6:
            return True
        return False

    def contour(self, ship):
        contour_dots = []
        for dot in ship.dots():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_dot = Dot(dot.x + i, dot.y + j)
                    if self.out(new_dot) or new_dot == dot:
                        continue
                    contour_dots.append(new_dot)
        return contour_dots

    def print_board(self):
        print("1 2 3 4 5 6", sep='|')
        for i, row in enumerate(self.field, start=1):
            print(i, *row)

    def make_shot(self, shot):
        if self.out:
            raise Exception
        elif self.field[dot.x][dot.y] == "T":
            raise Exception
        elif self.field[dot.x][dot.y] == '■':
            self.field[dot.x][dot.y] = "X"
            self.live_ships -= 1
        else:
            self.field[dot.x][dot.y] = "T"


class Player:
    def __init__(self, my_board, AI_board):
        self.my_board = my_board
        self.AI_board = AI_board

    def ask(self):
        pass

    def move(self):
        self.ask()

    def board_shot(self, shot_point):
        if shot_point == "T":
            raise Exception
        elif shot_point == "X":
            for dot in ship.dots():
                print("Корабль подбит. Сделайте повторный выстрел!")
            return True


class AI(Player):
    def ask(self):
        print("В какую клетку ИИ сделает выстрел?")


class User(Player):
    def ask(self):
        print("В какую клетку игрок сделает выстрел?")


class Game:
    def __init__(self, User_field, AI_field):
        self.User_field = User_field
        self.AI_field = AI_field
        user = User()
        ai = AI()

    def random_board(self):
        random.randint(1, 36)
        while dot in self.field == "X":
            dot = dot + 1
        else:
            print("На эту доску невозможно поставить корабль")


def greet(self):
    print("Добро пожаловать в игру Морской бой!")


def loop(self):
    self.mode()

    class Ai(Player):
        def verify(self):
            super().verify()
            if self.live_ships == 0:
                print("ИИ выиграл!")

    class User(Player):
        def verify(self):
            super().verify()

        if self.live_ships == 0:
            print("Игрок выиграл!")


def start(self):
    self.greet()
    self.loop()


new_game = Game()
Game.start()
