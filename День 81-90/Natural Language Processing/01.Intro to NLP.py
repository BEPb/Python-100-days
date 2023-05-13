import pandas as pd

# Владелец бизнеса предложил вам использовать отзывы о закусочных с веб-сайта Yelp, чтобы определить, какие блюда
# нравятся или не нравятся людям. Вы вытащили данные из Yelp. Прежде чем приступить к анализу, запустите ячейку кода
# ниже, чтобы быстро просмотреть данные, с которыми вам нужно работать.

# Load in the data from JSON file
data = pd.read_json('../input/nlp-course/restaurant.json')
data.head()

menu = ["Cheese Steak", "Cheesesteak", "Steak and Cheese", "Italian Combo", "Tiramisu", "Cannoli",
        "Chicken Salad", "Chicken Spinach Salad", "Meatball", "Pizza", "Pizzas", "Spaghetti",
        "Bruchetta", "Eggplant", "Italian Beef", "Purista", "Pasta", "Calzones",  "Calzone",
        "Italian Sausage", "Chicken Cutlet", "Chicken Parm", "Chicken Parmesan", "Gnocchi",
        "Chicken Pesto", "Turkey Sandwich", "Turkey Breast", "Ziti", "Portobello", "Reuben",
        "Mozzarella Caprese",  "Corned Beef", "Garlic Bread", "Pastrami", "Roast Beef",
        "Tuna Salad", "Lasagna", "Artichoke Salad", "Fettuccini Alfredo", "Chicken Parmigiana",
        "Grilled Veggie", "Grilled Veggies", "Grilled Vegetable", "Mac and Cheese", "Macaroni",
         "Prosciutto", "Salami"]

# Шаг 1: спланируйте анализ
# Учитывая данные из Yelp и список пунктов меню, есть ли у вас идеи, как найти, какие пункты меню разочаровали посетителей?
# Вы можете сгруппировать отзывы по элементам меню, в которых они упоминаются, а затем рассчитать средний рейтинг для
# отзывов, в которых упоминается каждый элемент. Вы можете сказать, какие продукты упоминаются в обзорах с низкими
# оценками, чтобы ресторан мог исправить рецепт или удалить эти продукты из меню.

# Шаг 2. Найдите элементы в одном обзоре
# Вы будете следовать этому плану расчета средних баллов по отзывам, в которых упоминается каждый пункт меню.
# В качестве первого шага вы напишете код для извлечения продуктов, упомянутых в одном обзоре.
# Поскольку элементы меню состоят из нескольких токенов, вы будете использовать PhraseMatcher, который может сопоставлять серии токенов.
# Введите значения ____ ниже, чтобы получить список элементов, соответствующих одному пункту меню.
import spacy
from spacy.matcher import PhraseMatcher

index_of_review_to_test_on = 14
text_to_test_on = data.text.iloc[index_of_review_to_test_on]

nlp = spacy.blank('en')
review_doc = nlp(text_to_test_on)

matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
menu_tokens_list = [nlp(item) for item in menu]
matcher.add("MENU", menu_tokens_list)
matches = matcher(review_doc)

for match in matches:
   print(f"Token number {match[1]}: {review_doc[match[1]:match[2]]}")

# Шаг 3. Сопоставление по всему набору данных
# Теперь запустите этот сопоставитель по всему набору данных и соберите рейтинги для каждого пункта меню. У каждого
# обзора есть рейтинг, review.stars. Для каждого элемента, который появляется в тексте обзора (review.text),
# добавьте рейтинг обзора в список оценок для этого элемента. Списки хранятся в словаре item_ratings.
#
# Чтобы получить совпадающие фразы, вы можете обратиться к документации PhraseMatcher для получения информации о
# структуре каждого объекта соответствия:
#
# Список кортежей (match_id, start, end), описывающих совпадения. Кортеж соответствия описывает документ диапазона [
# начало: конец]. Match_id - это идентификатор добавленного шаблона соответствия.
from collections import defaultdict

item_ratings = defaultdict(list)

for idx, review in data.iterrows():
    doc = nlp(review.text)
    matches = matcher(doc)

    found_items = set([doc[match[1]:match[2]].text.lower() for match in matches])

    for item in found_items:
        item_ratings[item].append(review.stars)

# Шаг 4. Какой товар получил наибольшее количество отзывов?
# Используя эти рейтинги пунктов, найдите пункт меню с худшим средним рейтингом.
# There are many ways to do this. Here is one.
mean_ratings = {item: sum(ratings)/len(ratings) for item, ratings in item_ratings.items()}
worst_item = sorted(mean_ratings, key=mean_ratings.get)[0]

print(worst_item)
print(mean_ratings[worst_item])

# Шаг 5: Важен ли здесь счет?
# Подобно среднему рейтингу, вы можете рассчитать количество отзывов для каждого элемента.
counts = {item: len(ratings) for item, ratings in item_ratings.items()}

item_counts = sorted(counts, key=counts.get, reverse=True)
for item in item_counts:
    print(f"{item:>25}{counts[item]:>5}")

sorted_ratings = sorted(mean_ratings, key=mean_ratings.get)

print("Worst rated menu items:")
for item in sorted_ratings[:10]:
    print(f"{item:20} Ave rating: {mean_ratings[item]:.2f} \tcount: {counts[item]}")

print("\n\nBest rated menu items:")
for item in sorted_ratings[-10:]:
    print(f"{item:20} Ave rating: {mean_ratings[item]:.2f} \tcount: {counts[item]}")

# Чем меньше данных у вас есть по какому-либо конкретному товару, тем меньше вы можете доверять тому, что средний
# рейтинг является «реальным» настроением клиентов. Это довольно здравый смысл. Если больше людей скажут вам одно и
# то же, вы с большей вероятностью поверите. Это также математически разумно. По мере увеличения количества точек
# данных ошибка среднего уменьшается как 1 / sqrt (n).






