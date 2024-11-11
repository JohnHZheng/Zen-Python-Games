""" A module to manage ship in alien invasion game."""
import os
import pygame

class Ship:
    """ A class to manage shipo"""
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
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

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that is not moving
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
