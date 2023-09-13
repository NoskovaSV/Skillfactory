def make_board(field):
    print("_____")
    print(*field[0:3],sep='|')
    print("_____")
    print(*field[3:6],sep='|')
    print("_____")
    print(*field[6:9],sep='|')
    print("_____")


def put_mark():
    while True:
        a = input("Куда поставим отметку?")
        if not a.isdigit():
            print("Вводите только цифры")
            a=int(a)
            continue
        if a<=0 or a>=10:
            print("Введите число в диапазоне от 1 до 9:")
            continue
        return a-1

def check_win(field):
    win_notes=(
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8),(2,4,6)
        )
    for i in win_notes:
        if field[i[0]]==field[i[1]]==field[i[2]]:
            return field[i[0]]

def main_board():
    counter=0
    field=list(range(1,10))
    while True:
        make_board(field)
        if counter%2==0:
            mark="X"
        else:
            mark="0"
            turn=put_mark()
            if isinstance(field[turn], int):
                field[turn]=mark
                counter+=1
                if counter>4:
                    tmp=check_win(field)
                    if tmp:
                        print(tmp,"выиграл!")
                        break
                    if counter==9:
                        print("Ничья!")
                        break
                    print("Конец игры")

