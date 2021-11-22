import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X = pd.read_csv('train.csv', index_col='Id')
X_test_full = pd.read_csv('test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

# Break off validation set from training data
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                random_state=0)

# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and
                        X_train_full[cname].dtype == "object"]

# Select numeric columns
numeric_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = low_cardinality_cols + numeric_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()
X_test = X_test_full[my_cols].copy()

# One-hot encode the data (to shorten the code, we use pandas)
X_train = pd.get_dummies(X_train)
X_valid = pd.get_dummies(X_valid)
X_test = pd.get_dummies(X_test)
X_train, X_valid = X_train.align(X_valid, join='left', axis=1)
X_train, X_test = X_train.align(X_test, join='left', axis=1)

# Шаг 1. Постройте модель
# Часть А
# На этом этапе вы создадите и обучите свою первую модель с усилением градиента.
#
# Начните с установки my_model_1 на модель XGBoost. Используйте класс XGBRegressor и установите для случайного начального числа значение 0 (random_state = 0). Оставьте все остальные параметры по умолчанию.
# Затем подгоните модель к обучающим данным в X_train и y_train.

from xgboost import XGBRegressor
# Define the model
my_model_1 = XGBRegressor(random_state=0)

# Fit the model
my_model_1.fit(X_train, y_train)

# Часть B¶
# Установите predictions_1 на прогнозы модели для данных проверки. Напомним, что функции проверки хранятся в X_valid.
from sklearn.metrics import mean_absolute_error

# Get predictions
predictions_1 = my_model_1.predict(X_valid)

# Часть C
# Наконец, используйте функцию mean_absolute_error () для вычисления средней абсолютной ошибки (MAE), соответствующей
# прогнозам для набора проверки. Напомним, что метки для данных проверки хранятся в y_valid.

# Calculate MAE
mae_1 = mean_absolute_error(predictions_1, y_valid)
print("Mean Absolute Error:" , mae_1)

# Uncomment to print MAE
# print("Mean Absolute Error:" , mae_1)
# Mean Absolute Error: 17662.736729452055

# Шаг 2: Улучшите модель¶
# Теперь, когда вы обучили модель по умолчанию в качестве базовой, пришло время поработать с параметрами, чтобы посмотреть, сможете ли вы повысить производительность!
#
# Начните с установки my_model_2 модели XGBoost, используя класс XGBRegressor. Используйте то, что вы узнали в предыдущем руководстве, чтобы выяснить, как изменить параметры по умолчанию (например, n_estimators и learning_rate) для получения лучших результатов.
# Затем подгоните модель к обучающим данным в X_train и y_train.
# Установите predictions_2 на прогнозы модели для данных проверки. Напомним, что функции проверки хранятся в X_valid.
# Наконец, используйте функцию mean_absolute_error () для вычисления средней абсолютной ошибки (MAE), соответствующей предсказаниям на наборе проверки. Напомним, что метки для данных проверки хранятся в y_valid.
# Чтобы этот шаг был отмечен как правильный, ваша модель в my_model_2 должна иметь более низкую MAE, чем модель в
# my_model_1.

# Define the model
my_model_2 = XGBRegressor(n_estimators=1000, learning_rate=0.05)

# Fit the model
my_model_2.fit(X_train, y_train)

# Get predictions
predictions_2 = my_model_2.predict(X_valid)

# Calculate MAE
mae_2 = mean_absolute_error(predictions_2, y_valid)
print("Mean Absolute Error:" , mae_2)

# Шаг 3: сломайте модель
# На этом шаге вы создадите модель, которая работает хуже, чем исходная модель на шаге 1. Это поможет вам развить интуицию в отношении того, как устанавливать параметры. Вы даже можете обнаружить, что случайно повысили производительность, что в конечном итоге является хорошей проблемой и ценным опытом обучения!
#
# Начните с установки my_model_3 модели XGBoost, используя класс XGBRegressor. Используйте то, что вы узнали в предыдущем руководстве, чтобы выяснить, как изменить параметры по умолчанию (например, n_estimators и learning_rate), чтобы спроектировать модель для получения высокой MAE.
# Затем подгоните модель к обучающим данным в X_train и y_train.
# Установите predictions_3 на прогнозы модели для данных проверки. Напомним, что функции проверки хранятся в X_valid.
# Наконец, используйте функцию mean_absolute_error () для вычисления средней абсолютной ошибки (MAE), соответствующей предсказаниям на наборе проверки. Напомним, что метки для данных проверки хранятся в y_valid.
# Чтобы этот шаг был отмечен как правильный, ваша модель в my_model_3 должна иметь более высокий MAE, чем модель в
# my_model_1.

# Define the model
my_model_3 = XGBRegressor(n_estimators=1)

# Fit the model
my_model_3.fit(X_train, y_train)

# Get predictions
predictions_3 = my_model_3.predict(X_valid)

# Calculate MAE
mae_3 = mean_absolute_error(predictions_3, y_valid)
print("Mean Absolute Error:" , mae_3)
















