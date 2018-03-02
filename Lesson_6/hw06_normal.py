from collections import namedtuple, OrderedDict
from string import ascii_uppercase as str_au, ascii_lowercase as str_al
from random import randint, choice
from functools import reduce

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# +1. Получить полный список всех классов школы
# +2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# +3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# +4. Узнать ФИО родителей указанного ученика
# +5. Получить список всех Учителей, преподающих в указанном классе

Name = namedtuple('Name', ('name', 'middle_name', 'surname'))
Parents = namedtuple('Parents', ('parent_1', 'parent_2'))

class School:
    def __init__(self, name, classes, subjects, teachers):
        self.name = name
        self.classes = classes
        self.subjects = subjects
        self.teachers = teachers

    @property
    def list_classes(self):
        return list(self.classes.keys())

    def print_learners_in_class(self, class_name):
        try:
            res = self.classes[class_name].print_learners_in_class
        except KeyError as e:
            res = None
        return res

    def list_learners_in_class(self, class_name):
        try:
            res = self.classes[class_name].leaners_list
        except KeyError as e:
            res = None
        return res

    def find_learner(self, name, class_name):
        #if type(name) is 
        #return list(self.list_learners_in_class(class_name))
        learners = None
        if class_name:
            learners = list(filter(lambda x: x.person_name == name, 
                                             self.list_learners_in_class(class_name)))
        else:
            learners = list(filter(lambda x: x.person_name == name, self.all_learners))
        return learners

    def print_program_for_learner(self, name, class_name):
        learners = self.find_learner(name, class_name)
        for learner in learners:
            learner.print_info
            self.classes[learner.class_name].print_subjects_teachers

    def print_names_parents(self, name, class_name):
        learners = self.find_learner(name, class_name)
        for learner in learners:
            learner.print_info
            learner.parents_name

    @property
    def all_learners(self):
        return list(reduce(lambda x, y: x + y, map(lambda x: x.leaners_list, self.classes.values())))

    @property
    def random_learner(self):
        return choice(self.all_learners)

    @property
    def random_class(self):
        return choice(self.list_classes)

    def __str__(self):
        return '{}\n{}'.format(self.name, self.classes)


class ClassSchool:
    def __init__(self, name, leaners_list, subjects_teachers):
        self.name = name
        self.leaners_list = leaners_list
        self.subjects_teachers = subjects_teachers

    @property
    def print_subjects_teachers(self):
        for s, t in self.subjects_teachers.items():
            print('{}: {}'.format(s, t))

    @property
    def print_learners_in_class(self):
        for learner in self.get_learners_in_class:
            print(learner)

    @property
    def get_learners_in_class(self):
        return list(map(str, self.leaners_list))

    @property
    def get_teachers(self):
        return list(self.subjects_teachers.values())


    def __str__(self):
        return 'Class: {}'.format(self.name)


class Person:
    """docstring for Person"""
    def __init__(self, name):
        self.person_name = name

    @property
    def print_full_name(self):
        return '\nsurname: {p.surname}\nname: {p.name}\nmiddle_name: {p.middle_name}\n'.format(p=self.person_name)

    def __str__(self):
        return '{n.surname} {n.name:.1}.{n.middle_name:.1}.'.format(n=self.person_name)

        
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)


class Learner(Person):
    def __init__(self, name, parent_1, parent_2, class_name):
        super().__init__(name)
        self.parents = Parents(parent_1, parent_2)
        self.class_name = class_name

    @property
    def print_info(self):
        print('\n' + '=' * 35)
        print('Learner:\n{}\nParent 1:\n{}\nParent 2:\n{}'.format(self.print_full_name, 
                                                                  self.parents.parent_1.print_full_name, 
                                                                  self.parents.parent_2.print_full_name))
        print('Class: {}'.format(self.class_name))
        print('=' * 35)

    @property
    def parents_name(self):
        print('\n' + '=' * 35)
        print('Parent 1:\n{}\nParent 2:\n{}'.format(self.parents.parent_1.print_full_name, 
                                                    self.parents.parent_2.print_full_name))
        print('=' * 35)


def gen_school():

    def gen_name():
        name = str(choice(str_au)) + ''.join([choice(str_al) for _ in range(randint(3, 10))])
        middle_name = str(choice(str_au)) + ''.join([choice(str_al) for _ in range(randint(3, 10))])
        surname = str(choice(str_au)) + ''.join([choice(str_al) for _ in range(randint(3, 10))])

        return Name(name, middle_name, surname)

    def gen_class():
        numbers = [str(i) for i in range(1, 12)]
        letters = list(str_au[:4])

        for num in numbers:
            for lt in letters:
                yield num + lt

    subjects = ['Математика', 'Русский', 'Английский', 'Физика', 'Химия', 'Физкультура', 'История']
    teachers = []
    for _ in range(10):
        teachers.append(gen_name())

    d = OrderedDict()
    for cl in gen_class():
        temp = []
        for _ in range(randint(10, 30)):
            learner_name = gen_name()
            parent_1 = Person(gen_name())
            parent_2 = Person(gen_name())
            temp.append(Learner(learner_name, parent_1, parent_2, cl))
        class_subjects = list(set([choice(subjects) for _ in range(randint(3, 7))]))
        class_teachers = [choice(teachers) for _ in range(len(class_subjects))]
        subjects_teachers = dict(zip(class_subjects, class_teachers))
        d[cl] = ClassSchool(cl, temp, subjects_teachers)

    return School('School', d, subjects, teachers)


def exercise_1():
    print('\n{:=^35}\n'.format('Задача-1'))
    school = gen_school()
    ans = None
    
    print('\n1.1\nВсе класы школы:\n{}'.format(school.list_classes))
    class_name = input('Enter class_name: ').strip()

    print('\n1.2')
    school.print_learners_in_class(class_name)

    print('\n1.3')
    school.print_program_for_learner(school.random_learner.person_name, '')

    print('\n1.4')
    school.print_names_parents(school.random_learner.person_name, '')

    print('\n1.5')
    school.classes[school.random_class].print_subjects_teachers


def main():
    exercise_1()
    print('\n' + '=' * 35)


if __name__ == '__main__':
    main()