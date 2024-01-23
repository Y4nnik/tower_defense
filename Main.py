import pygame
import math
import sys

vector = pygame.math.Vector2
background = pygame.image.load("images/background.png")
pentagon = pygame.image.load("images/fuenfeck.png")
screen = pygame.display.set_mode([1290,717])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Go = True #Spielvariable -> solange true lädt game weiter
Finish=pygame.draw.rect(screen, (0,0,0), (1287, 172, 1, 64))

livingEnemys = [] #darin werden lebende Gegner gesichert
spawncounter = 0 #zählt tics seit letztem spawn
def draw():
    a = 0 #dummy Funktion für mehr Übersicht
class Player:
    def __init__(self, Health):
        self.Health = Health

class Enemy:
    def __init__(self, speed, width, height, health, Schaden):
        self.position=(676-width/2,0-height/2)
        self.vector=vector(0 ,speed)
        self.width=width
        self.height=height
        self.health=health
        livingEnemys.append(self)
        self.waypoint1 = pygame.draw.rect(screen,(0,0,0),(675, 227+self.width/2, 1, 1) )
        self.waypoint2 = pygame.draw.rect(screen,(0,0,0),(405-self.width/2, 227, 1, 1) )
        self.waypoint3 = pygame.draw.rect(screen,(0,0,0),(405, 107-self.height/2, 1, 1) )
        self.waypoint4 = pygame.draw.rect(screen,(0,0,0),(188-self.width/2, 107, 1, 1) )
        self.waypoint5 = pygame.draw.rect(screen,(0,0,0),(188, 492+self.height/2, 1, 1) )
        self.waypoint6 = pygame.draw.rect(screen,(0,0,0),(969+self.width/2, 492, 1, 1) )
        self.waypoint7 = pygame.draw.rect(screen,(0,0,0),(969, 204-self.height/2, 1, 1) )

        self.figur = pygame.draw.rect(screen, (0,0,0),(676-(self.width/2), 0-(self.height/2), self.width, self.height))   

    def DrawEnemy(self):
        self.figur = pygame.draw.rect(screen, (0,0,0),(self.position[0], self.position[1], self.width, self.height))   
        
    def Move(self):
        self.position += self.vector
        if self.figur.colliderect(self.waypoint1):
            self.vector.rotate_ip(90)
            self.position=(675-self.width/2,227-self.height/2)   
            self.waypoint1 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.waypoint2):
            self.vector.rotate_ip(90)
            self.position=(405-self.width/2,227-self.height/2)   
            self.waypoint2 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.waypoint3):
            self.vector.rotate_ip(-90)
            self.position=(405-self.width/2,103-self.height/2)   
            self.waypoint3 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.waypoint4):
            self.vector.rotate_ip(-90)
            self.position=(188-self.width/2,103-self.height/2)   
            self.waypoint4 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.waypoint5):
            self.vector.rotate_ip(-90)
            self.position=(188-self.width/2,492-self.height/2)   
            self.waypoint5 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.waypoint6):
            self.vector.rotate_ip(-90)
            self.position=(969-self.width/2,492-self.height/2)   
            self.waypoint6 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.waypoint7):
            self.vector.rotate_ip(90)
            self.position=(969-self.width/2,204-self.height/2)   
            self.waypoint7 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )

        if self.figur.colliderect(Finish):
          livingEnemys.remove(self)

class Tower:
    def spwan():
         tower_rect = pygame.Rect(500,100,50,50)
         pygame.draw.rect(screen, (100,50,50), tower_rect, 0)
         tower_rohr_rect = pygame.Rect(tower_rect.centerx,tower_rect.centery-5,40,10)
         pygame.draw.rect(screen, (100,160,100), tower_rohr_rect, 0)    
               

while Go:
    if spawncounter == 20:
         Enemy1 = Enemy(6, 30, 30,10, 1)
         spawncounter = 0
         
    for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
        if event.type ==pygame.QUIT: 
             pygame.quit()
             sys.exit()#Spiel schließen
        if event.type ==pygame.QUIT: sys.exit()#Spiel schließen
    screen.blit(background, (0,0))
    Tower.spwan()
    for Enemys in livingEnemys:
         Enemys.Move()
         Enemys.DrawEnemy()
    draw()

    pygame.display.update()
    spawncounter +=1
    clock.tick(30)