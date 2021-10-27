import pygame
from pygame.locals import *


def capture_events(hero_plane):
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            hero_plane.move(y=5)
        if keys[pygame.K_d]:
            hero_plane.move(x=5)
        if keys[pygame.K_w]:
            hero_plane.move(y=-5)
        if keys[pygame.K_a]:
            hero_plane.move(x=-5)
