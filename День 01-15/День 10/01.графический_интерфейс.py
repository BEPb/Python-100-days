"""
Python 3.10 Используйте tkinter для создания графического интерфейса
-Верхнее окно
-Контроль
-Макет
-Event обратный вызов
Название файла '01.Связь_между_объектами.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

import tkinter  # импорт модуля графического интерфейса
import tkinter.messagebox  # импорт модуля сообщений


def main():  # главная функция
    flag = True  # переменной присваивается значение истина

    # Изменить текст на этикетке
    def change_label_text():  # функция изменения текста
        nonlocal flag  # получает значение переменной
        flag = not flag  # смена значения переменной на противоположное
        color, msg = ('red', 'Привет, пользователь!')\
            if flag else ('blue', 'Прощай, пользователь!')
        label.config(text=msg, fg=color)  # меняет цвет текста и сам текст в окне

    # подтвердить выход
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('вопрос', 'вы уверены, что хотите выйти?'):  # создает окно подтверждения
            # выхода
            top.quit()  # если ответ положительный то закрывает все окна

    # Создать окно верхнего уровня
    top = tkinter.Tk()
    # Установить размер окна
    top.geometry('440x160')
    # Установить заголовок окна
    top.title('окно')
    # Создать объект метки
    label = tkinter.Label(top, text='Программа запущена!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # Создаем контейнер для кнопок
    panel = tkinter.Frame(top)
    # Создать объект кнопки
    button1 = tkinter.Button(panel, text='изменить', command=change_label_text)  # задаем реакцию на эту кнопку - это
    # запуск функции Изменить текст на этикетке

    # Создать объект кнопки
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='выход', command=confirm_to_quit)  # задаем реакцию на эту кнопку - это
    # запуск функции выхода из программы
    button2.pack(side='right')
    panel.pack(side='bottom')
    # Откройте основной цикл событий
    tkinter.mainloop()


if __name__ == '__main__':  # если запущена эта программа
    main()  # выполняем главную функцию
