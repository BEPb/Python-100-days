"""
Python 3.9 программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла 03.learn faster.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-19
"""
import gym  # библиотека OpenAI с простыми играми
import numpy as np  # работа с массивами
import matplotlib.pyplot as plt



env = gym.make("MountainCar-v0")  # обращаемся к виртуальной среде (инициализировать среду)
env.reset()  # В случае с этим тренажерным залом наблюдения возвращаются из сбросов и шагов.

# Q-Learning settings
LEARNING_RATE = 0.1  # находится между 0 и 1
DISCOUNT = 0.95  # находится между 0 и 1
EPISODES = 25000  # общее количество эпиздов
SHOW_EVERY = 3000  # каждый 3000 эпизод для отображения

# Для статистики
ep_rewards = []
aggr_ep_rewards = { 'ep' : [], 'avg' : [], 'max' : [], 'min' : []}
STATS_EVERY = 100

# DISCRETE_OS_SIZE = [20, 20]  # задаем таблицу дискритизации возможных состояний машины
DISCRETE_OS_SIZE = [40] * len(env.observation_space.high)  # задаем таблицу дискритизации возможных состояний машины
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
    episode_reward = 0  # информацию о награде
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
        episode_reward += reward    # информацию о награде
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

    ep_rewards.append(episode_reward)
    if not episode % STATS_EVERY:
        average_reward = sum(ep_rewards[-STATS_EVERY:]) / STATS_EVERY
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(average_reward)
        aggr_ep_rewards['max'].append(max(ep_rewards[-STATS_EVERY:]))
        aggr_ep_rewards['min'].append(min(ep_rewards[-STATS_EVERY:]))
        print(f'Episode: {episode:>5d}, average reward: {average_reward:>4.1f}, current epsilon: {epsilon:>1.2f}')

    # сохраним Q-таблицу
    if episode % 10 == 0:  # для уменьшения объема данных сохраняем не все а только каждую 10-ю
        np.save(f"qtables/{episode}-qtable.npy", q_table)

env.close()

plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="average rewards")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="max rewards")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="min rewards")
plt.legend(loc=4)
plt.grid(True)
plt.show()
