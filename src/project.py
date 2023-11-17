import pygame

#TODO: Complete tasks within week timeframe
 # Week 1: Implement user input and basic gameplay
    #TODO: Create screen display and position placeholders
    #FOR WHEN YOU WAKE UP: Check out pygame documentation on sprites, create obstacle library, implement running bool
 # Week 2: Implement distance counter and animation function
 # Week 3: Implement obstacle destruction animation and menu

def main():
    #Runs game from here
    error_prevent = 1
    #Initialize Loop
    pygame.init()
    ##Screen and Display
    pygame.display.set_caption("The Pine's Blade")
    resolution = 1000, 800
    screen = pygame.display.set_mode(resolution)
    ##System
    running = True

    #Game Loop
    while running == True:
         for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   running = False
    #Render and Display
    screen.fill(color="black")

if __name__ == "__main__":
     main()