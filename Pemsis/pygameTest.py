import pygame

# Initializing Pygame
pygame.init()

# Initialing Color
color = (255,0,0)
colorCar = (0, 255, 0)
bgColor = (255,255,255)

# Initializing Object Sizes
carSize = 10
outerCircuitSize = 262
innerCircuitSize = 242

clock = pygame.time.Clock()
timer = 10
dt = 0

car_x = 175
car_y = 175

car1Init = car_x

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#        if (car_x < 425) and (car_y == 175):
#            car_x = car_x + 10
#        if (car_x == 425) and (car_y < 425):
#            car_y = car_y + 10
#        if (car_x > 175) and (car_y == 425):
#            car_x = car_x - 10
#        if (car_x == 175) and (car_y > 175):
#            car_y = car_y - 10
        
        
        
            
    # Initializing screen
    screen = pygame.display.set_mode((600,600))
    screen.fill(bgColor)
    
    pygame.draw.rect(screen, color, pygame.Rect(174, 174, outerCircuitSize, outerCircuitSize),  2)
    pygame.draw.rect(screen, color, pygame.Rect(184, 184, innerCircuitSize, innerCircuitSize),  2)
    
    car = pygame.draw.rect(screen, colorCar, pygame.Rect(car_x, car_y, carSize, carSize))
    car2 = pygame.draw.rect(screen, colorCar, pygame.Rect(car_x, car_y, carSize, carSize))
    
    dt = clock.tick(30) / 1000
    
    pygame.display.update()