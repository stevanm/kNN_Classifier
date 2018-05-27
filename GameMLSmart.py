from Game import Game
from random import randint
import numpy as np
import tflearn
import math
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean
from collections import Counter

class GameMLSmart:
    def __init__(self, initial_games = 1000, test_games = 100, goal_steps = 500, lr = 1e-2, filename = 'game_mlsmart.tflearn'):
        self.initial_games = initial_games
        self.test_games = test_games
        self.goal_steps = goal_steps
        self.lr = lr
        self.filename = filename

    def initial_population(self):
        training_data = []
        for _ in range(self.initial_games):
            game = Game()
            _, prev_score, player, checkpoint = game.start()
            prev_observation = self.generate_observation(player, checkpoint, game)
            prev_checkpoint_distance = self.get_checkpoint_distance(player, checkpoint)
            for _ in range(self.goal_steps):

                action, game_action = self.generate_action(player)
                done, score, player, checkpoint  = game.step(game_action)
                if done:
                    training_data.append([self.add_action_to_observation(prev_observation, action), -1])
                    break
                else:
                    checkpoint_distance = self.get_checkpoint_distance(player, checkpoint)
                    if score > prev_score or checkpoint_distance < prev_checkpoint_distance:
                        training_data.append([self.add_action_to_observation(prev_observation, action), 1])
                    else:
                        training_data.append([self.add_action_to_observation(prev_observation, action), 0])
                    prev_observation = self.generate_observation(player, checkpoint, game)
                    prev_checkpoint_distance = checkpoint_distance
        return training_data

    def generate_action(self, player):
        action = randint(0,2)-1
        return action, action #self.get_game_action(player, action)

    def generate_observation(self, player, checkpoint, game):
        car_direction = self.get_car_direction_vector(player)
        checkpoint_direction = self.get_checkpoint_direction_vector(player, checkpoint)
        barrier_left = game.gc.isThereObstacle(game.gc.map)[0]
        barrier_front = game.gc.isThereObstacle(game.gc.map)[1]
        barrier_right = game.gc.isThereObstacle(game.gc.map)[2]
        angle = self.get_angle(car_direction, checkpoint_direction)
        return np.array([int(barrier_left), int(barrier_front), int(barrier_right), angle])

    def add_action_to_observation(self, observation, action):
        return np.append([action], observation)

    def get_car_direction_vector(self, player):
        return np.array([player.frontCollisionLine[1].x - player.x, player.frontCollisionLine[1].y - player.y])

    def get_checkpoint_direction_vector(self, player, checkpoint):
        return np.array([checkpoint[0].x - player.x, checkpoint[0].y - player.y])

    def normalize_vector(self, vector):
        return vector / np.linalg.norm(vector)

    def get_checkpoint_distance(self, player, checkpoint):
        return np.linalg.norm(self.get_checkpoint_direction_vector(player, checkpoint))

    def get_angle(self, a, b):
        a = self.normalize_vector(a)
        b = self.normalize_vector(b)
        return math.atan2(a[0] * b[1] - a[1] * b[0], a[0] * b[0] + a[1] * b[1]) / math.pi

    def model(self):
        network = input_data(shape=[None, 5, 1], name='input')
        network = fully_connected(network, 25, activation='relu')
        network = fully_connected(network, 1, activation='linear')
        network = regression(network, optimizer='sgd', learning_rate=self.lr, loss='mean_square', name='target')
        model = tflearn.DNN(network, tensorboard_dir='log')
        return model

    def train_model(self, training_data, model):
        X = np.array([i[0] for i in training_data]).reshape(-1, 5, 1)
        y = np.array([i[1] for i in training_data]).reshape(-1, 1)
        model.fit(X,y, n_epoch = 3, shuffle = True, run_id = self.filename)
        model.save(self.filename)
        return model

    def test_model(self, model):
        steps_arr = []
        scores_arr = []
        for _ in range(self.test_games):
            steps = 0
            game_memory = []
            game = Game()
            _, score, player, checkpoint = game.start()
            prev_observation = self.generate_observation(player, checkpoint, game)
            for _ in range(self.goal_steps):
                predictions = []
                for action in range(-1, 2):
                    predictions.append(model.predict(self.add_action_to_observation(prev_observation, action).reshape(-1, 5, 1)))
                action = np.argmax(np.array(predictions))
                game_action = action-1
                done, score, player, checkpoint = game.step(game_action)
                game_memory.append([prev_observation, action])
                if done:
                    print('-----')
                    print(steps)
                    print(player)
                    print(checkpoint)
                    print(prev_observation)
                    print(predictions)
                    break
                else:
                    prev_observation = self.generate_observation(player, checkpoint, game)
                    steps += 1
            steps_arr.append(steps)
            scores_arr.append(score)
        print('Average steps:',mean(steps_arr))
        print(Counter(steps_arr))
        print('Average score:',mean(scores_arr))
        print(Counter(scores_arr))

    def visualise_game(self, model):
        game = Game(gui = True)
        _, _, player, checkpoint = game.start()
        prev_observation = self.generate_observation(player, checkpoint, game)
        for _ in range(100000):
            game.gc.GetInput()
            predictions = []
            for action in range(-1, 2):
                predictions.append(model.predict(self.add_action_to_observation(prev_observation, action).reshape(-1, 5, 1)))
            action = np.argmax(np.array(predictions))
            game_action = action-1
            done, _, player, checkpoint  = game.step(game_action)
            if done:
                break
            else:
                prev_observation = self.generate_observation(player, checkpoint, game)

    def train(self):
        training_data = self.initial_population()
        nn_model = self.model()
        nn_model = self.train_model(training_data, nn_model)
        self.test_model(nn_model)

    def visualise(self):
        nn_model = self.model()
        nn_model.load(self.filename)
        self.visualise_game(nn_model)

    def test(self):
        nn_model = self.model()
        nn_model.load(self.filename)
        self.test_model(nn_model)
        

if __name__ == "__main__":
    GameMLSmart().train()
    #GameMLSmart().visualise()
