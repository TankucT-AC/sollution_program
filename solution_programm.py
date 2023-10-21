from bext import title
import os
from math import pi, sqrt, sin


# №1 – функции ввода
def variable_x(x):
    true = True
    while true:
        try:
            x = float(x)
            if x > 0:
                true = False
            else:
                print(' Введите число, большее, чем ноль')
        except ValueError:
            print(" NaN_Error: Введите число")
        if true:
            x = input(' ')
    return x


# функция variable_abc() нужна лишь для ввода параметров квадратичного уравнения
def variable_abc(x):
    true = True
    while true:
        try:
            x = float(x)
            true = False
        except ValueError:
            print(" NaN_Error: Введите число")
        if true:
            x = input(' ')
    return x


def grad_to_rad(grad):
    return grad / 360 * pi * 2


def get_valid_answer():
    answer = input(" Хотите что-то ещё вычислить? (да/нет): ").lower()
    while answer not in ("да", "нет"):
        answer = input(" Просто ответьте \"да\" или \"нет\": ").lower()
    print()
    return False if answer == "нет" else True


# №2 – блок запуска и очистки экрана:
def print_board():
    clear_screen()
    print()
    print(" ---------------------------------------------------------------------------------------")
    print(" |Здравствуйте! Вас приветствует программа по вычислению значений из уравнений и формул|")
    print(' ---------------------------------------------------------------------------------------')
    print(' + Вот что я могу решить:                                                              +')
    print(' | 1. Квадратное уравнение                                                             |')
    print(' | 2. Формула площади                                                                  |')
    print(' + 3. Формула объёма                                                                   +')
    print(' *-------------------------------------------------------------------------------------*')
    index = input(" Выберите число рядом с видом функции:")

    while index != "1" and index != "2" and index != "3":
        print("Это нелегальная функция")
        index = input()
    if index == "1":
        block_1()
    if index == "2":
        block_2()
    if index == "3":
        block_3()


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# №3 – функциональный блок:

# блок 1
def block_1():
    print()
    print(' ax² + bx + c = 0')
    print()
    a = variable_abc(input(' Введите первое число вашего уравнения:'))
    b = variable_abc(input(' Введите второе число вашего уравнения:'))
    c = variable_abc(input(' Введите третье число вашего уравнения:'))

    d = b ** 2 - 4 * a * c

    if d < 0:
        print(" Пустое множество (корней нет)")
    elif d == 0:
        if a != 0:
            x = -b / (2 * a)
            print(f" Корнем уравнения является {x}")
        elif a != 0 and b == 0:
            x = 0
            print(f" Корнем уравнения является {x}")

        else:
            print(" Это не квадратное уравнение!")

    elif d > 0:
        try:
            x1 = (sqrt(d) - b) / (2 * a)
            x2 = (-(sqrt(d) + b)) / (2 * a)
            print(" Корнями являются %f и %f" % (x1, x2))
        except ZeroDivisionError:
            try:
                x = b / c
                print(f" Корнем уравнения является {x}")
            except ZeroDivisionError:
                print(" Корень уравнения - ноль")


# блок 2
def block_2():
    print(' _-----------------------------------------------------------------------------------_')
    print(' + 1.Прямоугольник                                                                   +')
    print(' | 2.Треугольник                                                                     |')
    print(' | 3.Квадрат                                                                         |')
    print(' + 4.Трапеция                                                                        +')
    print(' *-----------------------------------------------------------------------------------*')
    f = {'1': 'ab', '3': 'a²', '4': '0,5(a+b)h'}

    functions = [str(i) for i in range(1, 5)]

    while True:
        command = input(" Введите номер фигуры, площадь которой хотите найти:")
        search = [functions[i].find(command) for i in range(4)]
        if sum(search) == -4:
            print(' Данной функции не существует!')
        else:
            break

    if int(command) != 2:
        print(f' Формула: S = {f[command]}')

    if command == '1':
        a = variable_x(input(' Введите длину:'))
        b = variable_x(input(' Введите ширину:'))

        S = a * b
        print(f" Площадь прямоугольника равна {S}")
    elif command == '2':
        block_2_1()

    elif command == '3':
        a = variable_x(input(' Введите ребро квадрата:'))
        S = a ** 2
        print(f' Площадь квадрата равна {S}')
    else:
        a = variable_x(input(' Введите первое основание трапеции:'))
        b = variable_x(input(' Введите второе основание трапеции:'))
        h = variable_x(input(' Введите высоту трапеции:'))
        S = (a + b) * h / 2
        print(f' Площадь трапеции равна {S}')


def block_2_1():
    d = {'1': '√(p(p-a)(p-b)(p-c))', '2': '0,5ah', '3': '0,5ab×sin(c)'}
    print(' _~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_')
    print(" + 1.Формула Герона                                                                  +")
    print(" + 2.По стороне и её высоте                                                          +")
    print(" + 3.По синусу угла между двумя смежными сторонами                                   +")
    print(' *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')

    functions = [str(i + 1) for i in range(3)]
    while True:
        var = input(' Выберите способ нахождения площади треугольника: ')
        search = [functions[i].find(var) for i in range(3)]
        if sum(search) == -3:
            print(' Данной функции не существует!')
        else:
            break

    print(f'Формула: S = {d[var]}')
    if var == '1':

        a = variable_x(input(' Введите первую сторону треугольника:'))
        b = variable_x(input(' Введите вторую сторону треугольника:'))
        c = variable_x(input(' Введите третью сторону треугольника:'))

        data = sorted([a, b, c])
        if data[2] >= data[0] + data[1]:
            print(' Такого треугольника не существует!')
        else:
            p = (a + b + c) / 2
            S = sqrt(p * (p - a) * (p - b) * (p - c))
            print(f' Площадь треугольника равна {S}')

    elif var == '2':
        a = variable_x(input(' Введите длину основания:'))
        h = variable_x(input(' Введите высоту основания:'))
        S = 0.5 * a * h
        print(f' Площадь треугольника равна {S}')
    else:
        a = variable_x(input(' Введите первую сторону угла:'))
        b = variable_x(input(' Введите вторую сторону угла:'))
        corner = variable_x(input(' Введите угол:'))

        sinus = sin(grad_to_rad(corner))
        S = 0.5 * a * b * sinus
        print(f' Площадь треугольника равна {S}')


# блок 3
def block_3():
    print(' _~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_')
    print(" + 1.Параллелепипед                                                                  +")
    print(" ! 2.Куб                                                                             !")
    print(" | 3.Тетраэдр                                                                        |")
    print(" ! 4.Пирамида                                                                        !")
    print(" | 5.Конус                                                                           |")
    print(" ! 6.Цилиндр                                                                         !")
    print(" + 7.Сфера                                                                           +")
    print(' *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')

    f = {'1': 'abc', '2': 'a³', '3': '(S×h):3', '4': '(abh):3', '5': '(πr²h):3', '6': 'πr²h', '7': '(4πr³):3'}

    functions = [str(i + 1) for i in range(7)]

    while True:
        command = input(" Введите номер фигуры, объём которой хотите найти:")
        search = [functions[i].find(command) for i in range(6)]
        if sum(search) == -7:
            print(' Данной функции не существует!')
        else:
            break

    print(f' Формула: V = {f[command]}')

    if command == "1":
        a = variable_x(input(" Введите длину:"))
        b = variable_x(input(" Введите ширину:"))
        h = variable_x(input(" Введите высоту:"))
        V = a * b * h
        print(f" Объём параллелепипеда равен {V}")

    elif command == "2":
        a = variable_x(" Введите длину ребра куба:")
        V = a ** 3

        print(f" Объём куба равен {V}")

    elif command == "3":
        S = variable_x(input(" Введите площадь основания тетраэдра:"))
        h = variable_x(input(" Введите высоту тетраэдра:"))
        V = (S * h) / 3
        print(f" Объём тетраэдра равен {V}")

    elif command == "4":
        a = variable_x(input(" Введите длину основания пирамиды:"))
        b = variable_x(input(" Введите ширину основания пирамиды:"))
        h = variable_x(" Введите высоту пирамиды:")
        V = (a * b * h) / 3
        print(f" Объём пирамиды равен {V}")

    elif command == "5":
        r = variable_x(input(" Введите радиус основания"))
        h = variable_x(input(" Введите высоту конуса:"))

        V = (pi * (r ** 2) * h) / 3
        print(f" Объём конуса равен {V}")

    elif command == "6":
        r = variable_x(input(" Введите радиус основания:"))
        h = variable_x(input(" Введите высоту цилиндра:"))
        V = (pi * (r ** 2) * h)
        print(f" Объём цилиндра равен {V}")

    elif command == "7":
        r = variable_x(input(" Введите радиус шара:"))
        V = (4 * pi * (r ** 3)) / 3
        print(f" Объём шара равен {V}")


def main():
    title("solution_program.py")
    wants_to_work = True
    while wants_to_work:
        print_board()
        wants_to_work = get_valid_answer()
        if not wants_to_work:
            input('Нажмите на ENTER, чтобы выйти')


main()
