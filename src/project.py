import pygame
import objects

#TODO: Complete tasks within week timeframe
 # Week 1: Implement user input and basic gameplay
    #TODO: Create screen display and position placeholders
    #FOR WHEN YOU WAKE UP: Check out pygame documentation on sprites, create obstacle library, implement running bool
 # Week 2: Implement distance counter and animation function
 # Week 3: Implement obstacle destruction animation and menu
 
class Player(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        #Jump related variables
        

    def update(self, kb):
        for event in pygame.event.get():
            error = 0




        
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
    dt = 0
    ##Images
    background = pygame.image.load("forest.png")
    player = Player("marten.png", 100, 455)
    bush = objects.Bush("bush.png")
    ##Mechanics
    jumping = False
    y_velocity = 15
    on_ground = True

    #Game Loop
    while running == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        keys = pygame.key.get_pressed()
        #Checks if player is on ground before jumping
        if player.rect.y >= 455:
            on_ground = True
        elif player.rect.y < 455:
            on_ground = False
        else: #This line is in case the player goes past the ground
            player.rect.y = 455
            on_ground = True   

        if keys[pygame.K_SPACE]:
            jumping = True

        if jumping:
            player.rect.y -= y_velocity
            if y_velocity != -15:
                y_velocity -= 0.25

            if on_ground and y_velocity <= -15:
                jumping = False    
                y_velocity = 15
                player.rect.y = 455

        #Render and Display
        pygame.display.flip()
        screen.fill(color="black")
        screen.blit(background, (0, 0))
        screen.blit(player.image, player.rect)
        screen.blit(bush.image, bush.pos)
        bush.update()
        dt = clock.tick(24)


if __name__ == "__main__":
     main()