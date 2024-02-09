import pygame
import random

smallestship = pygame.image.load("images/smallestship.png")
smallestship = pygame.transform.rotate(smallestship, 180)
shipsmall = pygame.image.load("images/shipsmall.png")
shipsmall = pygame.transform.rotate(shipsmall, 180)
shipsmall2 = pygame.image.load("images/shipsmall2.png")
shipsmall2 = pygame.transform.rotate(shipsmall2, 180)
shipsmall3 = pygame.image.load("images/shipsmall3.png")
shipsmall3 = pygame.transform.rotate(shipsmall3, 180)
shipsmall4 = pygame.image.load("images/shipsmall4.png")
shipsmall4 = pygame.transform.rotate(shipsmall4, 180)
shipsmall5 = pygame.image.load("images/smallship5.png")
shipsmall5 = pygame.transform.rotate(shipsmall5, 180)
shipsmall6 = pygame.image.load("images/shipsmall6.png")
shipsmall6 = pygame.transform.rotate(shipsmall6, 180)
shipsmall8 = pygame.image.load("images/shipsmall8.png")
shipsmall8 = pygame.transform.rotate(shipsmall8, 180)
cruiser = pygame.image.load("images/cruiser.png")
cruiser = pygame.transform.rotate(cruiser, 180)
starship = pygame.image.load("images/starship.png")
starship = pygame.transform.rotate(starship, 180)
destroyer = pygame.image.load("images/destroyer.png")
destroyer = pygame.transform.rotate(destroyer, 180)

vector = pygame.math.Vector2
EnemyCollection = []
def newEnemy(speed, width, height, health, damage, value, picture):
    return Enemy(speed, width, height, health, damage, value, picture)

Values = [0,0,0,0,0,100,120,150,170,250]

class Enemy:
    def __init__(self, speed, width, height, health, dammage, value, picture):
        self.position = (676 - width / 2, 0 - height / 2)
        self.vector = vector(0, speed)
        self.width = width
        self.dammage=dammage
        self.height = height
        self.health = health
        self.value = value
        self.speed=speed
        self.picture = picture
        EnemyCollection.append(self)
        #EnemyCollection.sort(key = value)
Enemy(6,10,10,1,1,1,shipsmall4)
Enemy(8,10,10,8,8,10,shipsmall5)
Enemy(5,10,10,10,10,10,shipsmall)
def newWave(wave):
    Enemy(6,10,10,1,1,1, smallestship)
    Enemy(8,15,15,8,8,8, shipsmall6)
    Enemy(5,10,10,10,10,10, shipsmall2)    
    Enemy(5,11,11,20,15,15, shipsmall8)    
    Enemy(5,12,12,30,30,20, shipsmall3)
    Enemy(5,10,10,20,60,30, smallestship)
    Enemy(3,30,30,200,100,80, starship)
    Enemy(3,40,40,800,200,100, cruiser)
    Enemy(5,50,50,1600,20,150, destroyer)
    avaylableEnemys = EnemyCollection
    if wave <=10:
        value=Values[wave-1]
    else:
        value=wave*wave*3
    Wave = []
    if wave > 5:
        while value >= 0:
            newenemy = avaylableEnemys[random.randint(0, len(avaylableEnemys)-1)]
            if newenemy.value <= value:
                Wave.append(newenemy)
                value -= newenemy.value
            else: 
                if newenemy.value == 1:
                    value = 0
                value -= avaylableEnemys[0].value
                Wave.append(avaylableEnemys[0])
                if newenemy in avaylableEnemys: avaylableEnemys.remove(newenemy)
                
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

        