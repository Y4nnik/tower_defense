import pygame
import sys

hintergrund = pygame.image.load("images/background.png")
fuenfeck = pygame.image.load("images/fuenfeck.png")
screen = pygame.display.set_mode([1290,717])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Go = True #Spielvariable -> solange true lädt game weiter
Ziel=pygame.draw.rect(screen, (0,0,0), (1280, 172, 10, 32))

livingEnemys = [] #darin werden lebende Gegner gesichert
spawncounter = 0 #zählt tics seit letztem spawn

class Gegner:
    def __init__(self, geschw, breite, hoehe, leben, Schaden):
        self.x=676
        self.y=0
        self.geschw=geschw
        self.breite=breite
        self.hoehe=hoehe
        self.leben=leben
        livingEnemys.append(self)
        self.figur = pygame.draw.rect(screen, (0,0,0),(self.x-(self.breite/2), self.y-(self.hoehe/2), self.breite, self.hoehe))   
        

    def EnemyZeichnen(self):
        self.figur = pygame.draw.rect(screen, (0,0,0),(self.x-(self.breite/2), self.y-(self.hoehe/2), self.breite, self.hoehe))   
        
    def Laufen(self):
     if self.x==676 and self.y <= 227:
                self.y += self.geschw
                if self.y > 227:
                    self.y = 227
                    self.x = 675
     elif self.y==227 and self.x<=675 and self.x >= 405:
          self.x -= self.geschw
          if self.x < 405:
               self.x = 405
               self.y = 226
     elif self.x==405 and self.y<=226:
          self.y -= self.geschw
          if self.y <= 107:
               self.y = 107
               self.x = 404
     elif self.y == 107 and self.x <= 404:
          self.x -= self.geschw
          if self.x <= 188:
               self.x = 188
               self.y = 108
     elif self.x == 188 and self.y >= 107:
          self.y += self.geschw
          if self.y >= 492:
               self.y = 492
               self.x = 189
     elif self.y == 492:
          self.x += self.geschw
          if self.x >= 968:
               self.x = 968
               self.y = 493
     elif self.x == 968:
          self.y -=self.geschw
          if self.y <= 204:
               self.y = 204
               self.x = 969
     elif self.y == 204:
          self.x += self.geschw
          if self.x >= 1288:
               self.x = 1288
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