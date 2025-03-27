import pygame, sys

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

color = RED
clock = pygame.time.Clock()
FPS = 60

wl, wh = 1001, 601
screen = pygame.display.set_mode((wl, wh))
screen.fill(WHITE)

pen = "mouse"
last_event = None
pre, cur = None, None
pre_e, cur_e = None, None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pen = "mouse"
            if event.key == pygame.K_w:
                pen = "rectangle"
            if event.key == pygame.K_e:
                pen = "circle"
            if event.key == pygame.K_r:
                pen = "Eraser"
            
            if event.key == pygame.K_a:
                color = RED
            if event.key == pygame.K_s:
                color = GREEN
            if event.key == pygame.K_d:
                color = BLUE
            if event.key == pygame.K_f:
                color = BLACK
        
        if pen == "mouse":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
            if pre:
                pygame.draw.line(screen, color, pre, cur, 1)
                pre = cur
            if event.type == pygame.MOUSEBUTTONUP:
                pre = None
        
        if pen == "rectangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.line(screen, color, (x, y), (x1, y), 1)
                pygame.draw.line(screen, color, (x, y), (x, y1), 1)
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1)
                pygame.draw.line(screen, color, (x1, y), (x1, y1), 1)
                last_event = None
        
        if pen == "circle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.circle(screen, color, (((x + x1) // 2), ((y + y1) // 2)), abs((x1 - x) // 2))
                pygame.draw.circle(screen, WHITE, (((x + x1) // 2), ((y + y1) // 2)), abs((x1 - x) // 2) - 0.5)
                last_event = None
        
        if pen == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre_e = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur_e = pygame.mouse.get_pos()
            if pre_e:
                pygame.draw.line(screen, WHITE, pre_e, cur_e, 10)
                pre_e = cur_e
            if event.type == pygame.MOUSEBUTTONUP:
                pre_e = None
    
    clock.tick(FPS)
    pygame.display.flip()