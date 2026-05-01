import pygame

def draw_figure(surface,color,start_pos,end_pos,figure_type,thickness):
    start_x,start_y=start_pos
    curr_x,curr_y=end_pos
    
    rect=pygame.Rect(
        min(start_x,curr_x),
        min(start_y,curr_y),
        abs(start_x-curr_x),
        abs(start_y-curr_y)
    )

    if figure_type=="rect":
        pygame.draw.rect(surface,color,rect,thickness)
    if figure_type=="line":
        pygame.draw.line(surface,color,start_pos,end_pos,thickness)
    if figure_type=="circle":
        radius = max(rect.width, rect.height) // 2
        center = (min(start_x, curr_x) + radius, min(start_y, curr_y) + radius)
        if radius > 0:
            pygame.draw.circle(surface, color, center, radius, thickness)
    if figure_type=="right triangle":
        points = [(start_x, start_y), (start_x, curr_y), (curr_x, curr_y)]
        if len(set(points)) > 2: 
            pygame.draw.polygon(surface, color, points, thickness)
    if figure_type=="equilateral triangle":
        mid_x = (start_x + curr_x) // 2
        points = [(mid_x, start_y), (start_x, curr_y), (curr_x, curr_y)]
        if len(set(points)) > 2:
            pygame.draw.polygon(surface, color, points, thickness)
    if figure_type=="rhombus":
        mid_x, mid_y = (start_x + curr_x) // 2, (start_y + curr_y) // 2
        points = [(mid_x, start_y), (curr_x, mid_y), (mid_x, curr_y), (start_x, mid_y)]
        if len(set(points)) > 2:
            pygame.draw.polygon(surface, color, points, thickness)
def Flood_fill(surface,start_pos,fill_color):
    target_color = surface.get_at(start_pos)
    
    if target_color == fill_color or start_pos[1]<60:
        return

    width, height = surface.get_size()
    pixels_to_fill = [start_pos]

    while pixels_to_fill:
        x, y = pixels_to_fill.pop()
        if 0 <= x < width and 60 <= y < height:
            if surface.get_at((x, y)) == target_color:
                surface.set_at((x, y), fill_color)
                
                pixels_to_fill.append((x + 1, y))
                pixels_to_fill.append((x - 1, y))
                pixels_to_fill.append((x, y + 1))
                pixels_to_fill.append((x, y - 1))