# Convolution and ReLU
# Введение¶
# В этом упражнении вы поработаете немного над извлечением признаков. Сначала мы еще раз рассмотрим пример,
# который мы использовали в руководстве, но на этот раз с ядром, которое вы выберете сами. В этом курсе мы в основном
# работали с изображениями, но за всеми операциями, которые мы изучаем, стоит математика. Итак, мы также рассмотрим,
# как эти карты функций могут быть представлены в виде массивов чисел и какое влияние на них окажет свертка с ядром.

# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.computer_vision.ex2 import *

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')

tf.config.run_functions_eagerly(True)

# Применить преобразования¶
# Следующие несколько упражнений посвящены извлечению признаков так же, как и в примере в руководстве. Запустите
# следующую ячейку, чтобы загрузить изображение, которое мы будем использовать в следующих нескольких упражнениях.

image_path = '../input/computer-vision-resources/car_illus.jpg'
image = tf.io.read_file(image_path)
image = tf.io.decode_jpeg(image, channels=1)
image = tf.image.resize(image, size=[400, 400])

img = tf.squeeze(image).numpy()
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show();

# Вы можете запустить эту ячейку, чтобы увидеть некоторые стандартные ядра, используемые при обработке изображений.

import learntools.computer_vision.visiontools as visiontools
from learntools.computer_vision.visiontools import edge, bottom_sobel, emboss, sharpen

kernels = [edge, bottom_sobel, emboss, sharpen]
names = ["Edge Detect", "Bottom Sobel", "Emboss", "Sharpen"]

plt.figure(figsize=(12, 12))
for i, (kernel, name) in enumerate(zip(kernels, names)):
    plt.subplot(1, 4, i+1)
    visiontools.show_kernel(kernel)
    plt.title(name)
plt.tight_layout()

# 1) Определить ядро
# Используйте следующую ячейку кода, чтобы определить ядро. У вас есть выбор, какое ядро применить. Следует иметь в
# виду, что сумма чисел в ядре определяет, насколько ярким будет окончательное изображение. Как правило,
# вы должны стараться сохранять сумму чисел от 0 до 1 (хотя это не требуется для правильного ответа).

# В общем, ядро может иметь любое количество строк и столбцов. Для этого упражнения давайте использовать ядро 3 × 3,
# которое часто дает наилучшие результаты. Определите ядро с tf.constant.

# This is just one possibility.
kernel = tf.constant([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2],
])

# Теперь мы сделаем первый шаг извлечения признаков, шаг фильтрации. Сначала запустите эту ячейку, чтобы немного
# переформатировать TensorFlow.
# Reformat for batch compatibility.
image = tf.image.convert_image_dtype(image, dtype=tf.float32)
image = tf.expand_dims(image, axis=0)
kernel = tf.reshape(kernel, [*kernel.shape, 1, 1])
kernel = tf.cast(kernel, dtype=tf.float32)

# 2) Применить свертку
# Теперь применим ядро к изображению путем свертки. Слой в Keras, который делает это, - Layers.Conv2D. Какая
# бэкэнд-функция в TensorFlow выполняет ту же операцию?

conv_fn = tf.nn.conv2d

# Получив правильный ответ, запустите следующую ячейку, чтобы выполнить свертку и увидеть результат!
image_filter = conv_fn(
    input=image,
    filters=kernel,
    strides=1, # or (1, 1)
    padding='SAME',
)

plt.imshow(
    # Reformat for plotting
    tf.squeeze(image_filter)
)
plt.axis('off')
plt.show();

# Можете ли вы увидеть, как выбранное ядро соотносится с созданной им картой функций?
#
# 3) Применить ReLU
# Теперь определите эту особенность с помощью функции ReLU. В Keras вы обычно используете это как функцию активации
# на уровне Conv2D. Какая бэкэнд-функция в TensorFlow делает то же самое?

relu_fn = tf.nn.relu

# Изображение, которое вы видите ниже, представляет собой карту функций, созданную выбранным вами ядром. Если хотите,
# поэкспериментируйте с некоторыми из других предложенных выше ядер или попробуйте изобрести ядро, которое будет
# извлекать определенные функции.
image_detect = relu_fn(image_filter)

plt.imshow(
    # Reformat for plotting
    tf.squeeze(image_detect)
)
plt.axis('off')
plt.show();

# В этом руководстве мы обсуждали ядра и карты функций в основном визуально. Мы увидели эффект Conv2D и ReLU,
# наблюдая, как они преобразовывают некоторые изображения в качестве примера.
#
# Но операции в сверточной сети (как и во всех нейронных сетях) обычно определяются с помощью математических функций,
# путем вычисления чисел. В следующем упражнении мы уделим немного времени исследованию этой точки зрения.
#
# Давайте начнем с определения простого массива, который будет действовать как изображение, и другого массива,
# который будет действовать как ядро. Запустите следующую ячейку, чтобы увидеть эти массивы.

# Sympy is a python library for symbolic mathematics. It has a nice
# pretty printer for matrices, which is all we'll use it for.
import sympy
sympy.init_printing()
from IPython.display import display

image = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
])

kernel = np.array([
    [1, -1],
    [1, -1],
])

display(sympy.Matrix(image))
display(sympy.Matrix(kernel))
# Reformat for Tensorflow
image = tf.cast(image, dtype=tf.float32)
image = tf.reshape(image, [1, *image.shape, 1])
kernel = tf.reshape(kernel, [*kernel.shape, 1, 1])
kernel = tf.cast(kernel, dtype=tf.float32)

# 4) Наблюдать свертку на числовой матрице¶
# Что ты видишь? Изображение представляет собой длинную вертикальную линию слева и короткую горизонтальную линию
# справа внизу. Что с ядром? Как вы думаете, как это повлияет на это изображение? После того, как вы подумали об
# этом, запустите следующую ячейку, чтобы получить ответ.

# Правильный:
# В этом руководстве мы говорили о том, как образец положительных чисел сообщает вам, какие функции будет извлекать
# ядро. Это ядро имеет вертикальный столбец из единиц, поэтому мы ожидаем, что оно вернет функции вертикальных линий.
#
# А теперь попробуем. Запустите следующую ячейку, чтобы применить свертку и ReLU к изображению и отобразить результат.
image_filter = tf.nn.conv2d(
    input=image,
    filters=kernel,
    strides=1,
    padding='VALID',
)
image_detect = tf.nn.relu(image_filter)

# The first matrix is the image after convolution, and the second is
# the image after ReLU.
display(sympy.Matrix(tf.squeeze(image_filter).numpy()))
display(sympy.Matrix(tf.squeeze(image_detect).numpy()))
# Результат такой, как вы ожидали?
#
# Вывод
# В этом уроке вы узнали о первых двух операциях, которые сверточный классификатор использует для извлечения
# признаков: фильтрация изображения с помощью свертки и обнаружение признака с помощью выпрямленного линейного блока.


