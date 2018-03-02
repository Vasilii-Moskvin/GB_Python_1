from random import randint


# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
def exercise_1():
    print('\nЗадача-1' + '=' * 10 + '\n')

    lst = ["яблоко", "банан", "киви", "арбуз"]
    maxi = len(max(lst, key=lambda x: len(x)))
    for index, src in enumerate(lst, 1):
        print('{}. {:>{}}'.format(index, src, maxi))


# Подсказка: использует метод .format()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
def exercise_2():
    print('\nЗадача-2' + '=' * 10 + '\n')
    lst_1 = [randint(1, 100) for _ in range(0, randint(0, 30))]
    lst_2 = [randint(1, 100) for _ in range(0, randint(0, 30))]
    print('lst_1: {}\nlst_2: {}'.format(lst_1, lst_2))
    print('intersection before: {}'.format(set(lst_1) & set(lst_2)))
    del_lst = list(set(lst_1) & set(lst_2))
    for src in del_lst:
        for _ in range(lst_1.count(src)):
            lst_1.remove(src)
    print('intersection after: {}'.format(set(lst_1) & set(lst_2)))
    print('lst_1: {}\nlst_2: {}'.format(lst_1, lst_2))


# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def exercise_3():
    print('\nЗадача-3' + '=' * 10 + '\n')
    lst_1 = [randint(1, 10) for _ in range(0, randint(0, 10))]
    res = [src / 4 if not src % 2 else src * 2 for src in lst_1]
    print('lst_1: {}\nres: {}'.format(lst_1, res))


def main():
    exercise_1()
    #exercise_2()
    #exercise_3()
    print('\n' + '=' * 18)


if __name__ == '__main__':
    main()
