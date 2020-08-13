import json
import pygame
from time import sleep

pygame.init()

screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("Knockoff Pokemans")
icon = pygame.image.load('sprites\icon.png')
pygame.display.set_icon(icon)
running = True

#l o a d
Logo = pygame.image.load('sprites\logo.png')
Logox = 100
Logoy = 50
startChar = pygame.image.load('sprites\start.png')
charX = 0
charY = 0

def logo():
    screen.blit(Logo, (Logox,Logoy))

def StartChar():
    screen.blit(startChar, (charX, charY))
first = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    if first:
        StartChar()
        logo()
        pygame.display.update()
        sleep(7)
    pygame.display.update()
    first = False