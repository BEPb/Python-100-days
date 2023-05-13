"""
Python 3.9 программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла 02.update the Q-Values.py
Здесь мы научим нашу машину доходить до финиша

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-19

Добро пожаловать во вторую часть серии руководств по обучению с подкреплением, особенно с Q-Learning. Мы создали
нашу Q-таблицу, которая содержит все наши возможные дискретные состояния. Затем нам нужен способ обновить
Q-значения (значение для возможного действия для каждого уникального состояния), что привело нас к:

new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

Это DISCOUNT показатель того, насколько мы хотим заботиться о БУДУЩЕМ вознаграждении, а не о немедленном
вознаграждении. Как правило, это значение будет довольно высоким и находится в диапазоне от 0 до 1. Мы хотим,
чтобы оно было высоким, потому что цель Q Learning действительно состоит в том, чтобы изучить цепочку событий,
которая заканчивается положительным результатом, поэтому вполне естественно, что мы придаем большее значение в
долгосрочной перспективе, а не в краткосрочной.

max_future_q Хватают после того как мы проводили наши действия уже, а затем мы обновляем наши предыдущие значения,
основанные частично на лучшем значении Q следующего СТЭПА. Со временем, как только мы достигли цели один раз,
это значение «награды» медленно возвращается назад, шаг за шагом, за эпизод. Супер базовая концепция, но довольно
изящная, как она работает!

Итак, теперь мы знаем буквально все, что нам нужно знать, чтобы это работало. На самом деле это совсем не
«алгоритмический» код, нам просто нужно написать окружающую логику.

Итак, Q-таблица инициализируется .... случайным образом. Затем на каждом шаге агент получает -1. Единственный раз,
когда агент получает награду, ну, ничего (0) ... - это если они достигают цели. Нам нужен агент, чтобы когда-нибудь
достичь цели. Если они достигнут его только один раз, у них будет больше шансов достичь его снова, поскольку награда
будет распространяться обратно. По мере того, как у них появляется больше шансов добраться до него, они будут
добираться до него снова и снова ... и бум, они узнают. Но как нам добраться до него с первого раза ?!

Эпсилон!

Или, как это называют обычные люди: случайные ходы.

Когда агент изучает среду, он переходит от «исследования» к «эксплуатации». Прямо сейчас наша модель жадная и всегда
использует максимальные значения Q ... но эти значения Q сейчас бесполезны. Нам нужен агент для исследования!

Для этого мы добавим следующие значения:
# Настройки исследования
epsilon = 1 # не постоянный, ожидаемый к распаду
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2
epsilon_decay_value = epsilon / ( END_EPSILON_DECAYING - START_EPSILON_DECAYING )
Теперь мы хотим уменьшать значение эпсилон в каждом эпизоде, пока не закончим его. Мы сделаем это в конце каждого
эпизода (в основном в самом низу):

Распад выполняется для каждой серии, если номер серии находится в пределах диапазона убывания,
если END_EPSILON_DECAYING > = episode > = START_EPSILON_DECAYING :
        epsilon - = epsilon_decay_value

Теперь нам просто нужно использовать эпсилон. Мы будем использовать np.random.random()случайный выбор числа от 0 до
1. Если np.random.random () больше, чем значение epsilon, то мы будем исходить из максимального значения q,
как обычно. В противном случае мы просто будем перемещаться случайным образом:
"""
import gym  # библиотека OpenAI с простыми играми
import numpy as np  # работа с массивами
env = gym.make("MountainCar-v0")  # обращаемся к виртуальной среде (инициализировать среду)
env.reset()  # В случае с этим тренажерным залом наблюдения возвращаются из сбросов и шагов.

# Q-Learning settings
LEARNING_RATE = 0.1  # находится между 0 и 1
DISCOUNT = 0.95  # находится между 0 и 1
EPISODES = 25000  # общее количество эпиздов
SHOW_EVERY = 3000  # каждый 3000 эпизод для отображения

DISCRETE_OS_SIZE = [20, 20]  # задаем таблицу дискритизации возможных состояний машины
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE  # шаг дискритизации

# Exploration settings
# Настройки исследования
epsilon = 1  # не постоянный, ожидаемый к распаду (not a constant, qoing to be decayed)
START_EPSILON_DECAYING = 1  # начальный шаг распада
END_EPSILON_DECAYING = EPISODES//2  # конечный шаг распада
epsilon_decay_value = epsilon/(END_EPSILON_DECAYING - START_EPSILON_DECAYING)  # значение распада


q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))  # заполняем таблицу
# случайными значениями


# Затем нам нужна быстрая вспомогательная функция, которая преобразует текущее «состояние» нашей среды,
# которое  содержит непрерывные значения от new_state, reward, done, _ = env.step(action), которые в конечном итоге
# преобразуем в «дискретное» состояние и обновим нашу Q-таблицу
def get_discrete_state(state):  # функция преобразования в дискретные значения (на входе текущие значения)
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    # из текущих значений вычитаем минимальные значения и делим на шаг дискритизации
    return tuple(discrete_state.astype(np.int))  # возвращает целые числа результата деления

for episode in range(EPISODES):  # цикл пройгрыша всех эпизодов
    discrete_state = get_discrete_state(env.reset())  # берем дескретные значения
    done = False  # переменная характеризующая завершение программы

    if episode % SHOW_EVERY == 0:  # если пришло время показать чему мы научились за 3000 эпизодов
        render = True  # то показываем эпизод
        print(episode)  # выводим номер проигрываемого эпизода
    else:
        render = False  # не показывает эпизод

    while not done:  # пока работает этот эпизод (200 шагов)
        # Мы будем использовать np.random.random() случайный выбор числа от 0 до 1.
        # Если np.random.random() больше, чем значение epsilon, то мы будем исходить из максимального значения q,
        # как обычно. В противном случае мы просто будем перемещаться случайным образом
        if np.random.random() > epsilon:
            # Get action from Q table
            # мы будем исходить из максимального значения q
            action = np.argmax(q_table[discrete_state])
        else:
            # Get random action
            # мы просто будем перемещаться случайным образом
            action = np.random.randint(0, env.action_space.n)

        # action = np.argmax(q_table[discrete_state])  # 0 - толчок влево, 1 - оставаться на месте, а 2 - толкать вправо
        new_state, reward, done, _ = env.step(action)  # считаем текущие характиристики программы (машины)

        new_discrete_state = get_discrete_state(new_state)  # преобразует текущие значения в дискретные

        if episode % SHOW_EVERY == 0:  # если пришло время показать эпизод
            env.render()  # то показываем эпизод
        #new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

        # Теперь мы хотим обновить Q-значение. Обратите внимание, что мы обновляем значение Q для действия, которое мы *
        # уже сделали
        # If simulation did not end yet after last step - update Q table
        # Если симуляция еще не закончилась после последнего шага - обновить Q-таблицу, если не завершено
        if not done:

            # Maximum possible Q value in next step (for new state)
            # Максимально возможное значение Q на следующем шаге (для нового состояния)
            max_future_q = np.max(q_table[new_discrete_state])

            # Current Q value (for current state and performed action)
            # Текущее значение Q (для текущего состояния и выполняемого действия)
            current_q = q_table[discrete_state + (action,)]

            # And here's our equation for a new Q value for current state and action
            # И вот наше уравнение для нового значения Q для текущего состояния и действия
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

            # Update Q table with new Q value
            # Обновление Q таблицы с новым значением Q
            q_table[discrete_state + (action,)] = new_q


        # Simulation ended (for any reson) - if goal position is achived - update Q value with reward directly
        # Моделирование завершено (для любого резонанса) - если позиция цели достигнута - обновить значение Q с наградой напрямую
        elif new_state[0] >= env.goal_position:
            # q_table[discrete_state + (action,)] = reward
            q_table[discrete_state + (action,)] = 0

        discrete_state = new_discrete_state  # Теперь нам нужно сбросить discrete_stateпеременную

    # Decaying is being done every episode if episode number is within decaying range
    # Распад происходит в каждом эпизоде, если номер эпизода находится в диапазоне уменьшения
    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

env.close()