# Setup feedback system
# from learntools.core import binder
# binder.bind(globals())
# from learntools.feature_engineering_new.ex6 import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
from category_encoders import MEstimateEncoder
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

# Set Matplotlib defaults
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)
warnings.filterwarnings('ignore')


def score_dataset(X, y, model=XGBRegressor()):
    # Label encoding for categoricals
    for colname in X.select_dtypes(["category", "object"]):
        X[colname], _ = X[colname].factorize()
    # Metric for Housing competition is RMSLE (Root Mean Squared Log Error)
    score = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_squared_log_error",
    )
    score = -1 * score.mean()
    score = np.sqrt(score)
    return score


df = pd.read_csv("../input/fe-course-data/ames.csv")

# Сначала вам нужно выбрать, к каким функциям вы хотите применить целевую кодировку. Категориальные признаки с
# большим количеством категорий часто являются хорошими кандидатами. Запустите эту ячейку, чтобы увидеть,
# сколько категорий имеет каждая категориальная функция в наборе данных Эймса.

df.select_dtypes(["object"]).nunique()

# Мы говорили о том, как кодирование M-оценки использует сглаживание для улучшения оценок для редких категорий. Чтобы
# узнать, сколько раз категория встречается  в наборе данных, вы можете использовать метод value_counts. Эта ячейка
# показывает количество для SaleType, но вы можете рассмотреть и другие.

df["SaleType"].value_counts()

# 1) Выберите функции для кодирования
# Какие функции вы определили для целевой кодировки? После того, как вы обдумали свой ответ, запустите следующую
# ячейку для обсуждения.

# Функция "Окрестности" выглядит  многообещающей. У него больше всего категорий среди всех функций, а некоторые
# категории встречаются редко.  Также стоит подумать о SaleType, MSSubClass, Exterior1st, Exterior2nd. Фактически,
# стоит попробовать практически любую из номинальных характеристик из-за преобладания редких категорий.
#
# добавить Codeadd Markdown
# Теперь вы примените целевую кодировку к выбранной вами функции. Как мы обсуждали в руководстве, чтобы избежать
# переобучения, нам нужно подогнать кодировщик к данным, хранящимся в обучающем наборе. Запустите эту ячейку,
# чтобы создать расщепления кодирования и обучения:

# Encoding split
X_encode = df.sample(frac=0.20, random_state=0)
y_encode = X_encode.pop("SalePrice")

# Training split
X_pretrain = df.drop(X_encode.index)
y_train = X_pretrain.pop("SalePrice")

# 2) Применить кодирование M-оценки¶
# Примените целевую кодировку к выбранным вами категориальным функциям. Также выберите значение параметра сглаживания
# m (для правильного ответа подходит любое значение).

encoder = MEstimateEncoder(
    cols=["Neighborhood"],
    m=1.0,
)


# Fit the encoder on the encoding split
encoder.fit(X_encode, y_encode)

# Encode the training split
X_train = encoder.transform(X_pretrain, y_train)

feature = encoder.cols

plt.figure(dpi=90)
ax = sns.distplot(y_train, kde=True, hist=False)
ax = sns.distplot(X_train[feature], color='r', ax=ax, hist=True, kde=False, norm_hist=True)
ax.set_xlabel("SalePrice");

# Судя по графикам распределения, кодировка кажется информативной?
#
# И эта ячейка покажет вам оценку закодированного набора по сравнению с исходным набором:

X = df.copy()
y = X.pop("SalePrice")
score_base = score_dataset(X, y)
score_new = score_dataset(X_train, y_train)

print(f"Baseline Score: {score_base:.4f} RMSLE")
print(f"Score with Encoding: {score_new:.4f} RMSLE")

# Как вы думаете, стоило ли в данном случае целевого кодирования? В зависимости от того, какую функцию или функции
# вы  выбрали, вы могли получить результат значительно хуже, чем базовый уровень. В этом случае, вероятно,
# дополнительная  информация, полученная при кодировании, не сможет компенсировать потерю данных, используемых для
# кодирования.
#

# В этом вопросе  вы исследуете проблему переобучения целевыми кодировками. Это проиллюстрирует важность обучения
# подгонки целевых кодировщиков на данных, взятых из обучающего набора.
#
# Итак, давайте  посмотрим, что произойдет, когда мы поместим кодировщик и модель в один и тот же набор данных. Чтобы
# подчеркнуть,  насколько драматичным может быть переоснащение, мы подразумеваем кодирование функции, которая не
# должна иметь отношения к SalePrice, количество: 0, 1, 2, 3, 4, 5, ....

# Try experimenting with the smoothing parameter m
# Try 0, 1, 5, 50
m = 0

X = df.copy()
y = X.pop('SalePrice')

# Create an uninformative feature
X["Count"] = range(len(X))
X["Count"][1] = 0  # actually need one duplicate value to circumvent error-checking in MEstimateEncoder

# fit and transform on the same dataset
encoder = MEstimateEncoder(cols="Count", m=m)
X = encoder.fit_transform(X, y)

# Results
score =  score_dataset(X, y)
print(f"Score: {score:.4f} RMSLE")

plt.figure(dpi=90)
ax = sns.distplot(y, kde=True, hist=False)
ax = sns.distplot(X["Count"], color='r', ax=ax, hist=True, kde=False, norm_hist=True)
ax.set_xlabel("SalePrice");

# И распределения тоже почти такие же.
#
# 3) Переоснащение целевыми энкодерами
# Основываясь на вашем понимании того, как работает среднее кодирование, можете ли вы объяснить, как XGBoost смог
# получить почти идеальное соответствие после среднего кодирования функции подсчета?

# Поскольку Count никогда не имеет повторяющихся значений,  закодированный в среднем Count является, по сути,
# точной копией цели. Другими словами, среднее кодирование превратило совершенно бессмысленную функцию в идеальную.
#
# Единственная причина, по которой это сработало, заключается  в том, что мы обучили XGBoost на том же наборе,
# который использовали для обучения кодировщика. Если бы вместо  этого мы использовали набор удержания, ни одна из
# этих «фальшивых» кодировок не перешла бы в обучающие данные.
#
# Урок состоит в том, что при использовании целевого кодировщика очень важно использовать отдельные наборы данных для
# обучения кодировщика и обучения модели. В противном случае результаты могут быть очень неутешительными!





























