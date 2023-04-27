"""
Python 3.9 почтовый-клиент SMTP-протокол
Название файла '14.почтовый-клиент.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():  # главная функция
    message = MIMEMultipart()
    text_content = MIMEText('текст сообщения', 'plain', 'utf-8')
    message['Subject'] = Header('Здравствуте!', 'utf-8')
    message.attach(text_content)

    with open('/Users/admin/Desktop/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    with open('/Users/admin/Desktop/hi.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)

    smtper = SMTP('smtp.222.com')
    # smtper.starttls()
    sender = 'abcdefg@222.com'
    receivers = ['uvwxyz@qq.com']
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('почта отправлена!')


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
