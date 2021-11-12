"""
Когда не используются многопоточные задачи, требующие много времени, блокировка основного цикла событий

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox


def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('подсказка' , 'загрузка завершена!')


def show_about():
    tkinter.messagebox.showinfo('О программе', 'Автор: Андрей (v1.0)' )


def main():
    top = tkinter.Tk()
    top.title('резьбовым')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='About', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()


# После того, как вы нажмете кнопку загрузки без использования многопоточности, эта операция займет 10 секунд
# Весь основной цикл сообщений также будет заблокирован на 10 секунд и не сможет реагировать на другие события
# На самом деле последовательное выполнение подзадач без причинно-следственной связи нецелесообразно
