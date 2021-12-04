from Coach import Coach
from connect4_game import Connect4Game
from utils import *

from parl.utils import logger

args = dotdict({
    # master address of xparl cluster
    'master_address': 'localhost:8010',
    # number of remote actors (execute tasks [self-play/pitting/evaluate_test_dataset] in parallel).
    'actors_num': 25,

    # total number of iteration
    'numIters': 200,
    # Number of complete self-play games to simulate during a new iteration.
    'numEps': 500,
    # Number of games to play during arena (pitting) play to determine if new neural network will be accepted.
    'arenaCompare': 50,
    # Number of games moves for MCTS to simulate.
    'numMCTSSims': 800,
    # temp=1 (Temperature, τ (tau)) if episodeStep < tempThresholdStep, and thereafter uses temp=0.
    'tempThresholdStep': 15,
    # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'updateThreshold': 0.6,
    # CPUCT parameter
    'cpuct': 4,
    # alpha parameter of dirichlet noise which is added to the policy (pi)
    'dirichletAlpha': 1.0,
    # history of examples from numItersForTrainExamplesHistory latest iterations (training data)
    'numItersForTrainExamplesHistory': 20,

    # folder to save model and training examples
    'checkpoint': './saved_model/',
    # whether to load saved model and training examples
    'load_model': False,
    'load_folder_file': ('./saved_model', 'checkpoint_1.pth.tar'),
})

# Plays arenaCompare games in which player1 starts arenaCompare/2 games and player2 starts arenaCompare/2 games.
assert args.arenaCompare % 2 == 0

# make sure the tasks can be split evenly among different remote actors
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
