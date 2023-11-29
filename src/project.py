import pygame
import objects
import random

#TODO: Complete tasks within week timeframe
 # Week 1: Implement user input and basic gameplay
    #TODO: Create screen display and position placeholders
    #FOR WHEN YOU WAKE UP: Check out pygame documentation on sprites, create obstacle library, implement running bool
 # Week 2: Implement distance counter and animation function
 # Week 3: Implement obstacle destruction animation and menu
 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True #Checks if player collided with anything
        self.animation_list = self._frame_loader() #Uses frame loader to get list of images
        self.frame_num = 0 #Where in animation list img currently is
        self.img = self.animation_list[self.frame_num] #Displays current frame
        self.rect = self.img.get_rect() #Grabs rectangle from img
        self.rect.y = y #y position
        self.rect.x = x #x position (not actually that important)
        self.anim_cooldown = 1 #Makes frame change once every other second

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
        

class ObstacleManager():
    def __init__(self):
        self.countdown = 120
        self.bush_list = []
        self.web_list = []
        self.lumberjack_list = []
        
    def update(self, dt):
        self.spawner()
       
    
    # New idea: Just have a countdown that counts down from 120 so it spawns every frame, when it hits zero it spawns YIPEE THIS ONE WORKS
    def spawner(self):
        
        if self.countdown < 0:
            obstacle_type = 1
            if obstacle_type == 1:
                self.bush_list.append(objects.Bush("bush.png"))
                self.countdown = 120
                obstacle_type = 0
        else:
            self.countdown -= 1        


            


        
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
    
    web = objects.Web("web.png")
    lumberjack = objects.Lumberjack("lumberjack.png")
    ##Mechanics
    jumping = False
    y_velocity = 15
    on_ground = True
    manager = ObstacleManager()

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

        ##Obstacle spawning
        manager.update(dt)
        if len(manager.bush_list) != 0:
            for x in manager.bush_list:
                screen.blit(x.image, x.pos)
                x.update()

        ##Render and Display
        pygame.display.flip()
        screen.fill(color="black")
        screen.blit(background, (0, 0))
        if player.alive:
            player.update()
            screen.blit(player.img, player.rect)
        screen.blit(web.image, web.pos)
        web.update()
        
        dt = clock.tick(24)


if __name__ == "__main__":
     main()