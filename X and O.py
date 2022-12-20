

a = [['-']*3 for _ in range(3)]
def show_field(f):
    print('  0 1 2')
    for i in range(len(a)):
        print(str(i), *a[i])

def input_user1():
    while True:
        x1 = input('Первый игрок х1:')
        y1 = input('Первый игрок y1:')
        if not(x1.isdigit() and y1.isdigit()):
            print('Введите числа')
            continue
        x1 = int(x1)
        y1 = int(y1)
        if not(x1>=0 and x1<3 and y1>=0 and y1<3):
            print('Вышли из диапазона')
            continue
        if a[x1][y1] != '-':
            print('клетка занята')
            continue
        if x1 =='0' or x1 =='1' or x1 == '2':
            x1 = int(x1)
            continue
        break
    return x1,y1
def input_user2():
    while True:
        x1 = input('Второй игрок х2:')
        y1 = input('Второй игрок y2:')
        if not(x1.isdigit() and y1.isdigit()):
            print('Введите числа')
            continue
        x1 = int(x1)
        y1 = int(y1)
        if not(x1>=0 and x1<3 and y1>=0 and y1<3):
            print('Вышли из диапазона')
            continue
        if a[x1][y1] != '-':
            print('клетка занята')
            continue
        if x1 =='0' or x1 =='1' or x1 == '2':
            x1 = int(x1)
            continue
        break
    return x1,y1

def check_winner_1(a):
    if ((a[0][0] == 'x' and a[1][1] == 'x' and a[2][2] == 'x') or \
        (a[0][2] == 'x' and a[1][1] == 'x' and a[2][0] == 'x') or \
        (a[0][0] == 'x' and a[0][1] == 'x' and a[0][2] == 'x') or \
        (a[1][0] == 'x' and a[1][1] == 'x' and a[1][2] == 'x') or \
        (a[2][0] == 'x' and a[2][1] == 'x' and a[2][2] == 'x') or \
        (a[0][0] == 'x' and a[1][0] == 'x' and a[2][0] == 'x') or \
        (a[0][1] == 'x' and a[1][1] == 'x' and a[2][1] == 'x') or \
        (a[0][2] == 'x' and a[1][2] == 'x' and a[2][2] == 'x')):
            print('Первый игрок одержал победу')
            return True
    return False
def check_winner_2(a):
    if ((a[0][0] == '0' and a[1][1] == '0' and a[2][2] == '0') or \
        (a[0][2] == '0' and a[1][1] == '0' and a[2][0] == '0') or \
        (a[0][0] == '0' and a[0][1] == '0' and a[0][2] == '0') or \
        (a[1][0] == '0' and a[1][1] == '0' and a[1][2] == '0') or \
        (a[2][0] == '0' and a[2][1] == '0' and a[2][2] == '0') or \
        (a[0][0] == '0' and a[1][0] == '0' and a[2][0] == '0') or \
        (a[0][1] == '0' and a[1][1] == '0' and a[2][1] == '0') or \
        (a[0][2] == '0' and a[1][2] == '0' and a[2][2] == '0')):
            print('Второй игрок одержал победу')
            return True
    return False

k = 0
while True:
    # ----------------------------------------------------------------------------------------------------------
    print('Первый игрок, твой ход')
    x1, y1 = input_user1()
    a[x1][y1] = 'x'
    show_field(a)
    if check_winner_1(a):
        break
    k += 0.5
    # ----------------------------------------------------------------------------------------------------------
    if k == 4.5:
        print('Ничья')
        break
    print('второй игрок, твой ход')
    x2, y2 = input_user2()
    a[x2][y2] = '0'
    show_field(a)
    if check_winner_2(a):
        break
    k += 0.5

















