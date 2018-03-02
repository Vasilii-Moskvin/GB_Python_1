# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):
    number_lst = str(number).split('.')
    if len(number_lst) == 1:
        res = number
    elif len(number_lst) == 2:
        res_lst = [number_lst[0], number_lst[1][:ndigits]]
        for i in number_lst[1][ndigits:]:
            if int(i) >= 5:
                if res_lst[1]:
                    res_lst[1] = str(int(res_lst[1]) + 1)
                else:
                    res_lst[0] = str(int(res_lst[0]) + 1)
                break
            elif int(i) == 4:
                continue
            else:
                break
        if res_lst[1]:
            res = float('.'.join(res_lst))
        else:
            res = int(res_lst[0])
    # print('num: {}\nres: {}'.format(number, res))
    return res

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    str_ticket_number = str(ticket_number)
    left_side = str_ticket_number[:3]
    right_side = str_ticket_number[3:]

    return sum(map(int, left_side)) == sum(map(int, right_side))


def main():
    my_round(12.12346, 3)
    print(lucky_ticket(123321))


if __name__ == '__main__':
    main()