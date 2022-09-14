"""
PyOpenGL + Pygame
"""

import sys

import pygame as pg

from core.input import Input

SCREEN_SIZE = (512, 512)
FPS = 60


class Base:
    """
    Base class for a game
    """
    def __init__(self, screen_size=SCREEN_SIZE):
        pg.init()

        display_flags = pg.DOUBLEBUF | pg.OPENGL

        # antialiasing params
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)

        # cross-platform compatibility params
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)

        # screen definition
        self.screen = pg.display.set_mode(screen_size, display_flags)

        pg.display.set_caption('Graphics Window')

        self.running = True
        self.clock = pg.time.Clock()

        # manage user input
        self.input = Input()

    def initialize(self) -> None:
        """
        Initialize game
        :return:
        """

    def update(self) -> None:
        """
        Update game objects
        :return:
        """

    def run(self) -> None:
        """
        Game Life-cycle:

                     +------------------<<<<-----------------+
                     |                                       |
        STARTUP >>> INPUT >>> QUIT? >>> NO >>> UPDATE >>> RENDER
                               |
                               +>>> YES  >>> SHUTDOWN
        """

        # STARTUP
        self.initialize()

        # MAIN LOOP
        while self.running:

            # INPUT
            self.input.update()
            if self.input.quit:
                self.running = False

            # UPDATE
            self.update()

            # RENDER
            pg.display.flip()

            # pause if necessary to maintain FPS constant
            self.clock.tick(FPS)

        # SHUTDOWN
        pg.quit()
        sys.exit()
