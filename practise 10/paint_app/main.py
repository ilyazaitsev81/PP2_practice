import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint app")

clock = pygame.time.Clock()

colors = [
    (0, 0, 0),       
    (255, 0, 0),     
    (0, 255, 0),     
    (0, 0, 255),     
]

current_color = colors[0]


mode = "draw"   

drawing = False
start_pos = None

screen.fill((255, 255, 255))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_color = colors[0]
            if event.key == pygame.K_2:
                current_color = colors[1]
            if event.key == pygame.K_3:
                current_color = colors[2]
            if event.key == pygame.K_4:
                current_color = colors[3]

            if event.key == pygame.K_e:
                mode = "erase"

            if event.key == pygame.K_d:
                mode = "draw"

            if event.key == pygame.K_r:
                mode = "rect"

            if event.key == pygame.K_c:
                mode = "circle"

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos   

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None        
            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)

            if mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

    
    if drawing and mode == "draw":
        current_pos = pygame.mouse.get_pos()
        if last_pos is not None:
            pygame.draw.line(screen, current_color, last_pos, current_pos, 5)
        last_pos = current_pos
    
    
    if drawing and mode == "erase":
        current_pos = pygame.mouse.get_pos()
        if last_pos is not None:
            pygame.draw.line(screen, (255, 255, 255), last_pos, current_pos, 10)
        last_pos = current_pos

    pygame.display.flip()

pygame.quit()