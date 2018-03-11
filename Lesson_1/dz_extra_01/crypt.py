from pprint import pprint
import copy
import re
import numpy as np
import operator
from collections import Counter, OrderedDict
from itertools import combinations
from math import fabs


def load_test_data():
    raw_data = open('test_1.txt', encoding='utf-8').read().split('\n\n')
    data = []
    for src in raw_data:
        temp_lst = list(map(lambda x: x.strip(), src.split('\n')))
        temp = dict()
        for s in temp_lst:
            lst_s = s.split()
            temp[lst_s[0]] = lst_s[2]
        data.append(temp)
    return data


def get_dict_triplets(st):
    n = 3
    d = dict()
    for i_1 in range(len(st)):
        if i_1 + n <= len(st):
            st_1 = st[i_1:i_1 + n]
            if st_1 in d:
                continue
            else:
                d[st_1] = 1
            for i_2 in range(i_1 + n, len(st)):
                st_2 = st[i_2:i_2 + n]
                if st_1 == st_2:
                    d[st_1] += 1
    d = dict(map(lambda x: (x[0], x[1]), filter(lambda x: x[1] > 2, d.items())))
    return d

def dividers(number):
    res = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            res.append(i)
    res.append(number)
    return res

def common_divisors(lst):
    cd = set()
    for src in lst:
        temp = set(dividers(src))
        if cd:
            cd = cd & temp
        else:
            cd = temp
    return sorted(list(cd))


def get_len_key(d_common_divisors):
    res = dict()
    for k, v in d_common_divisors.items():
        for i in v:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
    d = dict(map(lambda x: (x[0], x[1]), filter(lambda x: x[1] > 2 and x[0] != 1, res.items())))                
    if d:
        res = max(d.items(), key=operator.itemgetter(1))[0]
        return res
    else:
        return None

def key_len_estimation(st):
    d = get_dict_triplets(st)
    d_index = dict([(k, [m.start() for m in re.finditer(k, st)]) for k in d.keys()])
    d_delta = dict([(k, list(np.diff(v))) for k, v in d_index.items()])
    d_common_divisors = dict([(k, common_divisors(v)) for k, v in d_delta.items()])
    len_key = get_len_key(d_common_divisors)
    
    
    #pprint(len_key)
    return len_key


def match_index(st):
    dct = dict([(i, [st[j::i] for j in range(i)]) for i in range(2, 10)])
    # pprint(st)
    # pprint(dct[2])
    len_index = []
    for k, v in dct.items():
        # print(k)
        temp = 0
        for src in v:
            temp += calc_freq(src)
            # print(calc_freq(src))
        temp /= len(v)
        if temp > 0.05:
            len_index.append((k, temp))
    max_index = max(len_index, key=lambda x: x[1])[0]
    # pprint('{}'.format(max_index))
    return max_index
    # for k, v in dct.items():

def calc_freq(st):
    c = Counter(st)
    len_st = len(st)
    p_i_2 = [(src / len_st) ** 2 for src in c.values()]
    return sum(p_i_2)

def calc_mutual_index(lst, st, keey=-1):
    ST_SYMB = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lst_comb = combinations(lst, 2)
    it = list(combinations(list(range(len(lst))), 2))
    shift = []
    for index, (one, two) in enumerate(lst_comb):
        o = Counter(one)
        temp = []
        for i in range(len(ST_SYMB)):
            mi = 0
            t = Counter(shift_sting(two, i))
            for s in ST_SYMB:
                mi += (o.get(s, 0) / sum(o.values())) *\
                     (t.get(s, 0) / sum(t.values()))
            temp.append(mi)
        shift.append(temp.index(max(temp)))
    shift = sorted(list(zip(it, shift)), key=lambda x: x[1], reverse=True)
    if keey != -1:
        if keey == 1:
            filt_lst = [(0, 1), (0, 2), (0, 6), (5, 6), (4, 6), (3, 5)]
            old_shift = list(filter(lambda x: x[0] in filt_lst, shift))
            shift = [tuple(filter(lambda x: x[0] == src, old_shift))[0] for src in filt_lst]
        elif keey == 0:
            filt_lst = [(0, 1), (0, 2), (0, 3), (0, 4)]
            old_shift = list(filter(lambda x: x[0] in filt_lst, shift))
            shift = [tuple(filter(lambda x: x[0] == src, old_shift))[0] for src in filt_lst]
        else:
            shift.sort(key=lambda x: (x[0][0], x[0][1]))
    else:
        shift.sort(key=lambda x: (x[0][0], x[0][1]))
    d = OrderedDict([(i, None) if i != 0 else (i, i) for i in range(len(lst))])
    for src in shift:
        if d[src[0][0]] is not None:
            if d[src[0][1]] is None:
                d[src[0][1]] = d[src[0][0]] + src[1]
                d[src[0][1]] = -d[src[0][1]] + (d[src[0][1]] // len(ST_SYMB) + 1)* len(ST_SYMB)
        elif d[src[0][1]] is not None:
            if d[src[0][0]] is None:
                d[src[0][0]] = d[src[0][1]] + src[1]
                d[src[0][0]] = d[src[0][0]] - (d[src[0][0]] // len(ST_SYMB)) * len(ST_SYMB)
    for i, s in enumerate(ST_SYMB):
        print('{}: '.format(i), end='')
        for k, v in d.items():
            index = i + v if i + v < len(ST_SYMB) else i + v - len(ST_SYMB)
            print(ST_SYMB[index], end='')
        print()
    sh = int(input('Enter shift: ').strip())
    for k, v in d.items():
        d[k] += sh
        if d[k] >= len(ST_SYMB):
            d[k] -= len(ST_SYMB)
    pprint(d)
    # st = ''.join(lst)
    new_st = ''
    for i, s in enumerate(st):
        index = i % len(lst)
        index_s = ST_SYMB.find(s)
        new_index_s = index_s - d[index] if index_s - d[index] >= 0 else index_s - d[index] + len(ST_SYMB)
        new_st += ST_SYMB[new_index_s]
    print(new_st)

def shift_sting(st, shift):
    ST_SYMB = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    len_ST_SYMB = len(ST_SYMB)
    new_st = ''
    for s in st:
        index_s = ST_SYMB.find(s)
        new_index_s = index_s + shift
        if new_index_s >= len_ST_SYMB:
            new_index_s -= len_ST_SYMB
        new_st += ST_SYMB[new_index_s]

    return new_st


def shift_from_index(index):
    SHIFTS = {0.0553: 0, 0.0366: 1, 0.0345: 2, 0.04: 3, 0.034: 4, 0.036: 5, 0.0326: 6, 0.0241: 7, 0.0287: 8, 0.0317: 9, 0.0265: 10, 0.0251: 11, 0.0244: 12, 0.0291: 13, 0.0322: 14, 0.0244: 15, 0.0249:16}
    delta = None
    shift = None
    for k, v in SHIFTS.items():
        if delta is None:
            delta = index - k
            if delta < 0:
                shift = -v
            else:
                shift = v
        else:
            temp = index - k
            if fabs(temp) < fabs(delta):
                delta = temp
                if delta < 0:
                    shift = -v
                else:
                    shift = v
    return shift



def exercise_1():
    print('\nЗадача-1' + '=' * 10 + '\n')
    # data = load_test_data()
    # for index, src in enumerate(data):
    #     st = src['Шифр']
    #     len_key = key_len_estimation(st)
    #     len_key_2 = match_index(st)
    #     dct = dict([(i, [st[j::i] for j in range(i)]) for i in range(2, 10)])
    #     calc_mutual_index(dct[int(len_key_2)], st, keey=index)
    st = open('vigenere.txt', encoding='utf-8').read()
    len_key = match_index(st)
    dct = dict([(i, [st[j::i] for j in range(i)]) for i in range(2, 10)])
    calc_mutual_index(dct[int(len_key)], st)


def main():
    exercise_1()
    print('\n' + '=' * 18)


if __name__ == '__main__':
    main()