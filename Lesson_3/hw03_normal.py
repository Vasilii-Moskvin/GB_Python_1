# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
from random import randint
from math import sqrt
import matplotlib.pyplot as plt

def fibonacci(n, m):
    a = b = 1
    res = []
    for i in range(1, m + 1):
        if n <= i:
            res.append(a)
        b, a = a + b, b
    return res

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    length_lst = len(origin_list)
    i = 0
    #print('raw_lst: {}'.format(origin_list))
    while i < length_lst:
        temp = origin_list[0]
        for index, src in enumerate(origin_list[1:length_lst - i], 1):
            if temp > src:
                origin_list[index], origin_list[index - 1] = origin_list[index - 1], origin_list[index]
            else:
                temp = src
        i += 1
    #print('new_lst: {}'.format(origin_list))

    return origin_list



# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, lst):
    return [src for src in lst if func(src)]

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a, b, c, d):
    length_points = lambda x_i, y_i: sqrt(sum(map(lambda x, y: (x - y) ** 2, x_i, y_i)))
    if length_points(a, b) == length_points(c, d) and length_points(b, c) == length_points(a, d):
        if (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0]) == 0:
            return True
        else:
            return False
    else:
        return False


def main():
    print()
    print(fibonacci(4, 10))
    sort_to_max([randint(-100, 100) for _ in range(randint(0, 100))])
    my_filter(lambda x: x == 0, [randint(-100, 100) for _ in range(randint(0, 100))])
    for _ in range(100000):
        points = [(randint(-10, 10), randint(-10, 10)) for _ in range(4)]
        if is_parallelogram(*points):
            print(True, end=': ')
            plt.plot(*list(zip(*points)), linestyle='-', marker='.', color='red', markersize=10)
            plt.show()
            plt.close()
        else:
            print(False, end=': ')
        print(points)






if __name__ == '__main__':
    main()