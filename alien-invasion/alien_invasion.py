import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion: 
    """Overall class to manage game assets and behavior"""
    def __init__(self) -> None:
        """Initialize the game, and create a game resources"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # Set the background color
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        """ State wtih the main loop fo r the game."""
        while True: 
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """ Update image on the screen, an flipt to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()       

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
