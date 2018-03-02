from random import randint


# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

# вычислите и выведите y

def exercise_1():
    print('\nЗадача-1' + '=' * 10 + '\n')
    equation = 'y = -12x + 11111140.2121'
    x = 2.5
    split_eq = equation.split(' ')[2:]
    if split_eq[1] == '+':
        res = float(split_eq[0][:-1]) * x + float(split_eq[2])
    elif split_eq[1] == '-':
        res = float(split_eq[0][:-1]) * x - float(split_eq[2])
    print(res)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'. Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

def exercise_2():
    print('\nЗадача-2' + '=' * 10 + '\n')
    date = '{:02}.{:02}.{:04}'.format(randint(-9, 32), randint(-9, 13), randint(-9, 10000))
    day = date[:2]
    month = date[3:5]
    year = date[6:]
    res = None
    calendar = {'01': 31,
                '02': 28,
                '03': 31,
                '04': 30,
                '05': 31,
                '06': 30,
                '07': 31,
                '08': 31,
                '09': 30,
                '10': 31,
                '11': 30,
                '12': 31
               }
    if day.isdigit() and month in calendar and 1 <= int(day) <= calendar[month]:
        if month.isdigit() and 1 <= int(month) <= 12:
            if year.isdigit() and 1 <= int(year) <= 9999:
                if len(day) == 2 and len(month) == 2 and len(year) == 4:
                    res = True
                else:
                    res = False
            else:
                res = False
        else:
            res = False
    else:
        res = False

    print('date: {}\nday: {}\nmonth: {}\nyear: {}\nДата {}корректна'.format(date, day, month, year, '' if res else 'не '))

    # Пример корректной даты
    #date = '01.11.1985'

    # Примеры некорректных дат
    #date = '01.22.1001'
    #date = '1.12.1001'
    #date = '-2.10.3001'

# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа,
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

def exercise_3():
    print('\nЗадача-3' + '=' * 10 + '\n')
    i_flat = 0
    number_room = 0
    i_count_room = 1
    input_number = randint(1, 2000000001)
    number_from_left = 0
    flag = False
    while True:
        for b in range(i_count_room):
            number_room += i_count_room
            i_flat += 1
            if number_room >= input_number:
                number_from_left = i_count_room - (number_room - input_number) % i_count_room
                flag = True
                break
        if flag:
            break
        i_count_room += 1

    print('Квартира:{}\nЭтаж: {}\nСлева: {}'.format(input_number, i_flat, number_from_left))


def main():
    #exercise_1()
    #exercise_2()
    exercise_3()
    print('\n' + '=' * 18)


if __name__ == '__main__':
    main()