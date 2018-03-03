import os
import shutil
import hw05_easy as hw

# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py

def print_menu():
    print('\n{:=^20}'.format('Меню'))
    print('''1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку''')
    print('='*20)


def exercise_1():
    print('\n{:=^20}'.format('Задача-1'))
    ans = None
    while ans != 'q':
        print_menu()
        ans = input('Enter the number (to exit press "q"):\n')
        if ans == '1' or ans == '3' or ans == '4':
            path_to_dir = os.path.abspath(input('Enter the path to directory:\n'))
        if ans == '1':
            try:
                os.chdir(path_to_dir)
            except OSError as e:
                print('Невозможно перейти в {}'.format(path_to_dir))
            else:
                print('Успешно перешел в {}'.format(path_to_dir))
        elif ans == '2':
            for src in os.listdir():
                print(src)
        elif ans == '3':
            try:
                shutil.rmtree(path_to_dir)
            except OSError as e:
                print('Невозможно удалить {}\n{}'.format(path_to_dir, e))
            else:
                print('Успешно удалено {}'.format(path_to_dir))
        elif ans == '4':
            try:
                os.mkdir(path_to_dir)
            except OSError as e:
                print('Невозможно создать {}'.format(path_to_dir))
            else:
                print('Успешно создано {}'.format(path_to_dir))



def py_test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s \n Ожидалось: %s' % (prefix, repr(got), repr(expected)))




def main():
    exercise_1()
    print('\n' + '=' * 20)


if __name__ == '__main__':
    main()