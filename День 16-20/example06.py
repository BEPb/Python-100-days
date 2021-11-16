"""
Кодирование и декодирование-BASE64
0-9A-Za-z + /
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode
-------------------------------------
Сериализация и десериализация
Сериализация-Превратите объект в последовательность байтов (bytes) или последовательность символов (str) -Serialization / Pickles
Десериализация - восстановление последовательности байтов или последовательности символов в объект
Поддержка сериализации стандартной библиотекой Python:
json-сериализация в символьной форме
pickle-сериализация в байтах
свалки / загрузки
"""
import base64
import json
import redis

from example02 import Person


class PersonJsonEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


def main():
    cli = redis.StrictRedis(host='120.77.222.217', port=6379, 
                            password='123123')
    data = base64.b64decode(cli.get('guido'))
    with open('guido2.jpg', 'wb') as file_stream:
        file_stream.write(data)
    # with open('guido.jpg', 'rb') as file_stream:
    #     result = base64.b64encode(file_stream.read())
    # cli.set('guido', result)
    # persons = [
    #     Person('骆昊', 39), Person('王大锤', 18),
    #     Person('白元芳', 25), Person('狄仁杰', 37)
    # ]
    # persons = json.loads(cli.get('persons'))
    # print(persons)
    # cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))


if __name__ == '__main__':
    main()

