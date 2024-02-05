# import a pygame library
import pygame
# call randint to display random characters
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the ball, and its x and y position, width and height.
        # Setting the background color and making it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(2, 4), randint(-4, 4)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    # updating scores function anytime the user makes one
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Displays bouncing balls
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
