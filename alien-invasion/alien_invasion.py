from bullet import Bullet
from alien import Alien
from settings import Settings
from ship import Ship
import pygame
import sys

class AlienInvasion: 
    """Overall class to manage game assets and behavior"""
    def __init__(self) -> None:
        """Initialize the game, and create a game resources"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Set the background color
        #self.bg_color = (230, 230, 230)

    def run_game(self):                           
        """ State wtih the main loop fo r the game."""
        while True: 
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respone to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key ==  pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respone to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a nwe bullet and add nit to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """ Update image on the screen, an flipt to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()      

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an aline
        alien = Alien(self)
        self.aliens.add(alien)
        align_width = alien.rect.width

        current_x = align_width
        while current_x < (self.settings.screen_width - 2 * align_width):
            self._create_alien(current_x)
            current_x += 2*align_width

    def _create_alien(self, x_position):
        """Create the alien and place it in the row"""
        # Make an aline
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
