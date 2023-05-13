# Word Vectors
# Векторизация языка
# Встраивания концептуально умны и практически эффективны.
#
# Итак, давайте попробуем их для модели анализа настроений, которую вы построили для ресторана. Затем вы можете найти
# наиболее похожий обзор в наборе данных с помощью некоторого примера текста. Это задача, по которой вы легко можете
# сами судить, насколько хорошо работают вложения.


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import spacy

# Load the large model to get the vectors
nlp = spacy.load('en_core_web_lg')

review_data = pd.read_csv('../input/nlp-course/yelp_ratings.csv')
review_data.head()

# Loading all document vectors from file
vectors = np.load('../input/nlp-course/review_vectors.npy')

# 1) Обучение модели на векторах документа¶
# Затем вы обучите модель LinearSVC, используя векторы документа. Он работает довольно быстро и хорошо работает в настройках большого размера, как здесь.
#
# После запуска модели LinearSVC вы можете попробовать поэкспериментировать с другими типами моделей, чтобы увидеть,
# улучшит ли это ваши результаты.
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(vectors, review_data.sentiment,
                                                    test_size=0.1, random_state=1)

# Create the LinearSVC model
model = LinearSVC(random_state=1, dual=False)
# Fit the model
model = LinearSVC(random_state=1, dual=False)
model.fit(X_train, y_train)


# 2) Центрирование векторов
# Иногда люди центрируют векторы документа при вычислении сходства. То есть они вычисляют средний вектор для всех
# документов и вычитают его из вектора каждого отдельного документа. Как вы думаете, почему это может помочь с
# показателями сходства?
#
# После того, как вы определились со своим ответом, введите следующую строку.
# Иногда ваши документы уже будут довольно похожи. Например, этот набор данных - это все обзоры предприятий. Между
# документами будет много общего по сравнению с новостными статьями, техническими руководствами и рецептами. Вы
# получаете все сходства между 0.8 и 1 и отсутствие антиподобных документов (подобие <0). Когда векторы центрированы,
# вы сравниваете документы в своем наборе данных, а не все возможные документы.

# 3) Найдите наиболее похожий обзор
# В приведенном ниже примере обзора найдите наиболее похожий документ в наборе данных Yelp, используя косинусное сходство.

review = """I absolutely love this place. The 360 degree glass windows with the 
Yerba buena garden view, tea pots all around and the smell of fresh tea everywhere 
transports you to what feels like a different zen zone within the city. I know 
the price is slightly more compared to the normal American size, however the food 
is very wholesome, the tea selection is incredible and I know service can be hit 
or miss often but it was on point during our most recent visit. Definitely recommend!

I would especially recommend the butternut squash gyoza."""

def cosine_similarity(a, b):
    return np.dot(a, b)/np.sqrt(a.dot(a)*b.dot(b))

review_vec = nlp(review).vector

    ## Center the document vectors
    # Calculate the mean for the document vectors
vec_mean = vectors.mean(axis=0)
    # Subtract the mean from the vectors
centered = vectors - vec_mean

    # Calculate similarities for each document in the dataset
    # Make sure to subtract the mean from the review vector
sims = np.array([cosine_similarity(review_vec - vec_mean, vec) for vec in centered])

    # Get the index for the most similar document
most_similar = sims.argmax()

print(review_data.iloc[most_similar].text)

# 4) Просмотр похожих обзоров
# Если вы посмотрите другие похожие обзоры, вы увидите множество кафе. Как вы думаете, почему отзывы о кофе похожи на
# пример обзора, в котором упоминается только чай?






