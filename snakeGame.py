import pygame
import random

# Initialising pygame
pygame.init()

# Set display window
windowWidth = 600
windowHeight = 600
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Snakes~~~~")

# Set FPS and clock
fps = 20
clock = pygame.time.Clock()

# Set game values
snakeSize = 20

# Define directions
UP = (0, -snakeSize)
DOWN = (0, snakeSize)
LEFT = (-snakeSize, 0)
RIGHT = (snakeSize, 0)

# Set colours
green = (0, 255, 0)
darkGreen = (10, 50, 10)
red = (255, 0, 0)
darkRed = (150, 0, 0)
white = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set sounds and music
pickUpSound = pygame.mixer.Sound("pickUpSound.wav")

def textDrawer(text, font, color, surface, x, y):
    """Draw text on the screen."""
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textSurface, textRect)

def inputHandler():
    """Handle user input."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def appleSpawner():
    """Spawn an apple at a random location."""
    appleX = random.randint(0, (windowWidth - snakeSize) // snakeSize) * snakeSize
    appleY = random.randint(0, (windowHeight - snakeSize) // snakeSize) * snakeSize
    return pygame.Rect(appleX, appleY, snakeSize, snakeSize)


def moveSnake(snakeHead, dx, dy):
    """Move the snake."""
    snakeHead.x += dx
    snakeHead.y += dy


def collisionsChecker(snakeHead, snakeBody):
    """Check for collisions with walls or itself."""
    if (snakeHead.left < 0 or snakeHead.right > windowWidth or
        snakeHead.top < 0 or snakeHead.bottom > windowHeight or
        any(snakeHead.colliderect(bodyPart) for bodyPart in snakeBody[1:])):
        return True
    return False

score = 0

# Main game loop
running = True
while running:
    # Event handling

    # Update display
    screen.fill(white)
    textDrawer("Score: " + str(score), font, green, screen, 10, 10)

    pygame.draw.rect(screen, red, appleSpawner())
    pygame.display.update()
    clock.tick(fps)