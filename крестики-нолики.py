pole = [i for i in range(1, 10)]
win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def show_pole():
    for i in range(3):
        print(f'{pole[0 + i * 3]} | {pole[1 + i * 3]} | {pole[2 + i * 3]}')


def mark_input(m):
    while True:
        a = int(input(f'Куда поставить {m}?  '))
        if a < 1 or a > 9:
            print('Число должно быть от 1 до 9')
            continue
        elif str(pole[a - 1]).isalpha():
            print('Эта клетка уже занята. Выберите другую цифру')
            continue
        else:
            pole[a - 1] = m
            break


def check():
    for n in win:
        if pole[n[0]] == pole[n[1]] == pole[n[2]]:
            return pole[n[1]]
    else:
        return False


s = 0
while True:
    show_pole()
    if s % 2 == 0:
        mark_input('X')
    else:
        mark_input('O')
    if s > 3:
        winner = check()
        if winner:
            show_pole()
            print(f'Победа за {winner}!')
            break
    s += 1
    if s > 8:
        show_pole()
        print('Ничья')
        break
