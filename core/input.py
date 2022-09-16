"""
Input class
"""
from typing import List

import pygame as pg


class Input:
    """
    Class to manage user inputs
    """

    def __init__(self) -> None:

        self.quit = False

        # lists to store key states
        # down, up: discrete event; lasts for one iteration
        # pressed: continuous event, between down and up events
        self.key_down_list: List[str] = []
        self.key_pressed_list: List[str] = []
        self.key_up_list: List[str] = []

    def update(self) -> None:
        """
        Update game state
        :return:
        """

        # reset discrete key states
        self.key_down_list = []
        self.key_up_list = []
        for event in pg.event.get():
            if event.type == pg.QUIT:  # close window
                print("\nQuitting program...")
                self.quit = True
            # check for key-down and keyup events;
            # get name of key from event
            # and append to or remove from corresponding lists
            if event.type == pg.KEYDOWN:
                key_name = pg.key.name(event.key)
                self.key_down_list.append(key_name)
                self.key_pressed_list.append(key_name)
            if event.type == pg.KEYUP:
                key_name = pg.key.name(event.key)
                self.key_pressed_list.remove(key_name)
                self.key_up_list.append(key_name)

    # functions to check key states
    def is_key_down(self, key_code):
        return key_code in self.key_down_list

    def is_key_pressed(self, key_code):
        return key_code in self.key_pressed_list

    def is_key_up(self, key_code):
        return key_code in self.key_up_list
