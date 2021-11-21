import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('train.csv', index_col='Id')
X_test_full = pd.read_csv('test.csv', index_col='Id')

# Obtain target and predictors
y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = X_full[features].copy()
X_test = X_test_full[features].copy()

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

print(X_train.head())
# Следующая ячейка кода определяет пять различных моделей случайного леса. Запустите эту ячейку кода без изменений.
from sklearn.ensemble import RandomForestRegressor

# Define the models
model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

models = [model_1, model_2, model_3, model_4, model_5]

# Чтобы выбрать лучшую модель из пяти, мы определяем функцию score_model () ниже. Эта функция возвращает среднюю
# абсолютную ошибку (MAE) из набора проверки. Напомним, что лучшая модель получит самую низкую MAE.  (Чтобы
# просмотреть среднюю абсолютную ошибку, посмотрите здесь.)

from sklearn.metrics import mean_absolute_error

# Function for comparing different models
def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)

for i in range(0, len(models)):
    mae = score_model(models[i])
    print("Model %d MAE: %d" % (i+1, mae))

# Шаг 1. Оцените несколько моделей¶
# Используйте результаты выше, чтобы заполнить строку ниже. Какая модель лучшая? Ваш ответ должен быть одним из
# model_1, model_2, model_3, model_4 или model_5.
# Fill in the best model
best_model = model_3

# Шаг 2. Сгенерируйте тестовые прогнозы¶
# Большой. Вы знаете, как оценить, что делает модель точной. Пришло время пройти процесс моделирования и сделать
# прогнозы. В строке ниже создайте модель случайного леса с именем переменной my_model.
# Define a model
my_model = best_model  # Your code here

# Запустить следующую ячейку кода без изменений. Код подбирает модель к данным обучения и проверки, а затем генерирует
# тестовые прогнозы, которые сохраняются в файле CSV. Эти тестовые прогнозы можно отправлять прямо на конкурс!
