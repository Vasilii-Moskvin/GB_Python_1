# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def cp_func():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        file_path = os.path.abspath(file_name)
        shutil.copy(file_path, file_path + '.copy')
    except OSError as e:
        print(e)


def rm_func():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.abspath(file_name)
    if not os.path.isfile(file_path):
        print("Необходимо указать вторым параметром имя файла, а не каталога")
        return
    ans = None
    while ans != 'n' and ans != 'y':
        ans = input('Вы действительно хотите удалить файл (y - да, n - нет) {}:\n'.format(file_path))

    if ans == 'y':
        try:
            os.remove(file_path)
            print('Успешно удалён файл {}'.format(file_path))
        except OSError as e:
            print('Не удалось удалить файл {}'.format(file_path))


def cd_func():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_name)
    except OSError as e:
        print('Невозможно перейти в {}'.format(dir_name))
    else:
        print('Успешно перешел в {}'.format(dir_name))


def ls_func():
    print(os.path.abspath('.'))


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_func,
    "rm": rm_func,
    "cd": cd_func,
    "ls": ls_func
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
