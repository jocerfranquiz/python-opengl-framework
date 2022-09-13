import pygame as pg
import sys

SCREEN_SIZE = (512, 512)
FPS = 60


class Base(object):
    def __init__(self, screen_size=SCREEN_SIZE):

        pg.init()

        display_flags = pg.DOUBLEBUF | pg.OPENGL

        # antialiasing params
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)

        # cross-platform compatibility params
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        # screen definition
        self.screen = pg.display.set_mode(screen_size, display_flags)

        pg.display.set_caption('Graphics Window')

        self.running = True
        self.clock = pg.time.Clock()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):

        self.initialize()

        # main loop
        while self.running:
            self.update()
            pg.display.flip()
            self.clock.tick(FPS)

        pg.quit()
        sys.exit()

