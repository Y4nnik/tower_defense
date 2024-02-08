import pygame
pygame.font.init() 
def draw_button(screen):
    smallfont = pygame.font.SysFont('Corbel',35) 
    text = smallfont.render('Restart' , True , (255,255,255)) 
    restart_button = pygame.Rect(400, 330, 271, 50)
    mouse = pygame.mouse.get_pos()
    if restart_button.collidepoint(mouse):
        pygame.draw.rect(screen, (155, 155, 155), restart_button, 0)
    else:
        pygame.draw.rect(screen, (0, 0, 0), restart_button, 0)
    screen.blit(text , (restart_button.x + 60, restart_button.y + 10))