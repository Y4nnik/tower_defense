import pygame
import math
import sys

vector = pygame.math.Vector2
hintergrund = pygame.image.load("images/background.png")
fuenfeck = pygame.image.load("images/fuenfeck.png")
screen = pygame.display.set_mode([1290,717])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Go = True #Spielvariable -> solange true lädt game weiter
Ziel=pygame.draw.rect(screen, (0,0,0), (1287, 172, 1, 64))

livingEnemys = [] #darin werden lebende Gegner gesichert
spawncounter = 0 #zählt tics seit letztem spawn

class Gegner:
    def __init__(self, geschw, breite, hoehe, leben, Schaden):
        self.position=(676-breite/2,0-hoehe/2)
        self.vector=vector(0 ,geschw)
        self.breite=breite
        self.hoehe=hoehe
        self.leben=leben
        livingEnemys.append(self)
        self.wegpunkt1 = pygame.draw.rect(screen,(0,0,0),(675, 227+self.breite/2, 1, 1) )
        self.wegpunkt2 = pygame.draw.rect(screen,(0,0,0),(405-self.breite/2, 227, 1, 1) )
        self.wegpunkt3 = pygame.draw.rect(screen,(0,0,0),(405, 107-self.hoehe/2, 1, 1) )
        self.wegpunkt4 = pygame.draw.rect(screen,(0,0,0),(188-self.breite/2, 107, 1, 1) )
        self.wegpunkt5 = pygame.draw.rect(screen,(0,0,0),(188, 492+self.hoehe/2, 1, 1) )
        self.wegpunkt6 = pygame.draw.rect(screen,(0,0,0),(969+self.breite/2, 492, 1, 1) )
        self.wegpunkt7 = pygame.draw.rect(screen,(0,0,0),(969, 204-self.hoehe/2, 1, 1) )

        self.figur = pygame.draw.rect(screen, (0,0,0),(676-(self.breite/2), 0-(self.hoehe/2), self.breite, self.hoehe))   
        

    def EnemyZeichnen(self):
        self.figur = pygame.draw.rect(screen, (0,0,0),(self.position[0], self.position[1], self.breite, self.hoehe))   
        
    def Laufen(self):
        self.position += self.vector
        if self.figur.colliderect(self.wegpunkt1):
            self.vector.rotate_ip(90)
            self.position=(675-self.breite/2,227-self.hoehe/2)   
            self.wegpunkt1 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.wegpunkt2):
            self.vector.rotate_ip(90)
            self.position=(405-self.breite/2,227-self.hoehe/2)   
            self.wegpunkt2 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.wegpunkt3):
            self.vector.rotate_ip(-90)
            self.position=(405-self.breite/2,103-self.hoehe/2)   
            self.wegpunkt3 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.wegpunkt4):
            self.vector.rotate_ip(-90)
            self.position=(188-self.breite/2,103-self.hoehe/2)   
            self.wegpunkt4 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.wegpunkt5):
            self.vector.rotate_ip(-90)
            self.position=(188-self.breite/2,492-self.hoehe/2)   
            self.wegpunkt5 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.wegpunkt6):
            self.vector.rotate_ip(-90)
            self.position=(969-self.breite/2,492-self.hoehe/2)   
            self.wegpunkt6 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )
        elif self.figur.colliderect(self.wegpunkt7):
            self.vector.rotate_ip(90)
            self.position=(969-self.breite/2,204-self.hoehe/2)   
            self.wegpunkt7 = pygame.draw.rect(screen,(0,0,0),(-10, -10, 1, 1) )

        if self.figur.colliderect(Ziel):
          livingEnemys.remove(self)
          print(len(livingEnemys))
         
               

Enemy1 = Gegner(6, 30, 30,10, 1)
while Go:
    if spawncounter == 20:
         Enemy1 = Gegner(6, 30, 30,10, 1)
         spawncounter = 0
         
    for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
        if event.type ==pygame.QUIT: sys.exit()#Spiel schließen
    screen.blit(hintergrund, (0,0))
    for Enemys in livingEnemys:
         Enemys.Laufen()
         Enemys.EnemyZeichnen()

    pygame.display.update()
    spawncounter +=1
    clock.tick(30)