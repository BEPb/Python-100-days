"""
Python 3.9 При использовании нескольких потоков трудоемкие задачи выполняются в отдельных потоках.
Название файла '08.многопоточная_работа.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

import time  # подключаем модуль времени
import tkinter  # модуль работы с GUI
import tkinter.messagebox  # модуль работы с GUI сообщениями
from threading import Thread  # подключаем модуль многопоточной работы


def main():  # главная функция

    class DownloadTaskHandler(Thread):

        def run(self):
            # Имитация задачи загрузки занимает 10 секунд
            time.sleep(10)
            tkinter.messagebox.showinfo('подсказка', 'загрузка завершена!')
            # Включить кнопку загрузки
            button1.config(state=tkinter.NORMAL)

    def download():  # функция загрузки (в процессе загрузки ещер раз на кнопку загрузить нельзя)
        # Отключить кнопку загрузки
        button1.config(state=tkinter.DISABLED)
        # Установите поток как поток демона через параметр демона (основная программа больше не будет продолжать выполнение при выходе)
        DownloadTaskHandler(daemon=True).start()

    def show_about():  # функция кнопки о программе
        tkinter.messagebox.showinfo('О программе', 'Автор: Андрей (v1.0)')

    top = tkinter.Tk()
    top.title('Загрузка информации')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Загрузить', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='О программе', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':  # проверка основной программы
    main()  # запуск главной функции