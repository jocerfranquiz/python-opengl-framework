from core.game import Game


class Test(Game):

    def initialize(self):
        print("Initializing game...")

    def update(self):
        pass


if __name__ == "__main__":
    Test().run()
