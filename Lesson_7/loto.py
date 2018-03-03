from random import choice, shuffle


#!/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
    
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.bag = None
        self.status = None

    def start_game(self):
        self.player_1.set_card(Card(self.player_1.name))
        self.player_2.set_card(Card(self.player_2.name))
        self.bag = self.set_bag()
        self.status = True
        
        counter = 90
        print()
        while self.status and not self.player_1.card.check_card and not self.player_2.card.check_card:
            num = next(self.bag)
            counter -= 1
            self.player_2.card.del_number(num)
            self.print_status_round(num, counter)
            cross_out = self.make_strike()
            self.check_cross_out(cross_out, num)
            self.check_winner()

    def check_cross_out(self, cross_out, num):
        if cross_out:
            if self.player_1.card.find_number(num):
                self.player_1.card.del_number(num)
            else:
                print('Player {} won\n(у вас не было номера {} на карточке)'.format(self.player_2.name, num))
                self.status = False
        else:
            if self.player_1.card.find_number(num):
                self.status = False
                print('Player {} won\n(у вас был номер {} на карточке)'.format(self.player_2.name, num))
            else:
                self.player_1.card.del_number(num)

            
    def make_strike(self):
        ans = ''
        while ans != 'y' and ans != 'n':
            ans = input('Зачеркнуть цифру? (y/n):').strip()
        if ans == 'y':
            return True
        else:
            return False

    def check_winner(self):
        if self.player_1.card.check_card and self.player_2.card.check_card:
                print('Draw')
                self.status = False
        elif self.player_1.card.check_card:
            print('Player {} won'.format(self.player_1.name))
            self.status = False
        elif self.player_2.card.check_card:
            print('Player {} won'.format(self.player_2.name))
            self.status = False

    def set_bag(self):
        numbers = ['{:>2}'.format(i) for i in range(1, 91)]
        shuffle(numbers)
        yield from numbers

    def print_status_round(self, num, counter):
        print('Новый бочонок: {} (осталось {:>2})'.format(num, counter))
        print(self.player_1.card)
        print(self.player_2.card)


    def __str__(self):
        return 'Player 1: {}\nPlayer 2: {}\n'.format(self.player_1, self.player_2)


class Player:
    """docstring for Player"""
    def __init__(self, name):
        self.name = name
        self.card = None

    def set_card(self, card):
        self.card = card

    def get_card(self):
        return self.card

    def __str__(self):
        return 'Name: {}\n'.format(self.name)


class Card:
    """docstring for Card"""
    def __init__(self, name):
        self.name = name
        self.num_in_lines = self.fill_num_in_lines()
        self.lines = self.fill_lines()

    @property
    def check_card(self):
        for line in self.num_in_lines:
            if line:
                break
        else:
            return True
        return False

    def find_number(self, num):
        for line in self.lines:
            if num in line:
                break
        else:
            return False
        return True


    def fill_num_in_lines(self):
        numbers = ['{:>2}'.format(i) for i in range(1, 91)]
        num_in_lines = []
        temp_line = []
        for i in range(1, 16):
            temp_num = choice(numbers)
            temp_line.append(temp_num)
            if i % 5 == 0:
                num_in_lines.append(sorted(temp_line))
                temp_line = []
            numbers.remove(temp_num)
        return num_in_lines
    
    def fill_lines(self):
        lines = []
        for i in range(3):
            it = iter(self.num_in_lines[i])
            pos = [j for j in range(9)]
            shuffle(pos)
            pos = pos[:4]
            temp_lines = ['  ' if j in pos else next(it) for j in range(9)]
            lines.append(temp_lines)
        return lines

    def del_number(self, num):
        for index, line in enumerate(self.lines):
            if num in line:
                i = line.index(num)
                self.lines[index][i] = ' -'
                self.num_in_lines[index].remove(num)
                break
    
    def __str__(self):
        first_line = '\n{:-^26}\n'.format(self.name)
        lines = '{}\n{}\n{}\n'.format(*list(map(lambda x: ' '.join(x), self.lines)))
        last_line = '-'*26 + '\n'
        return first_line + lines + last_line
        



def exercise_1():
    print('\n{:=^20}'.format('Задача-1'))


def main():
    #exercise_1()
    player_1 = Player('Игрок')
    player_2 = Player('Компьютер')
    game = Game(player_1, player_2)
    game.start_game()

    #print('\n' + '=' * 26)


if __name__ == '__main__':
    main()