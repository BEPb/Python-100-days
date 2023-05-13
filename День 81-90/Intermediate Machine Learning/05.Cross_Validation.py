import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
train_data = pd.read_csv('train.csv', index_col='Id')
test_data = pd.read_csv('test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
train_data.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = train_data.SalePrice
train_data.drop(['SalePrice'], axis=1, inplace=True)

# Select numeric columns only
numeric_cols = [cname for cname in train_data.columns if train_data[cname].dtype in ['int64', 'float64']]
X = train_data[numeric_cols].copy()
X_test = test_data[numeric_cols].copy()

print(X.head())

# Итак, вы узнали, как создавать конвейеры с помощью scikit-learn. Например, приведенный ниже конвейер будет
# использовать SimpleImputer () для замены отсутствующих значений в данных перед использованием RandomForestRegressor () для обучения модели случайного леса делать прогнозы. Мы устанавливаем количество деревьев в модели случайного леса с помощью параметра n_estimators, а установка random_state обеспечивает воспроизводимость.
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[
    ('preprocessor', SimpleImputer()),
    ('model', RandomForestRegressor(n_estimators=50, random_state=0))
])
# Вы также узнали, как использовать конвейеры для перекрестной проверки. В приведенном ниже коде используется функция
# cross_val_score () для получения средней абсолютной ошибки (MAE), усредненной по пяти различным кратным значениям. Напомним, мы устанавливаем количество складок с помощью параметра cv.

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("Average MAE score:", scores.mean())
# Average MAE score: 18276.410356164386

# Шаг 1. Напишите полезную функцию
# В этом упражнении вы будете использовать перекрестную проверку для выбора параметров модели машинного обучения.
#
# Начните с написания функции get_score (), которая сообщает средний (по трем периодам перекрестной проверки) MAE конвейера машинного обучения, который использует:
#
# данные в X и Y для создания складок,
# SimpleImputer () (со всеми параметрами, оставленными по умолчанию) для замены отсутствующих значений и
# RandomForestRegressor () (со random_state = 0) для соответствия модели случайного леса.
# Параметр n_estimators, передаваемый в get_score (), используется при установке количества деревьев в модели
# случайного леса.

def get_score(n_estimators):
    my_pipeline = Pipeline(steps=[
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(n_estimators, random_state=0))
    ])
    scores = -1 * cross_val_score(my_pipeline, X, y,
                                  cv=3,
                                  scoring='neg_mean_absolute_error')
    return scores.mean()

# Шаг 2. Проверьте разные значения параметров.
# Теперь вы будете использовать функцию, которую вы определили на шаге 1, чтобы оценить производительность модели, соответствующую восьми различным значениям количества деревьев в случайном лесу: 50, 100, 150, ..., 300, 350, 400.
#
# Сохраните свои результаты в словаре Python results, где results [i] - это средний MAE, возвращаемый get_score (i).

results = {}
for i in range(1,9):
    results[50*i] = get_score(50*i) # Your code here

# Используйте следующую ячейку для визуализации результатов, полученных на шаге 2. Запустите код без изменений.
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(list(results.keys()), list(results.values()))
plt.show()

# Шаг 3. Найдите наилучшее значение параметра
# Учитывая результаты, какое значение n_estimators кажется лучшим для модели случайного леса? Используйте свой ответ,
# чтобы установить значение n_estimators_best.

n_estimators_best = min(results, key=results.get)

# В этом упражнении вы изучили один метод выбора подходящих параметров в модели машинного обучения.
#
# Если вы хотите узнать больше об оптимизации гиперпараметров, вам рекомендуется начать с поиска по сетке, который представляет собой простой метод определения наилучшей комбинации параметров для модели машинного обучения. К счастью, scikit-learn также содержит встроенную функцию GridSearchCV (), которая может сделать ваш код поиска по сетке очень эффективным!
#
# Продолжать идти
# Продолжайте узнавать о повышении градиента, мощном методе, позволяющем достичь самых современных результатов на
# различных наборах данных.







































