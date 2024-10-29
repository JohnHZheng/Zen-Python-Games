#print("Hello world")
import sys
import pygame

class AlienInvasion: 
    """Overall class to manage game assets and behavior"""
    def __init__(self) -> None:
        """Initialize the game, and create a game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ State wtih the main loop fo r the game."""
        while True: 
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
