import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
import os
if not os.path.exists("../input/museum_visitors.csv"):
    os.symlink("../input/data-for-datavis/museum_visitors.csv", "../input/museum_visitors.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex2 import *
print("Setup Complete")

# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

# Print the last five rows of the data
museum_data.tail()
# How many visitors did the Chinese American Museum
# receive in July 2018?
ca_museum_jul18 = 2620
# In October 2018, how many more visitors did Avila
# Adobe receive than the Firehouse Museum?
avila_oct18 = 14658


# Шаг 3: убедите музейный совет
# Музей  Firehouse утверждает, что в 2014 году они проводили мероприятие, которое привлекло невероятное количество
# посетителей, и что им нужно получить дополнительный бюджет, чтобы провести подобное мероприятие снова. Другие
# музеи считают,  что такие мероприятия не так уж и важны, и бюджеты следует разделить исключительно на основе
# недавних посетителей в среднем за день.
#
# Чтобы показать  на доске музея, как мероприятие сравнивается с обычным трафиком в каждом музее, создайте линейную
# диаграмму, которая  показывает, как количество посетителей каждого музея менялось с течением времени. На вашей
# фигуре должно быть четыре линии (по одной на каждый музей).
#
# (Необязательно)  Примечание. Если у вас есть опыт построения графиков в Python, возможно, вы знакомы с командой
# plt.show ().  Если вы решите использовать эту команду, поместите ее после строки кода, проверяющей ваш ответ (в
# этом случае поместите ее после step_3.check () ниже) - в противном случае проверочный код вернет ошибку!

# Set the width and height of the figure
plt.figure(figsize=(12,6))
# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data)
# Add title
plt.title("Monthly Visitors to Los Angeles City Museums")


# Шаг 4. Оцените сезонность
# Встречаясь с сотрудниками  Avila Adobe, вы слышите, что одна из основных проблем заключается в том, что количество
# посетителей музея сильно  варьируется в зависимости от сезона, от низкого сезона (когда сотрудники отлично
# укомплектованы и счастливы),  а также высокого сезона (когда сотрудники недоукомплектованы и подвержены стрессу).
# Вы понимаете, что, если вы  можете предсказать эти высокие и низкие сезоны, вы можете заранее спланировать найм
# дополнительных сезонных сотрудников, которые помогут с дополнительной работой.
#
# Часть А
# Создайте линейную диаграмму,  показывающую, как количество посетителей Avila Adobe менялось с течением времени. (
# Если ваш код возвращает ошибку,  первое, что вы должны проверить, - правильно ли вы написали имя столбца! Вы должны
# написать имя столбца точно так,  как оно отображается в наборе данных.)

# Line plot showing the number of visitors to Avila Adobe over time

# Set the width and height of the figure
plt.figure(figsize=(12,6))
# Add title
plt.title("Monthly Visitors to Avila Adobe")
# Line chart showing the number of visitors to Avila Adobe over time
sns.lineplot(data=museum_data['Avila Adobe'])
# Add label for horizontal axis
plt.xlabel("Date")

# Часть B
# Привлекает ли Avila Adobe больше посетителей:
#
# в сентябре-феврале (в Лос-Анджелесе осенние и зимние месяцы), или
# в марте-августе (в ЛА весной и летом)?
# Используя эту информацию, когда следует укомплектовать музей дополнительными сезонными сотрудниками?











