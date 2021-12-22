"""
Python 3.9 модель будет сохраняться, обучаться и оцениваться один раз для каждой итерации, она вызываются шаг за
шагом через класс Coach.
программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла Coach.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-22
"""
import os
import sys
import pickle
from pickle import Pickler, Unpickler
from random import shuffle
from parl.utils import tensorboard

import numpy as np
from tqdm import tqdm

import parl
from parl.utils import logger
from actor import Actor
from utils import split_group, get_test_dataset
from alphazero_agent import create_agent


class Coach():
    # This class executes the self-play, learning and evaluating.
    """
    Этот класс выполняет самостоятельную игру, обучение и оценку.
    """

    def __init__(self, game, args):
        self.game = game
        self.args = args

        # neural network of current generation
        # нейронная сеть текущего поколения
        self.current_agent = create_agent(self.game)
        # neural network of previous generation
        # нейронная сеть предыдущего поколения
        self.previous_agent = create_agent(self.game)

        # history of examples from args.numItersForTrainExamplesHistory latest iterations
        # история примеров из последних итераций args.numItersForTrainExamplesHistory
        self.trainExamplesHistory = []

        self.test_dataset = get_test_dataset()

    def _create_remote_actors(self):
        # connect to xparl cluster to submit jobs
        # подключиться к кластеру xparl для отправки заданий
        parl.connect(self.args.master_address)
        # creating the actors synchronizely.
        # создание актеров синхронно.
        self.remote_actors = [Actor(self.game, self.args, seed) \
            for seed in range(self.args.actors_num)]

    def learn(self):
        # Each iteration:
        #         1. Performs numEps episodes of self-play.
        #         2. Retrains neural network with examples in trainExamplesHistory
        #            (which has a maximum length of numItersForTrainExamplesHistory).
        #         3. Evaluates the new neural network with the test dataset.
        #         4. Pits the new neural network against the old one and accepts it
        #            only if it wins >= updateThreshold fraction of games.
        """
           Каждая итерация:
         1. Выполняет множество эпизодов самостоятельной игры.
         2. Обучает нейронную сеть с примерами в trainExamplesHistory
            (который имеет максимальную длину numItersForTrainExamplesHistory).
         3. Оценивает новую нейронную сеть с помощью тестового набора данных.
         4. Сопоставляет новую нейронную сеть со старой и принимает ее.
            только если он выиграет> = updateThreshold доля игр.
        """

        # create remote actors to run tasks (self-play/pitting/evaluate_test_dataset) in parallel.
        # создавать удаленных участников для параллельного выполнения задач (самовоспроизведение/питтинг/оценка_теста_данных).
        self._create_remote_actors()

        for iteration in range(1, self.args.numIters + 1):
            # logger.info('Starting Iter #{} ...'.format(iteration))
            logger.info('Начало итерации № #{} ...'.format(iteration))

            ####################
            # logger.info('Step1: self-play in parallel...')
            logger.info('Шаг 1: самостоятельная игра параллельно ...')
            iterationTrainExamples = []
            # update weights of remote actors to the latest weights, and ask them to run self-play task
            # обновить веса удаленных участников до последних весов и попросить их запустить задачу самостоятельной игры
            episode_num_each_actor = self.args.numEps // self.args.actors_num

            weights = self.current_agent.get_weights()
            future_object_ids  = [remote_actor.self_play(
                weights, episode_num_each_actor) \
                for remote_actor in self.remote_actors]
            results = [
                future_object.get() for future_object in future_object_ids
            ]
            for result in results:
                iterationTrainExamples.extend(result)

            # save the iteration examples to the history
            # сохранить примеры итераций в истории
            self.trainExamplesHistory.append(iterationTrainExamples)
            if len(self.trainExamplesHistory
                   ) > self.args.numItersForTrainExamplesHistory:
                # logger.warning("Removing the oldest entry in trainExamples.")
                logger.warning("Удаление самой старой записи в поезде Примеры.")
                self.trainExamplesHistory.pop(0)
            'история резервного копирования в файл'
            self.saveTrainExamples(iteration)  # backup history to a file

            ####################
            # logger.info('Step2: train neural network...')
            logger.info('Шаг 2: обучите нейронную сеть ...')
            # shuffle examples before training
            # перемешайте примеры перед тренировкой
            trainExamples = []
            for e in self.trainExamplesHistory:
                trainExamples.extend(e)
            shuffle(trainExamples)

            # training new network, keeping a copy of the old one
            # обучение новой сети, сохраняя копию старой
            self.current_agent.save(
                os.path.join(self.args.checkpoint, 'temp.pth.tar'))
            self.previous_agent.restore(
                os.path.join(self.args.checkpoint, 'temp.pth.tar'))

            self.current_agent.learn(trainExamples)

            ####################
            logger.info('Step3: evaluate test dataset in parallel...')
            logger.info('Шаг 3: параллельно оцените тестовый набор данных ...')
            cnt = 0
            # update weights of remote actors to the latest weights, and ask them to evaluate assigned test dataset
            # обновить веса удаленных участников до последних весов и попросить их оценить назначенный набор тестовых данных
            split_datas = []
            for i, data in enumerate(
                    split_group(
                        self.test_dataset,
                        len(self.test_dataset) // self.args.actors_num)):
                split_datas.append(data)
                cnt += len(data)
            weights = self.current_agent.get_weights()
            future_object_ids  = [remote_actor.evaluate_test_dataset(
                weights, data) \
                for data, remote_actor in zip(split_datas, self.remote_actors)]
            results = [
                future_object.get() for future_object in future_object_ids
            ]
            perfect_moves_cnt, good_moves_cnt = 0, 0
            # wait for all remote actors (a total of self.args.actors_num) to return the evaluating results
            # ждем, пока все удаленные акторы (всего self.args.actors_num) вернут результаты оценки
            for result in results:
                (perfect_moves, good_moves) = result
                perfect_moves_cnt += perfect_moves
                good_moves_cnt += good_moves
            # logger.info('perfect moves rate: {}, good moves rate: {}'.format(perfect_moves_cnt / cnt, good_moves_cnt / cnt))
            logger.info('скорость идеальных ходов: {}, скорость хороших ходов: {}'.format(perfect_moves_cnt / cnt, good_moves_cnt / cnt))
            tensorboard.add_scalar('perfect_moves_rate', perfect_moves_cnt / cnt, iteration)
            tensorboard.add_scalar('good_moves_rate', good_moves_cnt / cnt, iteration)

            ####################
            # logger.info('Step4: pitting against previous generation in parallel...')
            logger.info('Шаг 4: параллельно противостоять предыдущему поколению ...')
            # transfer weights of previous generation and current generation to the remote actors, and ask them to pit.
            # передать веса предыдущего и текущего поколений удаленным участникам и попросить их
            games_num_each_actor = self.args.arenaCompare // self.args.actors_num
            pre_weights = self.previous_agent.get_weights()
            cur_weights = self.current_agent.get_weights()
            future_object_ids  = [remote_actor.pitting(
                pre_weights,
                cur_weights, games_num_each_actor) \
                    for remote_actor in self.remote_actors]
            results = [
                future_object.get() for future_object in future_object_ids
            ]

            previous_wins, current_wins, draws = 0, 0, 0
            for result in results:
                (pwins_, cwins_, draws_) = result
                previous_wins += pwins_
                current_wins += cwins_
                draws += draws_

            # logger.info('NEW/PREV WINS : %d / %d ; DRAWS : %d' % (current_wins, previous_wins, draws))
            logger.info('Новые/Предыдущие победы : %d / %d ; Розыгрыши : %d' % (current_wins, previous_wins, draws))
            if previous_wins + current_wins == 0 or float(current_wins) / (
                    previous_wins + current_wins) < self.args.updateThreshold:
                # logger.info('REJECTING NEW MODEL')
                logger.info('ОТКАЗ ОТ НОВОЙ МОДЕЛИ')
                self.current_agent.restore(
                    os.path.join(self.args.checkpoint, 'temp.pth.tar'))
            else:
                # logger.info('ACCEPTING NEW MODEL')
                logger.info('ПРИНЯТИЕ НОВОЙ МОДЕЛИ')
                self.current_agent.save(
                    os.path.join(self.args.checkpoint, 'best.pth.tar'))
            self.current_agent.save(
                os.path.join(self.args.checkpoint,
                             self.getCheckpointFile(iteration)))

    def getCheckpointFile(self, iteration):
        return 'checkpoint_' + str(iteration) + '.pth.tar'

    def saveTrainExamples(self, iteration):
        folder = self.args.checkpoint
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = os.path.join(
            folder,
            self.getCheckpointFile(iteration) + ".examples")
        with open(filename, "wb+") as f:
            Pickler(f).dump(self.trainExamplesHistory)
        f.closed

    def loadModel(self):
        self.current_agent.restore(
            os.path.join(self.args.load_folder_file[0],
                         self.args.load_folder_file[1]))

    def loadTrainExamples(self):
        modelFile = os.path.join(self.args.load_folder_file[0],
                                 self.args.load_folder_file[1])
        examplesFile = modelFile + ".examples"
        if not os.path.isfile(examplesFile):
            logger.warning(
                # "File {} with trainExamples not found!".format(examplesFile))
                "Файл {} с trainExamples не найден!".format(examplesFile))
            # r = input("Continue? [y|n]")
            r = input("Продолжить? [y|n]")
            if r != "y":
                sys.exit()
        else:
            # logger.info("File with trainExamples found. Loading it...")
            logger.info("Файл с trainExamples найден. Загрузка ...")
            with open(examplesFile, "rb") as f:
                self.trainExamplesHistory = Unpickler(f).load()
            # logger.info('Loading done!')
            logger.info('Загрузка завершена!')
