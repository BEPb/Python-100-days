"""
хэш-сводка - цифровая подпись/отпечаток пальца - односторонняя хэш-функция (без обратной функции необратима)
	области применения:
	1. конфиденциальная для пользователя информация в базе данных сохраняется в хэш-сводке
	2. данные проверки подписи, созданные для создания данных, не были злонамеренно подделаны
	3. секундная передача облачных служб хранения данных (де-тяжелая функциональность)
"""


class StreamHasher():
    """генератор дайджеста"""

    def __init__(self, algorithm='md5', size=4096):
        """метод инициализации
        @params:
            algorithm - алгоритм хэш-дайджеста
            size - размер данных, считываемых каждый раз
        """
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()
    

    def digest(self, file_stream):
        """создать шестнадцатеричную сводную строку"""
        # data = file_stream.read(self.size)
        # while data:
        #     self.hasher.update(data)
        #     data = file_stream.read(self.size)
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """основная функция"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('Python-3.7.2.tar.xz', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()
