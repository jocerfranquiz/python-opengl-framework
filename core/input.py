"""
Input class
"""

import pygame as pg


class Input:
    """
    Class to manage user inputs
    """

    def __init__(self) -> None:

        self.quit = False

    def update(self) -> None:
        """
        Update game state
        :return:
        """

        for event in pg.event.get():
            if event.type == pg.QUIT:  # close window
                print("\nQuitting program...")
                self.quit = True
