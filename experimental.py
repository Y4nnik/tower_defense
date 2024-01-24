import pygame
import math
import sys
pygame.font.init() 


my_font = pygame.font.SysFont('Comic Sans MS', 30)#definiert Schriftart
killed = 0 #für Herz bei tot von Enemy (Counter)
vector = pygame.math.Vector2
brokenheart = pygame.image.load("images/damage.png")
hintergrund = pygame.image.load("images/background.png")
fuenfeck = pygame.image.load("images/fuenfeck.png")
heart = pygame.image.load("images/heart.png")
screen = pygame.display.set_mode([1290,717])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Go = True #Spielvariable -> solange true lädt game weiter
Ziel=pygame.draw.rect(screen, (0,0,0), (1287, 172, 1, 64))
a=100



livingEnemys = [] #darin werden lebende Gegner gesichert
spawncounter = 20 #zählt tics seit letztem spawn
def schaden(damage):
    global a
    a = a-damage
class Gegner:
    def __init__(self, geschw, breite, hoehe, leben, Schaden):
        self.position=(676-breite/2,0-hoehe/2)
        self.vector=vector(0 ,geschw)
        self.breite=breite
        self.hoehe=hoehe
        self.leben=leben
        self.schaden=Schaden
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
          global killed
          killed = 5
          schaden(self.schaden)
          livingEnemys.remove(self)
          print(len(livingEnemys))
         
               

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
    
    text_surface = my_font.render(str(a), False, (0, 0, 0))
    screen.blit(text_surface, (10,5))
    screen.blit(heart, (70, 10))
    
    if killed != 0: 
        screen.blit(brokenheart, (1252, 185))
        killed -= 1
    pygame.display.update()
    spawncounter +=1
    clock.tick(30)