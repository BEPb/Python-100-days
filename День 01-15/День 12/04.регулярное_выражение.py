"""
Python 3.10 регулярное выражение
Название файла '04.регулярное_выражение.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""
import re  # подключаем модуль регулярных выражений


def main():  # главная функция
    # Создайте объект регулярного выражения, используя упреждающий просмотр и проверку, чтобы убедиться, что перед и после номера мобильного телефона не должно быть чисел.
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    Важно то, что 8130123456789 раз мой мобильный номер 13512346789,
    Это не 15600998765, это 110 или 119, номер мобильного телефона Ваньки - 15600998765.
    '''

    mylist = re.findall(pattern, sentence) # Найдем все совпадения и сохраним их в списке
    print(mylist)  # выведем список
    print('--------Великолепный разделитель--------')
    # Используйте функцию поиска, чтобы указать место поиска, чтобы найти все совпадения
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------Великолепный разделитель--------')
    # Используйте функцию поиска, чтобы указать место поиска, чтобы найти все совпадения
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
