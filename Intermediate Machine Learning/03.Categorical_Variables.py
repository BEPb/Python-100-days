# Set up code checking
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X = pd.read_csv('train.csv', index_col='Id')
X_test = pd.read_csv('test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll drop columns with missing values
cols_with_missing = [col for col in X.columns if X[col].isnull().any()]
X.drop(cols_with_missing, axis=1, inplace=True)
X_test.drop(cols_with_missing, axis=1, inplace=True)

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

print(X_train.head())


# Обратите внимание, что набор данных содержит как числовые,  так и категориальные переменные. Перед обучением модели
# вам необходимо закодировать категориальные данные.
# Для сравнения разных моделей вы будете использовать  ту же функцию score_dataset () из учебника. Эта функция
# сообщает среднюю абсолютную ошибку (MAE) для модели случайного леса.
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Шаг 1. Удалите столбцы с категориальными данными
# Вы начнете с самого  простого подхода. Используйте ячейку кода ниже для предварительной обработки данных в X_train
# и X_valid для удаления  столбцов с категориальными данными. Установите для предварительно обработанных DataFrames
# значения drop_X_train и drop_X_valid соответственно.
# Fill in the lines below: drop columns in training and validation data
# Drop columns in training and validation data
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

print("MAE from Approach 1 (Drop categorical variables):")
print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))
# MAE from Approach 1 (Drop categorical variables):
# 17837.82570776256

# Прежде чем перейти к порядковому кодированию, мы исследуем набор данных. В частности,  мы рассмотрим столбец
# «Condition2». В ячейке кода ниже печатаются уникальные записи как в обучающем, так и в проверочном наборах.

print("Unique values in 'Condition2' column in training data:", X_train['Condition2'].unique())
print("\nUnique values in 'Condition2' column in validation data:", X_valid['Condition2'].unique())

# Unique values in 'Condition2' column in training data: ['Norm' 'PosA' 'Feedr' 'PosN' 'Artery' 'RRAe']
#
# Unique values in 'Condition2' column in validation data: ['Norm' 'RRAn' 'RRNn' 'Artery' 'Feedr' 'PosN']

# Шаг 2: Порядковое кодирование
# Часть А
# Если вы сейчас напишете код на:
#
# подгоните порядковый кодировщик к обучающим данным, а затем
# использовать его для преобразования данных обучения и проверки,
# вы получите сообщение об ошибке. Вы понимаете, почему это так?  (Чтобы ответить на этот вопрос, вам нужно будет
# использовать приведенный выше вывод.)
# Подгонка порядкового кодировщика к столбцу в обучающих данных создает соответствующую целочисленную метку для
# каждого уникального значения, которое  появляется в обучающих данных. В случае, если данные проверки содержат
# значения, которые также не отображаются  в данных обучения, кодировщик выдаст ошибку, поскольку этим значениям не
# будет присвоено целое число. Обратите  внимание, что столбец «Condition2» в данных проверки содержит значения
# «RRAn» и «RRNn», но они не отображаются  в данных обучения - таким образом, если мы попытаемся использовать
# порядковый кодировщик с scikit-learn, код выдаст ошибку.

# Это распространенная проблема, с которой вы  столкнетесь с реальными данными, и есть много подходов к ее
# устранению. Например, вы можете написать  собственный порядковый кодировщик для работы с новыми категориями. Однако
# самый простой подход - отбросить проблемные категориальные столбцы.
#
# Запустите ячейку кода ниже, чтобы сохранить проблемные столбцы в списке Python bad_label_cols. Точно так же
# столбцы, которые можно безопасно закодировать по порядковому номеру, хранятся в good_label_cols.

# Categorical columns in the training data
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely ordinal encoded
good_label_cols = [col for col in object_cols if
                   set(X_valid[col]).issubset(set(X_train[col]))]

# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols) - set(good_label_cols))

print('Categorical columns that will be ordinal encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)

# Часть B
# Используйте следующую ячейку кода для порядкового  кодирования данных в X_train и X_valid. Установите для
# предварительно обработанных DataFrames значений label_X_train и label_X_valid соответственно.
#
# Мы предоставили код ниже, чтобы удалить категориальные столбцы в bad_label_cols из набора данных.
# Вы должны по порядку кодировать категориальные столбцы в good_label_cols.
from sklearn.preprocessing import OrdinalEncoder

# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)

# Apply ordinal encoder
ordinal_encoder = OrdinalEncoder()
label_X_train[good_label_cols] = ordinal_encoder.fit_transform(X_train[good_label_cols])
label_X_valid[good_label_cols] = ordinal_encoder.transform(X_valid[good_label_cols])

print("MAE from Approach 2 (Ordinal Encoding):")
print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))
# MAE from Approach 2 (Ordinal Encoding):
# 17098.01649543379

# До сих пор вы пробовали два разных подхода к работе с категориальными  переменными. И вы видели, что кодирование
# категориальных данных дает лучшие результаты, чем удаление столбцов из набора данных.
#
# Вскоре вы попробуете одноразовое кодирование.  А до этого нам нужно затронуть еще одну тему. Начните с запуска
# следующей ячейки кода без изменений.
# Get number of unique entries in each column with categorical data
object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))

# Print number of unique entries by column, in ascending order
sorted(d.items(), key=lambda x: x[1])

# Шаг 3: исследование количества элементов
# Часть А
# Приведенный выше вывод показывает для каждого столбца с категориальными данными количество уникальных значений в столбце. Например, столбец «Улица» в данных обучения имеет два уникальных значения: «Grvl» и «Pave», соответствующие гравийной дороге и асфальтированной дороге соответственно.
#
# Мы называем количество уникальных записей категориальной переменной мощностью этой категориальной переменной. Например, переменная Street имеет мощность 2.
#
# Используйте вывод выше, чтобы ответить на вопросы ниже.
# How many categorical variables in the training data
# have cardinality greater than 10?
high_cardinality_numcols = 3

# How many columns are needed to one-hot encode the
# 'Neighborhood' variable in the training data?
num_cols_neighborhood = 25
# Часть B
# Для больших наборов данных с большим количеством строк однократное кодирование может значительно увеличить размер набора данных. По этой причине мы обычно используем только одноразовое кодирование столбцов с относительно низкой мощностью. Затем столбцы с высокой мощностью можно либо исключить из набора данных, либо использовать порядковое кодирование.
#
# В качестве примера рассмотрим набор данных из 10 000 строк, содержащий один категориальный столбец со 100 уникальными записями.
#
# Если этот столбец заменяется соответствующей горячей кодировкой, сколько записей добавляется в набор данных?
# Если вместо этого мы заменим столбец порядковой кодировкой, сколько записей будет добавлено?
# Используйте свои ответы, чтобы заполнить строки ниже
# How many entries are added to the dataset by
# replacing the column with a one-hot encoding?
OH_entries_added = 1e4*100 - 1e4

# How many entries are added to the dataset by
# replacing the column with an ordinal encoding?
label_entries_added = 0

# Чтобы вычислить, сколько записей добавляется в набор данных посредством однократного кодирования, начните с
# вычисления, сколько записей необходимо для кодирования категориальной переменной (путем умножения количества строк на количество столбцов при однократном кодировании) . Затем, чтобы узнать, сколько записей добавлено в набор данных, вычтите количество записей в исходном столбце.

# Далее вы поэкспериментируете с горячим кодированием. Но вместо кодирования всех категориальных переменных в наборе данных вы создадите однократное кодирование только для столбцов с количеством элементов меньше 10.
#
# Запустите приведенную ниже ячейку кода без изменений, чтобы установить low_cardinality_cols в список Python,
# содержащий столбцы, которые будут закодированы в горячем режиме. Аналогичным образом high_cardinality_cols содержит список категориальных столбцов, которые будут удалены из набора данных.

# Columns that will be one-hot encoded
low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]

# Columns that will be dropped from the dataset
high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)

# Шаг 4: быстрое кодирование
# Используйте следующую ячейку кода для быстрого кодирования данных в X_train и X_valid. Установите для предварительно обработанных DataFrames значений OH_X_train и OH_X_valid соответственно.
#
# Полный список категориальных столбцов в наборе данных можно найти в списке Python object_cols.
# Вам следует только горячо кодировать категориальные столбцы в low_cardinality_cols. Все остальные категориальные
# столбцы следует исключить из набора данных.

# Apply one-hot encoder to each column with categorical data
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

# Remove categorical columns (will replace with one-hot encoding)
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

print("MAE from Approach 3 (One-Hot Encoding):")
print(score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))

# MAE from Approach 3 (One-Hot Encoding):
# 17525.345719178084























































