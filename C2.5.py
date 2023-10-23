from random import randint

class Dot:
    def __init__(self, coord_X, coord_Y):
        self.coord_X = coord_X
        self.coord_Y = coord_Y

    def __eq__(self, other):
        if isinstance(other, Dot):
            return self.coord_X == other.coord_X and self.coord_Y == other.coord_Y
        return False

class Ship:
    def __init__(self, length, bow_dot, ship_direction):
        self.length = length
        self.bow_dot = bow_dot
        self.ship_direction = ship_direction
        self.life_quantity = length

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
    def __init__(self):
        self.field = [['0'] * 6 for _ in range(6)]
        self.ship_lst = []
        self.hid = True
        self.live_ships = 0

    def add_ship(self, ship):
        for dot in ship.dots():
            if self.out(dot) or self.board[dot.coord_X][dot.coord_Y] == '■':
                raise Exception("Эта клетка уже занята")
        for dot in ship.dots():
                self.board[dot.coord_X][dot.coord_Y] = "■"
            self.ship_lst.append(ship)
        self.live_ships += 1

    def out(self, dot):
        if dot.coord_X < 0 or dot.coord_Y < 0 or dot.coord_X >= 6 or dot.coord_Y >= 6:
            return True
        return False

    def contour(self, ship):
        contour_dots = []
        for dot in ship.dots():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_dot = Dot(dot.coord_X + i, dot.coord_Y + j)
                    if self.is_out(new_dot) or new_dot == dot:
                        continue
                    contour_dots.append(new_dot)
        return contour_dots

    def print_board(self):
        print("1 2 3 4 5 6", sep='|')
        for i, row in enumerate(self.field, start=1):
            print(i, *row)

    def make_shot(self, dot):
        if self.out(dot) or self.board[dot.coord_X][dot.coord_Y] == 'T':
            raise Exception("Сюда нельзя сделать выстрел")
        elif self.board[dot.coord_X][dot.coord_Y] == '■':
            self.board[dot.coord_X][dot.coord_Y] = 'X'
            self.live_ships -= 1
        else:
            self.board[dot.coord_X][dot.coord_Y] = 'T'

class BoardOut(Exception):
    pass

class Player:
    def __init__(self, my_board, AI_board):
        self.my_board = my_board
        self.AI_board = AI_board

    def ask(self):

    def board_shot(self, shot_point):
        while True:
            dot = self.ask()
            try:
                board_shot = self.AI_board.shot(dot)
            except BoardOut(Exception) as e:
                print(e)
            else:
                return board_shot

    def move(self):
        self.ask()

class AI:
    def ask(self):
        coord_X = random.randint(0, 6)
        coord_Y = random.randint(0, 6)
        return Dot(coord_X, coord_Y)

class User:
    def ask(self):
        coord_X = int(input("Введите координату х: "))
        coord_Y = int(input("Введите координату у: "))
        return Dot(coord_X, coord_Y)

class Game:
    def __init__(self, User_field, AI_field):
        self.User_field = User_field
        self.AI_field = AI_field
        user = User()
        ai = AI()
        self.user_ships = self.random_board()
        self.ai_ships = self.random_board()

    def random_board(self):
        ships = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        for length in ships:
            while True:
                coord_X = random.randint(0, 6)
                coord_Y = random.randint(0, 6)
                direction = random.choice(['vertical', 'horizontal'])
                dot_list = []
                for i in range(length):
                    if direction == 'horizontal':
                        dot = Dot(coord_X+ i, coord_Y)
                    else:
                        dot = Dot(coord_X, coord_Y + i)
                    if board.out(dot):
                        break
                    dot_list.append(dot)
                else:
                    board.add_ship(dot_list)
                    break
        return board

    def greet(self):
        print("Начинаем игру 'Морской бой'!")

    def loop(self):
        variable = Board()
        while True:
            print("Поле игрока:")
            print(self.user.field.print_table())
            print("Поле компьютера:")
            print(self.ai.field.print_table())

            user_shot = self.user.move()
            ai_shot = self.ai.move()

            if user_shot:
                print("Попадание игрока!")
            else:
                print("Промах игрока!")

            if ai_shot:
                print("Попадание ИИ!")
            else:
                print("Промах ИИ!")

            if self.user.my_board.field.count(1) == 0:
                print("ИИ победил!")
                break
            elif self.ai.my_board.field.count(1) == 0:
                print("Игрок победил!")
                break

    def start(self):
        self.greet()
        self.loop()

    game = Game()
    game.start()