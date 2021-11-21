import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('train.csv', index_col='Id')
X_test_full = pd.read_csv('test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)

print(X_train.head())
# Shape of training data (num_rows, num_columns)
print(X_train.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])


# Часть А
# Используйте вышеприведенный вывод, чтобы ответить на вопросы ниже.

# Fill in the line below: How many rows are in the training data?
num_rows = 1168

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = 3

# Fill in the line below: How many missing entries are contained in
# all of the training data?
tot_missing = 276

# Часть B
# Учитывая ваши ответы выше, какой, по вашему мнению, лучший подход к работе с недостающими значениями?
#Поскольку в данных относительно мало пропущенных записей (в столбце с наибольшим процентом пропущенных значений
# отсутствует менее 20% записей), можно ожидать, что удаление столбцов вряд ли  даст хорошие результаты. Это связано
# с тем, что мы потеряем много ценных данных, и поэтому вменение, вероятно, будет работать лучше.


# Чтобы сравнить различные подходы к работе с отсутствующими значениями, вы воспользуетесь той же функцией
# score_dataset () из учебника. Эта функция сообщает о средней абсолютной ошибке (MAE) для модели случайного леса.
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Шаг 2. Удалите столбцы с пропущенными значениями
# На этом этапе вы предварительно обработаете данные в X_train и X_valid, чтобы удалить столбцы с пропущенными
# значениями. Установите для предварительно обработанных DataFrames значения Red_X_train и Red_X_valid соответственно.
# Get names of columns with missing values
cols_with_missing = [col for col in X_train.columns
                     if X_train[col].isnull().any()]

# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

print("MAE (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

# Шаг 3: вменение
from sklearn.impute import SimpleImputer

# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

print("MAE (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))

# Часть B
# Сравните MAE для каждого подхода. Вас что-нибудь удивляет в результатах? Как вы думаете, почему один подход работает лучше, чем другой?
#
# Верный:
#
# Учитывая, что в наборе данных так мало пропущенных значений, мы ожидаем, что вменение будет работать лучше,
# чем полное удаление  столбцов. Однако мы видим, что удаление столбцов выполняется немного лучше! Хотя это,
# вероятно, частично  может быть связано с шумом в наборе данных, другое возможное объяснение заключается в том,
# что метод вменения не  очень подходит для этого набора данных. То есть, возможно, вместо заполнения среднего
# значения имеет смысл  установить каждое отсутствующее значение на значение 0, заполнить наиболее часто
# встречающееся значение  или использовать какой-либо другой метод. Например, рассмотрим столбец GarageYrBlt (который
# указывает год постройки  гаража). Вполне вероятно, что в некоторых случаях отсутствующее значение может указывать
# на дом, в котором нет  гаража. Имеет ли смысл указывать среднее значение в каждом столбце в этом случае? Или мы
# могли бы получить лучшие  результаты, заполнив минимальное значение в каждом столбце? Не совсем понятно,
# что лучше в этом случае,  но, возможно, мы можем сразу исключить некоторые варианты - например, установка
# отсутствующих значений в этом столбце на 0, вероятно, приведет к ужасным результатам!


# Шаг 4. Сгенерируйте тестовые прогнозы
# На этом последнем шаге вы воспользуетесь любым подходом по вашему выбору для работы с недостающими значениями. После предварительной обработки функций обучения и проверки вы обучите и оцените модель случайного леса. Затем вы предварительно обработаете тестовые данные, прежде чем сгенерировать прогнозы, которые можно будет отправить на конкурс!
#
# Часть А
# Используйте следующую ячейку кода для предварительной обработки данных обучения и проверки. Установите для предварительно обработанных DataFrames значения final_X_train и final_X_valid. Здесь вы можете использовать любой подход по вашему выбору! Для того, чтобы этот шаг был отмечен как правильный, вам нужно только убедиться:
#
# предварительно обработанные DataFrames имеют одинаковое количество столбцов,
# предварительно обработанные DataFrames не имеют пропущенных значений,
# final_X_train и y_train имеют одинаковое количество строк, и
# final_X_valid и y_valid имеют одинаковое количество строк.

# Imputation
final_imputer = SimpleImputer(strategy='median')
final_X_train = pd.DataFrame(final_imputer.fit_transform(X_train))
final_X_valid = pd.DataFrame(final_imputer.transform(X_valid))

# Imputation removed column names; put them back
final_X_train.columns = X_train.columns
final_X_valid.columns = X_valid.columns

# Define and fit model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)

# Get validation predictions and MAE
preds_valid = model.predict(final_X_valid)
print("MAE (Your approach):")
print(mean_absolute_error(y_valid, preds_valid))

# Часть B
# Используйте следующую ячейку кода для предварительной обработки ваших тестовых данных. Убедитесь, что вы используете метод, соответствующий тому, как вы предварительно обработали данные обучения и проверки, и установите для предварительно обработанных тестовых функций значение final_X_test.
#
# Затем используйте предварительно обработанные тестовые функции и обученную модель, чтобы сгенерировать тестовые прогнозы в preds_test.
#
# Чтобы этот шаг был отмечен как правильный, вам нужно только убедиться:
#
# предварительно обработанный тестовый DataFrame не имеет пропущенных значений, и
# final_X_test имеет то же количество строк, что и X_test.

# Preprocess test data
final_X_test = pd.DataFrame(final_imputer.transform(X_test))

# Get test predictions
preds_test = model.predict(final_X_test)

# Save test predictions to file
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': preds_test})
output.to_csv('submission.csv', index=False)






