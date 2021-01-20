import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 

pygame.init()
  
# Set width and height
size = (550, 425)
screen = pygame.display.set_mode(size)

# Images
background_image = pygame.image.load("back1.png").convert()

# Loop
done = False
clock = pygame.time.Clock()

# Rectangle
rect_x = 630
rect_y = 160
rect_change_y = 5
rect_width = 50
rect_length = 50
rect1_y = 420
rect1_change_y = -5

def draw_stick_figure(screen, x, y):
    
  pygame.draw.ellipse(screen, BLACK, [5+x,y,50,50], 0)
  pygame.draw.ellipse(screen, RED, [15+x,10+y,10,10], 0)
  pygame.draw.ellipse(screen, RED, [35+x,10+y,10,10], 0)

circle_x = 100
circle_y = 250
    
circle_x_speed = 25
circle_y_speed = 25
    

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            done = True

    # animation code
    if rect_y > 450 or rect_y < 160:
      rect_change_y = rect_change_y * -1
    
    if rect1_y > 450 or rect1_y < 160:
      rect1_change_y = rect1_change_y * -1

    rect_y += rect_change_y
    rect1_y += rect1_change_y

    screen.blit(background_image, [0, 0])
    pygame.draw.rect(background_image, WHITE, [rect_x, rect_y, rect_width, rect_length])

    pygame.draw.rect(background_image, RED, [rect_x, rect1_y, rect_width, rect_length])
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x_speed = -3
      elif event.key == pygame.K_RIGHT:
        x_speed = 3
      elif event.key == pygame.K_UP:
        y_speed = -3
      elif event.key == pygame.K_DOWN:
        y_speed = 3
 
    # User let up on a key
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_speed = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_speed = 0

    circle_x += circle_x_speed
    circle_y += circle_y_speed

    draw_stick_figure(screen, circle_x, circle_y)

    # locating curser 
    player_position = pygame.mouse.get_pos()
    player_x = player_position[0]
    player_y = player_position[1]

   # screen update
    pygame.display.flip()

    # limit to 20 frames per second
    clock.tick(20)

