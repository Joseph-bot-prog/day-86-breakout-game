# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import the pygame library and initialise the game engine
import pygame
# import the Paddle Class, the Ball Class & the brick class
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

# Define some colors
WHITE = (255, 255, 255)
DARKBLUE = (0, 173, 181)
LIGHTBLUE = (255, 255, 255)
RED = (170, 216, 211)
ORANGE = (238, 238, 238)
YELLOW = (57, 62, 70)

score = 0
lives = 3

# Open a new window for GUI display
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ "
                           "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ "
                           "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ BREAKOUT GAME")

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Create the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Create the ball sprite
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Create a Pygame sprite group to store all the bricks
all_bricks = pygame.sprite.Group()

# Create the first row of red bricks
for i in range(7):
    # Create a Brick object with color RED, width 80, and height 30
    brick = Brick(RED, 80, 30)

    # Position each brick horizontally with a gap of 100 pixels
    brick.rect.x = 60 + i * 100

    # Position all bricks in the first row at a vertical coordinate of 60 pixels
    brick.rect.y = 60

    # Add the brick to the sprite list for updating and rendering
    all_sprites_list.add(brick)

    # Add the brick to the group of all bricks
    all_bricks.add(brick)

# Create the second row of orange bricks
for i in range(7):
    # Create a Brick object with color ORANGE, width 80, and height 30
    brick = Brick(ORANGE, 80, 30)

    # Position each brick horizontally with a gap of 100 pixels
    brick.rect.x = 60 + i * 100

    # Position all bricks in the second row at a vertical coordinate of 100 pixels
    brick.rect.y = 100

    # Add the brick to the sprite list for updating and rendering
    all_sprites_list.add(brick)

    # Add the brick to the group of all bricks
    all_bricks.add(brick)

# Create the third row of yellow bricks
for i in range(7):
    # Create a Brick object with color YELLOW, width 80, and height 30
    brick = Brick(YELLOW, 80, 30)

    # Position each brick horizontally with a gap of 100 pixels
    brick.rect.x = 60 + i * 100

    # Position all bricks in the third row at a vertical coordinate of 140 pixels
    brick.rect.y = 140

    # Add the brick to the sprite list for updating and rendering
    all_sprites_list.add(brick)

    # Add the brick to the group of all bricks
    all_bricks.add(brick)

# Add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Set the font for the countdown
countdown_font = pygame.font.Font(None, 74)

# Display the initial countdown
for i in range(3, 0, -1):
    screen.fill(DARKBLUE)  # Clear the screen
    text = countdown_font.render(str(i), 1, WHITE)
    text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  # Wait for 1 second

# Clear the screen before starting the main loop
screen.fill(DARKBLUE)
pygame.display.flip()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # The program should respond to user exit behaviour, so we exit this loop

    # Get the current state of all keys
    keys = pygame.key.get_pressed()

    # Check if the left arrow key is pressed
    if keys[pygame.K_LEFT]:
        # If pressed, move the paddle to the left by 5 units
        paddle.moveLeft(5)

    # Check if the right arrow key is pressed
    if keys[pygame.K_RIGHT]:
        # If pressed, move the paddle to the right by 5 units
        paddle.moveRight(5)

    # --- Game logic should go here
    all_sprites_list.update()

    # Check if the ball is hitting the right wall
    if ball.rect.x >= 790:
        # If hitting, reverse the horizontal velocity to bounce back
        ball.velocity[0] = -ball.velocity[0]

    # Check if the ball is hitting the left wall
    if ball.rect.x <= 0:
        # If hitting, reverse the horizontal velocity to bounce back
        ball.velocity[0] = -ball.velocity[0]

    # Check if the ball is hitting the bottom wall
    if ball.rect.y > 590:
        # Reverse the vertical velocity to bounce back
        ball.velocity[1] = -ball.velocity[1]

        # Decrease the number of lives by 1
        lives -= 1

        # Check if there are no lives remaining
        if lives == 0:
            # It should display a game over screen
            # Display Game Over Message for 3 seconds if no lives left
            # Create a font for the game over message
            font = pygame.font.Font(None, 74)

            # Render the "GAME OVER" message with white color
            text = font.render("GAME OVER", 1, WHITE)

            # Position the message on the screen
            screen.blit(text, (250, 300))

            # Update the display
            pygame.display.flip()

            # Wait for 3 seconds
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    # Check if the ball hits the top wall, reverse its vertical velocity
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddle
    if pygame.sprite.collide_mask(ball, paddle):
        # Move the ball back to avoid overlapping with the paddle
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]

        # Bounce the ball off the paddle
        ball.bounce()

    # Check if the ball collides with any of the bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        # Bounce the ball off the brick
        ball.bounce()

        # Increase the score by 1
        score += 1

        # Remove the brick from the sprite group
        brick.kill()

        # Check if all bricks are destroyed
        if len(all_bricks) == 0:
            # Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()

            # Wait for 3 seconds
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    # Drawing code
    # Clear the screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # Display the score and number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Once the main loop exits, stop the game engine
pygame.quit()
