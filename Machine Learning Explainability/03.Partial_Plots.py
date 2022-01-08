# Partial Plots
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Environment Set-Up for feedback system.
from learntools.core import binder
binder.bind(globals())
from learntools.ml_explainability.ex3 import *
print("Setup Complete")

# Data manipulation code below here
data = pd.read_csv('../input/new-york-city-taxi-fare-prediction/train.csv', nrows=50000)

# Remove data with extreme outlier coordinates or negative fares
data = data.query('pickup_latitude > 40.7 and pickup_latitude < 40.8 and ' +
                  'dropoff_latitude > 40.7 and dropoff_latitude < 40.8 and ' +
                  'pickup_longitude > -74 and pickup_longitude < -73.9 and ' +
                  'dropoff_longitude > -74 and dropoff_longitude < -73.9 and ' +
                  'fare_amount > 0'
                  )

y = data.fare_amount

base_features = ['pickup_longitude',
                 'pickup_latitude',
                 'dropoff_longitude',
                 'dropoff_latitude']

X = data[base_features]


train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
first_model = RandomForestRegressor(n_estimators=30, random_state=1).fit(train_X, train_y)
print("Data sample:")
data.head()

# Вопрос 1
# Вот код для построения графика частичной зависимости для pickup_longitude. Запустите следующую ячейку.
from matplotlib import pyplot as plt
from pdpbox import pdp, get_dataset, info_plots

feat_name = 'pickup_longitude'
pdp_dist = pdp.pdp_isolate(model=first_model, dataset=val_X, model_features=base_features, feature=feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

for feat_name in base_features:
    pdp_dist = pdp.pdp_isolate(model=first_model, dataset=val_X,
                               model_features=base_features, feature=feat_name)
    pdp.pdp_plot(pdp_dist, feat_name)
    plt.show()

# Из результатов важности перестановки у нас есть ощущение, что расстояние является наиболее важным фактором,
# определяющим стоимость проезда на такси.
#
# Эта модель не включала измерения расстояния (такие как абсолютное изменение широты или долготы) в качестве
# характеристик, поэтому функции координат (такие как pickup_longitude) учитывают влияние расстояния. Если вас
# подберут ближе к центру значений долготы, прогнозируемые тарифы в среднем снижаются, потому что это означает более
# короткие поездки (в среднем).
#
# По той же причине мы видим общую U-образную форму на всех наших графиках частных зависимостей.
#
# вопрос 2
# Теперь вы запустите двухмерный график частичной зависимости. Напоминаю, вот код из туториала.
# Создайте 2D-график для объектов pickup_longitude и dropoff_longitude. Нарисуй как следует?
#
# Как вы ожидаете, что это будет выглядеть?
fnames = ['pickup_longitude', 'dropoff_longitude']
longitudes_partial_plot  =  pdp.pdp_interact(model=first_model, dataset=val_X,
                                            model_features=base_features, features=fnames)
pdp.pdp_interact_plot(pdp_interact_out=longitudes_partial_plot,
                      feature_names=fnames, plot_type='contour')
plt.show()

# Вы должны ожидать, что на графике будут контуры, идущие по диагонали. Мы видим это в некоторой степени,
# хотя есть интересные оговорки.
#
# Мы ожидаем диагональные контуры, потому что это пары значений, в которых долготы посадки и высадки находятся рядом,
# что указывает на более короткие поездки (с учетом других факторов).
#
# По мере удаления от центральной диагонали следует ожидать, что цены будут расти, поскольку расстояния между
# долготами посадки и высадки также увеличиваются.
#
# Удивительной особенностью является то, что цены растут по мере того, как вы продвигаетесь дальше в правый верхний
# угол этого графика, даже оставаясь около этой линии под углом 45 градусов.
#
# Это может заслуживать дальнейшего изучения, хотя эффект перемещения в правый верхний угол этого графика невелик по
# сравнению с удалением от этой линии под углом 45 градусов.
savings_from_shorter_trip = 15

# Вопрос 4
# В PDP, которые вы видели до сих пор, функции местоположения в основном служили в качестве прокси для определения
# пройденного расстояния. На уроках важности перестановки вы добавили функции abs_lon_change и abs_lat_change в
# качестве более прямой меры расстояния.
#
# Создайте эти функции снова здесь. Вам нужно заполнить только две верхние строки. Затем запустите следующую ячейку.
# This is the PDP for pickup_longitude without the absolute difference features. Included here to help compare it to the new PDP you create
feat_name = 'pickup_longitude'
pdp_dist_original = pdp.pdp_isolate(model=first_model, dataset=val_X, model_features=base_features, feature=feat_name)

pdp.pdp_plot(pdp_dist_original, feat_name)
plt.show()



# create new features
data['abs_lon_change'] = abs(data.dropoff_longitude - data.pickup_longitude)
data['abs_lat_change'] = abs(data.dropoff_latitude - data.pickup_latitude)

features_2  = ['pickup_longitude',
               'pickup_latitude',
               'dropoff_longitude',
               'dropoff_latitude',
               'abs_lat_change',
               'abs_lon_change']

X = data[features_2]
new_train_X, new_val_X, new_train_y, new_val_y = train_test_split(X, y, random_state=1)
second_model = RandomForestRegressor(n_estimators=30, random_state=1).fit(new_train_X, new_train_y)

feat_name = 'pickup_longitude'
pdp_dist = pdp.pdp_isolate(model=second_model, dataset=new_val_X, model_features=features_2, feature=feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

# Вопрос 5
# Рассмотрим сценарий, в котором у вас есть только две прогностические функции, которые мы назовем feat_A и feat_B.
# Оба признака имеют минимальные значения -1 и максимальные значения 1. График частичной зависимости для feat_A резко
# возрастает во всем диапазоне, тогда как график частичной зависимости для признака B увеличивается медленнее (менее
# круто) во всем диапазоне.
#
# Гарантирует ли это, что feat_A будет иметь более высокую важность перестановки, чем feat_B. Почему или почему нет?
#
# После того, как вы подумали об этом, раскомментируйте строку ниже для решения.

# Нет. Это не гарантирует, что feat_a важнее. Например, feat_a может иметь большой эффект в тех случаях,
# когда он варьируется, но может иметь одно значение в 99% случаев. В этом случае перестановка feat_a не имеет
# большого значения, так как большинство значений останутся неизменными.



# Вопрос 6
# Ячейка кода ниже делает следующее:
#
# Создает два объекта, X1 и X2, имеющие случайные значения в диапазоне [-2, 2].
# Создает целевую переменную y, которая всегда равна 1.
# Обучает модель RandomForestRegressor прогнозировать y с учетом X1 и X2.
# Создает график PDP для X1 и график рассеяния X1 в зависимости от y.
# У вас есть прогноз о том, как будет выглядеть сюжет PDP? Запустите ячейку, чтобы узнать.
#
# Измените инициализацию y так, чтобы наш график PDP имел положительный наклон в диапазоне [-1,1] и отрицательный
# наклон во всем остальном. (Примечание: вы должны изменить только создание y, оставив без изменений X1,
# X2 и my_model.)

import numpy as np
from numpy.random import rand

n_samples = 20000

# Create array holding predictive feature
X1 = 4 * rand(n_samples) - 2
X2 = 4 * rand(n_samples) - 2
# Create y. you should have X1 and X2 in the expression for y

# There are many possible solutions.
# One example expression for y is.
y = -2 * X1 * (X1<-1) + X1 - 2 * X1 * (X1>1) - X2
# You don't need any more changes

# create dataframe because pdp_isolate expects a dataFrame as an argument
my_df = pd.DataFrame({'X1': X1, 'X2': X2, 'y': y})
predictors_df = my_df.drop(['y'], axis=1)

my_model = RandomForestRegressor(n_estimators=30, random_state=1).fit(predictors_df, my_df.y)

pdp_dist = pdp.pdp_isolate(model=my_model, dataset=my_df, model_features=['X1', 'X2'], feature='X1')

# visualize your results
pdp.pdp_plot(pdp_dist, 'X1')
plt.show()

# Вопрос 7¶
# Создайте набор данных с двумя объектами и целью, чтобы pdp первого объекта был плоским, но его важность
# перестановки была высокой. Мы будем использовать RandomForest для модели.
#
# Примечание. Вам нужно указать только те строки, которые создают переменные X1, X2 и y. Предоставляется код для
# построения модели и расчета аналитических данных.
import eli5
from eli5.sklearn import PermutationImportance

n_samples = 20000

# Create array holding predictive feature
X1 = 4 * rand(n_samples) - 2
X2 = 4 * rand(n_samples) - 2
# Create y. you should have X in the expression for y
y = X1 * X2

# Aside from these lines, use the code provided


# create dataframe because pdp_isolate expects a dataFrame as an argument
my_df = pd.DataFrame({'X1': X1, 'X2': X2, 'y': y})
predictors_df = my_df.drop(['y'], axis=1)

my_model = RandomForestRegressor(n_estimators=30, random_state=1).fit(predictors_df, my_df.y)


pdp_dist = pdp.pdp_isolate(model=my_model, dataset=my_df, model_features=['X1', 'X2'], feature='X1')
pdp.pdp_plot(pdp_dist, 'X1')
plt.show()

perm = PermutationImportance(my_model).fit(predictors_df, my_df.y)

# Check your answer
q_7.check()

# show the weights for the permutation importance you just calculated
eli5.show_weights(perm, feature_names = ['X1', 'X2'])

