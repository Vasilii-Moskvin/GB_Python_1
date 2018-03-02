from random import randint
import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
def exercise_1():
    print('\nЗадача-1' + '='*10 + '\n')

    x = randint(1, 100000)
    print('x = {}'.format(x))
    x_str = str(x)

    print(max(x_str))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
def exercise_2():
    print('\nЗадача-2' + '='*10 + '\n')

    a = randint(1, 100) # input('Введите a: ')
    b = randint(1, 100) # input('Введите b: ')

    print('a = {}, b = {}'.format(a, b))

    b, a = a, b

    print('a = {}, b = {}'.format(a, b))

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
def exercise_3():
    print('\nЗадача-3' + '='*10 + '\n')

    a = randint(1, 100) # input('Введите a: ')
    b = randint(1, 100) # input('Введите b: ')
    c = randint(1, 100) # input('Введите b: ')

    print('{} * x^2 + {} * x + {}'.format(a, b, c))

    d = b ** 2 - 4 * a * c
    if d < 0:
	    print('Нет вещественных корней!')
    elif d == 0:
	    x1 = x2 = -b / (2 * a)
	    print('x1 = {}\nx2 = {}'.format(x1, x2))
    else:
	    x1 = (-b + math.sqrt(d)) / (2 * a)
	    x2 = (-b - math.sqrt(d)) / (2 * a)
	    print('x1 = {}\nx2 = {}'.format(x1, x2))


def main():
	exercise_1()
	exercise_2()
	exercise_3()
	print('\n' + '='*18)


if __name__ == '__main__':
	main()