# Setup plotting
import matplotlib.pyplot as plt
from learntools.deep_learning_intro.dltools import animate_sgd
plt.style.use('seaborn-whitegrid')
# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('animation', html='html5')

# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.deep_learning_intro.ex3 import *

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.model_selection import train_test_split

fuel = pd.read_csv('../input/dl-course-data/fuel.csv')

X = fuel.copy()
# Remove target
y = X.pop('FE')

preprocessor = make_column_transformer(
    (StandardScaler(),
     make_column_selector(dtype_include=np.number)),
    (OneHotEncoder(sparse=False),
     make_column_selector(dtype_include=object)),
)

X = preprocessor.fit_transform(X)
y = np.log(y) # log transform target instead of standardizing

input_shape = [X.shape[1]]
print("Input shape: {}".format(input_shape))

# Uncomment to see original data
fuel.head()
# Uncomment to see processed features
pd.DataFrame(X[:10,:]).head()

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=input_shape),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(1),
])

model.compile(
    optimizer='adam',
    loss='mae'
)

history = model.fit(
    X, y,
    batch_size=128,
    epochs=200
)

import pandas as pd

history_df = pd.DataFrame(history.history)
# Start the plot at epoch 5. You can change this to get a different view.
history_df.loc[5:, ['loss']].plot();


# Это зависит от того, как развивались потери во время обучения: если кривые обучения выровнялись, обычно не будет
# никаких преимуществ от обучения для дополнительных эпох. И наоборот, если кажется, что потери все еще уменьшаются,
# то более длительная тренировка может быть полезной.
#
# Благодаря скорости обучения и размеру пакета у вас есть некоторый контроль над:
#
# Сколько времени нужно на обучение модели
# Насколько шумны кривые обучения
# Насколько малы потери
# Чтобы лучше понять эти два параметра, мы рассмотрим линейную модель, нашу простейшую нейронную сеть. Имея только
# один вес и смещение, легче увидеть, какой эффект имеет изменение параметра.
#
# Следующая ячейка сгенерирует анимацию, как в учебнике. Измените значения для learning_rate, batch_size и
# num_examples (сколько точек данных), а затем запустите ячейку. (Это может занять минуту или две.) Попробуйте
# следующие комбинации или попробуйте свои собственные:


# YOUR CODE HERE: Experiment with different values for the learning rate, batch size, and number of examples
learning_rate = 0.05
batch_size = 32
num_examples = 256

animate_sgd(
    learning_rate=learning_rate,
    batch_size=batch_size,
    num_examples=num_examples,
    # You can also change these, if you like
    steps=50, # total training steps (batches seen)
    true_w=3.0, # the slope of the data
    true_b=2.0, # the bias of the data
)

