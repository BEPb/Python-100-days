# Вступление
# В этом руководстве вы немного узнали об обучении с подкреплением и использовали пакет stable-baselines,
# чтобы научить агента побеждать случайного противника. В этом упражнении вы проверите свое понимание и повозитесь с
# кодом, чтобы углубить свою интуицию.
from learntools.core import binder
binder.bind(globals())
from learntools.game_ai.ex4 import *


# 1) Установите архитектуру
# В этом руководстве вы узнали об одном способе создания нейронной сети, которая может выбирать ходы в Connect Four.
# Нейронная сеть имела выходной слой с семью узлами: по одному на каждый столбец игрового поля.
#
# Допустим, вы хотите создать нейронную сеть, которая может играть в шахматы. Сколько узлов вы должны поместить в
# выходной слой?
#
# Вариант A: 2 узла (количество игроков)
# Вариант B: 16 узлов (количество игровых фишек, с которыми начинает каждый игрок)
# Вариант C: 4672 узла (количество возможных ходов)
# Вариант D: 64 узла (количество квадратов на игровом поле)
# Используйте свой ответ, чтобы установить значение переменной best_option ниже. Ваш ответ должен быть одним из «A», «B», «C» или «D».
#
# Заполнить бланк
best_option = 'C'

# Правильно: если мы используем аналогичную сеть, как в учебнике, сеть должна выводить вероятность для каждого
# возможного хода.

# 2) Определите награду
# В этом руководстве вы узнали, как дать своему агенту награду, которая побудит его выигрывать игры Connect Four.
# Рассмотрим теперь обучение агента для победы в игре «Сапер». Цель игры - очистить доску, не взорвав бомбы.
#
# Чтобы играть в эту игру в поиске Google, нажмите кнопку [Играть] по этой ссылке.
#
# Изображение
# С каждым ходом выполняется одно из следующего:
#
# Агент выбрал неверный ход (другими словами, он попытался раскрыть квадрат, который был обнаружен как часть
# предыдущего хода). Предположим, на этом игра заканчивается, и агент проигрывает.
# Агент очищает квадрат, в котором не было спрятанной мины. Агент побеждает в игре, потому что открываются все
# клетки без мин.
# Агент очищает квадрат, в котором не было спрятанной мины, но который еще не выиграл или не проиграл игру.
# Агент подрывает мину и проигрывает игру.
# Как вы могли бы указать вознаграждение для каждого из этих четырех случаев, чтобы, максимизируя совокупное
# вознаграждение, агент попытался выиграть игру?
#
# После  того, как вы определились со своим ответом, запустите ячейку кода ниже, чтобы получить кредит за ответ на
# этот вопрос.
#
# Решение: вот возможное решение - после каждого хода мы даем агенту награду, которая говорит ему, насколько хорошо
# он справился:
#
# Если агент выигрывает игру этим ходом, он получает награду +1.
# В противном случае, если агент выбирает недопустимый ход, он получает награду -10.
# В противном случае, если он взорвет мину, он получит награду -1.
# В противном случае, если агент очищает квадрат без скрытой мины, он получает награду +1/100.
# Чтобы  проверить правильность своего ответа, обратите внимание, что награда за выбор неверного хода и за подрыв
# мины  должна быть отрицательной. Награда за победу в игре должна быть положительной. И награда за очистку квадрата
# без скрытой мины должна быть либо нулевой, либо слегка положительной.
#
# 3) (Необязательно) Измените код
# В  этой следующей части упражнения вы измените код из учебника, чтобы поэкспериментировать с созданием собственных
# агентов!  Существует множество гиперпараметров, связанных с указанием агента обучения с подкреплением,
# и у вас будет возможность изменить их, чтобы увидеть, как это повлияет на производительность.
#
# Во-первых,  нам нужно убедиться, что ваш блокнот Kaggle настроен для запуска кода. Начните с просмотра меню
# «Настройки» справа от записной книжки. Ваше меню будет выглядеть следующим образом:
#
# Если  ваш параметр «Интернет» отображается как ссылка «Требуется подтверждение по телефону», щелкните по этой
# ссылке.  Это перенесет вас в новое окно; затем следуйте инструкциям, чтобы подтвердить свою учетную запись. После
# выполнения этого шага в настройках «Интернет» будет отображаться значение «Выкл.», Как в примере справа.
#
# Когда  в настройках «Интернет» отображается значение «Выкл.», Нажмите, чтобы включить его. Вы увидите всплывающее
# окно,  в котором вам нужно будет «Принять», чтобы завершить процесс и переключить настройку на «Вкл.». Как только
# Интернет будет включен, вы готовы к работе!
#
# Начните с запуска ячейки кода ниже.
#
#import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

!pip install 'tensorflow==1.15.0'

import tensorflow as tf
from kaggle_environments import make, evaluate
from gym import spaces

!apt-get update
!apt-get install -y cmake libopenmpi-dev python3-dev zlib1g-dev
!pip install "stable-baselines[mpi]==2.9.0"

from stable_baselines.bench import Monitor
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO1, A2C, ACER, ACKTR, TRPO
from stable_baselines.a2c.utils import conv, linear, conv_to_fc
from stable_baselines.common.policies import CnnPolicy

class ConnectFourGym:
    def __init__(self, agent2="random"):
        ks_env = make("connectx", debug=True)
        self.env = ks_env.train([None, agent2])
        self.rows = ks_env.configuration.rows
        self.columns = ks_env.configuration.columns
        # Learn about spaces here: http://gym.openai.com/docs/#spaces
        self.action_space = spaces.Discrete(self.columns)
        self.observation_space = spaces.Box(low=0, high=2,
                                            shape=(self.rows,self.columns,1), dtype=np.int)
        # Tuple corresponding to the min and max possible rewards
        self.reward_range = (-10, 1)
        # StableBaselines throws error if these are not defined
        self.spec = None
        self.metadata = None
    def reset(self):
        self.obs = self.env.reset()
        return np.array(self.obs['board']).reshape(self.rows,self.columns,1)
    def change_reward(self, old_reward, done):
        if old_reward == 1: # The agent won the game
            return 1
        elif done: # The opponent won the game
            return -1
        else: # Reward 1/42
            return 1/(self.rows*self.columns)
    def step(self, action):
        # Check if agent's move is valid
        is_valid = (self.obs['board'][int(action)] == 0)
        if is_valid: # Play the move
            self.obs, old_reward, done, _ = self.env.step(int(action))
            reward = self.change_reward(old_reward, done)
        else: # End the game and penalize agent
            reward, done, _ = -10, True, {}
        return np.array(self.obs['board']).reshape(self.rows,self.columns,1), reward, done, _

# Create ConnectFour environment
env = ConnectFourGym(agent2="random")

# Create directory for logging training information
log_dir = "log/"
os.makedirs(log_dir, exist_ok=True)

# Logging progress
monitor_env = Monitor(env, log_dir, allow_early_resets=True)

# Create a vectorized environment
vec_env = DummyVecEnv([lambda: monitor_env])

# Neural network for predicting action values
def modified_cnn(scaled_images, **kwargs):
    activ = tf.nn.relu
    layer_1 = activ(conv(scaled_images, 'c1', n_filters=32, filter_size=3, stride=1,
                         init_scale=np.sqrt(2), **kwargs))
    layer_2 = activ(conv(layer_1, 'c2', n_filters=64, filter_size=3, stride=1,
                         init_scale=np.sqrt(2), **kwargs))
    layer_2 = conv_to_fc(layer_2)
    return activ(linear(layer_2, 'fc1', n_hidden=512, init_scale=np.sqrt(2)))

class CustomCnnPolicy(CnnPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomCnnPolicy, self).__init__(*args, **kwargs, cnn_extractor=modified_cnn)
#

# Initialize agent
model = PPO1(CustomCnnPolicy, vec_env, verbose=0)

# Train agent
model.learn(total_timesteps=100000)

# Plot cumulative reward
with open(os.path.join(log_dir, "monitor.csv"), 'rt') as fh:
    firstline = fh.readline()
    assert firstline[0] == '#'
    df = pd.read_csv(fh, index_col=None)['r']
df.rolling(window=1000).mean().plot()
plt.show()

# Если ваш агент хорошо обучен, график (который показывает средние совокупные вознаграждения) со временем должен
# увеличиваться.
#
# Убедившись, что код работает, попробуйте внести поправки, чтобы посмотреть, сможете ли вы повысить
# производительность. Вы можете:
#
# измените PPO1 на A2C (или ACER, или ACKTR, или TRPO) при определении модели в этой строке кода: model = PPO1 (
# CustomCnnPolicy,  vec_env, verbose = 0). Это позволит вам увидеть, как на производительность может повлиять
# изменение алгоритма  с Proximal Policy Optimization [PPO] на один из:
# Преимущество актер-критик (A2C),
# или актер-критик с опытом воспроизведения (ACER),
# Актер-критик, использующий зону доверия с учетом фактора Кронекера (ACKTR), или
# Оптимизация политики доверенного региона (TRPO).
# измените метод c hange_reward () в классе ConnectFourGym, чтобы изменить вознаграждения, которые агент получает в
# различных условиях.  Вам также может потребоваться изменить self.reward_range в методе __init__ (этот кортеж всегда
# должен соответствовать минимальному и максимальному вознаграждению, которое может получить агент).
# измените agent2 на  другого агента при создании среды ConnectFour с env = ConnectFourGym (agent2 = "random").
# Например, вы можете  использовать агент «negamax» или другой настраиваемый агент. Учтите, что чем умнее вы сделаете
# оппонента, тем сложнее будет обучать вашего агента!


