import pygame
import math
import sys

pygame.font.init() 

killed = 0 #für Herz bei tot von Enemy (Counter)

my_font = pygame.font.SysFont('Comic Sans MS', 30)#definiert Schriftart
vector = pygame.math.Vector2

background = pygame.image.load("images/background.png")
pentagon = pygame.image.load("images/fuenfeck.png")
brokenheart = pygame.image.load("images/damage.png")
heart = pygame.image.load("images/heart.png")

screen = pygame.display.set_mode([1290, 717])  # Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Finish=pygame.draw.rect(screen, (0,0,0), (1287, 172, 1, 64))

livingEnemys = [] #darin werden lebende Gegner gesichert
spawncounter = 0 #zählt tics seit letztem spawn

def draw():
    text_surface = my_font.render(str(Player1.health), False, (0, 0, 0))
    screen.blit(text_surface, (10,5))
    screen.blit(heart, (70, 10))
    global killed
    if killed != 0: 
        screen.blit(brokenheart, (1252, 185))
        killed -= 1

livingEnemys = []  # darin werden lebende Gegner gesichert
livingTowers = []  # darin werden lebende Türme gesichert
spawncounter = 0  # zählt tics seit letztem spawn


class Player:
    def __init__(self, Health):
        self.health = Health
    def GetDammage(self, damageTaken):
        self.health -= damageTaken
        if self.health <= 0: print("Game Over :P")


class Enemy:
    def __init__(self, speed, width, height, health, dammage):
        self.position = (676 - width / 2, 0 - height / 2)
        self.vector = vector(0, speed)
        self.width = width
        self.dammage=dammage
        self.height = height
        self.health = health
        livingEnemys.append(self)
        self.waypoint1 = pygame.draw.rect(screen, (0, 0, 0), (675, 227 + self.width / 2, 1, 1))
        self.waypoint2 = pygame.draw.rect(screen, (0, 0, 0), (405 - self.width / 2, 227, 1, 1))
        self.waypoint3 = pygame.draw.rect(screen, (0, 0, 0), (405, 107 - self.height / 2, 1, 1))
        self.waypoint4 = pygame.draw.rect(screen, (0, 0, 0), (188 - self.width / 2, 107, 1, 1))
        self.waypoint5 = pygame.draw.rect(screen, (0, 0, 0), (188, 492 + self.height / 2, 1, 1))
        self.waypoint6 = pygame.draw.rect(screen, (0, 0, 0), (969 + self.width / 2, 492, 1, 1))
        self.waypoint7 = pygame.draw.rect(screen, (0, 0, 0), (969, 204 - self.height / 2, 1, 1))

        self.figur = pygame.draw.rect(screen, (0, 0, 0),
                                      (676 - (self.width / 2), 0 - (self.height / 2), self.width, self.height))

    def GetDammage(self, damageTaken):
        self.health -= damageTaken
        if self.health <= 0: livingEnemys.remove(self)
        #Funktion für Geld fehlt

    def doDamage(self):
        Player1.GetDammage(self.dammage)

    def DrawEnemy(self):
        self.figur = pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.height))

    def Move(self):
        self.position += self.vector
        if self.figur.colliderect(self.waypoint1):
            self.vector.rotate_ip(90)
            self.position = (675 - self.width / 2, 227 - self.height / 2)
            self.waypoint1 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint2):
            self.vector.rotate_ip(90)
            self.position = (405 - self.width / 2, 227 - self.height / 2)
            self.waypoint2 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint3):
            self.vector.rotate_ip(-90)
            self.position = (405 - self.width / 2, 103 - self.height / 2)
            self.waypoint3 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint4):
            self.vector.rotate_ip(-90)
            self.position = (188 - self.width / 2, 103 - self.height / 2)
            self.waypoint4 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint5):
            self.vector.rotate_ip(-90)
            self.position = (188 - self.width / 2, 492 - self.height / 2)
            self.waypoint5 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint6):
            self.vector.rotate_ip(-90)
            self.position = (969 - self.width / 2, 492 - self.height / 2)
            self.waypoint6 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint7):
            self.vector.rotate_ip(90)
            self.position = (969 - self.width / 2, 204 - self.height / 2)
            self.waypoint7 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))

        if self.figur.colliderect(Finish):
            global killed
            killed = 5
            Player1.GetDammage(self.dammage)
            livingEnemys.remove(self)


class Tower:


    def __init__(self, number_targets, damage, range, fire_rate, price, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tower_rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50)
        self.targets_number = 0
        self.max_targets = number_targets
        self.target_enemy = Enemy(0, 0, 0, 0, 0)
        self.tower_shoting_range = pygame.Rect(self.x_pos - 125, self.y_pos - 125, 300, 300)
        livingTowers.append(self)

    def spwan(self):
        pygame.draw.rect(screen, (100, 50, 50), self.tower_rect, 0)
        tower_rohr_rect = pygame.Rect(self.tower_rect.centerx, self.tower_rect.centery - 5, 40, 10)
        pygame.draw.rect(screen, (100, 160, 100), tower_rohr_rect, 0)

    def detect(self):
        pygame.draw.rect(screen, (0, 0, 0), self.tower_shoting_range, 1)
        for self.enemy in livingEnemys:
            if self.enemy.figur.colliderect(self.tower_shoting_range) and self.targets_number <= self.max_targets:
                self.targets_number += 1
                self.target_enemy = self.enemy

    def shoot(self):
        if self.target_enemy.figur.colliderect(self.tower_shoting_range):
            pygame.draw.line(screen, (0, 0, 0), self.tower_rect.center, self.target_enemy.figur.center, 1)
        else:
            self.targets_number -= 1

Player1=Player(100)
Enemy1 = Enemy(6, 30, 30, 10, 1)
while True:
    if spawncounter == 20:
         Enemy1 = Enemy(6, 30, 30,10, 1)
         spawncounter = 0
         
    for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
        if event.type ==pygame.QUIT: 
             pygame.quit()
             sys.exit()#Spiel schließen
        if event.type ==pygame.QUIT: sys.exit()#Spiel schließen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # mausposition anzeigen
                archer = Tower(1, 2, 300, 5, 100, event.pos[0], event.pos[1])
                # print(pygame.mouse.get_pos())
    screen.blit(background, (0,0))
    for Enemys in livingEnemys:
         Enemys.Move()
         Enemys.DrawEnemy()
    for archer in livingTowers:
        archer.spwan()
        archer.detect()
        archer.shoot()
    draw()
    pygame.display.update()
    spawncounter += 1
    clock.tick(30)
