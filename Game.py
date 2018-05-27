from GameController import  GameController

class Game():
    def __init__(self, gui = False):
        self.score = 0
        self.done = False
        self.gui = gui
        self.gc = GameController()


    def start(self):
        return self.gc.generate_observations()



    def step(self, game_action):
        if self.gc.done == True:
            self.end_game()
        self.gc.player.ChangeDirection(game_action)
        self.done = self.gc.Move()
        self.score = self.gc.Score()
        self.gc.done = self.done
        if self.gui:
            self.gc.Draw()
        return self.gc.generate_observations()