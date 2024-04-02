"""
https://www.youtube.com/watch?v=tnq0whNwhZE&list=PLdBHMlEKo8UfnkIpJhwiOenHWxytitHpJ&ab_channel=PiotrBaja
"""
import sys
import pygame

print(pygame.__version__)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
x = 10
box = pygame.Rect(10, 10, 50, 50)
clock = pygame.time.Clock()
dt = 0.0

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Hej")
    
    # Ticking
    dt += clock.tick()/1000.0
    while dt > 1.0:
        print(dt)

    # Input
    # x += 1

    # box.x += 1
    # box.y += 1
    # box.w += 1
    # box.h += 1

    # Checking inputs

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        box.x += 1
    if keys[pygame.K_a]:
        box.x -= 1
    if keys[pygame.K_s]:
        box.y += 1
    if keys[pygame.K_w]:
        box.y -= 1

    
    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 150, 255), pygame.Rect(x, 70, 60, 70))
    pygame.draw.rect(screen, (100, 150, 55), box)
    pygame.display.flip()
