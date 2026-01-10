"""Sideways gun shooter game main module."""
import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from gun import Gun
from bullet import Bullet
from goku import Goku

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways shooter 2")

        self.stats = GameStats(self)
        print(f"Initial guns_left from stats: {self.stats.guns_left}")  # DEBUG
        print(f"guns_limit from settings: {self.settings.guns_limit}")  # DEBUG

        self.gun = Gun(self)
        self.bullets = pygame.sprite.Group()
        self.gokus = pygame.sprite.Group()

        self._create_army()

        # start Sideways shooter game in an active state
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_active:
                self.gun.update()
                self._update_bullets()
                self._update_gokus()

            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            # move gun upwards
            self.gun.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.gun.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update positions of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_goku_collisions()
        
    def _check_bullet_goku_collisions(self):
        """Respond to bullet goku collisions."""
        # detect collision between bullet and goku, if yes get rid of both
        collisions = pygame.sprite.groupcollide(self.bullets, self.gokus, True, True)

        if not self.gokus:
            # Destroy existing bullets and create new army
            self.bullets.empty()
            self._create_army()

    def _update_gokus(self):
        """Update positions of all gokus in the army."""
        self._check_army_edges()
        self.gokus.update()

        # look for shooter(gun)-goku collisions
        if pygame.sprite.spritecollideany(self.gun, self.gokus):
            self._gun_hit()

        # look for gokus hitting the left edge of screen
        self._check_gokus_left_edge()
    
    def _gun_hit(self):
        """Respond to the gun being hit by a goku."""
        print(f"Guns left: {self.stats.guns_left}")  # Debug line
        if self.stats.guns_left > 0:
            # Decrement guns left.
            self.stats.guns_left -= 1
            # Get rid of remaining bullets and gokus
            self.bullets.empty()
            self.gokus.empty()
            # create a new army 
            self._create_army()
            # recenter the gun 
            self.gun.center_gun()
            # pause the game for the user to register this as new game starting
            sleep(0.5)
        else:
            self.game_active = False
    
    def _check_gokus_left_edge(self):
        """Check if any gokus reached the left edge of the screen."""
        for goku in self.gokus.sprites():
            if goku.rect.left <= 0:
                # TReat this same as goku hitting the gun
                self._gun_hit()
                break

    def _create_army(self):
        """Create the army of gokus."""
        # create a goku and keep adding gokus until no room left 
        # spacing between each goku is equal to goku width
        goku = Goku(self)
        goku_width, goku_height = goku.rect.size

        current_x, current_y = self.settings.screen_width , goku_height
        while current_x > 4 * goku_width:
            
            # create a column of gokus
            while current_y < self.settings.screen_height - goku_height:
                self._create_goku(current_x, current_y)
                current_y += 2 * goku_height
            
            # finished a column, reset y and decrement x, i.e. move left
            current_x -= 2*goku_width
            current_y = goku_height

    def _create_goku(self, x_position, y_position):
        """Create a goku and place it in the army."""
        new_goku = Goku(self)
        new_goku.rect.x = x_position
        new_goku.rect.y = y_position
        new_goku.x = float(new_goku.rect.x)
        new_goku.y = float(new_goku.rect.y)
        self.gokus.add(new_goku)

    def _check_army_edges(self):
        """Return true if army (any goku) reaches top or bottom edge of screen."""
        for goku in self.gokus.sprites():
            if goku.check_edges():
                self._change_army_direction()
                break

    def _change_army_direction(self):
        "Slide entire army and change army's driection(top or bottom)"
        for goku in self.gokus.sprites():
            goku.rect.x -= self.settings.army_sliding_speed
        self.settings.army_direction *= -1

    def _update_screen(self):
        """Update images on screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.gun.blitme()
        self.gokus.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
