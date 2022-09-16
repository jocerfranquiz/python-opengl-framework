from core.base import Base


# check input
class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):
        # # debug printing
        # if len(self.input.key_down_list) > 0:
        #     print("Keys down:", self.input.key_down_list)
        # if len(self.input.key_pressed_list) > 0:
        #     print("Keys pressed:", self.input.key_pressed_list)
        # if len(self.input.key_up_list) > 0:
        #     print("Keys up:", self.input.key_up_list)

        # typical usage
        if self.input.is_key_down("space"):
            print("The 'space' key was just pressed down.")
        if self.input.is_key_pressed("right"):
            print("The 'right' key is currently being pressed. ")


if __name__ == "__main__":
    Test().run()
