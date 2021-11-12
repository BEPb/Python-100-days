"""
При использовании нескольких потоков трудоемкие задачи выполняются в отдельных потоках.

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            # Имитация задачи загрузки занимает 10 секунд
            time.sleep(10)
            tkinter.messagebox.showinfo('подсказка', 'загрузка завершена!')
            # Включить кнопку загрузки
            button1.config(state=tkinter.NORMAL)

    def download():
        # Отключить кнопку загрузки
        button1.config(state=tkinter.DISABLED)
        # Установите поток как поток демона через параметр демона (основная программа больше не будет продолжать выполнение при выходе)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('О программе', 'Автор: Андрей (v1.0)')

    top = tkinter.Tk()
    top.title('резьбовым')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='About', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
