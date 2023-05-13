# Deep Neural Networks
import tensorflow as tf

# Setup plotting
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)

# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.deep_learning_intro.ex2 import *

import pandas as pd

concrete = pd.read_csv('../input/dl-course-data/concrete.csv')
concrete.head()

# YOUR CODE HERE
input_shape = [8]

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=input_shape),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1),
])

# 3) Слои активации
# Давайте рассмотрим некоторые функции активации.
#
# Обычный способ прикрепления функции активации к плотному слою - включить ее как часть определения с аргументом
# активации. Иногда вам нужно поместить какой-то другой слой между плотным слоем и его функцией активации. (Мы увидим
# пример этого в Уроке 5 с пакетной нормализацией.) В этом случае мы можем определить активацию на собственном уровне
# активации, например так:
#
# слои плотные (единиц = 8),
# слои.Активация ('relu')
# Это полностью эквивалентно обычному способу: Layers.Dense (units = 8, Activation = 'relu').
#
# Перепишите следующую модель, чтобы каждая активация находилась на своем собственном уровне активации.

model = keras.Sequential([
    layers.Dense(32, input_shape=[8]),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(1),
])

# Необязательно: альтернативы ReLU
# Существует целое семейство вариантов активации «relu» - «elu», «selu» и «swish» среди прочих - все из которых вы
# можете использовать в Keras. Иногда одна активация будет работать лучше, чем другая для данной задачи, поэтому вы
# можете попробовать поэкспериментировать с активациями при разработке модели. Активация ReLU, как правило,
# справляется с большинством проблем, так что это хороший вариант для начала.
#
# Давайте посмотрим на графики некоторых из них. Измените активацию с «relu» на одну из вышеперечисленных. Затем
# запустите ячейку, чтобы увидеть график. (Дополнительные идеи можно найти в документации.)

# YOUR CODE HERE: Change 'relu' to 'elu', 'selu', 'swish'... or something else
activation_layer = layers.Activation('relu')

x = tf.linspace(-3.0, 3.0, 100)
y = activation_layer(x) # once created, a layer is callable just like a function

plt.figure(dpi=100)
plt.plot(x, y)
plt.xlim(-3, 3)
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()
