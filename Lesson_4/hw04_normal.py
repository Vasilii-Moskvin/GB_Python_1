import re
from random import randint

# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


def exercise_1():
    print('\n{:=^20}'.format('Задача-1'))
    test = 'mtMmEZUOmcqMdJl'
    global line
    def with_str(x):
        res_lst = []
        temp = ''
        for s in x:
            if s.islower():
               temp += s
            else:
               if temp:
                   res_lst.append(temp)
                   temp = ''
        if temp:
            res_lst.append(temp)
        return res_lst

    def with_re(x):
        rexp = re.compile(r'(?:^|(?<=[A-Z])|[A-Z]+)([a-z]+)(?:[A-Z]+|$)')
        res_lst = re.findall(rexp, x)
        return res_lst
    #print(with_re(test))
    py_test(with_re(line), with_str(line))

# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
# Т.е. из строки "sGAMkgAYEOmHBSQs" нужно получить ['GAM', 'EO']
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
             'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
             'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
             'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
             'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
             'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
             'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
             'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
             'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
             'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
             'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
             'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


def exercise_2():
    print('\n{:=^20}'.format('Задача-2'))

    test = 'zMUtmSQQZGHlmQKJndiAXbIzV'
    global line_2
    def with_str(x):
        res_lst = []
        temp = ''
        temp_lst = []
        flag_pattern_rec = False
        flag_pattern = False
        pattern =''
        for s in x:
            if s.isupper():
                temp += s
                if flag_pattern_rec:
                    if len(pattern) == 1:
                        pattern = ''
                        flag_pattern_rec = False
                        temp_lst.pop(0)
                    elif 2 <= len(pattern) <= 3:
                        pattern += s
                    else:
                        flag_pattern_rec = False
                        flag_pattern = True

            else:
                if temp:
                    if not temp_lst:
                        temp_lst.append(temp)
                    else:
                        temp_lst.append(temp)
                        if flag_pattern:
                            if len(temp) > 2:
                                res_lst.append((temp_lst[0], temp_lst[1][2:]))
                        flag_pattern = False
                        pattern = ''
                        temp_lst.pop(0)
                    temp = ''
                    flag_pattern_rec = True
                if temp_lst:
                    if len(pattern) < 2:
                        pattern += s
                    else:
                        pattern = ''
                        temp_lst = []
                        flag_pattern_rec = False


        return res_lst

    def with_re(x):
        main_pattern = r'(?:[a-z]{2}[A-Z]{2})'
        left_pattern = r'([A-Z]+|(?<=[A-Z][a-z]{2})[A-Z]{3,})'
        right_pattern = r'([A-Z]+)'
        re_common = r'(?:[a-z]{2}[A-Z]{2})([A-Z]+)'
        #rex = re.compile(r'([A-Z]+)[a-z]{2}[A-Z]{2}([A-Z]+)]')
        #rexp_1 = re.compile(r'([A-Z]+)' + re_common)
        rexp = re.compile(left_pattern + main_pattern + right_pattern)
        rexp_2 = re.compile(r'((?<=[A-Z][a-z]{2})[A-Z]{3,}|[A-Z]+)' + re_common)
        #rexp = rexp_1 or rexp_2
        res_lst = re.findall(rexp, x)
        return res_lst
    #print(with_re(line_2))
    #py_test(with_re(line_2), with_str(line_2))
    py_test(with_re(test), [('MU', 'QZGH'), ('SQQZGH', 'J')])



# Задача-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла) произвольными целыми
# числами, в результате в файле должно быть 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле.

def exercise_3():
    print('\n{:=^20}'.format('Задача-3'))
    my_gen = (randint(0, 9) for _ in range(2500))

    with open('raw.txt', 'w') as f:
        for src in my_gen:
            f.write(str(src))

    with open('raw.txt', 'r') as f:
        data = f.read()
    rex = re.compile(r'((\d)\2+)')
    finded_num = rex.findall(data)
    max_value = max(finded_num, key=lambda x: len(x[0]))
    print('max value: {}\nlen: {}'.format(max_value, len(max_value[0])))

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