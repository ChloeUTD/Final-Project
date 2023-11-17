import pygame

#TODO: Complete tasks within week timeframe
 # Week 1: Implement user input and basic gameplay
    #TODO: Create screen display and position placeholders
    #FOR WHEN YOU WAKE UP: Check out pygame documentation on sprites, create obstacle library, implement running bool
 # Week 2: Implement distance counter and animation function
 # Week 3: Implement obstacle destruction animation and menu
 

def main():
    #Runs game from here
    
    #Initialize Loop
    pygame.init()
    ##Screen and Display
    pygame.display.set_caption("The Pine's Blade")
    resolution = 1000, 800
    screen = pygame.display.set_mode(resolution)
    ##System
    running = True
    clock = pygame.time.Clock()
    ##Images
    background = pygame.image.load('forest.png')
    

    #Game Loop
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #Render and Display
        pygame.display.flip()
        screen.fill(color="black")
        screen.blit(background, (100, 100))
        clock.tick(24)


if __name__ == "__main__":
     main()