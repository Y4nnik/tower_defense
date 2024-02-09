import pygame
import math
import sys
import newenemy
from newenemy import Enemy

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
    pygame.draw.circle(screen, (255, 223, 0),(210,28), 15, width=0)
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
            livingEnemys.remove(self)
            global total_gold
            total_gold += 100
            self.pause = 1
    def GetSlowed(self, slow):
        if self.howMuchSlowed < 5:
            self.vector = self.vector * slow
            self.howMuchSlowed += 1

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
            self.image = pygame.transform.rotate(self.image, -90)
            self.position = (675 - self.width / 2, 227 - self.height / 2)
            self.waypoint1 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint2):
            self.vector.rotate_ip(90)
            self.image = pygame.transform.rotate(self.image, -90)
            self.position = (405 - self.width / 2, 227 - self.height / 2)
            self.waypoint2 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint3):
            self.vector.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (405 - self.width / 2, 103 - self.height / 2)
            self.waypoint3 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint4):
            self.vector.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (188 - self.width / 2, 103 - self.height / 2)
            self.waypoint4 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint5):
            self.vector.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (188 - self.width / 2, 492 - self.height / 2)
            self.waypoint5 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint6):
            self.vector.rotate_ip(-90)
            self.image = pygame.transform.rotate(self.image, 90)
            self.position = (969 - self.width / 2, 492 - self.height / 2)
            self.waypoint6 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))
        elif self.figur.colliderect(self.waypoint7):
            self.vector.rotate_ip(90)
            self.image = pygame.transform.rotate(self.image, -90)
            self.position = (969 - self.width / 2, 204 - self.height / 2)
            self.waypoint7 = pygame.draw.rect(screen, (0, 0, 0), (-10, -10, 1, 1))

        if self.figur.colliderect(Finish):
            global killed
            killed = 5
            Player1.GetDammage(self.dammage)
            livingEnemys.remove(self)


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
        self.upgrade_button1 = pygame.Rect(self.tower_shoting_range.centerx +50, self.tower_shoting_range.centery - 25, 100, 50)
        self.upgrade_button2 = pygame.Rect(self.tower_shoting_range.centerx -150, self.tower_shoting_range.centery - 25, 100, 50)

            

    def is_mouse_over(self):
        if self.tower_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and shop_open == False:
            self.selected = True
        
        elif pygame.mouse.get_pressed()[0] == 1 and not self.tower_rect.collidepoint(pygame.mouse.get_pos()) and not self.upgrade_button1.collidepoint(pygame.mouse.get_pos()) and not self.upgrade_button2.collidepoint(pygame.mouse.get_pos()):
            self.color = 100
            self.selected = False
            

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
                        pygame.draw.line(screen, (0, 255, 0), self.rect.center, self.enemy.figur.center, 6)
                        self.cooldown = self.fire_rate
                    if self.name == "slower":
                        pygame.draw.circle(screen, (0, 0, 255), self.rect.center, self.radius, 1)
                        self.radius += 15
                        if self.radius >= self.tower_shoting_range.width / 2:
                            self.radius = 0
                            self.cooldown = self.fire_rate

                    self.enemy.GetDammage(self.damage)
                else:
                    self.cooldown -= 1
            else:
                self.targets_number -= 1
                self.target_enemys.remove(self.enemy)
    def draw(self):
        self.tower_shoting_range = pygame.Rect(self.x_pos - self.range/2, self.y_pos - self.range/2, self.range, self.range)
        if self.selected == True:
            self.range_rect = pygame.Surface(( self.range, self.range))
            self.range_rect.set_alpha(94)
            self.range_rect.fill((0, 0, 0))
            screen.blit(self.range_rect, (self.tower_shoting_range.x, self.tower_shoting_range.y))
        if self.name == "archer":
            pygame.draw.rect(screen, (100, 50, 50), self.tower_rect, 0)
        if self.name == "canon":
            pygame.draw.rect(screen, (50, 100, 50), self.tower_rect, 0)
        if self.name == "slower":
            pygame.draw.rect(screen, (50, 50, 100), self.tower_rect, 0)
        if self.selected == True and pygame.key.get_pressed()[pygame.K_d] == 1:
            livingTowers.remove(self)

    def upgrade(self):
        global total_gold
        if self.selected == True:
            self.smallfont = pygame.font.SysFont('Corbel',15) 
            text1 = self.smallfont.render('Upgrade' , True , (255,255,255)) 
            text2 = self.smallfont.render('Upgrade2' , True , (255,255,255))
            mouse = pygame.mouse.get_pos()
            if self.upgrade_button1.collidepoint(mouse):
                pygame.draw.rect(screen, (155, 155, 155), self.upgrade_button1, 0)
                if pygame.mouse.get_pressed()[0] == 1 and total_gold >= 100:
                    self.range += 10
                    total_gold -= 100
            else:
                pygame.draw.rect(screen, (0, 0, 0), self.upgrade_button1, 0)
            if self.upgrade_button2.collidepoint(mouse):
                pygame.draw.rect(screen, (155, 155, 155), self.upgrade_button2, 0)
                if pygame.mouse.get_pressed()[0] == 1 and total_gold >= 150:
                   self.damage += 1
                   total_gold -= 150
            else:
                pygame.draw.rect(screen, (0, 0, 0), self.upgrade_button2, 0)
            screen.blit(text1 , (self.upgrade_button1.x, self.upgrade_button1.y))
            screen.blit(text2 , (self.upgrade_button2.x, self.upgrade_button2.y))

            
    def spwan(self):
        if self.name != "slower":
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
                self.enemy.GetSlowed(0.8)
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
            self.placement_indicator_rect = pygame.Rect(pygame.mouse.get_pos()[0] - 25, pygame.mouse.get_pos()[1] - 25, 50, 50)
            self.placement_range_indicator = pygame.Surface((300, 300))
            self.placement_range_indicator.set_alpha(127)
            self.placement_range_indicator.fill((0, 0, 0))
            screen.blit(self.placement_range_indicator, (pygame.mouse.get_pos()[0] - 150, pygame.mouse.get_pos()[1] - 150))               
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
            
        self.placement_range_indicator.set_alpha(127)
        self.placement_range_indicator.fill((0, 0, 0))
        height = self.placement_range_indicator.get_height()
        width = self.placement_range_indicator.get_width()
        screen.blit(self.placement_range_indicator, (pygame.mouse.get_pos()[0] - height/2, pygame.mouse.get_pos()[1] - width/2))               
        self.placement_indicator = pygame.Surface((50, 50))
        self.placement_indicator.set_alpha(127)
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
shop_open = False    
placement = False
placement_valid = True
cooldown = 0
checkprice = False
selected_tower = ""
price_to_check = 0
Tower_that_mouse_is_over = []
speed_button = pygame.Rect(10, 650, 50, 50)

game_state = "running"
while True:
    screen.blit(background, (0,0))
    if game_state == "game over":
        smallfont = pygame.font.SysFont('Corbel',35) 
        text = smallfont.render('Restart' , True , (255,255,255)) 
        restart_button = pygame.Rect(1010, 660, 271, 50)
        mouse = pygame.mouse.get_pos()
        if restart_button.collidepoint(mouse):
            pygame.draw.rect(screen, (155, 155, 155), restart_button, 0)
        else:
            pygame.draw.rect(screen, (0, 0, 0), restart_button, 0)
        screen.blit(text , (restart_button.x + 60, restart_button.y + 10))
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
            Player1=Player(1)
            shop = Shop()
            is_mouse_over_button = False
            is_mouse_over_archer = False
            is_mouse_over_canon = False
            is_mouse_over_slower = False
            shop_open = False    
            placement = False
            placement_valid = True
            cooldown = 0
            checkprice = False
            selected_tower = ""
            price_to_check = 0
            Tower_that_mouse_is_over = []
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
                        archer = Tower(1, 1, 300, 5, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "archer")
                    if selected_tower == "canon":
                        total_gold -= 150
                        canon = Tower(1, 4, 400, 20, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "canon")
                    if selected_tower == "slower":
                        total_gold -= 125
                        slower = Tower(1, 0, 250, 20, 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "slower")
                    placement = False
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
                    price_to_check = 150
                    checkprice = True
                if event.button == 1 and is_mouse_over_button == True and shop_open == True:
                    shop_open = False
                    cooldown = 10



        for Enemys in livingEnemys:
            Enemys.Move()
            Enemys.DrawEnemy()
        for archer in livingTowers:
            archer.draw()
            archer.shoot()
            archer.spwan()
            archer.detect()
            archer.is_mouse_over()
            archer.upgrade()
        if checkprice == True:
            game.check_price(price_to_check)
        if placement == True:
            game.placement_funktion()
        if shop_open == True:
            shop.draw()
            shop.draw_towers("Archer", "100", 1015, 255) 
            shop.draw_towers("Canon", "150", 1015, 255+80) 
            shop.draw_towers("Slower", "100", 1015, 255+160) 
        if cooldown > 0:
            cooldown -= 1
        if cooldown == 0:
            shop.check()
        shop.draw_button()

        draw()
        pygame.display.update()
        if spawncounter != 20: spawncounter += 1
    clock.tick(gamespeed)
