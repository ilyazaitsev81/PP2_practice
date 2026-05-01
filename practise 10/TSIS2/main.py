import pygame
import datetime
from tools import draw_figure,Flood_fill
pygame.init()
WIDTH,HIGHT=800,600
PANEL_HIGHT=60
buttons = [
    (10, 10, 80, 40, 2),
    (100, 10, 80, 40, 5),
    (190, 10, 80, 40, 10)
]
screen= pygame.display.set_mode((WIDTH,HIGHT))
base_layer=pygame.Surface((WIDTH,HIGHT))
base_layer.fill((255,255,255))
screen.fill((255,255,255))
pygame.display.set_caption("drawing")
LMBpressed= False
thickness=5
currx=curry=0
prevx=prevy=0
COLOR_RED=(255,0,0)
COLOR_BLUE=(0,0,255)
COLOR_GREEN=(0,255,0)
COLOR_BLACK=(0,0,0)
curr_color=COLOR_BLACK
draw_mode="pen"
figures=["rect","circle","square","right triangle","equilateral triangle","rhombus","line"]
font=pygame.font.SysFont('Arial',26)
text_pos=(0,0)
text_input=""
button_clicked=False
clock=pygame.time.Clock()
running= True
while running:
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, PANEL_HIGHT))
    for bx, by, bw, bh, size in buttons:
        pygame.draw.rect(screen, (150, 150, 150), (bx, by, bw, bh))
        label = pygame.font.SysFont("Arial", 18).render(f"{size} px", True, (0, 0, 0))
        screen.blit(label, (bx + 15, by + 10))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            LMBpressed=True
            currx,curry=event.pos
            if draw_mode!="type":
                prevx,prevy=event.pos
            if not button_clicked and curry > PANEL_HIGHT:
                if draw_mode == "fill":
                    Flood_fill(screen, event.pos, curr_color)
            button_clicked=False
            for bx, by, bw, bh, size in buttons:
                if bx <= currx <= bx + bw and by <= curry <= by + bh:
                    thickness = size
                    button_clicked = True
        if event.type==pygame.MOUSEMOTION:
            if LMBpressed:
                currx,curry=event.pos  
                if draw_mode in figures:
                    screen.blit(base_layer,(0,0))
                    draw_figure(screen,curr_color,(prevx,prevy),(currx,curry),draw_mode,thickness)
        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            LMBpressed=False
            if draw_mode in figures:
                currx,curry=event.pos
                draw_figure(screen,curr_color,(prevx,prevy),(currx,curry),draw_mode,thickness)
            base_layer.blit(screen,(0,0))
        if event.type==pygame.KEYDOWN:
            if draw_mode=="type":
                if event.key==pygame.K_RETURN:
                    draw_mode="pen"
                    text_input=""
                elif event.key==pygame.K_ESCAPE:
                    screen.blit(base_layer,(0,0))
                    draw_mode="pen"
                    text_input=""
                elif event.key==pygame.K_BACKSPACE:
                    text_input=text_input[:-1]
                else:
                    text_input+=event.unicode
            else:
                if event.key==pygame.K_1:
                    thickness=5
                if event.key==pygame.K_2:
                    thickness=2
                if event.key==pygame.K_3:
                    thickness=10
                if event.key==pygame.K_4:
                    curr_color=COLOR_RED
                if event.key==pygame.K_5:
                    curr_color=COLOR_GREEN
                if event.key==pygame.K_6:
                    curr_color=COLOR_BLUE
                if event.key==pygame.K_7:
                    curr_color=COLOR_BLACK
                if event.key==pygame.K_e:
                    draw_mode="erase"
                if event.key==pygame.K_p:
                    draw_mode="pen"
                if event.key==pygame.K_r:
                    draw_mode="rect"
                if event.key==pygame.K_l:
                    draw_mode="line"
                if event.key==pygame.K_c:
                    draw_mode="circle"
                if event.key==pygame.K_t:
                    draw_mode="right triangle"
                if event.key==pygame.K_8:
                    draw_mode="equilateral triangle"
                if event.key==pygame.K_9:
                    draw_mode="rhombus"
                if event.key==pygame.K_f:
                    draw_mode="fill"
                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"canvas_{timestamp}.png"
                    pygame.image.save(screen, filename)
                if event.key == pygame.K_0:
                    draw_mode="type"
    if draw_mode=="pen":
        if LMBpressed:
            pygame.draw.line(screen,curr_color,(prevx,prevy),(currx,curry),thickness)
            prevx,prevy=currx,curry
    if draw_mode=="erase":
        if LMBpressed:
            pygame.draw.line(screen,(255,255,255),(prevx,prevy),(currx,curry),thickness)
            prevx,prevy=currx,curry
    if draw_mode=="type":
        screen.blit(base_layer,(0,0))
        text_surf=font.render(text_input,True,curr_color)
        screen.blit(text_surf,(prevx,prevy))

    pygame.display.flip()
    clock.tick(60)
        

pygame.quit()

