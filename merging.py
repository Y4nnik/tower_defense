import pygame
import math
import sys
import newenemy
from newenemy import Enemy
import random
pygame.font.init() 
wave = 0 #Wellencounter
Wavelist = []
killed = 0 #für Herz bei tot von Enemy (Counter)

my_font = pygame.font.SysFont('Comic Sans MS', 30)#definiert Schriftart
vector = pygame.math.Vector2

background = pygame.image.load("images/backgroundimmage.png")
pentagon = pygame.image.load("images/fuenfeck.png")
brokenheart = pygame.image.load("images/damage.png")
heart = pygame.image.load("images/heart.png")
speedarrow = pygame.image.load("images/speedarrow.png")
doublespeedarrow = pygame.image.load("images/doublespeedarrow.png")
screen = pygame.display.set_mode([1290, 717])  # Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
Finish=pygame.draw.rect(screen, (0,0,0), (1287, 172, 1, 64))

livingEnemys = [] #darin werden lebende Gegner gesichert
spawncounter = 0 #zählt tics seit letztem spawn

def draw():
    wavetext = "Welle: " + str(wave)
    remainingEnemys = "Verbleibende Gegner: " + str(len(Wavelist)+len(livingEnemys))
    text_health = my_font.render(str(Player1.health), False, (0, 0, 0))
    text_remainingenemys = my_font.render(remainingEnemys, False, (0, 0, 0))
    text_wave = my_font.render(wavetext, False, (0, 0 ,0))
    text_surface_gold = my_font.render(str(total_gold), False, (0, 0, 0))
    screen.blit(text_surface_gold, (120,5))
    if total_gold >= 10000: pygame.draw.circle(screen, (255, 223, 0),(230,28), 15, width=0)
    else: pygame.draw.circle(screen, (255, 223, 0),(210,28), 15, width=0)
    if total_gold >= 100000: pygame.draw.circle(screen, (255, 223, 0),(250,28), 15, width=0)
    screen.blit(text_health, (10,5))
    screen.blit(text_wave, (260,5))
    screen.blit(text_remainingenemys, (770, 5))
    screen.blit(heart, (70, 10))
    pygame.draw.rect(screen, (40,40,40), (10, 650, 50, 50))
    if speedmode: screen.blit(doublespeedarrow, (10, 650))
    else: screen.blit(speedarrow, (10, 650))
        
    
    global killed
    if killed != 0: 
        screen.blit(brokenheart, (1252, 185))
        killed -= 1

livingTowers = []  # darin werden lebende Türme gesichert

angel = 90
tower_aiming_indicator_org = pygame.Surface((40, 10))
tower_aiming_indicator_org.set_colorkey((0, 0, 0))
tower_aiming_indicator_org.fill((100, 160, 100))
tower_aiming_indicator = tower_aiming_indicator_org.copy()
tower_aiming_indicator.set_colorkey((0, 0, 0))


total_gold = 1000


class Player:
    def __init__(self, Health):
        self.health = Health
    def GetDammage(self, damageTaken):
        self.health -= damageTaken
        if self.health <= 0: 
            global game_state
            game_state = "game over"


class Enemy:
    def __init__(self, speed, width, height, health, dammage, value, image):
        self.position = (676 - width / 2, 0 - height / 2)
        self.vector = vector(0, speed)
        self.width = width
        self.dammage=dammage
        self.pause=0
        self.basehealth = health
        self.height = height
        self.health = health
        self.value = value
        self.howMuchSlowed = 0
        self.meltcountdwon = 0
        self.org_vektor =  vector(0, speed)
        self.image = image
        #livingEnemys.append(self)
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
        if self.health <= 0 and self.pause == 0: 
            if self in livingEnemys: livingEnemys.remove(self)
            global total_gold
            total_gold += 100
            self.pause = 1
    def GetSlowed(self, slow):
        if self.howMuchSlowed < 5:
            self.vector = self.vector * slow
            self.howMuchSlowed += 1
        self.meltcountdwon = 0
    def melt(self):
        self.meltcountdwon += 1
        if self.meltcountdwon >= 50:
            if self.howMuchSlowed > 0:
                self.vector = self.org_vektor.copy()
            self.howMuchSlowed = 0
            self.meltcountdwon = 0
    def doDamage(self):
        Player1.GetDammage(self.dammage)

    def DrawEnemy(self):
        screen.blit(self.image, (self.position[0], self.position[1]))
        self.figur = pygame.Rect( (self.position[0], self.position[1], self.width, self.height))
        healthbar = self.health/self.basehealth*self.width
        pygame.draw.rect(screen, (210,15,2), (self.position[0], self.position[1]-4, self.width, 3))
        self.healthbar = pygame.draw.rect(screen, (75,219,27), (self.position[0], self.position[1]-4, healthbar, 3))


    def Move(self):
        self.position += self.vector
        if self.figur.colliderect(self.waypoint1):
            self.vector.rotate_ip(90)
            self.org_vektor.rotate_ip(90)
            self.image = pygame.transform.rotate(self.image, -90)
            self.position = (675 - self.width / 2, 227 - self.height / 2)
            self.waypoint1 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint2):
            self.vector.rotate_ip(90)
            self.org_vektor.rotate_ip(90)
            self.image = pygame.transform.rotate(self.image, -90)
            self.position = (405 - self.width / 2, 227 - self.height / 2)
            self.waypoint2 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint3):
            self.vector.rotate_ip(-90)
            self.org_vektor.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (405 - self.width / 2, 103 - self.height / 2)
            self.waypoint3 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint4):
            self.vector.rotate_ip(-90)
            self.org_vektor.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (188 - self.width / 2, 103 - self.height / 2)
            self.waypoint4 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint5):
            self.vector.rotate_ip(-90)
            self.org_vektor.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (188 - self.width / 2, 492 - self.height / 2)
            self.waypoint5 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint6):
            self.vector.rotate_ip(-90)
            self.org_vektor.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (969 - self.width / 2, 492 - self.height / 2)
            self.waypoint6 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint7):
            self.vector.rotate_ip(90)
            self.org_vektor.rotate_ip(90)
            self.image = pygame.transform.rotate(self.image, -90)
            self.position = (969 - self.width / 2, 204 - self.height / 2)
            self.waypoint7 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))

        if self.figur.colliderect(Finish):
            global killed
            killed = 5
            Player1.GetDammage(self.dammage)
            if self in livingEnemys: livingEnemys.remove(self)


class Shop:
    def draw_button(self):
        self.smallfont = pygame.font.SysFont('Corbel',35) 
        text = self.smallfont.render('open Shop' , True , (255,255,255)) 
        self.shop_button = pygame.Rect(1010, 660, 271, 50)
        mouse = pygame.mouse.get_pos()
        if self.shop_button.collidepoint(mouse):
            pygame.draw.rect(screen, (155, 155, 155), self.shop_button, 0)
        else:
            pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
        screen.blit(text , (self.shop_button.x + 60, self.shop_button.y + 10))
    def check(self):
        self.shop_button = pygame.Rect(1010, 660, 271, 50)
        mouse = pygame.mouse.get_pos()
        if self.shop_button.collidepoint(mouse):
            global is_mouse_over_button
            is_mouse_over_button = True
            global shop_open
            if pygame.mouse.get_pressed()[0] == 1:
                shop_open = True
                       
        else:
            is_mouse_over_button = False
    def draw(self):
        self.shop_rect = pygame.Surface((271, 410))
        self.shop_rect.set_alpha(127)
        self.shop_rect.fill((0, 0, 0))
        screen.blit(self.shop_rect, (1010, 250))
    
    def draw_towers(self, name, price, x, y):
        self.name = name
        self.font = pygame.font.SysFont('Corbel',30) 
        self.smallfont = pygame.font.SysFont('Corbel',20)
        text = self.font.render(self.name , True , (255,255,255)) 
        price_text = self.smallfont.render(price , True , (255,255,255))
        self.shop_button = pygame.Rect(x, y, 260, 70)
        mouse = pygame.mouse.get_pos()
        if self.shop_button.collidepoint(mouse):
            pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
            if self.name == "Archer":
                global is_mouse_over_archer
                is_mouse_over_archer = True
            if self.name == "Canon":
                global is_mouse_over_canon
                is_mouse_over_canon = True
            if self.name == "Slower":
                global is_mouse_over_slower
                is_mouse_over_slower = True
            if self.name == "Inferno":
                global is_mouse_over_inferno
                is_mouse_over_inferno = True
            if self.name == "Tesla":
                global is_mouse_over_tesla
                is_mouse_over_tesla = True
        elif self.shop_button.collidepoint(mouse) == False:
            if self.name == "Archer":
                if selected_tower == "archer":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
                is_mouse_over_archer = False
            if self.name == "Canon":
                if selected_tower == "canon":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
                is_mouse_over_canon = False
            if self.name == "Slower":
                if selected_tower == "slower":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
                is_mouse_over_slower = False
            if self.name == "Inferno":
                if selected_tower == "inferno":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
                is_mouse_over_inferno = False
            if self.name == "Tesla":
                if selected_tower == "tesla":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
                is_mouse_over_tesla = False
        else:
           if self.name == "Archer":
                if selected_tower == "archer":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
           if self.name == "Canon":
                if selected_tower == "canon":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
           if self.name == "Slower":
                if selected_tower == "slower":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
           if self.name == "Inferno":
                if selected_tower == "inferno":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
           if self.name == "Tesla":
                if selected_tower == "tesla":
                    pygame.draw.rect(screen, (68, 68, 68), self.shop_button, 0)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.shop_button, 0)
        screen.blit(text , (self.shop_button.x + 85, self.shop_button.y + 20))
        screen.blit(price_text , (self.shop_button.x + 200, self.shop_button.y + 50))
        pygame.draw.circle(screen, (255, 223, 0),(self.shop_button.x + 240, self.shop_button.y + 60) , 8, width=0)
        self.archer_rect = pygame.Rect(x+10, y+10, 50, 50) 
        pygame.draw.rect(screen, (100, 50, 50), self.archer_rect, 0)
        tower_rohr_rect = pygame.Rect(self.archer_rect.centerx, self.archer_rect.centery - 5, 40, 10)
        pygame.draw.rect(screen, (100, 160, 100), tower_rohr_rect, 0)

        
class Tower:


    def __init__(self, number_targets, damage, range, fire_rate, price, x_pos, y_pos, name):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.range = range
        self.name = name
        self.tower_rect = pygame.Rect(self.x_pos-25, self.y_pos-25, 50, 50)
        self.targets_number = 0
        self.max_targets = number_targets
        self.target_enemys = []
        self.angle = 0
        self.tower_shoting_range = pygame.Rect(self.x_pos - self.range/2, self.y_pos - self.range/2, self.range, self.range)
        livingTowers.append(self)
        self.rect = tower_aiming_indicator.get_rect()
        self.rect.center = (self.tower_rect.centerx, self.tower_rect.centery)
        self.new_image = pygame.transform.rotate(tower_aiming_indicator, self.angle * -180 / math.pi)
        self.cooldown = 0
        self.fire_rate = fire_rate
        self.damage = damage
        self.price = price
        self.radius = 0
        self.ice = 0
        self.selected = False
        self.upgrade_button1 = pygame.Rect(self.tower_rect.centerx+45, self.tower_rect.centery-75, 50, 50)
        self.upgrade_button2 = pygame.Rect(self.tower_rect.centerx-95, self.tower_rect.centery-75, 50, 50)
        self.slowAmount = 0.8
        self.laser_width = 2
        self.infernoincrease = 0.1
        self.upgrade1 = 0
        self.upgrade2 = 0
        self.crit_chance = 10
            

    def is_mouse_over(self):
        global number_selected_towers
        if self.tower_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and placement == False and number_selected_towers == 0 and selected_tower == "":
            move_tower = livingTowers.pop(livingTowers.index(self))
            livingTowers.append(move_tower)
            selected_towers.append(self)
            self.selected = True
            number_selected_towers += 1
        
        elif pygame.mouse.get_pressed()[0] == 1 and not self.tower_rect.collidepoint(pygame.mouse.get_pos()) and not self.upgrade_button1.collidepoint(pygame.mouse.get_pos()) and not self.upgrade_button2.collidepoint(pygame.mouse.get_pos()) and self.selected == True and number_selected_towers == 1:
            self.color = 100
            self.selected = False
            if self in selected_towers: selected_towers.remove(self)
            number_selected_towers -= 1
        if self.selected == True and pygame.key.get_pressed()[pygame.K_d] == 1:
            selected_towers.remove(self)
            number_selected_towers -= 1

    def shoot(self):
        for self.enemy in self.target_enemys:
            if self.enemy.figur.colliderect(self.tower_shoting_range) and self.enemy.health > 0:
                x = self.enemy.figur.centerx - self.tower_rect.centerx
                y = self.enemy.figur.centery - self.tower_rect.centery
                self.angle = math.atan2(y, x)
                if self.cooldown == 0:
                    if self.name == "archer":
                        pygame.draw.line(screen, (255, 0, 0), self.rect.center, self.enemy.figur.center, 2)
                        self.cooldown = self.fire_rate
                    if self.name == "canon":
                        crit_desicion = random.randint(1, 100)
                        if crit_desicion <= self.crit_chance:
                            self.enemy.GetDammage(self.damage * 2)
                            pygame.draw.line(screen, (255, 0, 0), self.rect.center, self.enemy.figur.center, 6)
                        else:
                            self.enemy.GetDammage(self.damage)
                            pygame.draw.line(screen, (0, 255, 0), self.rect.center, self.enemy.figur.center, 6)
                        self.cooldown = self.fire_rate
                    if self.name == "slower":
                        if self.enemy in melting_enemys:
                            melting_enemys.remove(self.enemy)
                        pygame.draw.circle(screen, (0, 0, 255), self.rect.center, self.radius, 1)
                        self.radius += 15
                        if self.radius >= self.tower_shoting_range.width / 2:
                            self.radius = 0
                            self.cooldown = self.fire_rate
                    if self.name == "inferno":
                        pygame.draw.line(screen, (255, 255, 0), self.rect.center, self.enemy.figur.center, int(self.laser_width))
                        self.damage += self.infernoincrease
                        self.cooldown = self.fire_rate
                        self.laser_width += self.infernoincrease
                    if self.name == "tesla":
                        pygame.draw.line(screen, (10, 10, 255), self.rect.center, self.enemy.figur.center, 2)
                        self.cooldown = self.fire_rate
                    if self.name != "canon":
                        self.enemy.GetDammage(self.damage)
                else:
                    self.cooldown -= 1
            else:
                self.targets_number -= 1
                if self.name == "inferno":
                    self.damage = 0.1
                    self.laser_width = 2
                if self.enemy in self.target_enemys: 
                    if self.name == "slower":
                        melting_enemys.append(self.enemy)
                    self.target_enemys.remove(self.enemy)

    def draw(self):
        self.tower_shoting_range = pygame.Rect(self.x_pos - self.range/2, self.y_pos - self.range/2, self.range, self.range)
        if self.name == "archer":
            pygame.draw.rect(screen, (100, 50, 50), self.tower_rect, 0)
        if self.name == "canon":
            pygame.draw.rect(screen, (50, 100, 50), self.tower_rect, 0)
        if self.name == "slower":
            pygame.draw.rect(screen, (50, 50, 100), self.tower_rect, 0)
        if self.name == "inferno":
            pygame.draw.rect(screen, (100, 100, 100), self.tower_rect, 0)
        if self.name == "tesla":
            pygame.draw.rect(screen, (200, 100, 100), self.tower_rect, 0)
        if self.selected == True and pygame.key.get_pressed()[pygame.K_d] == 1:
            if self in livingTowers: livingTowers.remove(self)
    def draw_if_select(self):
         if self.selected == True:
            self.range_rect = pygame.Surface(( self.range, self.range))
            self.range_rect.set_alpha(94)
            self.range_rect.fill((32, 208, 214))
            screen.blit(self.range_rect, (self.tower_shoting_range.x, self.tower_shoting_range.y))
            pygame.draw.rect(screen, (28, 159, 163), self.tower_shoting_range, 1)
            damage_icon_rect = pygame.Rect(self.tower_rect.x - 60, self.tower_rect.y + 60, 20, 20)
            global damage_icon
            damage_icon = pygame.transform.scale(damage_icon, (20, 20))
            screen.blit(damage_icon, damage_icon_rect)
            self.smallfont = pygame.font.SysFont('sans',20)
            if self.name == "inferno":
                self.damage = round(self.damage, 1)
            if self.name == "tesla":
                self.damage = round(self.damage, 2)
            damage_text = self.smallfont.render(str(self.damage), True, (255, 255, 255))
            screen.blit(damage_text, (damage_icon_rect.x + 25, damage_icon_rect.y-2))
            range_icon_rect = pygame.Rect(self.tower_rect.x, self.tower_rect.y + 60, 20, 20)
            global range_icon
            range_icon = pygame.transform.scale(range_icon, (20, 20))
            screen.blit(range_icon, range_icon_rect)
            range_text = self.smallfont.render(str(self.range), True, (255, 255, 255))
            screen.blit(range_text, (range_icon_rect.x + 30, range_icon_rect.y-2))
            if self.name == "archer":
                firerate_icon_rect = pygame.Rect(self.tower_rect.x + 70, self.tower_rect.y + 60, 20, 20)
                global firerate_icon
                screen.blit(firerate_icon, firerate_icon_rect)
                firerate_text = self.smallfont.render(str(self.fire_rate), True, (255, 255, 255))
                screen.blit(firerate_text, (firerate_icon_rect.x + 30, firerate_icon_rect.y-2))
            if self.name == "canon":
                crit_icon_rect = pygame.Rect(self.tower_rect.x + 70, self.tower_rect.y + 60, 20, 20)
                global crit_icon
                crit_icon = pygame.transform.scale(crit_icon, (20, 20))
                screen.blit(crit_icon, crit_icon_rect)
                crit_text = self.smallfont.render(str(self.crit_chance) + "%", True, (255, 255, 255))
                screen.blit(crit_text, (crit_icon_rect.x + 30, crit_icon_rect.y-2))
            if self.name == "slower":
                ice_icon_rect = pygame.Rect(self.tower_rect.x + 70, self.tower_rect.y + 60, 20, 20)
                global ice_icon
                ice_icon = pygame.transform.scale(ice_icon, (20, 20))
                screen.blit(ice_icon, ice_icon_rect)
                slowmow = -100 + self.slowAmount * 100
                slowmow = round(slowmow, 1)
                slowmow = int(slowmow)
                ice_text = self.smallfont.render(str(slowmow) + "%", True, (255, 255, 255))
                screen.blit(ice_text, (ice_icon_rect.x + 30, ice_icon_rect.y-2))
            if self.name == "inferno":
                inferno_icon_rect = pygame.Rect(self.tower_rect.x + 70, self.tower_rect.y + 60, 20, 20)
                global inferno_icon
                inferno_icon = pygame.transform.scale(inferno_icon, (20, 20))
                screen.blit(inferno_icon, inferno_icon_rect)
                self.infernoincrease = round(self.infernoincrease, 1)
                inferno_text = self.smallfont.render(str(self.infernoincrease), True, (255, 255, 255))
                screen.blit(inferno_text, (inferno_icon_rect.x + 30, inferno_icon_rect.y-2))
            if self.name == "tesla":
                number_targets_icon_rect = pygame.Rect(self.tower_rect.x + 70, self.tower_rect.y + 60, 20, 20)
                global number_targets_icon
                number_targets_icon = pygame.transform.scale(number_targets_icon, (20, 20))
                screen.blit(number_targets_icon, number_targets_icon_rect)
                number_targets_text = self.smallfont.render(str(self.max_targets), True, (255, 255, 255))
                screen.blit(number_targets_text, (number_targets_icon_rect.x + 30, number_targets_icon_rect.y-2))
    def upgrade(self):
        global total_gold
        global mouse_clicked
        if self in selected_towers:
            self.smallfont = pygame.font.SysFont('sans',15) 
            mouse = pygame.mouse.get_pos()
            pygame.draw.line(screen, (31, 216, 222), self.tower_rect.center, (self.tower_rect.centerx+70, self.tower_rect.centery), 1)
            pygame.draw.line(screen, (31, 216, 222), (self.tower_rect.centerx+70, self.tower_rect.centery), (self.tower_rect.centerx+70, self.tower_rect.centery-50), 1)
            pygame.draw.line(screen, (31, 216, 222), self.tower_rect.center, (self.tower_rect.centerx-70, self.tower_rect.centery), 1)
            pygame.draw.line(screen, (31, 216, 222), (self.tower_rect.centerx-70, self.tower_rect.centery), (self.tower_rect.centerx-70, self.tower_rect.centery-50), 1)
            if self.upgrade_button1.collidepoint(mouse):
                pygame.draw.rect(screen, (6, 108, 156), self.upgrade_button1, 0)
                if pygame.mouse.get_pressed()[0] == 1 and total_gold >= 100 and mouse_clicked == False and self.upgrade1 < 5:
                    self.upgrade1 += 1
                    if self.name == "archer":
                        self.fire_rate -= 1
                    if self.name == "canon":
                        self.damage += 1
                    if self.name == "slower":
                        self.fire_rate -= 1
                    if self.name == "inferno":
                        self.range += 10
                    if self.name == "tesla":
                        self.max_targets += 1
                    total_gold -= 100
                    mouse_clicked = True
                if pygame.mouse.get_pressed()[0] == 0 and mouse_clicked == True:
                    mouse_clicked = False
            else:
                pygame.draw.rect(screen, (3, 67, 97), self.upgrade_button1, 0)
            if self.upgrade_button2.collidepoint(mouse):
                pygame.draw.rect(screen, (6, 108, 156), self.upgrade_button2, 0)
                if pygame.mouse.get_pressed()[0] == 1 and total_gold >= 150 and mouse_clicked == False and self.upgrade2 < 5:
                    self.upgrade2 += 1
                    if self.name == "archer":
                        self.damage += 10
                    if self.name == "canon":
                        self.crit_chance += 10
                    if self.name == "slower":
                        self.slowAmount -= 0.05
                    if self.name == "inferno":
                        self.infernoincrease += 0.1
                    if self.name == "tesla":
                        self.damage += 0.05
                    total_gold -= 150
                    mouse_clicked = True
                if pygame.mouse.get_pressed()[0] == 0 and mouse_clicked == True:
                    mouse_clicked = False
            else:
                pygame.draw.rect(screen, (3, 67, 97), self.upgrade_button2, 0)
            global arrow_up_icon
            arrow_up_icon = pygame.transform.scale(arrow_up_icon, (20, 20))
            if self.name == "archer":
                screen.blit(firerate_icon, (self.tower_rect.centerx+50, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx+70, self.tower_rect.centery-71))
                price1_text = self.smallfont.render("100", True, (255, 255, 255))
                screen.blit(price1_text, (self.tower_rect.centerx+50, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx+84, self.tower_rect.centery-38) , 8, width=0)
                screen.blit(damage_icon, (self.tower_rect.centerx-90, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx-70, self.tower_rect.centery-71))
                price2_text = self.smallfont.render("150", True, (255, 255, 255))
                screen.blit(price2_text, (self.tower_rect.centerx-90, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx-56, self.tower_rect.centery-38) , 8, width=0)
            if self.name == "canon":
                screen.blit(damage_icon, (self.tower_rect.centerx+50, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx+70, self.tower_rect.centery-71))
                price1_text = self.smallfont.render("100", True, (255, 255, 255))
                screen.blit(price1_text, (self.tower_rect.centerx+50, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx+84, self.tower_rect.centery-38) , 8, width=0)
                screen.blit(crit_icon, (self.tower_rect.centerx-90, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx-70, self.tower_rect.centery-71))
                price2_text = self.smallfont.render("150", True, (255, 255, 255))
                screen.blit(price2_text, (self.tower_rect.centerx-90, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx-56, self.tower_rect.centery-38) , 8, width=0)
            if self.name == "slower":
                screen.blit(firerate_icon, (self.tower_rect.centerx+50, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx+70, self.tower_rect.centery-71))
                price1_text = self.smallfont.render("100", True, (255, 255, 255))
                screen.blit(price1_text, (self.tower_rect.centerx+50, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx+84, self.tower_rect.centery-38) , 8, width=0)
                screen.blit(ice_icon, (self.tower_rect.centerx-90, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx-70, self.tower_rect.centery-71))
                price2_text = self.smallfont.render("150", True, (255, 255, 255))
                screen.blit(price2_text, (self.tower_rect.centerx-90, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx-56, self.tower_rect.centery-38) , 8, width=0)
            if self.name == "inferno":
                screen.blit(range_icon, (self.tower_rect.centerx+50, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx+70, self.tower_rect.centery-71))
                price1_text = self.smallfont.render("100", True, (255, 255, 255))
                screen.blit(price1_text, (self.tower_rect.centerx+50, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx+84, self.tower_rect.centery-38) , 8, width=0)
                screen.blit(inferno_icon, (self.tower_rect.centerx-90, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx-70, self.tower_rect.centery-71))
                price2_text = self.smallfont.render("150", True, (255, 255, 255))
                screen.blit(price2_text, (self.tower_rect.centerx-90, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx-56, self.tower_rect.centery-38) , 8, width=0)
            if self.name == "tesla":
                screen.blit(number_targets_icon, (self.tower_rect.centerx+50, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx+70, self.tower_rect.centery-71))
                price1_text = self.smallfont.render("100", True, (255, 255, 255))
                screen.blit(price1_text, (self.tower_rect.centerx+50, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx+84, self.tower_rect.centery-38) , 8, width=0)
                screen.blit(damage_icon, (self.tower_rect.centerx-90, self.tower_rect.centery-70))
                screen.blit(arrow_up_icon, (self.tower_rect.centerx-70, self.tower_rect.centery-71))
                price2_text = self.smallfont.render("150", True, (255, 255, 255))
                screen.blit(price2_text, (self.tower_rect.centerx-90, self.tower_rect.centery-47))
                pygame.draw.circle(screen, (255, 223, 0),(self.tower_rect.centerx-56, self.tower_rect.centery-38) , 8, width=0)


            
    def spwan(self):
        if self.name != "slower" and self.name != "tesla":
            if self.targets_number == 0:
                screen.blit(self.new_image, self.rect)
            if self.targets_number == 1:
                old_center = self.rect.center
                self.new_image = pygame.transform.rotate(tower_aiming_indicator_org, self.angle * -180 / math.pi)
                self.rect = self.new_image.get_rect()
                self.rect.center = old_center
                screen.blit(self.new_image, self.rect)
                
    
    def detect(self):
        for self.enemy in livingEnemys:
            if self.enemy.figur.colliderect(self.tower_shoting_range) and self.targets_number < self.max_targets and self.enemy not in self.target_enemys:
                self.targets_number += 1
                self.target_enemys.append(self.enemy)
            if self.name == "slower" and self.enemy.figur.colliderect(self.tower_shoting_range) and self.ice == 0:
                self.enemy.GetSlowed(self.slowAmount)
        if self.ice == 0:
            self.ice = self.fire_rate
        if self.ice > 0:
            self.ice -= 1

                
class Game_funktions:
    def __init__(self):
        self.shop = pygame.Rect(1010, 250, 271, 410)
    def check_price(self, price):
        if total_gold >= price:
            global placement
            placement = True
        else:
            placement = False
            self.placement_indicator_rect = pygame.Rect(pygame.mouse.get_pos()[0] - 25, pygame.mouse.get_pos()[1] - 25, 50, 50)
            if selected_tower == "archer":
                self.placement_range_indicator = pygame.Surface((300, 300))
            if selected_tower == "canon":
                self.placement_range_indicator = pygame.Surface((400, 400))
            if selected_tower == "slower":
                self.placement_range_indicator = pygame.Surface((250, 250))
            if selected_tower == "inferno":
                self.placement_range_indicator = pygame.Surface((300, 300))
            if selected_tower == "tesla":
                self.placement_range_indicator = pygame.Surface((300, 300))
            self.placement_range_indicator.set_alpha(127)
            self.placement_range_indicator.fill((0, 0, 0))
            height = self.placement_range_indicator.get_height()
            width = self.placement_range_indicator.get_width()
            screen.blit(self.placement_range_indicator, (pygame.mouse.get_pos()[0] - height/2, pygame.mouse.get_pos()[1] - width/2))                
            self.placement_indicator = pygame.Surface((50, 50))
            self.placement_indicator.set_alpha(127)
            self.placement_indicator.fill((255, 0, 0))
            screen.blit(self.placement_indicator, (pygame.mouse.get_pos()[0] - 25, pygame.mouse.get_pos()[1] - 25))  
            
    def placement_funktion(self):
        self.placement_indicator_rect = pygame.Rect(pygame.mouse.get_pos()[0] - 25, pygame.mouse.get_pos()[1] - 25, 50, 50)
        if self.placement_indicator_rect.colliderect(self.shop):
            global placement_valid
            placement_valid = False
        else:
            placement_valid = True
        wayline1 = pygame.draw.line(screen, (64, 63, 63), (675, 0), (675, 226), 70)
        wayline2 = pygame.draw.line(screen, (64, 63, 63), (710, 225), (405, 225), 70)
        wayline3 = pygame.draw.line(screen, (64, 63, 63), (405, 260), (405, 107), 70)
        wayline4 = pygame.draw.line(screen, (64, 63, 63), (440, 108), (188, 108), 70)
        wayline5 = pygame.draw.line(screen, (64, 63, 63), (189, 74), (189, 492), 70)
        wayline6 = pygame.draw.line(screen, (64, 63, 63), (155, 490), (969, 490), 70)
        wayline7 = pygame.draw.line(screen, (64, 63, 63), (968, 525), (968, 204), 70)
        wayline8 = pygame.draw.line(screen, (64, 63, 63), (933, 205), (1290, 205), 70)
        
        
        
        for tower in livingTowers:
            if tower.tower_rect.colliderect(self.placement_indicator_rect):
                placement_valid = False 
                break
            else:
                if self.placement_indicator_rect.colliderect(self.shop):
                    placement_valid = False
                else:
                    placement_valid = True
        if selected_tower == "archer":
            self.placement_range_indicator = pygame.Surface((300, 300))
        if selected_tower == "canon":
            self.placement_range_indicator = pygame.Surface((400, 400))
        if selected_tower == "slower":
            self.placement_range_indicator = pygame.Surface((250, 250))
        if selected_tower == "inferno":
            self.placement_range_indicator = pygame.Surface((300, 300))
        if selected_tower == "tesla":
            self.placement_range_indicator = pygame.Surface((300, 300))
            
        self.placement_range_indicator.set_alpha(127)
        self.placement_range_indicator.fill((0, 0, 0))
        height = self.placement_range_indicator.get_height()
        width = self.placement_range_indicator.get_width()
        screen.blit(self.placement_range_indicator, (pygame.mouse.get_pos()[0] - height/2, pygame.mouse.get_pos()[1] - width/2))               
        self.placement_indicator = pygame.Surface((50, 50))
        self.placement_indicator.set_alpha(127)
        if wayline1.colliderect(self.placement_indicator_rect) or wayline2.colliderect(self.placement_indicator_rect) or wayline3.colliderect(self.placement_indicator_rect) or wayline4.colliderect(self.placement_indicator_rect) or wayline5.colliderect(self.placement_indicator_rect) or wayline6.colliderect(self.placement_indicator_rect) or wayline7.colliderect(self.placement_indicator_rect) or wayline8.colliderect(self.placement_indicator_rect):
            placement_valid = False
        if placement_valid == True:
            self.placement_indicator.fill((0, 255, 0))
        else:
            self.placement_indicator.fill((255, 0, 0))
        screen.blit(self.placement_indicator, (pygame.mouse.get_pos()[0] - 25, pygame.mouse.get_pos()[1] - 25))  
game = Game_funktions()
Player1=Player(100)
shop = Shop()
basespeed = 30
spawnsumme = 20
gamespeed = 30
speedmode = False
is_mouse_over_button = False
is_mouse_over_archer = False
is_mouse_over_canon = False
is_mouse_over_slower = False
is_mouse_over_inferno = False
is_mouse_over_tesla = False
shop_open = False    
placement = False
placement_valid = True
cooldown = 0
checkprice = False
selected_tower = ""
price_to_check = 0
Tower_that_mouse_is_over = []
speed_button = pygame.Rect(10, 650, 50, 50)
number_selected_towers = 0
mouse_clicked = False
game_state = "startMenu"
selected_towers = []
melting_enemys = []
damage_icon = pygame.image.load('images\Icon_damage.webp').convert_alpha()
range_icon = pygame.image.load('images/range_icon.png').convert_alpha()
firerate_icon = pygame.image.load('images/firerate_icon.svg').convert_alpha()
crit_icon = pygame.image.load('images\Icon_critical_damage.webp').convert_alpha()
ice_icon = pygame.image.load('images\ice_icon.png').convert_alpha()
inferno_icon = pygame.image.load('images\laser-icon.png').convert_alpha()
number_targets_icon = pygame.image.load('images/number_targets_icon.png').convert_alpha()
arrow_up_icon = pygame.image.load('images/arrow_up.png').convert_alpha()
firerate_icon = pygame.transform.scale(firerate_icon, (20, 20))
while True:
    screen.blit(background, (0,0))
    if game_state == "startMenu":
        start_menu = pygame.Rect(1290/2 - 250, 50, 500, 600)
        pygame.draw.rect(screen, (30, 30, 30), start_menu, 0)
        title_font = pygame.font.SysFont('Corbel',80)
        title = title_font.render('Star Defense' , True , (255,255,255))
        screen.blit(title , (1290/2 - 250 + 50, 100))
        smallfont = pygame.font.SysFont('Corbel',50) 
        text = smallfont.render('Start' , True , (255,255,255)) 
        start_button = pygame.Rect(1290/2 - 250 + 100, 300, 300, 75)
        mouse = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse):
            pygame.draw.rect(screen, (112, 169, 171), start_button, 0)
        else:
            pygame.draw.rect(screen, (55, 55, 55), start_button, 0)
        screen.blit(text , (start_button.x + 100, start_button.y + 15))
        if start_button.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
            game_state = "running"
        else:
            is_mouse_over_button = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT: 
                pygame.quit()
                sys.exit()


    if game_state == "game over":
        start_menu = pygame.Rect(1290/2 - 250, 50, 500, 600)
        pygame.draw.rect(screen, (30, 30, 30), start_menu, 0)
        title_font = pygame.font.SysFont('Corbel',80)
        title = title_font.render('Game Over' , True , (255,255,255))
        screen.blit(title , (1290/2 - 240 + 50, 100))
        smallfont = pygame.font.SysFont('Corbel',50) 
        text = smallfont.render('Restart' , True , (255,255,255)) 
        restart_button = pygame.Rect(1290/2 - 250 + 100, 350, 300, 75)
        mouse = pygame.mouse.get_pos()
        if restart_button.collidepoint(mouse):
            pygame.draw.rect(screen, (112, 169, 171), restart_button, 0)
        else:
            pygame.draw.rect(screen, (55, 55, 55), restart_button, 0)
        wave_text = smallfont.render('Wave: ' + str(wave) , True , (255,255,255))
        screen.blit(wave_text , (restart_button.x + 80, restart_button.y - 150))
        screen.blit(text , (restart_button.x + 80, restart_button.y + 15))

        if restart_button.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
            game_state = "running"
        else:
            is_mouse_over_button = False
        if restart_button.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
            game_state = "running"
            wave = 0
            spawnsumme = 20
            Wavelist = []
            killed = 0
            livingEnemys = []
            spawncounter = 0
            livingTowers = []
            total_gold = 1000
            Player1=Player(100)
            shop = Shop()
            is_mouse_over_button = False
            is_mouse_over_archer = False
            is_mouse_over_canon = False
            is_mouse_over_slower = False
            is_mouse_over_inferno = False
            is_mouse_over_tesla = False
            shop_open = False    
            placement = False
            placement_valid = True
            cooldown = 0
            checkprice = False
            selected_tower = ""
            price_to_check = 0
            Tower_that_mouse_is_over = []
            game_state = "running"
            selected_towers = []
            number_selected_towers = 0
            
                       
        else:
            is_mouse_over_button = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT: 
                pygame.quit()
                sys.exit()
    if game_state == "paused":
        start_menu = pygame.Rect(1290/2 - 250, 50, 500, 600)
        pygame.draw.rect(screen, (30, 30, 30), start_menu, 0)
        title_font = pygame.font.SysFont('Corbel',80)
        title = title_font.render('Pause' , True , (255,255,255))
        screen.blit(title , (1290/2- 100, 100))
        smallfont = pygame.font.SysFont('Corbel',50) 
        text = smallfont.render('Continue' , True , (255,255,255)) 
        start_button = pygame.Rect(1290/2 - 250 + 100, 300, 300, 75)
        mouse = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse):
            pygame.draw.rect(screen, (112, 169, 171), start_button, 0)
        else:
            pygame.draw.rect(screen, (55, 55, 55), start_button, 0)
        screen.blit(text , (start_button.x + 55, start_button.y + 15))
        if start_button.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
            game_state = "running"
        else:
            is_mouse_over_button = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
    if game_state == "running":
        if spawncounter >= spawnsumme:
            if len(Wavelist)==0 and len(livingEnemys)==0:
                wave += 1
                if wave % 10 == 0:
                    spawnsumme = spawnsumme *3/4
                savelist = []
                savelist = newenemy.newWave(wave)
                for enemys in savelist:
                    Wavelist.append(Enemy(enemys.speed, enemys.width, enemys.height, enemys.health, enemys.dammage, enemys.value, enemys.picture))
                
            if len(Wavelist)>0:
                livingEnemys.append(Wavelist[0])
                Wavelist.remove(Wavelist[0])
                
                spawncounter = 0    
                        
        for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
            if event.type ==pygame.QUIT: 
                pygame.quit()
                sys.exit()#Spiel schließen
            if event.type ==pygame.QUIT: sys.exit()#Spiel schließen
            if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
                game_state = "paused"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if speed_button.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    if speedmode:
                        speedmode = False
                        gamespeed=basespeed
                    else: 
                        speedmode = True
                        gamespeed = basespeed*3
                if event.button == 3:
                    placement = False
                    checkprice = False
                    selected_tower = ""
                if event.button == 1 and placement == True and placement_valid == True:
                    if selected_tower == "archer":
                        total_gold -= 100
                        archer = Tower(1, 1, 300, 7, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "archer")
                    if selected_tower == "canon":
                        total_gold -= 150
                        canon = Tower(1, 4, 400, 20, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "canon")
                    if selected_tower == "slower":
                        total_gold -= 125
                        slower = Tower(1, 0, 250, 20, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "slower")
                    if selected_tower == "inferno":
                        total_gold -= 200
                        inferno = Tower(1, 0.1, 300, 0, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "inferno")
                    if selected_tower == "tesla":
                        total_gold -= 175
                        tesla = Tower(3, 0.1, 300, 0, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "tesla")
                if event.button == 1 and is_mouse_over_archer == True:
                    selected_tower = "archer"
                    price_to_check = 100
                    checkprice = True
                if event.button == 1 and is_mouse_over_canon == True:
                    selected_tower = "canon"
                    price_to_check = 150
                    checkprice = True
                if event.button == 1 and is_mouse_over_slower == True:
                    selected_tower = "slower"
                    price_to_check = 125
                    checkprice = True
                if event.button == 1 and is_mouse_over_inferno == True:
                    selected_tower = "inferno"
                    price_to_check = 200
                    checkprice = True
                if event.button == 1 and is_mouse_over_tesla == True:
                    selected_tower = "tesla"
                    price_to_check = 175
                    checkprice = True
                if event.button == 1 and is_mouse_over_button == True and shop_open == True:
                    shop_open = False
                    cooldown = 10



        if placement == True:
            game.placement_funktion()
        for Enemys in livingEnemys:
            Enemys.Move()
            Enemys.DrawEnemy()
        for archer in livingTowers:
            archer.draw_if_select()
            archer.upgrade()
            archer.draw()
            archer.shoot()
            archer.spwan()
            archer.detect()
            archer.is_mouse_over()
        for Enemys in melting_enemys:
            Enemys.melt()
        if checkprice == True:
            game.check_price(price_to_check)
        if shop_open == True:
            shop.draw()
            shop.draw_towers("Archer", "100", 1015, 255) 
            shop.draw_towers("Canon", "150", 1015, 255+80) 
            shop.draw_towers("Slower", "125", 1015, 255+160) 
            shop.draw_towers("Inferno", "200", 1015, 255+240)
            shop.draw_towers("Tesla", "175", 1015, 255+320)
        if cooldown > 0:
            cooldown -= 1
        if cooldown == 0:
            shop.check()
        shop.draw_button()

        draw()
        pygame.display.update()
        if spawncounter != 20: spawncounter += 1
    clock.tick(gamespeed)
