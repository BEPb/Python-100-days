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
from learntools.deep_learning_intro.ex1 import *

import pandas as pd

red_wine = pd.read_csv('../input/dl-course-data/red-wine.csv')
red_wine.head()

red_wine.shape # (rows, columns)

# 1) Форма ввода
# Насколько хорошо мы можем предсказать воспринимаемое качество вина по физико-химическим измерениям?
#
# Цель - «качество», а остальные столбцы - это характеристики. Как бы вы установили параметр input_shape для модели
# Keras в этой задаче?
# YOUR CODE HERE
input_shape = [11]

from tensorflow import keras
from tensorflow.keras import layers

# YOUR CODE HERE
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[11])
])

# 3) Посмотрите на вес
# Внутри Keras представляет веса нейронной сети с тензорами. Тензоры - это, по сути, версия TensorFlow массива Numpy
# с некоторыми отличиями, которые делают их более подходящими для глубокого обучения. Одним из наиболее важных
# является то, что тензоры совместимы с ускорителями GPU и TPU. Фактически, TPU разработаны специально для тензорных
# вычислений.
#
# Веса модели хранятся в ее атрибуте weights в виде списка тензоров. Получите веса модели, которую вы определили
# выше. (Если хотите, вы можете отобразить веса примерно так: print ("Weights \ n {} \ n \ nBias \ n {}". Format (w,
# b))).

w, b = model.weights

print("Weights\n{}\n\nBias\n{}".format(w, b))


import tensorflow as tf
import matplotlib.pyplot as plt

model = keras.Sequential([
    layers.Dense(1, input_shape=[1]),
])

x = tf.linspace(-1.0, 1.0, 100)
y = model.predict(x)

plt.figure(dpi=100)
plt.plot(x, y, 'k')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("Input: x")
plt.ylabel("Target y")
w, b = model.weights # you could also use model.get_weights() here
plt.title("Weight: {:0.2f}\nBias: {:0.2f}".format(w[0][0], b[0]))
plt.show()
