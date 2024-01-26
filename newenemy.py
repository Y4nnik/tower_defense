import pygame
import random

vector = pygame.math.Vector2
EnemyCollection = []
def newEnemy(speed, width, height, health, damage, value):
    return Enemy(speed, width, height, health, damage, value)

Values = [0,0,0,0,0,100,120,150,170,250]

class Enemy:
    def __init__(self, speed, width, height, health, dammage, value):
        self.position = (676 - width / 2, 0 - height / 2)
        self.vector = vector(0, speed)
        self.width = width
        self.dammage=dammage
        self.height = height
        self.health = health
        self.value = value
        self.speed=speed
        EnemyCollection.append(self)
        #EnemyCollection.sort(key = value)
Enemy(6,10,10,1,1,1)
Enemy(8,10,10,8,8,8)
Enemy(5,10,10,10,10,10)
print("verfügbare Gegner " + str(len(EnemyCollection)))
def newWave(wave):
    Enemy(6,10,10,1,1,1)
    Enemy(8,15,15,8,8,8)
    Enemy(5,10,10,10,10,10)
    print(len(EnemyCollection))
    avaylableEnemys = EnemyCollection
    if wave <=10:
        value=Values[wave-1]
    else:
        value=wave*wave*3
    Wave = []
    if wave > 5:
        while value >= 0:
            newenemy = avaylableEnemys[random.randint(0, len(avaylableEnemys)-1)]
            if newenemy.value <= value/2:
                Wave.append(newenemy)
                value -= newenemy.value
            else: 
                if newenemy.value == 1:
                    value = 0
                value -= avaylableEnemys[0].value
                Wave.append(avaylableEnemys[0])
                avaylableEnemys.remove(newenemy)
                
    elif wave == 1:
        Wave.append(avaylableEnemys[0])
    elif wave == 2:
        Wave.append(avaylableEnemys[0])
    elif wave == 3:
        Wave.append(avaylableEnemys[0])
    elif wave == 4:
        Wave.append(avaylableEnemys[0])
    elif wave == 5:
        Wave.append(avaylableEnemys[0])
    return Wave

        