# Setup feedback system
# from learntools.core import binder
# binder.bind(globals())
# from learntools.feature_engineering_new.ex2 import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression

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


# Load data
df = pd.read_csv("../input/fe-course-data/ames.csv")


# Utility functions from Tutorial
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


def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")


features = ["YearBuilt", "MoSold", "ScreenPorch"]
sns.relplot(
    x="value", y="SalePrice", col="variable", data=df.melt(id_vars="SalePrice", value_vars=features), facet_kws=dict(sharex=False),
);

# 1) Поймите взаимную информацию¶
# Основываясь на графиках, какая функция, по вашему мнению, будет иметь наибольшую взаимную информацию с SalePrice?

# Основываясь на графиках, YearBuilt должен иметь наивысший балл MI, поскольку знание года имеет тенденцию
# ограничивать SalePrice меньшим диапазоном возможных значений. Однако, как правило, это не относится к MoSold.
# Наконец, поскольку ScreenPorch обычно имеет только одно значение, 0, в среднем он мало что скажет вам о SalePrice (
# хотя и больше, чем MoSold).


# Набор данных Эймса содержит семьдесят восемь функций - много, с чем нужно работать одновременно! К счастью,
# вы можете определить функции с наибольшим потенциалом.
#
# Используйте функцию make_mi_scores (представленную в руководстве) для вычисления оценок взаимной информации для
# функций Эймса:

X = df.copy()
y = X.pop('SalePrice')

mi_scores = make_mi_scores(X, y)

# Теперь проверьте оценки, используя функции в этой ячейке. Особенно обратите внимание на верхние и нижние ряды.

print(mi_scores.head(20))
# print(mi_scores.tail(20))  # uncomment to see bottom 20

plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores.head(20))
# plot_mi_scores(mi_scores.tail(20))  # uncomment to see bottom 20

# 2) Изучите показатели MI¶
# Оценки кажутся разумными? Отражают ли характеристики с высокими показателями то, что, по вашему мнению, будет ценно
# для большинства людей в доме? Вы замечаете какие-то темы в том, что они описывают?

# Вот некоторые общие темы среди большинства этих функций:
#
# Расположение: Окрестности
# Размер: все функции Area и SF, включая FullBath и GarageCars.
# Качество: все функции Qual
# Год: YearBuilt и YearRemodAdd
# Типы: описание функций и стилей, таких как Foundation и GarageType.
# Это все виды функций, которые вы обычно видите в объявлениях о недвижимости (например, на Zillow). Хорошо,
# что наша метрика взаимной информации высоко оценила их. С другой стороны, функции с самым низким рейтингом,
# по-видимому, в основном представляют вещи, которые в некотором роде редки или исключительны, и поэтому не будут
# иметь отношения к среднему покупателю дома.


# На этом этапе вы исследуете  возможные эффекты взаимодействия для функции BldgType. Эта функция описывает общую
# структуру жилища по пяти категориям:
#
# Тип дома (номинал): Тип жилья
#
#    1Fam На одну семью Отдельно стоящий
#    2FmCon Конверсия на две семьи; изначально построенный как односемейный дом
#    Дуплекс Дуплекс
#    TwnhsE Концевой блок таунхауса
#    Таунхаус TwnhsI, внутренний блок

# Функция BldgType не получила очень высокий балл MI. График подтверждает, что категории в BldgType плохо справляются
# с различением значений в SalePrice (другими словами, распределения выглядят довольно похоже):


sns.catplot(x="BldgType", y="SalePrice", data=df, kind="boxen");

# Тем не менее, тип жилья кажется важной информацией. Выясните, оказывает ли BldgType значительное взаимодействие с
# одним из следующих элементов:
#
# GrLivArea # Надземная жилая площадь
# MoSold # Месяц продано
# Выполните следующую ячейку дважды, в первый раз с feature = "GrLivArea", а в следующий раз с feature = "MoSold":

# YOUR CODE HERE:
feature = "MoSold"

sns.lmplot(
    x=feature, y="SalePrice", hue="BldgType", col="BldgType",
    data=df, scatter_kws={"edgecolor": 'w'}, col_wrap=3, height=4,
)

# Значительное различие линий тренда от одной категории к другой указывает на эффект взаимодействия.
#

# 3) Откройте для себя взаимодействия
# Судя по графикам, похоже, что BldgType проявляет эффект взаимодействия с GrLivArea или MoSold
# Линии трендов в каждой категории BldgType явно сильно различаются, что указывает на взаимодействие между этими
# функциями. Поскольку знание BldgType говорит нам больше о том, как GrLivArea относится к SalePrice,
# мы должны рассмотреть возможность включения BldgType в наш набор функций.
#
# Однако линии тренда для MoSold почти все те же. Эта функция не стала более информативной для знания BldgType.


# Первый набор функций разработки
# Давайте возьмем момент, чтобы составить список функций, на которых мы могли бы сосредоточиться. В упражнении Урока
# 3 вы начнете создавать более информативный набор функций за счет комбинаций исходных функций, которые вы
# определили как имеющие высокий потенциал.
#
# Вы обнаружили, что десятью функциями с наивысшими показателями MI были:

# Вы узнаете здесь темы? Расположение, размер и качество. Вам не нужно ограничивать разработку только этими главными
# функциями, но теперь у вас есть хорошее место для начала. Комбинирование этих основных функций с другими
# связанными функциями, особенно с теми, которые вы определили как создание взаимодействий, является хорошей
# стратегией для создания очень информативного набора функций для обучения вашей модели.

































