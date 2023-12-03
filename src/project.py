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
        self.mask = pygame.mask.from_surface(self.img)
        self.mask_img = self.mask.to_surface() #This is really just for debug purposes
        self.rect.y = y #y position
        self.rect.x = x #x position (not actually that important)
        self.anim_cooldown = 1 #Makes frame change once every other second

    def _frame_loader(self):
        #Anim list guide: frames 0-7 running, frame 8 slide, frame 9 slash, frame 10 - 13 jumping 
        running_anim = 8
        jump_anim = 1
        animation_list = []
        for x in range(running_anim):
            animation_list.append(pygame.image.load(f"fp_run_{x}.png").convert_alpha())

        animation_list.append(pygame.image.load("fp_slide_1.png").convert_alpha())
        animation_list.append(pygame.image.load("fp_slash_1.png").convert_alpha())
        for x in range(10, 14):
            animation_list.append(pygame.image.load(f"fp_jump_{jump_anim}.png").convert_alpha())
            jump_anim += 1

        return animation_list    

    def update(self, sld, jmp, slsh, y_vel):
        sliding = sld
        jumping = jmp
        slashing = slsh
        if sliding:
            self.frame_num = 8
        elif slashing:
            self.frame_num = 9  
        elif jumping:
            if y_vel > 5:
                self.frame_num = 10
            elif y_vel > 0 and y_vel <= 5:
                self.frame_num = 11
            elif y_vel > -5 and y_vel <= 0:
                self.frame_num = 12
            else:
                self.frame_num = 13            
        else:    
            if self.anim_cooldown != 0:
                self.anim_cooldown -= 1
            else: 
                if self.frame_num < 7:
                    self.frame_num += 1
                else:
                    self.frame_num = 0
                self.anim_cooldown = 1    
 
        self.img = self.animation_list[self.frame_num]
        self.mask = pygame.mask.from_surface(self.img)
        self.mask_img = self.mask.to_surface()
        
        

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
            obstacle_type = random.randrange(1, 4)
            if obstacle_type == 1:
                self.bush_list.append(objects.Bush("fp_bush.png"))
                self.countdown = 120
                obstacle_type = 0
            elif obstacle_type == 2:
                self.web_list.append(objects.Web("fp_web.png"))
                self.countdown = 120
                obstacle_type = 0
            else:
                self.lumberjack_list.append(objects.Lumberjack("fp_lumberjack_1.png"))
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
    hitbox = pygame.Surface((100, 100))
    hb_pos = (500, 433)
    hb_rect = hitbox.get_rect()
    ##Images
    end_screen = pygame.image.load("fp_end_screen.png")
    player = Player(0, 487)
    slash_list = []
    mask_list = []
    slash_pos = (450, 400)
    for x in range(8):
        slash_list.append(pygame.image.load(f"fp_slash_bar_{x}.png").convert_alpha())
        mask_list.append(pygame.mask.from_surface(slash_list[x]))
    frame_num = 0
    ##Parallax
    front = [pygame.image.load("fp_parallax_bg_3.png").convert_alpha()]
    front_rect = [front[0].get_rect()]
    mid = [pygame.image.load("fp_parallax_bg_2.png").convert_alpha()]
    mid_rect = [mid[0].get_rect()]
    back = [pygame.image.load("fp_parallax_bg_1.png").convert_alpha()]
    back_rect = [back[0].get_rect()]
    front_vel = 10
    mid_vel = 5
    
    ##Mechanics
    jumping = False
    sliding = False
    slashing = False
    sld_cooldown = 96
    slsh_cooldown = 24
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

        if keys[pygame.K_DOWN]:
            sliding = True

        if keys[pygame.K_RIGHT]:
            slashing = True
        ##Player actions
        if sliding:
            if sld_cooldown != 0:
                sld_cooldown -= 1
                jumping = False
                player.rect.y = 654
            else:
                sliding = False
                sld_cooldown = 96
                player.rect.y = 486        

        if jumping:
            player.rect.y -= y_velocity * 1.5
            if y_velocity != -15:
                y_velocity -= 0.25

            if on_ground and y_velocity <= -15:
                jumping = False    
                y_velocity = 15
                player.rect.y = 487

        if slashing:
            if slsh_cooldown != 0:
                slsh_cooldown -= 1
                hitbox.fill("Red")
                player.rect.y = 409
            else:
                slashing = False
                slsh_cooldown = 24
                hitbox.fill("Black")
                player.rect.y = 486 

        
            
        ##Obstacle spawning
        manager.update(dt)
        if len(manager.bush_list) != 0:
            for x in manager.bush_list:
                if player.alive:
                    screen.blit(x.image, x.pos)
                
                #THIS WORKS
                if player.mask.overlap(x.mask, (x.pos[0] - player.rect.x, x.pos[1] - player.rect.y)):
                    player.alive = False
                x.update()
                if x.rect.right < 0:
                    manager.bush_list.pop(manager.bush_list.index(x))
                

        if len(manager.web_list) != 0:
            for x in manager.web_list:
                if player.alive:
                    screen.blit(x.image, x.pos)
                if player.mask.overlap(x.mask, (x.pos[0] - player.rect.x, x.pos[1] - player.rect.y)):
                    player.alive = False
                x.update()
                if x.rect.right < 0:
                    manager.web_list.pop(manager.web_list.index(x))

        if len(manager.lumberjack_list) != 0:
            for x in manager.lumberjack_list:
                if mask_list[frame_num].overlap(x.mask, (x.pos[0] - slash_pos[0], x.pos[1] - slash_pos[1])) and slashing:
                    manager.lumberjack_list.pop(manager.lumberjack_list.index(x))
                if player.alive:     
                    screen.blit(x.image, x.pos)
                if player.mask.overlap(x.mask, (x.pos[0] - player.rect.x, x.pos[1] - player.rect.y)):
                    player.alive = False
                x.update()
                if x.rect.right < 0:
                    manager.lumberjack_list.pop(manager.lumberjack_list.index(x))

        if player.anim_cooldown == 0:
            if frame_num < 7:
                frame_num += 1    
            else:
                frame_num = 0             

        ##Render and Display
        pygame.display.flip()
        screen.fill(color="black")
       
        screen.blit(back[0], back_rect[0])
        for x in mid_rect:
            if x.right == 1000:
                mid_rect.append(mid[0].get_rect(x=1000, y=0))
            if x.right <= 0:
                mid_rect.pop(mid_rect.index(x))   
            x.x -= mid_vel     
            screen.blit(mid[0], x)  
        for x in front_rect:
            if x.right == 1000:
                front_rect.append(front[0].get_rect(x=1000, y=0))
            if x.right <= 0:
                front_rect.pop(front_rect.index(x))   
            x.x -= front_vel     
            screen.blit(front[0], x)
            
          
            
        if player.alive:
            player.update(sliding, jumping, slashing, y_velocity)
            screen.blit(player.img, player.rect)
            screen.blit(slash_list[frame_num], slash_pos)
        else:
            screen.blit(end_screen, (0, 0))    
               
        dt = clock.tick(24)


if __name__ == "__main__":
     main()