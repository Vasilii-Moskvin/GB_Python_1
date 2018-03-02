from collections import namedtuple, OrderedDict
from random import randint, choice
import fractions
import math

Worker = namedtuple('Worker', ('name', 'surname', 'salary', 'post', 'norma'))
Hour = namedtuple('Hour', ('name', 'surname', 'hour'))

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3

def generate_frac():
    n = randint(-100, 100)
    n = '{}'.format(n) if n else ''

    y = randint(1, 100)
    if n:
        x = randint(0, y - 1)
    else:
        x = randint(-100, 100)

    if x:
        x = '{}'.format(x)
        y = '{}'.format(y)
        xy = ' {}/{}'.format(x, y)
    else:
        xy = ''

    if not n and not x:
        res = '0'
    else:
        res = '{}{}'.format(n, xy)

    return res


def check_Fr(temp_a_lst):
    chek_Fr_a = None
    if len(temp_a_lst) == 2:
        if temp_a_lst[0][0] == '-':
            chek_Fr_a = -1 * (fractions.Fraction(temp_a_lst[0][1:]) + fractions.Fraction(temp_a_lst[1]))
        else:
            chek_Fr_a = fractions.Fraction(temp_a_lst[0]) + fractions.Fraction(temp_a_lst[1])
    elif len(temp_a_lst) == 1:
        chek_Fr_a = fractions.Fraction(temp_a_lst[0])

    return chek_Fr_a

def check_Fr_1(temp_a_lst):
    res = None
    if len(temp_a_lst) == 2:
        y_num, y_div = tuple(map(int, temp_a_lst[1].split('/')))
        if temp_a_lst[0][0] == '-':
            x = -1 * (int(temp_a_lst[0][1:]) * y_div + y_num)
        else:
            x = int(temp_a_lst[0]) * y_div + y_num
        res = '{}/{}'.format(x, y_div)
    elif len(temp_a_lst) == 1:
        if '/' in temp_a_lst[0]:
            res = temp_a_lst[0]
        else:
            res = '{}/1'.format(temp_a_lst[0])

    return res

def opera(a, oper, b):
    num_a, div_a = tuple(map(int, a.split('/')))
    num_b, div_b = tuple(map(int, b.split('/')))

    div_all = div_a * div_b
    if oper == '+':
        num = num_a * div_b + num_b * div_a
    else:
        num = num_a * div_b - num_b * div_a

    res = '{}/{}'.format(num, div_all)
    return res

def gen_eq():
    a = generate_frac()
    b = generate_frac()
    oper = choice([' + ', ' - '])
    eq = '{}{}{}'.format(a, oper, b)

    return eq


def exercise_1(eq):
    #print('\nЗадача-1' + '=' * 10 + '\n')


    lst_eq = eq.split()
    index_sep = lst_eq.index('-') if '-' in lst_eq else lst_eq.index('+')
    temp_a_lst = lst_eq[:index_sep]
    oper = lst_eq[index_sep]
    temp_b_lst = lst_eq[index_sep + 1:]
    #print('eq: {}\n'.format(eq))
    # print('{} {} {}\n'.format(temp_a_lst, oper, temp_b_lst))

    chek_Fr_a = check_Fr(temp_a_lst)
    chek_Fr_b = check_Fr(temp_b_lst)

    if oper == '+':
        c_Fr = chek_Fr_a + chek_Fr_b
    elif oper == '-':
        c_Fr = chek_Fr_a - chek_Fr_b

    str_res = str(c_Fr)
    str_res = get_result(str_res)

    return str_res


def get_result(str_res):
    if '/' in str_res:
        num, div = tuple(map(int, str_res.split('/')))
        if num > 0:
            int_part = int(num // div)
            frac_part = int(num % div)
        elif num < 0:
            int_part = -int(-num // div)
            frac_part = int(-num % div)
        else:
            int_part = 0
            frac_part = 0
            frac = ''
        if frac_part:
            my_gcd = fractions.gcd(frac_part, div)
            if my_gcd != 1:
                frac_part = int(frac_part / my_gcd)
                div = int(div / my_gcd)
            frac = ' {}/{}'.format(frac_part, div)
            if int_part == 0:
                int_part = ''

        else:
            frac = ''
    else:
        int_part = str_res
        frac = ''
    str_res = '{}{}'.format(int_part, frac)

    # print(str_res)

    return str_res

def exercise_1_1(eq):
    #print('\nЗадача-1' + '=' * 10 + '\n')
    # eq = gen_eq()

    lst_eq = eq.split()
    index_sep = lst_eq.index('-') if '-' in lst_eq else lst_eq.index('+')
    temp_a_lst = lst_eq[:index_sep]
    oper = lst_eq[index_sep]
    temp_b_lst = lst_eq[index_sep + 1:]
    #print('eq: {}\n'.format(eq))
    # print('{} {} {}\n'.format(temp_a_lst, oper, temp_b_lst))

    chek_Fr_a_1 = check_Fr_1(temp_a_lst)
    chek_Fr_b_1 = check_Fr_1(temp_b_lst)

    str_res = opera(chek_Fr_a_1, oper, chek_Fr_b_1)

    frac = None
    str_res = get_result(str_res)

    return str_res






# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def exercise_2():
    print('\nЗадача-2' + '=' * 10 + '\n')

    with open('data/workers', 'r', encoding='utf-8') as f:
        workers = [Worker(*map(lambda x: int(x) if x.isdigit() else x, line.strip().split())) for line in f]
        workers.pop(0)

    with open('data/hours_of', 'r', encoding='utf-8') as f:
        hours = [Hour(*map(lambda x: int(x) if x.isdigit() else x, line.strip().split())) for line in f]
        hours.pop(0)

    for worker in workers:
        hour = list(filter(lambda x: x.name == worker.name and x.surname == worker.surname, hours))[0]
        delta = hour.hour - worker.norma
        selary = ((worker.norma - math.fabs(delta)) / worker.norma) * worker.salary if delta < 0 \
                                                        else worker.salary + 2 * (worker.salary / worker.norma) * delta

        print('{:<10} {:<10} отработал: {:<3} по норме {:<3} часов.'
              ' Оклад: {:>7.02f} руб, Зарплата: {:>7.02f} руб.'.format(worker.name,
                                                                      worker.surname,
                                                                      hour.hour,
                                                                      worker.norma,
                                                                      worker.salary,
                                                                      selary))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
def exercise_3():
    print('\nЗадача-3' + '=' * 10 + '\n')
    with open('data/fruits.txt', 'r', encoding='utf-8') as f:
        data = [line for line in f]

    for _ in range(data.count('\n')):
        data.remove('\n')
    data.sort(key=lambda x: x[0])
    dict_fruits = OrderedDict()
    for fruit in data:
        if fruit[0].upper() not in dict_fruits:
            dict_fruits[fruit[0].upper()] = [fruit]
        else:
            dict_fruits[fruit[0].upper()].append(fruit)

    for litera, fruits in dict_fruits.items():
        with open('data/fruit_{}'.format(litera), 'w', encoding='utf-8') as w:
            w.writelines(fruits)

def main():
    # for _ in range(1000000):
    #     eq = gen_eq()
    #     e_1 = exercise_1(eq)
    #     e_1_1 = exercise_1_1(eq)
    #     if e_1 != e_1_1:
    #         print('Error:\neq: {}\nFr: {}\nmy: {}'.format(eq, e_1, e_1_1))
    #     if len(e_1_1.split()) == 1:
    #         print(e_1_1)


    #exercise_2()
    exercise_3()
    print('\n' + '=' * 18)


if __name__ == '__main__':
    main()