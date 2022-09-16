from core.base import Base


class Test(Base):

    def initialize(self):
        print("Initializing game...")

    def update(self):
        pass


if __name__ == "__main__":
    Test().run()
