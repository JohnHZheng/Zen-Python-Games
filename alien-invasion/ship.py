""" A module to manage ship in alien invasion game."""
import os
import pygame

class Ship:
    """ A class to manage shipo"""
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.

        # current_dir = os.getcwd()
        # project_root = os.path.abspath(os.path.join(current_dir, os.pardir))

        image_path = os.path.join('Zen-Python-Games', 'alien-invasion', 'images', 'ship.bmp')
        self.image = pygame.image.load(image_path)
        # self.image = pygame.image.load("c:\\GitHubRoot\\Zen-Python-Games\\alien-invasion\\images\\ship.bmp")
        self.rect  = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
