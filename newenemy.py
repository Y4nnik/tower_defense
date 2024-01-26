import pygame

vector = pygame.math.Vector2

def newEnemy(speed, width, height, health, damage):
    return Enemy(speed, width, height, health, damage)
class Enemy:
    def __init__(self, speed, width, height, health, dammage):
        self.position = (676 - width / 2, 0 - height / 2)
        self.vector = vector(0, speed)
        self.width = width
        self.dammage=dammage
        self.height = height
        self.health = health

