from GameController import GameController



if __name__ == '__main__':

    gc = GameController()

    while True:
        gc.GetInput()
        gc.Draw()
        gc.Move()
        gc.Score()