# Введение
# В этом уроке мы увидели, как создать классификатор изображений, прикрепив головку из плотных слоев к предварительно
# обученной основе. База, которую мы использовали, была от модели под названием VGG16. Мы увидели, что архитектура
# VGG16 была склонна переоценивать этот набор данных. В ходе этого курса вы узнаете несколько способов улучшить эту
# первоначальную попытку.
# Первый способ, который вы увидите, - это использовать базу, более подходящую для набора данных. База, на которой
# основана эта модель, называется InceptionV1 (также известная как GoogLeNet). InceptionV1 был одним из первых
# победителей конкурса ImageNet. Один из его преемников, InceptionV4, сегодня является одним из самых современных.

# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.computer_vision.ex1 import *

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

# Модель InceptionV1, предварительно обученная в ImageNet, доступна в репозитории TensorFlow Hub, но мы загрузим ее
# из локальной копии. Запустите эту ячейку, чтобы загрузить InceptionV1 для своей базы.

import tensorflow_hub as hub

pretrained_base = tf.keras.models.load_model(
    '../input/cv-course-models/cv-course-models/inceptionv1'
)

# 1) Определите предварительно обученную базу
# Теперь, когда у вас есть предварительно обученная база для извлечения наших признаков, решите, должна ли эта база
# быть обучаемой или нет.

# YOUR_CODE_HERE
pretrained_base.trainable = False

# Правильно: при переносе обучения, как правило, не рекомендуется переобучать всю базу - по крайней мере,
# без некоторой осторожности. Причина в том, что случайные веса в голове изначально создают большие обновления
# градиента, которые распространяются обратно на базовые слои и уничтожают большую часть предварительной тренировки.
# Используя методы, известные как точная настройка, можно дополнительно обучить базу на новых данных, но для этого
# требуется некоторая осторожность.

# 2) Прикрепите голову
# Теперь, когда база определена для извлечения признаков, создайте заголовок плотных слоев для выполнения классификации,
# Подсказка: вам нужно добавить два новых плотных слоя. У первого должно быть 6 юнитов и активация relu. Второй
# должен иметь 1 единицу и «сигмовидную» активацию.

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    pretrained_base,
    layers.Flatten(),
    # YOUR CODE HERE. Attach a head of dense layers.
    layers.Dense(6, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

# 3) Тренировка
# Перед обучением модели в Keras вам необходимо указать оптимизатор для выполнения градиентного спуска,
# функцию потерь, которая должна быть минимизирована, и (необязательно) любые показатели производительности. Алгоритм
# оптимизации, который мы будем использовать в этом курсе, называется «Адам», который обычно хорошо работает
# независимо от того, какую проблему вы пытаетесь решить.

# Однако потери и показатели должны соответствовать той проблеме, которую вы пытаетесь решить. Наша проблема -
# проблема двоичной классификации: автомобиль закодирован как 0, а грузовик закодирован как 1. Выберите подходящие
# потери и соответствующую метрику точности для двоичной классификации.
optimizer = tf.keras.optimizers.Adam(epsilon=0.01)
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

# train
history = model.fit(
    ds_train,
    validation_data=ds_valid,
    epochs=30,
)

# analiz
import pandas as pd
history_frame = pd.DataFrame(history.history)
history_frame.loc[:, ['loss', 'val_loss']].plot()
history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot();

# 4) Изучите потери и точность
# Вы замечаете разницу между этими кривыми обучения и кривыми для VGG16 из учебника? Что эта разница говорит вам о
# том, чему научилась эта модель (InceptionV2) по сравнению с VGG16? Есть ли способы, в которых один лучше другого?
# Худший?
# После того, как вы подумали об этом, запустите ячейку ниже, чтобы увидеть ответ.

# То, что потеря обучения и потеря проверки остаются довольно близкими, свидетельствует о том, что модель не просто
# запоминает данные обучения, а, скорее, изучает общие свойства двух классов. Но поскольку эта модель сходится с
# большими потерями, чем модель VGG16, вполне вероятно, что она недостаточно подходит для некоторых и может выиграть
# от некоторой дополнительной емкости.

# Вывод
# В этом первом уроке вы изучили основы сверточных классификаторов изображений, которые состоят из основы для
# извлечения функций из изображений и головы, которая использует функции для определения класса изображения. Вы также
# увидели, как построить классификатор с трансферным обучением на предварительно обученной основе.


