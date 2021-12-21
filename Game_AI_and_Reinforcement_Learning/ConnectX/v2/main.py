
from Coach import Coach
from connect4_game import Connect4Game
from utils import *

from parl.utils import logger

args = dotdict({
    # master address of xparl cluster
    # главный адрес кластера xparl
    'master_address': 'localhost:8010',

    # number of remote actors (execute tasks [self-play/pitting/evaluate_test_dataset] in parallel).
    # количество удаленных участников (выполняющих задачи [self-play / pitting / valu_test_dataset] параллельно).
    # не должно превышать количества ядер
    'actors_num': 5,

    # total number of iteration
    # общее количество итераций
    'numIters': 24,

    # Number of complete self-play games to simulate during a new iteration.
    # Количество полных игр с самостоятельной игрой для моделирования во время новой итерации.
    'numEps': 500,

    # Number of games to play during arena (pitting) play to determine if new neural network will be accepted.
    # Количество игр, которые нужно сыграть во время игры на арене (питтинг), чтобы определить, будет ли принята новая
    # нейронная сеть.
    'arenaCompare': 50,

    # Number of games moves for MCTS to simulate.
    # Количество игровых ходов для моделирования MCTS.
    'numMCTSSims': 800,
    # temp=1 (Temperature, τ (tau)) if episodeStep < tempThresholdStep, and thereafter uses temp=0.
    'tempThresholdStep': 15,

    # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    # Во время плей-офф арены новая нейронная сеть будет принята, если будет выиграно пороговое или большее количество игр.
    'updateThreshold': 0.6,
    # CPUCT parameter
    'cpuct': 4,

    # alpha parameter of dirichlet noise which is added to the policy (pi)
    # альфа-параметр шума дирихле, который добавляется в политику (пи)
    'dirichletAlpha': 1.0,

    # history of examples from numItersForTrainExamplesHistory latest iterations (training data)
    # история примеров из последних итераций numItersForTrainExamplesHistory (данные обучения)
    'numItersForTrainExamplesHistory': 20,

    # folder to save model and training examples
    # папка для сохранения моделей и обучающих примеров
    # 'checkpoint': './saved_model/',
    'checkpoint': '/home/user/PycharmProjects/Python-100-days/Game_AI_and_Reinforcement_Learning/ConnectX/v2/saved_model',

    # whether to load saved model and training examples
    # загружать ли сохраненную модель и примеры обучения
    # 'load_model': False,
        'load_model': True,
    # 'load_folder_file': ('./saved_model', 'checkpoint_24.pth.tar'),
    'load_folder_file': ('G/home/user/PycharmProjects/Python-100-days/Game_AI_and_Reinforcement_Learning/ConnectX/v2/saved_model',
                         'checkpoint_24.pth.tar'),
})

# Plays arenaCompare games in which player1 starts arenaCompare/2 games and player2 starts arenaCompare/2 games.
# Играет в игры arenaCompare, в которых игрок 1 начинает игры arenaCompare/2, а игрок 2 начинает игры arenaCompare / 2.
assert args.arenaCompare % 2 == 0

# make sure the tasks can be split evenly among different remote actors
# убедитесь, что задачи могут быть равномерно распределены между разными удаленными участниками
assert args.numEps % args.actors_num == 0
assert (args.arenaCompare // 2) % args.actors_num == 0
assert 1000 % args.actors_num == 0  # there are 1000 boards state in test_dataset


def main():
    game = Connect4Game()

    c = Coach(game, args)

    if args.load_model:
        logger.info('Loading checkpoint {}...'.format(args.load_folder_file))
        c.loadModel()
        logger.info("Loading 'trainExamples' from file {}...".format(
            args.load_folder_file))
        c.loadTrainExamples()

    c.learn()


if __name__ == "__main__":
    main()
