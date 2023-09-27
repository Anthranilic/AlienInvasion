import pygame
from pygame.sprite import Sprite
import random

class AlienBullet(Sprite):
    """A class to manage bullets fired from alien ships."""

    def __init__(self, ai_game):
        """Create a bullet object at a random alien ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color
        self.aliens = ai_game.aliens

        # Convert the Group object to a list and then randomly select an alien
        aliens_list = list(self.aliens.sprites())
        self.alien = random.choice(aliens_list)

        # create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width, self.settings.alien_bullet_height)
        self.rect.midbottom = self.alien.rect.midbottom

        # store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # update the exact position of the bullet.
        self.y += self.settings.alien_bullet_speed
        # update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)