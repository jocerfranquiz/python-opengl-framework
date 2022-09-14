from core.base import Base


class Test(Base):

    def initialize(self):
        print("Initializing game...")

    def update(self):
        pass


Test().run()
