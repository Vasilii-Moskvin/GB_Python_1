
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>] save_filename
    export_openweather.py --json filename [<город>] save_filename
    export_openweather.py --html filename [<город>] save_filename
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
import os
import sqlite3
from collections import namedtuple
from bs4 import BeautifulSoup
from urllib.request import urlopen


header = ('id_city', 'city', 'date', 'temp', 'id_weather')
City = namedtuple('City', header)


def exercise_1():
    print('\n{:=^26}'.format('Задача-1'))
    args = sys.argv
    len_args = len(args)
    if len_args == 5:
        key, filename, city, save_path = args[1:]
        do = {'--csv': conver_to_csv, '--json': conver_to_json, '--html': conver_to_html}
        if not os.path.exists(filename):
            print("Не найден файл: {}".format(filename))
            print('Для справки введите: "export_openweather.py --format"')
            sys.exit(1)
        conn = sqlite3.connect(filename)
        cur = conn.cursor()
        cur.execute('SELECT * FROM weather WHERE city = ?', (city,))
        d = cur.fetchall()
        cur.close()
        if d:
            res = City(*d[0])
        else:
            print('Нет такого города в базе данных')
        if do.get(key):
            do[key](res, save_path)
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
            print('Для справки введите: "export_openweather.py --format"')
            sys.exit(1)

    elif len_args > 4:
        print('Слишком много аргументов! Для справки введите: "export_openweather.py --format"')
        sys.exit(1)
    else:
        if len_args == 2 and args[1] == '--format':
            print_format_input()
        else:
            print('Слишком мало аргументов! Для справки введите: "export_openweather.py --format"')
            sys.exit(1)


def conver_to_csv(data, save_path):
    global header
    with open(save_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerow(data._asdict())


def conver_to_json(data, save_path):
    with open(save_path, 'w') as outfile:
        json.dump(data._asdict(), outfile)


def conver_to_html(data, save_path):
    add_to_td = []
    for k, v in data._asdict().items():
        temp = '<tr><td>{}</td><td>{}</td></tr>\n'.format(k, v)
        add_to_td.append(temp)
    img_url = get_img_url(data.id_weather)
    html = \
    '''
    <html>
        <body>
            <img src="{}">
            <table>
                {}                
            </table>
        </body>
    </html>
    '''.format(img_url, ''.join(add_to_td))

    with open(save_path, 'w', newline='') as f:
        f.write(html)


def get_img_url(id_weather):
    html_doc = urlopen('http://openweathermap.org/weather-conditions').read()
    soup = BeautifulSoup(html_doc, "lxml")
    table = soup.findAll("table", {"class": "table table-bordered"})[1:-4]
    #print(table)
    img_dct = dict()
    for src in table:
        for index, row in enumerate(src.findAll("tr")):
            temp = []
            for i, src in enumerate(row.findAll('td')):
                if i == 0:
                    temp.append(str(src.contents[0]).strip())
                elif i == 2:
                    temp.append(src.find('img').get('src'))
            if temp:
                img_dct[int(temp[0])] = temp[1]

    res = img_dct.get(id_weather, '#')

    return res


def print_format_input():
    print('''export_openweather.py --csv filename [<город>] save_filename
export_openweather.py --json filename [<город>] save_filename
export_openweather.py --html filename [<город>] save_filename''')


def main():
    exercise_1()
    print('\n' + '=' * 26)


if __name__ == '__main__':
    main()
