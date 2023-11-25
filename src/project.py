import pygame
import objects

#TODO: Complete tasks within week timeframe
 # Week 1: Implement user input and basic gameplay
    #TODO: Create screen display and position placeholders
    #FOR WHEN YOU WAKE UP: Check out pygame documentation on sprites, create obstacle library, implement running bool
 # Week 2: Implement distance counter and animation function
 # Week 3: Implement obstacle destruction animation and menu
 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = False #Checks if player collided with anything
        self.animation_list = self._frame_loader()
        self.frame_num = 0
        self.img = self.animation_list[self.frame_num]
        self.rect = self.img.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.anim_cooldown = 1

    def _frame_loader(self):
        running_anim = 8
        animation_list = []
        for x in range(running_anim):
            animation_list.append(pygame.image.load(f"fp_run_{x}.png"))

         
        return animation_list    

        

    def update(self):
        if self.anim_cooldown != 0:
            self.anim_cooldown -= 1
        else: 
            if self.frame_num < 7:
                self.frame_num += 1
            else:
                self.frame_num = 0
            self.anim_cooldown = 1    
 
        self.img = self.animation_list[self.frame_num]
        #self.rect = self.img.get_rect(center=(self.rect.y, self.rect.x))


            




        
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
    player = Player(0, 487)
    bush = objects.Bush("bush.png")
    web = objects.Web("web.png")
    lumberjack = objects.Lumberjack("lumberjack.png")
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
        ##Jumping 
        #Checks if player is on ground before jumping
        if player.rect.y >= 487:
            on_ground = True
        elif player.rect.y < 487:
            on_ground = False
        else: #This line is in case the player goes past the ground
            player.rect.y = 487
            on_ground = True   

        if keys[pygame.K_UP]:
            jumping = True

        if jumping:
            player.rect.y -= y_velocity
            if y_velocity != -15:
                y_velocity -= 0.25

            if on_ground and y_velocity <= -15:
                jumping = False    
                y_velocity = 15
                player.rect.y = 487

        #Render and Display
        pygame.display.flip()
        screen.fill(color="black")
        screen.blit(background, (0, 0))
        screen.blit(player.img, player.rect)
        screen.blit(web.image, web.pos)
        web.update()
        player.update()
        dt = clock.tick(24)


if __name__ == "__main__":
     main()