import requests
import sqlite3
import os
import datetime
import urllib
import gzip
import shutil
import json
from pprint import pprint
from random import shuffle
import re

""" OpenWeatherMap
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API для доступа к данным о текущей погоде, прогнозам, для web-сервисов и мобильных приложений. Архивные данные доступны только на коммерческой основе. В качестве источника данных используются официальные метеорологические службы, данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ вытащить со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке: http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
        (воспользоваться модулем gzip или вызвать распаковку через создание процесса архиватора через модуль subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
    {"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
    {"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,"temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},"rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,"sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,"sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite с следующей структурой данных (если файла 
   базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами
- используется созданная база данных, новые данные добавляются и обновляются



При работе с XML-файлами:

Доступ к данным в XML файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
def load_data(path_to_json):
    country = set()
    with open(path_to_json, encoding='utf-8') as f:
        data = json.load(f)

    for src in data:
        country.add(src['country']) 

    return data, country

def input_country(country):
    ans = None
    while ans not in country:
        ans = input('Enter name of county: ')
    return ans


def id_in_string(data, user_country):
    lst = list(map(lambda x: str(x['id']), 
                   filter(lambda x: x['country'] == user_country, data)))
    shuffle(lst)
    return ','.join(lst[:12])


def exercise_1():
    print('\n{:=^26}'.format('Задача-1'))
    destination = 'city.list.json.gz'
    path_to_json = '.'.join(destination.split('.')[:-1])
    if not os.path.exists(destination):
        load_list_of_city(destination)
    if not os.path.exists(path_to_json):
        path_to_json = unzip(destination, path_to_json)
    data, country = load_data(path_to_json)
    ans = None
    while ans != 'city' and ans != 'country':
        ans = input('add city or random citys from country (city/country)?: ')
        if ans == 'city':
            add_user_city(path_to_json)
        elif ans == 'country':
            add_12_random_city(data, country)
        else:
            pass


def add_12_random_city(data, country):
    pprint(country)
    user_country = input_country(country)
    ids = id_in_string(data, user_country)
    push_data_to_DB(ids)


def add_user_city(path_to_json):
    with open(path_to_json, encoding='utf-8') as f:
        raw_data = f.read()
    city = input('Enter the city: ').strip()
    st = r'"id": (\d+),\s+"name": "{}"'.format(city)
    city_pattern = re.compile(st)
    ids = city_pattern.findall(raw_data)
    if ids:
        push_data_to_DB(','.join(ids))


def push_data_to_DB(ids):
    c_db, conn_db = connect_with_DB()
    api_url = "http://api.openweathermap.org/data/2.5/group"
    params = {'id': '{}'.format(ids),'units': 'metric', 'appid': 'c5c61378559033a63825562396af6a30'}
    res = requests.get(api_url, params=params)
    temp = res.json()
    for k, v in temp.items():
        if k == 'list':
            for index, src in enumerate(v):
                st = (src['id'], src['name'], datetime.date.fromtimestamp(src['dt']), src['main']['temp_min'], src['weather'][0]['id'])
                c_db.execute('SELECT EXISTS(SELECT id_city FROM wather WHERE id_city = ?)', (src['id'],))
                flag = c_db.fetchall()
                if flag != [(0,)]:
                    c_db.execute('SELECT date FROM wather WHERE id_city = ?', (src['id'],))
                    d = c_db.fetchall()[0][0]
                    c_db.execute('UPDATE wather set temp = ? where id_city = ?', (src['main']['temp_min'], src['id']))
                    c_db.execute('UPDATE wather set id_wather = ? where id_city = ?', (src['weather'][0]['id'], src['id']))
                    if datetime.date(*list(map(int, d.split('-')))) != st[2]:
                        c_db.execute('UPDATE wather set date = ? where id_city = ?', (st[2], src['id']))
                else:
                    c_db.execute('insert into wather values (?,?,?,?,?)', st)
                conn_db.commit()
    c_db.close()


def connect_with_DB():
    path_to_db = r'C:\Users\vasil\YandexDisk\WorkPlace\Scripts\Git\GB_Python_1\Lesson_8\test'
    if os.path.exists(path_to_db):
        conn = sqlite3.connect(path_to_db)
        return conn.cursor(), conn
    else:
        conn = sqlite3.connect(path_to_db)
        c = conn.cursor()
        c.execute('''create table wather (id_city INTEGER PRIMARY KEY, city VARCHAR(255), date DATE, temp INTEGER, id_wather INTEGER)''') 
        conn.commit()
        return c, conn


def load_list_of_city(destination):
    url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
    urllib.request.urlretrieve(url, destination)


def unzip(destination, path_to_json):
    with gzip.open(destination, 'rb') as f_in:
        with open(path_to_json, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return path_to_json


def main():
    exercise_1()
    print('\n' + '=' * 26)


if __name__ == '__main__':
    main()
