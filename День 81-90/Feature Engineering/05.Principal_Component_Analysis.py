# Setup feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.feature_engineering_new.ex5 import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.feature_selection import mutual_info_regression
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


def apply_pca(X, standardize=True):
    # Standardize
    if standardize:
        X = (X - X.mean(axis=0)) / X.std(axis=0)
    # Create principal components
    pca = PCA()
    X_pca = pca.fit_transform(X)
    # Convert to dataframe
    component_names = [f"PC{i+1}" for i in range(X_pca.shape[1])]
    X_pca = pd.DataFrame(X_pca, columns=component_names)
    # Create loadings
    loadings = pd.DataFrame(
        pca.components_.T,  # transpose the matrix of loadings
        columns=component_names,  # so the columns are the principal components
        index=X.columns,  # and the rows are the original features
    )
    return pca, X_pca, loadings


def plot_variance(pca, width=8, dpi=100):
    # Create figure
    fig, axs = plt.subplots(1, 2)
    n = pca.n_components_
    grid = np.arange(1, n + 1)
    # Explained variance
    evr = pca.explained_variance_ratio_
    axs[0].bar(grid, evr)
    axs[0].set(
        xlabel="Component", title="% Explained Variance", ylim=(0.0, 1.0)
    )
    # Cumulative Variance
    cv = np.cumsum(evr)
    axs[1].plot(np.r_[0, grid], np.r_[0, cv], "o-")
    axs[1].set(
        xlabel="Component", title="% Cumulative Variance", ylim=(0.0, 1.0)
    )
    # Set up figure
    fig.set(figwidth=8, dpi=100)
    return axs


def make_mi_scores(X, y):
    X = X.copy()
    for colname in X.select_dtypes(["object", "category"]):
        X[colname], _ = X[colname].factorize()
    # All discrete features should now have integer dtypes
    discrete_features = [pd.api.types.is_integer_dtype(t) for t in X.dtypes]
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features, random_state=0)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores


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


# Давайте выберем несколько функций, которые сильно коррелируют с нашей целью SalePrice.
features = [
    "GarageArea",
    "YearRemodAdd",
    "TotalBsmtSF",
    "GrLivArea",
]

print("Correlation with SalePrice:\n")
print(df[features].corrwith(df.SalePrice))

# Мы будем полагаться на PCA, чтобы распутать корреляционную структуру этих функций и предложить взаимосвязи,
# которые можно было бы с пользой смоделировать с помощью новых функций.
#
# Запустите эту ячейку, чтобы применить PCA и извлечь нагрузки.

X = df.copy()
y = X.pop("SalePrice")
X = X.loc[:, features]

# `apply_pca`, defined above, reproduces the code from the tutorial
pca, X_pca, loadings = apply_pca(X)
print(loadings)

# 1) Интерпретация нагрузок на компоненты
# Посмотрите на загрузку компонентов PC1 и PC3. Можете ли вы описать, какой контраст улавливает каждый компонент?
# После того, как вы обдумали это, запустите следующую ячейку для решения.

# Первый компонент,  PC1, по-видимому, является своего рода компонентом «размера», аналогичным тому, что мы видели в
# учебнике: все функции  имеют один и тот же знак (положительный), что указывает на то, что этот компонент описывает
# контраст между домами, имеющими большие размеры. ценности и дома, имеющие небольшие значения для этих характеристик.
#
# Интерпретация третьего  компонента PC3 немного сложнее. Функции GarageArea и YearRemodAdd имеют почти нулевую
# загрузку, поэтому давайте  проигнорируем их. Этот компонент в основном посвящен TotalBsmtSF и GrLivArea. Он
# описывает контраст между  домами с большой жилой площадью, но маленькими (или несуществующими) подвалами,
# и противоположностью: маленькими домами с большими подвалами.
#
# добавить Codeadd Markdown
# Ваша цель в этом вопросе - использовать результаты PCA для обнаружения одной или нескольких новых функций,
# которые улучшают  производительность вашей модели. Один из вариантов - создать элементы, вдохновленные нагрузками,
# как мы это делали  в учебнике. Другой вариант - использовать сами компоненты в качестве функций (то есть добавить
# один или несколько столбцов X_pca к X).

# 2) Создание новых функций¶
# Добавьте одну или несколько новых функций в набор данных X. Для правильного решения получите оценку валидации ниже
# 0,140 RMSLE. (Если вы застряли, воспользуйтесь подсказкой ниже!)


# Solution 1: Inspired by loadings
X = df.copy()
y = X.pop("SalePrice")

X["Feature1"] = X.GrLivArea + X.TotalBsmtSF
X["Feature2"] = X.YearRemodAdd * X.TotalBsmtSF

score = score_dataset(X, y)
print(f"Your score: {score:.5f} RMSLE")


# Solution 2: Uses components
X = df.copy()
y = X.pop("SalePrice")

X = X.join(X_pca)
score = score_dataset(X, y)
print(f"Your score: {score:.5f} RMSLE")

# В следующем вопросе исследуется способ использования PCA для обнаружения выбросов в наборе данных (то есть точек
# данных, которые в некотором роде необычно экстремальны). Выбросы могут отрицательно повлиять на производительность
# модели, поэтому хорошо знать о них, если вам потребуется предпринять корректирующие действия. PCA, в частности,
# может показать вам аномальные вариации, которые могут не быть очевидными из исходных деталей: ни маленькие дома,
# ни дома с большими подвалами не являются необычными, но для маленьких домов необычны большие подвалы. Это то,
# что вам может показать главный компонент.
#
# Запустите следующую ячейку, чтобы отобразить графики распределения для каждого из основных компонентов, которые вы
# создали выше.
sns.catplot(
    y="value",
    col="variable",
    data=X_pca.melt(),
    kind='boxen',
    sharey=False,
    col_wrap=2,
);

# Как видите, в каждой из компонент есть несколько точек, лежащих на крайних концах распределений - выбросы, то есть.
#
# Теперь запустите следующую ячейку, чтобы увидеть те дома, которые находятся на краях компонента:

# 3) Обнаружение выбросов¶
# Вы замечаете какие-то закономерности в экстремальных значениях? Кажется, выбросы происходят из какого-то особого
# подмножества данных?
#
# После того, как вы обдумали свой ответ, запустите следующую ячейку для решения и некоторого обсуждения.

# Обратите внимание, что в районе Эдвардс  есть несколько особняков, внесенных в список частичных продаж. Частичная
# продажа - это то, что происходит, когда  есть несколько владельцев собственности, и один или несколько из них
# продают свою «частичную» собственность.
#
# Эти виды продаж часто происходят во время урегулирования семейного поместья или ликвидации бизнеса и публично не
# афишируются. Если бы вы пытались спрогнозировать стоимость дома на открытом рынке, вы, вероятно,
# были бы оправданы, если бы исключили такие продажи из своего набора данных - они действительно являются выбросами.























