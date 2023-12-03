import pygame
# Needs a float variable that increases the y value by itself while taking away 0.1 of itself every frame. Once it becomes the negative value of its starting number
# it stops decreasing. It will automatically be reset once the player hits the floor and jumping = False. 
def main():
    pygame.init()
    resolution = 1000, 800
    screen = pygame.display.set_mode(resolution)
    ##System
    running = True
    clock = pygame.time.Clock()
    dt = 0
    player = pygame.image.load("fp_run_0.png").convert_alpha()
    player_rect = player.get_rect()
    #Relevant code
    player_mask = pygame.mask.from_surface(player)
    mask_image = player_mask.to_surface()
    
    player_rect.x = 100
    player_rect.y = 455
    
    jumping = False
    y_velocity = 15
    on_ground = True

    while running == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Relevant code
        keys = pygame.key.get_pressed()
        #Checks if player is on ground before jumping
        if player_rect.y >= 455:
            on_ground = True
        elif player_rect.y < 455:
            on_ground = False
        else: #This line is in case the player goes past the ground
            player_rect.y = 455
            on_ground = True   

        if keys[pygame.K_SPACE] and on_ground:
            jumping = True
            
        if jumping:
            player_rect.y -= y_velocity
            if y_velocity != -15:
                y_velocity -= 0.25

            if on_ground and y_velocity <= -15:
                jumping = False    
                y_velocity = 15
                player_rect.y = 455
            

        pygame.display.flip()
        screen.fill(color="black")
        screen.blit(player, player_rect)
        screen.blit(mask_image, (player_rect.x,player_rect.y))     
        dt = clock.tick(24)            
        

if __name__ == "__main__":
     main()                