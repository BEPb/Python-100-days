# Data Augmentation
# Введение
# В этих упражнениях вы исследуете, какое влияние различные случайные преобразования оказывают на изображение,
# рассмотрите, какой вид дополнения может быть уместным для данного набора данных, а затем использовать увеличение
# данных с помощью набора данных Car или Truck для обучения настраиваемой сети.
#
# Запустите ячейку ниже, чтобы все настроить!
# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.computer_vision.ex6 import *

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

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

# Изучите Augmentation¶
# all of the "factor" parameters indicate a percent-change
augment = keras.Sequential([
    # preprocessing.RandomContrast(factor=0.5),
    preprocessing.RandomFlip(mode='horizontal'), # meaning, left-to-right
    # preprocessing.RandomFlip(mode='vertical'), # meaning, top-to-bottom
    # preprocessing.RandomWidth(factor=0.15), # horizontal stretch
    # preprocessing.RandomRotation(factor=0.20),
    # preprocessing.RandomTranslation(height_factor=0.1, width_factor=0.1),
])


ex = next(iter(ds_train.unbatch().map(lambda x, y: x).batch(1)))

plt.figure(figsize=(10,10))
for i in range(16):
    image = augment(ex, training=True)
    plt.subplot(4, 4, i+1)
    plt.imshow(tf.squeeze(image))
    plt.axis('off')
plt.show()

# Выбранные вами преобразования кажутся разумными для набора данных Car или Truck?
#

# В этом упражнении мы рассмотрим несколько наборов данных и подумаем, какие расширения могут быть уместными. Ваше
# рассуждение может отличаться от того, что мы обсуждаем в решении. Это нормально. Суть этих проблем - просто
# подумать о том, как преобразование может взаимодействовать с проблемой классификации - к лучшему или к худшему.

# Набор данных EuroSAT состоит из спутниковых изображений Земли, классифицированных по географическим признакам. Ниже
# приведены несколько изображений из этого набора данных.

# 1) EuroSAT
# Какие преобразования могут быть подходящими для этого набора данных?

# 2) Цветы TensorFlow
# Какие виды преобразований могут быть подходящими для набора данных TensorFlow Flowers?

# Автору кажется, что сначала стоит попробовать горизонтальные сальто и умеренные вращения. Некоторые библиотеки
# дополнений включают преобразование оттенка (например, красного в синий). Поскольку цвет цветка кажется
# отличительным от его сорта, изменение оттенка может быть менее успешным. С другой стороны, существует удивительное
# разнообразие культурных цветов, таких как розы, так что, в зависимости от набора данных, в конце концов,
# это может быть улучшением!

# Теперь вы будете использовать расширение данных с помощью настраиваемой свертки, аналогичной той, которую вы
# создали в упражнении 5. Поскольку увеличение данных эффективно увеличивает размер набора данных, мы,
# в свою очередь, можем увеличить емкость модели без большого риска переобучения.
#

# 3) Добавить слои предварительной обработки
# Добавьте эти слои предварительной обработки к данной модели.

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.InputLayer(input_shape=[128, 128, 3]),

    # Data Augmentation
    preprocessing.RandomContrast(factor=0.10),
    preprocessing.RandomFlip(mode='horizontal'),
    preprocessing.RandomRotation(factor=0.10),

    # Block One
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Two
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Three
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
    layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Head
    layers.BatchNormalization(renorm=True),
    layers.Flatten(),
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

# Теперь обучим модель. Запустите следующую ячейку, чтобы скомпилировать ее с метрикой потерь и точности и подогнать
# под обучающий набор.

optimizer = tf.keras.optimizers.Adam(epsilon=0.01)
model.compile(
    optimizer=optimizer,
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

history = model.fit(
    ds_train,
    validation_data=ds_valid,
    epochs=50,
)

# Plot learning curves
import pandas as pd
history_frame = pd.DataFrame(history.history)
history_frame.loc[:, ['loss', 'val_loss']].plot()
history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot();

# 4) Модель поезда
# Изучите тренировочные кривые. Какие там переоснащения? Как производительность этой модели сравнивается с другими
# моделями, которые вы обучили в этом курсе?


# Решение: кривые обучения в этой модели оставались близкими гораздо дольше, чем в предыдущих моделях. Это говорит о том, что аугментация помогла предотвратить переоснащение, позволяя модели продолжать улучшаться.
#
# И обратите внимание, что эта модель показала наивысшую точность из всех моделей курса! Это не всегда так, но это показывает, что хорошо спроектированная настраиваемая свёртка иногда может работать так же или лучше, чем гораздо более крупная предварительно обученная модель. В зависимости от вашего приложения, наличие модели меньшего размера (которая требует меньше ресурсов) может быть большим преимуществом.
#

# Вывод
# Увеличение данных - мощный и широко используемый инструмент для улучшения обучения моделей не только для сверточных сетей, но и для многих других типов моделей нейронных сетей. Какой бы ни была ваша проблема, принцип остается тем же: вы можете восполнить неадекватность ваших данных, добавив «фальшивые» данные, чтобы скрыть это. Поэкспериментируйте с дополнениями - отличный способ узнать, насколько далеко могут зайти ваши данные!
#

# Конец
# Это все, что касается компьютерного зрения на Kaggle Learn! Готовы ли вы применить свои знания? Посмотрите наши два бонусных урока! Они проведут вас через подготовку заявки на соревнование, а вы узнаете, как тренировать нейронные сети с помощью TPU, самого продвинутого ускорителя Kaggle. В конце концов, у вас будет полный блокнот, который можно дополнить вашими собственными идеями.
#
# Создайте свою первую заявку - подготовьте заявку для наших лепестков на конкурс Metal Getting Started. Вы научите нейронную сеть распознавать более 100 видов цветов.
# Болезнь листьев маниоки - Скорее соревноваться за деньги и медали? Обучите нейронную сеть для диагностики распространенных заболеваний маниоки, одной из основных культур для обеспечения безопасности в Африке.
# Удачи в обучении!


