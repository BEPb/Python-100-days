# Custom Convnets
# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.computer_vision.ex5 import *

# Imports
import os, warnings
import matplotlib.pyplot as plt
from matplotlib import gridspec

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Reproducability
def set_seed(seed=31415):
    np.random.seed(seed)
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
set_seed()

# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')
warnings.filterwarnings("ignore") # to clean up output cells


# Load training and validation sets
ds_train_ = image_dataset_from_directory(
    '../input/car-or-truck/train',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=True,
)
ds_valid_ = image_dataset_from_directory(
    '../input/car-or-truck/valid',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=False,
)

# Data Pipeline
def convert_to_float(image, label):
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    return image, label

AUTOTUNE = tf.data.experimental.AUTOTUNE
ds_train = (
    ds_train_
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)
ds_valid = (
    ds_valid_
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)

# Создайте Convnet
# Давайте спроектируем сверточную сеть с блочной архитектурой, как мы видели в руководстве. Модель из примера
# состояла из трех блоков, каждый с одним сверточным слоем. Его производительность в задаче «Автомобиль или грузовик»
# была удовлетворительной, но далека от того, чего мог достичь предварительно обученный VGG16. Возможно,
# в нашей простой сети отсутствует возможность извлекать достаточно сложные функции. Мы могли бы попробовать улучшить
# модель, добавив больше блоков или добавив свертки к имеющимся у нас блокам.
#
# Пойдем со вторым подходом. Мы сохраним трехблочную структуру, но увеличим количество слоев Conv2D во втором блоке
# до двух, а в третьем блоке до трех.

# 1) Определить модель
# Учитывая диаграмму выше, завершите модель, определив слои третьего блока.

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    # Block One
    layers.Conv2D(filters=32, kernel_size=3, activation='relu', padding='same',
                  input_shape=[128, 128, 3]),
    layers.MaxPool2D(),

    # Block Two
    layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Three
    layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
    layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Head
    layers.Flatten(),
    layers.Dense(6, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid'),
])

# 2) Скомпилировать
# Чтобы подготовиться к обучению, скомпилируйте модель с соответствующей метрикой потерь и точности для набора данных
# «Автомобиль или грузовик».

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

# Наконец, давайте протестируем производительность этой новой модели. Сначала запустите эту ячейку, чтобы подогнать
# модель к обучающей выборке.
history = model.fit(
    ds_train,
    validation_data=ds_valid,
    epochs=50,
)

# А теперь запустите ячейку ниже, чтобы построить кривые потерь и метрики для этого тренировочного прогона.
import pandas as pd
history_frame = pd.DataFrame(history.history)
history_frame.loc[:, ['loss', 'val_loss']].plot()
history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot();

# 3) Обучите модель
# Как бы вы интерпретировали эти тренировочные кривые? Эта модель улучшила модель из учебника?

# Вывод
# Эти упражнения показали вам, как разработать собственную сверточную сеть для решения конкретной задачи
# классификации. Хотя большинство моделей в наши дни будут построены на основе предварительно обученной базы,
# в определенных обстоятельствах меньшая настраиваемая свёртка может быть предпочтительнее - например, с меньшим или
# необычным набором данных или когда вычислительные ресурсы очень ограничены. Как вы видели здесь, с некоторыми
# проблемами они могут работать так же хорошо, как и предварительно обученные модели.






