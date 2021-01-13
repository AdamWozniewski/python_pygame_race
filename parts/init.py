import pygame
from parts.variables import display_width, display_height

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ścigałka')
clock = pygame.time.Clock()
