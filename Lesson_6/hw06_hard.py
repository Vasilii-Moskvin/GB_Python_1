from collections import namedtuple
import math

Worker = namedtuple('Worker', ('name', 'surname', 'salary', 'post', 'norma'))
Hour = namedtuple('Hour', ('name', 'surname', 'hour'))


pattern = '{:<10} {:<10} отработал: {:<3} по норме {:<3} часов. Оклад: {:>7.02f} руб, Зарплата: {:>7.02f} руб.'



def exercise_1_old():

    with open('data/workers', 'r', encoding='utf-8') as f:
        workers = [Worker(*map(lambda x: int(x) if x.isdigit() else x, line.strip().split())) for line in f]
        workers.pop(0)

    with open('data/hours_of', 'r', encoding='utf-8') as f:
        hours = [Hour(*map(lambda x: int(x) if x.isdigit() else x, line.strip().split())) for line in f]
        hours.pop(0)

    res = []    
    for worker in workers:
        hour = list(filter(lambda x: x.name == worker.name and x.surname == worker.surname, hours))[0]
        delta = hour.hour - worker.norma
        selary = ((worker.norma - math.fabs(delta)) / worker.norma) * worker.salary if delta < 0 \
                                                        else worker.salary + 2 * (worker.salary / worker.norma) * delta

        temp = pattern.format(worker.name, worker.surname, hour.hour, worker.norma, worker.salary, selary)
        res.append(temp)
    return res


# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП,
# пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла

class Worker_new:
    def __init__(self, name, surname, salary, post, norma):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.post = post
        self.norma = norma

    def __str__(self):
        return '{} {} {} {} {}'.format(self.name, self.surname, self.salary, self.post, self.norma)


class Hour_new:
    def __init__(self, name, surname, hour):
        self.name = name
        self.surname = surname
        self.hour = hour

    def __str__(self):
        return '{} {} {}'.format(self.name, self.surname, self.hour)


def exercise_1_new():
    print('\n{:=^35}\n'.format('Задача-1'))

    with open('data/workers', 'r', encoding='utf-8') as f:
        workers = [Worker_new(*map(lambda x: int(x) if x.isdigit() else x, line.strip().split())) for line in f]
        workers.pop(0)

    with open('data/hours_of', 'r', encoding='utf-8') as f:
        hours = [Hour_new(*map(lambda x: int(x) if x.isdigit() else x, line.strip().split())) for line in f]
        hours.pop(0)


    res = []
    for worker in workers:
        hour = list(filter(lambda x: x.name == worker.name and x.surname == worker.surname, hours))[0]
        delta = hour.hour - worker.norma
        selary = ((worker.norma - math.fabs(delta)) / worker.norma) * worker.salary if delta < 0 \
                                                        else worker.salary + 2 * (worker.salary / worker.norma) * delta

        temp = pattern.format(worker.name, worker.surname, hour.hour, worker.norma, worker.salary, selary)
        res.append(temp)

    return res



def py_test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s \n Ожидалось: %s' % (prefix, repr(got), repr(expected)))


def main():
    old_res = exercise_1_old()
    new_res = exercise_1_new()
    py_test(new_res, old_res)
    print('\n' + '=' * 35)


if __name__ == '__main__':
    main()