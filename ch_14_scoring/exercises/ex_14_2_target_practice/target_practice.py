"""Main module to handle Target Practice game."""

import sys
import pygame

from time import sleep
from button import Button
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from target import Target

class TargetPractice:
    """Overall calss to manage game assets and behavior."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # Start the game in an inactive state
        self.game_active = False

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        # Track game stats
        self.stats = GameStats(self)
        # self.misses = 0

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        # self._create_target()       

        # Make the play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
            self._update_screen()

            self.clock.tick(60)
    
    def _check_events(self):
        """Helper method to main loop"""
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
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when player clicks play button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) #flag stores boolean value

        # Below condition resets game on clicking play button
        if button_clicked:
            self._start_game()
    
    def _start_game(self):
        """Start a new game when user clicks play."""
        if not self.game_active:
            # Reset game stats.
            self.stats.reset_stats()
            self.game_active = True
            # Remove remaining bullets 
            self.bullets.empty()
            # Recenter target after collision
            self.target.center_target()
            # Recenter ship
            self.ship.center_ship()
    
    def _check_keydown_events(self, event):
        """Helper function for events: Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Helper function for events: Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        """Helper function: create a new bullet and add to bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Helper function for events: Update positions of old bullets and get rid of old ones (from memory)."""
        # Update bullet positions.
        self.bullets.update()

        # get rid of bullets that have disappeared from the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self._bullet_missed() # count as a miss
        
        # Check for bullet-target collisions
        self._check_target_collision()
    
    def _bullet_missed(self):
        """Handle when a bullet misses the target."""
        self.stats.attempts_left -= 1
        if self.stats.attempts_left < 0:
            self.game_active = False  # End game
            
    def _check_target_collision(self):
        """Respond to bullet-target collisions."""
        # detect collisions
        collisions = pygame.sprite.spritecollideany(self.target, self.bullets)
        if collisions:
            self._target_hit()
        
    def _target_hit(self):
        """Respond to bullet-target collisions."""
        # Remove remaining bullets 
        self.bullets.empty()
        # Recenter target after collision
        self.target.center_target()
        # Pause game.
        sleep(0.5)

    def _update_target(self):
        """Update target position."""
        self._check_target_edge()
        self.target.update()

    # def _create_target(self):
    #     """Create a target."""
    #     new_target = Target(self)

    def _check_target_edge(self):
        """Check if target has reached top or bottom edge, and switch direction."""
        if self.target.check_edges():
            self.settings.target_direction *= -1
    
    def _update_screen(self):
        """Helper function for main loop: Update images on screen, and flip to the new screen."""
        # Redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        # bulletsare drawn before ship, so that ther not visible before being fired
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blit_me()
        self.target.draw_target()

        # Draw the play button if game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    tp = TargetPractice()
    tp.run_game()