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
    def __init__(self, field, ship_lst, hid, live_ships):
        self.field = [['0'] * 6 for _ in range(6)]
        self.ship_lst = []
        self.hid = hid
        self.live_ships = live_ships

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot):
                raise Exception
            else:
                for dot in ship.dots:
                    self.field[dot.x][dot.y] = "■"
            self.ship_lst.append(ship)

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
                    if self.is_out(new_dot) or new_dot == dot:
                        continue
                    contour_dots.append(new_dot)
        return contour_dots

    def print_board(self):
        print("1 2 3 4 5 6", sep='|')
        for i, row in enumerate(self.field, start=1):
            print(i, *row)

    def make_shot(self, dot, shot):
        try:
            if dot <= 0 or dot >= 6:
                except Exception as e:
            print(e)
        try:
            elif dot == "X":
            except ShotError as e:
        print("Сюда нельзя произвести выстрел")
        elif x or y== 0 and shot == "T":
        print("Промах")
        return False

        elif dot == "X":
        for ship in ship_lst:
        x += 1
        y += 1
        elif ship_health == 0:
        print("Корабль потоплен")
        return True
        else:
        print("Корабль ранен")
        return True


class Player:
    def __init__(self, my_board, AI_board):
        self.my_board = my_board
        self.AI_board = AI_board

    def ask(self):
        pass

    def board_shot(self, shot_point):
        try:

        except Exception as e:
            print(e)

    def move(self):
        self.ask()


class AI:
    def ask(self):
        print("В какую клетку сделать выстрел?")


class User:
    def ask(self):
        print("В какую клетку сделать выстрел?")


human = Ship()
computer = Ship()


class Game:
    def __init__(self, User_field, AI_field):
        self.User_field = User_field
        self.AI_field = AI_field
        user = User()
        ai = AI()

    def random_board(self):
        pass

    def greet(self):
        print("Добро пожаловать в игру Морской бой!")

    def loop(self):
        self.mode

    def start(self):
        self.greet("")
        self.loop("")

    Game = Game()
    Game.start
