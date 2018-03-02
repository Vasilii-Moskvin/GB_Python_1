import math
from collections import namedtuple, OrderedDict
import string
from functools import reduce
import matplotlib.pyplot as plt
from random import randint



Point = namedtuple('Point', ('x', 'y'))

class WrongNumberOfPoints(Exception):
    pass

class Figure:
    def __init__(self, p):
        self.count_points = len(p)
        self._gen_name_points = (x for x in string.ascii_uppercase)
        self.points = OrderedDict((next(self._gen_name_points), Point(*src)) for src in p)
        self.sides_length = OrderedDict((src,
                                        math.sqrt((self.points[src[1]].x - self.points[src[0]].x) ** 2 +
                                                  (self.points[src[1]].y - self.points[src[0]].y) ** 2))
                                       for src in self.name_sides)

    @property
    def name_sides(self):
        lst_name_side = []
        for index, src in enumerate(self.name_points):
            if index < self.count_points - 1:
                lst_name_side.append(src + self.name_points[index + 1])
            else:
                if len(lst_name_side) != 1:
                    lst_name_side.append(src + self.name_points[0])
        return tuple(lst_name_side)

    @property
    def name_points(self):
        return tuple(self.points.keys())

    @property
    def perimeter(self):
        return sum(self.sides_length.values())

    def __str__ (self):
        lst_points = ['\n{}: x={} y={}'.format(k, *v) for k, v in self.points.items()]
        return '\n{}:'.format(type(self).__name__) + ''.join(lst_points)


class Triangle(Figure):
    def __init__(self, p):
        super().__init__(p)
        if self.count_points != 3:
            raise WrongNumberOfPoints

    @property
    def heights(self):
        return dict(map(lambda s: (s, 0.5 * self.square / self.sides_length[s]), self.name_sides))

    @property
    def side_to_point(self):
        order_of_side =  list(self.name_sides)[1:]
        order_of_side.append(self.name_sides[0])
        s_t_p = dict((s, p) for s, p in zip(order_of_side, self.name_points))
        return s_t_p

    @property
    def square(self):
        p = 0.5 * self.perimeter
        return math.sqrt(p * reduce(lambda x, y: x * y, map(lambda x: p - x, self.sides_length.values())))


class Quadrilateral(Figure):
    def __init__(self, p):
        super().__init__(p)
        if self.count_points != 4:
            raise WrongNumberOfPoints
        else:
            if len(set(self.points)) != 4:
                raise WrongNumberOfPoints

    @property
    def is_isosceles(self):
        # if ((self.points['A'].x - self.points['B'].x) * (self.points['C'].y - self.points['D'].y) -
        #     (self.points['A'].y - self.points['B'].y) * (self.points['C'].x - self.points['D'].x) == 0) or\
        #         ((self.points['B'].x - self.points['C'].x) * (self.points['D'].y - self.points['A'].y) -
        #          (self.points['B'].y - self.points['C'].y) * (self.points['D'].x - self.points['A'].x) == 0):
        if (self.points['B'].x - self.points['C'].x) * (self.points['D'].y - self.points['A'].y) - \
                        (self.points['B'].y - self.points['C'].y) * (self.points['D'].x - self.points['A'].x) == 0:
            # if self.sides_length['AB'] == self.sides_length['CD'] or self.sides_length['BC'] == self.sides_length['DA']:
            if self.sides_length['AB'] == self.sides_length['CD']:
                if self.diagonals['d1'] == self.diagonals['d2'] and self.diagonals['d1'] is not None:
                    if self.angles['A'] == self.angles['D']:
                        if self.angles['A'] == self.angles['D'] == self.angles['B'] == self.angles['C']  and self.angles['A'] != 90:
                            return False
                        else:
                            return True
                    else:
                        False
                else:
                    return False
            else:
                return False
        else:
            return False

    @property
    def diagonals(self):
        try:
            d_1 = math.sqrt(self.sides_length['CD'] ** 2 + self.sides_length['DA'] * self.sides_length['BC'] - ((self.sides_length['DA'] * (self.sides_length['CD'] ** 2 - self.sides_length['AB'] ** 2)) / (self.sides_length['DA'] - self.sides_length['BC'])))
            d_2 = math.sqrt(self.sides_length['AB'] ** 2 + self.sides_length['DA'] * self.sides_length['BC'] - ((self.sides_length['DA'] * (self.sides_length['AB'] ** 2 - self.sides_length['CD'] ** 2)) / (self.sides_length['DA'] - self.sides_length['BC'])))
        except ZeroDivisionError as e:
            return {'d1': None, 'd2': None}

        return {'d1': d_1, 'd2': d_2}

    def calc_angel(self, p1, p2, p3):
        m1 = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        m2 = math.sqrt((p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2)
        sm = (p2.x - p1.x) * (p3.x - p1.x) + (p2.y - p1.y) * (p3.y - p1.y)
        try:
            angle = (180 / math.pi) * math.acos(sm / (m1 * m2))
        except ZeroDivisionError as e:
            raise WrongNumberOfPoints
        except ValueError as e:
            raise WrongNumberOfPoints
        return angle

    @property
    def angles(self):
        angle_A = self.calc_angel(self.points['A'], self.points['B'], self.points['D'])
        angle_B = self.calc_angel(self.points['B'], self.points['C'], self.points['A'])
        angle_C = self.calc_angel(self.points['C'], self.points['D'], self.points['B'])
        angle_D = self.calc_angel(self.points['D'], self.points['A'], self.points['C'])
        return {'A': angle_A, 'B': angle_B, 'C': angle_C, 'D': angle_D}

    @property
    def height(self):
        return self.sides_length['AB'] * math.sin((math.pi / 180) * self.angles['A'])

    @property
    def square(self):
        return (self.sides_length['BC'] + self.sides_length['DA']) * (self.height / 2)

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

def exercise_1():
    print('\n{:=^35}\n'.format('Задача-1'))
    t = Triangle(((1, 1), (2, 2), (3, 1)))
    print('{}\nsquare: {}\nperimeter: {}\nheight: {}'.format(t, t.square, t.perimeter, t.heights))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


def exercise_2():
    print('\n{:=^35}'.format('Задача-2'))
    for _ in range(100000):
         points =  ((randint(-10, 10), randint(-10, 10)),
                    (randint(-10, 10), randint(-10, 10)),
                    (randint(-10, 10), randint(-10, 10)),
                    (randint(-10, 10), randint(-10, 10)))
         #points = ((1, 1), (2, 2), (3, 2), (1, 1))
         try:
            f = Quadrilateral(points)

            if f.is_isosceles:
                print(True, end=': ')
                print('height: {:.2f}'.format(f.height))
                print('square: {:.2f}'.format(f.square))
                #plt.plot(*list(zip(*points)), linestyle='-', marker='.', color='red', markersize=10)
                #plt.show()
                #plt.close()
         except WrongNumberOfPoints as e:
             pass




def main():
    #exercise_1()
    exercise_2()
    print('\n' + '=' * 35)

if __name__ == '__main__':
    main()

