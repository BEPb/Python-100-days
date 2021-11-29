# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.feature_engineering_new.ex4 import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

# Алгоритм k-средних чувствителен к масштабированию. Это означает, что нам нужно подумать о том, как и нужно ли
# изменять масштаб наших функций, поскольку мы можем получить очень разные результаты в зависимости от нашего
# выбора. Как показывает практика, если функции уже напрямую сопоставимы (например, результат теста в разное время),
# вам не следует изменять масштаб. С другой стороны, функции, масштабы которых не сопоставимы (например,
# рост и вес), обычно выигрывают от масштабирования. Однако иногда выбор не будет однозначным. В этом случае вам
# следует попытаться руководствоваться здравым смыслом, помня, что функции с большими значениями будут иметь больший
# вес.
#
# 1) Функции масштабирования
# Рассмотрим следующие наборы функций. Для каждого решите, нужно ли:
#
# их обязательно нужно масштабировать,
# их определенно не следует масштабировать, или
# либо может быть разумным
# Функции:
#
# Широта и долгота городов Калифорнии
# Площадь участка и жилая площадь домов в Эймсе, штат Айова
# Количество дверей и мощность автомобиля модели 1989 года
# Как только вы обдумаете свои ответы, запустите ячейку ниже для обсуждения.

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


# Prepare data
df = pd.read_csv("../input/fe-course-data/ames.csv")


# Нет, поскольку изменение масштаба исказит естественные расстояния, описываемые широтой и долготой.
# Любой выбор может быть разумным, но поскольку жилая площадь дома имеет тенденцию быть более ценной на квадратный
# фут, имеет смысл изменить масштаб этих функций, чтобы площадь участка не взвешивалась при кластеризации
# пропорционально ее влиянию на SalePrice. , если это то, что вы пытались предсказать.
# Да, поскольку у них нет сопоставимых единиц. Без изменения масштаба количество дверей в автомобиле (обычно 2 или
# 4) имело бы незначительный вес по сравнению с его мощностью (обычно исчисляемой сотнями).
# Что вы должны извлечь из этого, так это то, что решение о том, следует ли и как изменять масштаб функций,
# редко бывает автоматическим - это обычно будет зависеть от некоторых знаний о ваших данных и того,
# что вы пытаетесь предсказать. Также может быть полезно сравнение различных схем масштабирования с помощью
# перекрестной проверки. (Возможно, вы захотите проверить модуль предварительной обработки в scikit-learn,
# чтобы узнать о некоторых методах масштабирования, которые он предлагает.)



# 2) Создайте функцию меток кластера
# Создание кластеризации k-средних со следующими параметрами:
#
# особенности: LotArea, TotalBsmtSF, FirstFlrSF, SecondFlrSF, GrLivArea
# количество кластеров: 10
# итераций: 10
# (Это может занять некоторое время.)


X = df.copy()
y = X.pop("SalePrice")

features = [
    "LotArea",
    "TotalBsmtSF",
    "FirstFlrSF",
    "SecondFlrSF",
    "GrLivArea",
]

# Standardize
X_scaled = X.loc[:, features]
X_scaled = (X_scaled - X_scaled.mean(axis=0)) / X_scaled.std(axis=0)

kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)
X["Cluster"] = kmeans.fit_predict(X_scaled)


# Вы можете запустить эту ячейку, чтобы увидеть результат кластеризации, если хотите.


Xy = X.copy()
Xy["Cluster"] = Xy.Cluster.astype("category")
Xy["SalePrice"] = y
sns.relplot(
    x="value", y="SalePrice", hue="Cluster", col="variable",
    height=4, aspect=1, facet_kws={'sharex': False}, col_wrap=3,
    data=Xy.melt(
        value_vars=features, id_vars=["SalePrice", "Cluster"],
    ),
)

# И, как и раньше, score_dataset будет оценивать вашу модель XGBoost с помощью этой новой функции, добавленной к
# обучающим данным.

score_dataset(X, y)

# Алгоритм k-средних предлагает альтернативный способ создания функций. Вместо того, чтобы маркировать каждый объект
# ближайшим центроидом кластера, он может измерять расстояние от точки до всех центроидов и возвращать эти
# расстояния как объекты.



# 3) Кластерные особенности
# Теперь добавьте объекты с кластерным расстоянием в свой набор данных. Вы можете получить эти функции расстояния,
# используя метод fit_transform для kmeans вместо fit_predict.

kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)

# YOUR CODE HERE: Create the cluster-distance features using `fit_transform`
X_cd = kmeans.fit_transform(X_scaled)

# Label features and join to dataset
X_cd = pd.DataFrame(X_cd, columns=[f"Centroid_{i}" for i in range(X_cd.shape[1])])
X = X.join(X_cd)

score_dataset(X, y)