import pygame

carImg = pygame.image.load('assets/images/car.png')
carLeft = carImg
carRight = carImg
obstacle_Img = pygame.image.load('assets/images/obstacle.png')
texture = pygame.image.load('assets/images/texture.png')

(car_width, car_height) = carImg.get_rect().size
(carL_width, carL_height) = carLeft.get_rect().size
(carR_width, carR_height) = carRight.get_rect().size
(thing_width, thing_height) = obstacle_Img.get_rect().size
(texture_width, texture_height) = texture.get_rect().size

logo = pygame.image.load('assets/images/logo.jpg')
pygame.display.set_icon(logo)

background = pygame.image.load('assets/images/background.jpg')
background_still = pygame.image.load('assets/images/background_inv.png')
backgroundRect = background.get_rect()