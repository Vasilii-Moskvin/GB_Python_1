import os
import shutil
import sys


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def exercise_1():
    print('\n{:=^20}'.format('Задача-1'))
    if len(sys.argv) != 2:
        print('usage: python hw05_easy.py {--mk | --rm}')
        sys.exit(1)

    option = sys.argv[1]
    lst_dir = ('dir_{}'.format(i) for i in range(1, 10))
    if option == '--mk':
        for src in lst_dir:
            try:
                os.mkdir(src)
            except OSError as e:
                print(e, src)
    elif option == '--rm':
        for src in lst_dir:
            try:
                shutil.rmtree(src)
            except OSError as e:
                print(e, src)
    else:
        print('usage: python hw05_easy.py {--mk | --rm}')
        sys.exit(1)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def exercise_2():
    print('\n{:=^20}'.format('Задача-2'))
    for src in os.listdir():
        if os.path.isdir(os.path.join(os.getcwd(), src)):
            print(src)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def exercise_3(path_to_file=os.path.realpath(__file__)):
    print('\n{:=^20}'.format('Задача-3'))
    shutil.copy(path_to_file, path_to_file + '.copy')


def py_test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s \n Ожидалось: %s' % (prefix, repr(got), repr(expected)))




def main():
    exercise_1()
    exercise_2()
    exercise_3()
    print('\n' + '=' * 20)


if __name__ == '__main__':
    main()