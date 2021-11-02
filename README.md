![Profile views](https://gpvc.arturio.dev/BEPb) 
![GitHub top language](https://img.shields.io/github/languages/top/BEPb/django-phonebook) 
![GitHub language count](https://img.shields.io/github/languages/count/BEPb/django-phonebook)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BEPb/django-phonebook)
![GitHub repo size](https://img.shields.io/github/repo-size/BEPb/django-phonebook) 
![GitHub](https://img.shields.io/github/license/BEPb/django-phonebook) 
![GitHub last commit](https://img.shields.io/github/last-commit/BEPb/django-phonebook)

![GitHub User's stars](https://img.shields.io/github/stars/BEPb?style=social)
## Сайт телефонный корпоративный справочник

____
![](./phonebooke_site/media/photos/do-web-development-using-python-django.png)
____

Сайт телефонный корпоративный справочник написан на фреймворке python Django, используется по умолчанию СУБД SQLite3. В данном проекте используются:
- одно приложение 'phonebook', применяется двухуровневый шаблон страниц (с подгрузкой навбара и сайдбара);
- подключена статика bootstrap в локальном режиме (позволяет запустить сервер офлайн) все элементы сохранят свой вид;
- реализованы пользовательские теги;
- реализованы формы заполнения данных;
- реализована регистрация, вход, аутентификция и разграничение прав пользователей;
- реализована пагинация данных;
- применяются мексины;  
- подключено приложение для отладки сайта DebagToolbar.


___
Содержание проекта:
- папка data - место хранения исходных капч (5 цифр)
- README.md - описание проекта
- update_pakets.py -  обновление пакетов проекта в автоматическом режиме
- django_command - описание команд python при подготовке проекта и его запуска
- for_mysql.py -  проверка подключения к базе данных MySQL

- папка phonebooke_site - размещение проекта
- db.sqlite3 - база данных sqlite3
- manage.py - основной исполняемый файл сайта
- my.cnf - конфигурация MySQL
- mySQL_command - команды MySQL
- django_cache - папка для хранения кеша
- media - папка хранения медиафайлов (фотографий)
- phonebook - папка приложения телефонный справочник
- phonebooke_site - папка размещения основы сайта
- static - папка для размещения статических файлов
- templates - папка хранения htmal страниц

____

Библиотеки применяемые в проекте:
- settings - подгружаем настройки в режиме отладки
- static, path, include, reverse_lazy - для работы с статическими, ленивыми и url адресами
- forms - модуль работы с формами
- re - модуль регулярных выражений, для работы с данными в форме (для применения собственных проверок
- ValidationError - модуль обработок собственных ошибок
- UserCreationForm, AuthenticationForm - модуль регистрации пользователя и логирования
- User - модуль работы с пользователями
- send_mail - модуль отправки сообщений
- models - импортируем модуль работы с базами данных
- LoginRequiredMixin - импортируем штатный миксин проверки аутентификации
- Paginator - пагинация страниц
- UserCreationForm  - создание формы регистрации пользователя
- messages - модуль сообщений
- login, logout - модуль логирования и выхода
- send_mail - модуль отправки сообщений
- Count, F - модуль подсчета значений и фильтрации 


### Клонируем репозиторий (Clone the repository)
 
```sh
$ cmd
$ git clone https://github.com/BEPb/first.git
$ cd django-phonebook
```
 
### Устанавливаем необходимые пакеты (Install dependencies)
```sh
$ pip install -r requirements.txt / pipenv install
```
 
### Запускаем локальный сервер (Run the application locally)
 
```sh
$ python manage.py runserver
```
Открывает Ваш браузер по адресу http://localhost:8000/
 
