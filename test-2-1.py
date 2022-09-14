from core.game import Game


class Test(Game):

    def initialize(self):
        print("Initializing game...")

    def update(self):
        pass


Test().run()
