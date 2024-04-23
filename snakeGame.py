import pygame
import random

# Initialising pygame
pygame.init()

# Set display window
windowWidth = 600
windowHeight = 600
displaySurface = pygame.display.set_mode((windowWidth, windowHeight))
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
