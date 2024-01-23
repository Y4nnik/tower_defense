import pygame
import sys

hintergrund = pygame.image.load("images/background.png")
fuenfeck = pygame.image.load("images/fuenfeck.png")
screen = pygame.display.set_mode([1290,717])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Go = True

livingEnemys = [] #darin werden lebende Gegner gesichert

class Gegner:
    def __init__(self, geschw, breite, hoehe, leben):
        self.x=676
        self.y=0
        self.geschw=geschw
        self.breite=breite
        self.hoehe=hoehe
        self.leben=leben
        livingEnemys.append(self)

    def EnemyZeichnen(self):
        
        screen.blit(fuenfeck, (self.x-self.breite/2, self.y-self.hoehe/2))#Zeichnen funktioniert noch nicht :(
         #pygame.draw.rect(screen, (200,200,200),(self.x-(self.breite/2), self.y-(self.hoehe/2)), self.breite, self.hoehe, 0)   
        
    def Laufen(self):
     if self.x==676 and self.y <= 227:
                self.y += self.geschw
                print(self.y)#Kontrollwert
                if self.y>227:
                    self.y=227
                    self.x=675
     elif self.y==227 and self.x<=675 and self.x >= 405:
          self.x -= self.geschw
          if self.x<405:
               self.x=405
               self.y=226
     elif self.x==405 and self.y<=226:
          self.y -= self.geschw
          if self.y <= 107:
               self.y=107
               self.x=404
     elif self.y==107 and self.x<=404:
          self.x -= self.geschw
          if self.x <= 188:
               self.x=188
               self.y=108
     if self.x==188 and self.y <= 107:
          self.y += self.geschw

class Tower:
    def spwan():
         tower_rect = pygame.Rect(500,100,50,50)
         pygame.draw.rect(screen, (100,50,50), tower_rect, 0)
         tower_rohr_rect = pygame.Rect(tower_rect.centerx,tower_rect.centery-5,40,10)
         pygame.draw.rect(screen, (100,160,100), tower_rohr_rect, 0)
                       
               

Enemy1 = Gegner(10, 30, 30,10)
print(len(livingEnemys))#Kontrolle, ob in Liste aufgenommen

while Go:
    for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
        if event.type ==pygame.QUIT: 
             pygame.quit()
             sys.exit()#Spiel schließen
    screen.blit(hintergrund, (0,0))
    Tower.spwan()
    for Enemys in livingEnemys:
         Enemys.Laufen()
         Enemys.EnemyZeichnen()
    pygame.display.update()
    clock.tick(30)