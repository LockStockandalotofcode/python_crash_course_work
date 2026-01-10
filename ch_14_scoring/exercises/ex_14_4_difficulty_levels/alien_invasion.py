"""Alien invasion game main module."""
import sys
import pygame

from time import sleep
from button import Button
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1100, 700))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make th play button
        self.play_button = Button(self, "Play")
        
        # Make the difficulty level buttons.
        self._make_difficulty_buttons()

        # Start the game in an inactive state
        self.game_active = False

    def _make_difficulty_buttons(self):
        """Make buttons that allow player to select dificulty level."""
        self.easy_button = Button(self, "Easy")
        self.medium_button = Button(self, "Medium")
        self.difficult_button = Button(self, "Difficulty")

        # Position buttons so they don't overlap.
        # self.easy_button.rect.top = (self.play_button.rect.top + 1.5*self.play_button.rect.height)
        self.easy_button.rect.top = self.play_button.rect.bottom + 20
        self.easy_button._update_msg_position()

        self.medium_button.rect.top = (self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button._update_msg_position()

        self.difficult_button.rect.top = (self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.difficult_button._update_msg_position()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Helper function for main loop: Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) # flag stores boolean value
        
        # below conditional statement resets the game on clicking play button
        if button_clicked:
            # Reset game settings.
            self.settings.initialize_dynamic_settings()
            self._start_game()
    
    def _check_difficulty_buttons(self, mouse_pos):
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        difficult_button_clicked = self.difficult_button.rect.collidepoint(mouse_pos)
        if easy_button_clicked:
            self.settings.difficulty_level = "easy"
            # self.settings.set_difficulty("easy")
        elif medium_button_clicked:
            self.settings.difficulty_level = "medium"
            # self.settings.set_difficulty("medium")
        elif difficult_button_clicked:
            self.settings.difficulty_level = "difficult"
            # self.settings.set_difficulty("difficult")

        self.settings.initialize_dynamic_settings()
    
    def _start_game(self):
        """Start the game on P-keypresses and clicking play button only when game is inactive to begin with."""
        if not self.game_active:
            # reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True
            # get rid of remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Build a new alien fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        """Helper function for events: Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # move ship to right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Helper function for events: Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Helper function for events: 
        Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Helper function for main loop: Update positions of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Responfd to bullet-alien collisions."""
        # REmove any aliens and bullets that have collided.
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_aliens(self):
        """check if the fleet is at an edge, then Update positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the ground
        self._check_aliens_bottom()
        
    def _check_aliens_bottom(self):
        """Check if any aliens have reached bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # treat this same as colliding wiht ship
                self._ship_hit()
                break
    
    def _ship_hit(self):
        """Respond to ship being hit by alien."""

        if self.stats.ships_left > 0:
            # decrement ships left
            self.stats.ships_left -= 1
            # delete remaining bullets and remaining alien fleet
            self.bullets.empty()
            self.aliens.empty()
            # create new fleet
            self._create_fleet()
            # recenter ship on screen
            self.ship.center_ship()
            # pause game
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create fleet of aliens."""
        # Make an alien and keep adding aliens to until no room left in a row.
        # spacing between aliens is one width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 4*alien_height):
            while current_x < (self.settings.screen_width - (2*alien_width)):
                # create an alien and place it in the row until no room left
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
            
            # Finished a row; now reset x value and increment y value.
            current_x = alien_width
            current_y += alien_width*2

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        """REspond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop entire fleet and change fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Helper function for main loop: Update images on screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.difficult_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
