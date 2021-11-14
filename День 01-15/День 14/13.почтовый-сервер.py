"""
Python 3.9 почтовый-сервер SMTP-протокол
Название файла '13.почтовый-сервер.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():  # главная функция
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com', 'uvwxyz@126.com']
    message = MIMEText('Письмо для Вас.', 'plain', 'utf-8')
    message['From'] = Header('Andrej', 'utf-8')
    message['To'] = Header('You', 'utf-8')
    message['Subject'] = Header('Переговоры', 'utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('Письмо отправлено!')


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию