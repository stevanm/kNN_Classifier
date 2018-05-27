from GameController import  GameController

class Game():
    def __init__(self, board_width = 20, board_height = 20, gui = False):
        self.score = 0
        self.done = False
        self.board = {'width': board_width, 'height': board_height}
        self.gui = gui
        self.gc = GameController()


    def start(self):
        return self.gc.generate_observations()



    def step(self, game_action):
        #print(game_action)
        if self.gc.done == True:
            self.end_game()
        self.gc.player.ChangeDirection(game_action)
        self.done = self.gc.Move()
        self.score = self.gc.Score()
        self.gc.done = self.done
        #print(self.done)
        if self.gui:
            self.gc.Draw()
        return self.gc.generate_observations()


    def end_game(self):
        if self.gui: self.render_destroy()
        raise Exception("Game over")
