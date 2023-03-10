#next steps:

# FIRST STEP 

##GAME##

#- items werden eher gedropped bei höheren leveln
#- high score 
#- score auf game over
#- hit counter
#- player eingabe und ingame speicher wer gerade spielt



### ENEMY####

# Lebensbalken 
# rückstoß bei treffer 

##CHARACKTER##

#- ausweichen  
#- dash zur seite spring - skill (level 5 + speed auf 10 
#- richtung schießen als lezttes geguckt
#- start waffel auswahl 
# spieler und enemys etwas kleiner 



### WAFFEN ##

# Pfeil und Bogen
# Blitze 


from Player_.Class_Player import Player_Knight
from Player_.Class_Player import Player_Bow



from Enemys.Enemy_1 import Enemy_1

from asyncio.windows_events import NULL
from cgi import print_arguments
from io import SEEK_SET
from turtle import update
import pygame
import math
import random
#from PythonApplication1 import player

# In the game loop...

# Generate a random number between 0 and 100
rand = random.randint(0, 100)

class Level:
    def __init__(self, number_of_enemies):
        self.number_of_enemies = number_of_enemies


class Avatar:
    def __init__(self):
        self.bow_on = 0
        self.knight_on = 1
         





# Create a player object


global avatar
avatar = Avatar()



#Goblin enemy type
goblin_walkRight = [pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f0.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f1.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f2.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f3.png"), (50,50)), 
             pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f4.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f5.png"), (50,50))]

goblin_walkLeft = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f0.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f1.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f2.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f3.png"), (50,50)), True, False), 
             pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f4.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("goblin_run_anim_f5.png"), (50,50)), True, False)]

#fireball_sprites
fb_sx=100
fb_sy=100
fireball = [pygame.transform.smoothscale(pygame.image.load("fb0.png"), (fb_sx,fb_sy)), pygame.transform.smoothscale(pygame.image.load("fb1.png"), (fb_sx,fb_sy)), pygame.transform.smoothscale(pygame.image.load("fb2.png"), (fb_sx,fb_sy)), pygame.transform.smoothscale(pygame.image.load("fb3.png"), (fb_sx,fb_sy)), 
             pygame.transform.smoothscale(pygame.image.load("fb4.png"), (fb_sx,fb_sy)), pygame.transform.smoothscale(pygame.image.load("fb5.png"), (fb_sx,fb_sy))]

fb_delay_counter = 0
#fb_counter
t_sx=50
t_sy=50
cast = [pygame.transform.scale(pygame.image.load("t0.png"), (t_sx,t_sy)), pygame.transform.scale(pygame.image.load("t1.png"), (t_sx,t_sy)), pygame.transform.scale(pygame.image.load("t2.png"), (t_sx,t_sy)), pygame.transform.scale(pygame.image.load("t3.png"), (t_sx,t_sy)), 
             pygame.transform.scale(pygame.image.load("t4.png"), (t_sx,t_sy)), pygame.transform.scale(pygame.image.load("t5.png"), (t_sx,t_sy))]





#kaitest        
# Define the Projectile class
class Projectile:
    def __init__(self, x, y,radius=50):
        self.x = x
        self.y = y
        self.speed = 7
        self.radius = radius  # add radius attribute
        self.image = pygame.transform.smoothscale(pygame.image.load("fb0.png"), (fb_sx,fb_sy))  # load projectile image
        self.timer = 0  # elapsed time since projectile was created
        self.delay = 1000  # delay before projectile disappears (milliseconds)
        self.created_time = pygame.time.get_ticks()  # time when projectile was created
        self.xdir = 0
        self.ydir = 0
        self.counter = 0 # sprite counter 0 to 5 updated in update()
        self.delay_counter = 0 # so counter doesnt update every timestep
        self.alpha = 0

    def update(self, projectiles):
    # Update the projectile's position
        #xdir,ydir are set in game loop for every created projectile
        #y direction is mirrored -1 => up, +1 => down
        self.x += self.xdir * self.speed 
        self.y += self.ydir * self.speed
        self.image = pygame.transform.rotate(fireball[self.counter], self.alpha)
        #if self.xdir == 0:
        #    if self.ydir == 0:
        #        self.x += self.speed # shoot right if idle position
        #        self.image = fireball[self.counter]
        #    elif self.ydir == -1:
        #        self.image = pygame.transform.rotate(fireball[self.counter], 90)
        #    elif self.ydir == 1:
        #        self.image = pygame.transform.rotate(fireball[self.counter], -90)
        #elif self.xdir == -1:
        #    if self.ydir == 0:
        #        self.image = pygame.transform.rotate(fireball[self.counter], 180)
        #    elif self.ydir == -1:
        #        self.image = pygame.transform.rotate(fireball[self.counter], 135)
        #    elif self.ydir == 1:
        #        self.image = pygame.transform.rotate(fireball[self.counter], 225)
        #elif self.xdir == 1:
        #    if self.ydir == 0:
        #        self.image = fireball[self.counter]
        #    elif self.ydir == -1:
        #        self.image = pygame.transform.rotate(fireball[self.counter], 45)
        #    elif self.ydir == 1:
        #        self.image = pygame.transform.rotate(fireball[self.counter], -45)
        #self.image = fireball[self.counter]
        self.delay_counter +=1
        if self.delay_counter >5: # number of timesteps between counter increase
            self.delay_counter =0
            self.counter +=1
        if self.counter > 5:
            self.counter = 0


        # Get the current time
        current_time = pygame.time.get_ticks()

        # Calculate the elapsed time
        self.timer = current_time - self.created_time

        # Check if the projectile has been on the screen for more than the delay
        if self.timer > self.delay:
            # Remove the projectile from the list
            projectiles.remove(self)


class Cast:
    def __init__(self, x, y, centerx, centery):
        self.x = x
        self.y = y
        self.freq = 20000 # timesteps until circle is complete
        self.dist = 100 # distance from projectile to player
        self.radius = 50
        #self.firedelay = 1000 # timesteps between two projectiles
        self.centerx = centerx
        self.centery = centery
        self.image = pygame.transform.scale(pygame.image.load("t0.png"), (t_sx,t_sy))  # load projectile image
        self.timer = 0  # elapsed time since projectile was created
        self.delay = 5000  # delay before projectile disappears (milliseconds)
        self.created_time = pygame.time.get_ticks()  # time when projectile was created
        #self.xdir = 1
        #self.ydir = 0
        self.counter = 0 # sprite counter 0 to 5 updated in update()
        self.delay_counter = 0 # so counter doesnt update every timestep
        self.counter_pos = 0

    def update(self, casts):
    # Update the casts's position
        #xdir,ydir are set in game loop for every created projectile
        #y direction is mirrored -1 => up, +1 => down
        self.x = self.centerx + self.dist * math.sin((self.counter_pos/self.freq)*360) + 30
        self.y = self.centery + self.dist * math.cos((self.counter_pos/self.freq)*360) + 20
        self.image = cast[self.counter]
        self.delay_counter +=1
        if self.delay_counter >50: # number of timesteps between counter increase
            self.delay_counter =0
            self.counter +=1
        if self.counter > 5:
            self.counter = 0
        
        self.counter_pos += 1
        if self.counter_pos > self.freq:
            self.counter_pos = 0


        #self.xdir = (1.0/(math.sqrt(((self.x - 20) - self.centerx)**2.0 + (self.y - self.centery)**2.0)))*((self.x - 20) - self.centerx)
        #self.ydir = (1.0)*math.sin(math.acos(self.xdir))


        # Get the current time
        current_time = pygame.time.get_ticks()

        # Calculate the elapsed time
        self.timer = current_time - self.created_time

        # Check if the projectile has been on the screen for more than the delay
        if self.timer > self.delay:
            # Remove the projectile from the list
            casts.remove(self)

# Set the game start flag to False
game_start = False





def start_game(player):


    # Initialize Pygame
    pygame.init()
    # Set the game window size
    game_width = 1200
    game_height = 800


    # Set the score needed to reach the next level
    level_up_score = 100



    # Set up the display window
    screen = pygame.display.set_mode((game_width, game_height))

        # Load the life points image
    life_points_image = pygame.image.load("life_points.png")


    # Load the background image
    background_image = pygame.image.load("background.jpg")

    # Create a rect object for the background image
    #background_rect = pygame.Rect(0, 0, 400, 300)  # (x, y, width, height)


    # Get the size of the game window
    #game_width, game_height = screen.get_size()
    background_width = game_width + 1000
    background_height = game_height + 1000

    # Scale the background image to the size of the game window
    background_image = pygame.transform.scale(background_image, (background_width, background_height))


    
    # Set a flag to track whether the image has been flipped
    #image_flipped = False
    #player_flipped = False



    # Load the enemy image
    enemy_image = pygame.image.load("goblin_idle_anim_f0.png")

    # Load the enemy spawn indicator image
    enemy_spawn_indicator_image = pygame.image.load("enemy_spawn_indicator.png")


    #enemy prototype for collision borders before any enemy is defined
    ref_enemy = Enemy_1(200, 50, enemy_image, 1)

    # Create an enemy object

    # Add the enemy to the list of enemies
    enemies = []


    # Create an empty list of enemies to remove
    enemies_to_remove = []

    # Enable key repeating
    pygame.key.set_repeat(50, 50)  # delay, interval (milliseconds)

    # Create a list to store the projectiles
    projectiles = []

    # Create a list to store the casts
    casts = []



    enemy_count = 0

    enemy_level = 25


    enemy_count_destroyed = 0
    
    # for automatic shooting
    last_space_down_time = 0

    last_cast_time = 0

    idle_counter = 0

    walk_counter = 0

    walk_delay_counter = 0

    # Set the game start flag to False
    global game_start 
    game_start = False


    # Set the game over flag
    global game_over 
    game_over = False

    # Create a game loop
    while True:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()

        





            # Check if the player's health is zero or below
        if player.player_health <= 0:

            game_over = True


        # Create a new level with 10 enemies and a background image
        level = Level(10)
                            # Generate a random number between 0 and 100
        rand = random.randint(0, 100)

        # If the random number is greater than 95, create a new enemy
        if rand > 95 and enemy_count <= enemy_level:
            # Generate a random position for the enemy
            #x = random.randint(50, game_width - background_width)  # 50 is the enemy's radius
            x = random.randint(0, game_width - (game_width - background_width) - ref_enemy.width)  # 50 is the enemy's radius
            y = random.randint(0, game_height - (game_height - background_height) - ref_enemy.height)
            
            
            # Draw the spawn indicator image
            # Create a new enemy object
            enemy = Enemy_1(x, y, enemy_image, 1)
                        # Clear the screen
            # Add the enemy to the list of enemies
            enemies.append(enemy)
            enemy_count += 1
           



        # Set startime for shooting (doesnt work without)
        if pygame.time.get_ticks() > 1:
            
             
             # Get the current time
             current_time = pygame.time.get_ticks()

             # Check if the elapsed time since the player last shot is greater than the shooting delay
             if current_time - last_space_down_time > player.shooting_delay:
                # Create a new projectile 2 pixels away from the player's position
                #projectile = Projectile(player.x - player.width/2.0, player.y - player.height/2.0)
                # Check player movement direction
                #for event in pygame.event.get():
                    #if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position
                    #mouse_x, mouse_y = pygame.mouse.get_pos() 
                    #keys = pygame.key.get_pressed()
                    mouse = pygame.mouse.get_pressed(num_buttons=5)[0]
                    #print(mouse)
                    if mouse == True:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            mouse_pos_display_x = mouse_x - game_width/2.0
                            mouse_pos_display_y = mouse_y - game_height/2.0
                            #print(mouse_pos_display_y)

                        #if event.type == pygame.MOUSEBUTTONDOWN:
                            projectile = Projectile(player.x - player.width/2.0, player.y - player.height/2.0)
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        # Get the mouse position
                            #mouse_x, mouse_y = pygame.mouse.get_pos() #
                            #mouse_x - game_width/2.0
                            #mouse_y + game_height/2.0
                             #= math.atan = (mouse_x - game_width/2.0)/(mouse_y + game_height/2.0)
                            alpha = math.atan2((mouse_x - game_width/2.0),(mouse_y - game_height/2.0)) # in -pi to pi radiant
                            projectile.alpha = (alpha * 360 / (2*math.pi)) - 90 # in -90 to 270 degree, fuer image rotation in update()
                            #print(alpha_degree)
                            projectile.xdir = (1.0)*math.sin(alpha)
                            projectile.ydir = (1.0)*math.cos(alpha)
                            #projectile.image = pygame.transform.rotate(projectile.image, alpha_degree)
                            # Check for mouse clicks on the start button
                            #if start_button.x < mouse_x < start_button.x + start_button.image.get_width() and start_button.y < mouse_y < start_button.y + start_button.image.get_height():
                                # Set the game start flag to True
                        #if event.type == pygame.KEYDOWN:
                        #keys = pygame.key.get_pressed()
                        #if keys[pygame.K_a]:     
                        #    projectile.xdir = -1
                            #projectile.image = pygame.transform.rotate(projectile.image, -135)
                        #if keys[pygame.K_d]:
                        #    projectile.xdir = 1
                            #projectile.image = pygame.transform.rotate(projectile.image, 45)
                        #if keys[pygame.K_w]:
                        #    projectile.ydir = -1
                            #projectile.image = pygame.transform.rotate(projectile.image, -225)
                        #if keys[pygame.K_s]:
                        #    projectile.ydir = 1
                            #projectile.image = pygame.transform.rotate(projectile.image, -45)
                        #if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                            #projectile.image = pygame.transform.rotate(projectile.image, 90)
                        #if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                            #projectile.image = pygame.transform.rotate(projectile.image, -90)
                        #if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                            #projectile.image = pygame.transform.rotate(projectile.image, 180)
                        # Add the projectile to the list
                            projectiles.append(projectile)

                            # Update the time when the player last shot
                            last_space_down_time = current_time
             if player.cast_on == True:
                 if current_time - last_cast_time > 4.0*player.shooting_delay:
                    cast = Cast(player.x - 20, player.y -20, player.x - 20, player.y - 20)
                    casts.append(cast)
                    last_cast_time = current_time
        

        # Limit the frame rate to 60 FPS
        clock = pygame.time.Clock()
        clock.tick(60)



    
            

   
        
    
        

            # Iterate over the list of enemies
        for enemy in enemies:
                # Check if the enemy has collided with the player
                if enemy.x > player.x - 0.7*enemy.width and enemy.x < player.x + 0.7*player.width and enemy.y > player.y - 0.6*enemy.height and enemy.y < player.y + 0.6*player.height:
                    # The enemy has collided with the player, so handle the collision
                    player.player_health -= 1
                # Update the enemy's position
                # Calculate the distance between the enemy and the player
                dx = player.x - enemy.x
                dy = player.y - enemy.y
                # Calculate the angle between the enemy and the player
                angle = math.atan2(dy, dx)
                # Calculate the new enemy position based on the angle and movement speed
                enemy.x += enemy.speed * math.cos(angle)
                enemy.y += enemy.speed * math.sin(angle)



                if math.cos(angle) < 0:
                    enemy.image = goblin_walkLeft[enemy.counter]
                else: 
                    enemy.image = goblin_walkRight[enemy.counter]
                enemy.delay_counter +=1
                if enemy.delay_counter >4:  # number of timesteps between counter increase
                    enemy.delay_counter = 0
                    enemy.counter += 1
                if enemy.counter > 5: # number of frames until animation reset
                    enemy.counter = 0 
                # Check if the enemy has been hit by a projectile
                for projectile in projectiles:
                    if enemy.x > projectile.x - enemy.width and enemy.x < projectile.x + projectile.radius and enemy.y > projectile.y - enemy.height and enemy.y < projectile.y + projectile.radius: # size of enemy hitbox: (dx,dy) = (50,50)
                        # The enemy has been hit by a projectile, so handle the collision
                        # Add the enemy to the list of enemies to remove
                        enemies_to_remove.append(enemy)
                        projectiles.remove(projectile)  # remove the projectile from the list
                        enemy.health -= 1
                for cast in casts:
                    if enemy.x > cast.x - enemy.width and enemy.x < cast.x + cast.radius and enemy.y > cast.y - enemy.height and enemy.y < cast.y + cast.radius: # size of enemy hitbox: (dx,dy) = (50,50)
                        # The enemy has been hit by a projectile, so handle the collision
                        # Add the enemy to the list of enemies to remove
                        enemies_to_remove.append(enemy)
                        casts.remove(cast)  # remove the projectile from the list
                        enemy.health -= 1


        

     #player.x > game_width - (game_width - background_width) - player.width

                # Keep the enemy within the   game window
        for enemy in enemies:
            if enemy.x < 0:
                enemy.x = 0
            elif enemy.x > game_width - (game_width - background_width) - enemy.width:  # 50 is the player's radius
                enemy.x = game_width - (game_width - background_width) - enemy.width
            elif enemy.x < 0:
                enemy.x = 0
            if enemy.y < 0:
                enemy.y = 0
            elif enemy.y > enemy.y > game_height - (game_height - background_height) - enemy.height:  # 50 is the player's radius
                enemy.y = enemy.y > game_height - (game_height - background_height) - enemy.height


        # Update the player's position (example code)
        # Check for arrow key presses
        #keys = pygame.key.get_pressed()

        
        #if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            player.image = player.walkRight[walk_counter]
            #player_image = pygame.transform.flip(player_image, True, False)
            walk_delay_counter +=1
            if walk_delay_counter >10:
                walk_delay_counter = 0
                walk_counter += 1
            if walk_counter > 5:
                walk_counter = 0
            # Update the player's x position
            #player.x += player.speed
            if (not keys[pygame.K_w] and (not keys[pygame.K_s])):
                player.x += player.speed
            if keys[pygame.K_w]:
                player.x += (1.0/math.sqrt(2.0))*player.speed
                player.y -= (1.0/math.sqrt(2.0))*player.speed
            if keys[pygame.K_s]:
                player.x += (1.0/math.sqrt(2.0))*player.speed
                player.y += (1.0/math.sqrt(2.0))*player.speed

        if keys[pygame.K_a]:
            player.image = player.walkLeft[walk_counter]
            #player_image = pygame.transform.flip(player_image, True, False)
            walk_delay_counter +=1
            if walk_delay_counter >10:
                walk_delay_counter = 0
                walk_counter += 1
            if walk_counter > 5:
                walk_counter = 0
            # Update the player's x position
            #player.x += player.speed
            if (not keys[pygame.K_w] and (not keys[pygame.K_s])):
                player.x -= player.speed
            if keys[pygame.K_w]:
                player.x -= (1.0/math.sqrt(2.0))*player.speed
                player.y -= (1.0/math.sqrt(2.0))*player.speed
            if keys[pygame.K_s]:
                player.x -= (1.0/math.sqrt(2.0))*player.speed
                player.y += (1.0/math.sqrt(2.0))*player.speed


        if keys[pygame.K_w] and ((not keys[pygame.K_a]) and (not keys[pygame.K_d])):
            player.image = player.walkRight[walk_counter]
            player.y -= player.speed
        #    player.image = walkRight[walk_counter]
            #player_image = pygame.transform.flip(player_image, True, False)
            walk_delay_counter +=1
            if walk_delay_counter >10:
                walk_delay_counter = 0
                walk_counter += 1
            if walk_counter > 5:
                walk_counter = 0

        #    player.y -= player.speed
        #if event.key == pygame.K_DOWN:
        if keys[pygame.K_s] and ((not keys[pygame.K_a]) and (not keys[pygame.K_d])):
            player.image = player.walkLeft[walk_counter]
            player.y += player.speed
        #if keys[pygame.K_DOWN]:   
        #    player.image = walkLeft[walk_counter]
            walk_delay_counter +=1
            if walk_delay_counter >10:
                walk_delay_counter = 0
                walk_counter += 1
            if walk_counter > 5:
                walk_counter = 0
        #    player.y += player.speed

        if ((not keys[pygame.K_s]) and (not keys[pygame.K_a]) and (not keys[pygame.K_d]) and (not keys[pygame.K_w])):
            player.image = player.idle[idle_counter]
            walk_delay_counter +=1
            if walk_delay_counter >10:
                walk_delay_counter = 0
                idle_counter += 1
            if idle_counter > 5:
                idle_counter = 0
            player.x = player.x
        #walk_delay_counter +=1
        #if walk_delay_counter >10:
        #    walk_delay_counter = 0
        #    walk_counter += 1
        #if walk_counter > 5:
        #    walk_counter = 0

        for cast in casts:
            cast.centerx = player.x - 20
            cast.centery = player.y - 20
         




            # Keep the player within the game window
        if player.x < 0:
            player.x = 0
        elif player.x > game_width - (game_width - background_width) - player.width:  # 50 is the player's radius
            player.x = game_width - (game_width - background_width) - player.width
        if player.y < 0:
            player.y = 0
        elif player.y > game_height - (game_height - background_height) - player.height:  # 50 is the player's radius
            player.y = game_height - (game_height - background_height) - player.height




            # Remove the enemies from the list
        for enemy in enemies_to_remove:
            if enemy.health <= 0:
                


                try:
                    enemies.remove(enemy)
                                    # Update the player's score
                    enemy_count_destroyed += 1
                    player.score += 10
                except ValueError:
                    # Do nothing, because the enemy is not in the list
                    pass

            # Check if the player has reached the next level
        if player.score >= level_up_score:
            enemy_level += 10
            # Increase the player's level by 1
            player.level += 1
            # Set the score needed to reach the next level
            level_up_score += 500
            # Update the display
                            # Set the font and font size
            

            pygame.display.update()

        # Clear the screen
        screen.fill((0, 0, 0))  # fill with black



        # Draw the background image on the screen
        #screen.blit(background_image, (0, 0))
        screen.blit(background_image, ((-1.0)*player.x + game_width/2.0, (-1.0)*player.y  + game_height/2.0))
        
        if player.level == 1:
            font = pygame.font.Font(None, 36)
            # Set the text to display
            text = "Level 1"
            # Render the text as an image
            text_image = font.render(text, True, (0, 0, 0))
            # Get the text image's rectangle
            text_rect = text_image.get_rect()
            # Set the position of the text image
            text_rect.topright = (790, 10)
            # Blit the text image to the screen
            screen.blit(text_image, text_rect)
            # Set the font and font size


        if player.level == 2:
            font = pygame.font.Font(None, 36)
            # Set the text to display
            text = "Level 2"
            # Render the text as an image
            text_image = font.render(text, True, (0, 0, 0))
            # Get the text image's rectangle
            text_rect = text_image.get_rect()
            # Set the position of the text image
            text_rect.topright = (790, 10)
            # Blit the text image to the screen
            screen.blit(text_image, text_rect)
            # Set the font and font size
            skilltree()


        if player.level == 3:
            font = pygame.font.Font(None, 36)
            # Set the text to display
            text = "Level 3"
            # Render the text as an image
            text_image = font.render(text, True, (0, 0, 0))
            # Get the text image's rectangle
            text_rect = text_image.get_rect()
            # Set the position of the text image
            text_rect.topright = (790, 10)
            # Blit the text image to the screen
            screen.blit(text_image, text_rect)
            # Set the font and font size


        font = pygame.font.Font(None, 36)
        # Set the text to display
        text = f"Score: {player.score}"
        # Render the text as an image
        text_image = font.render(text, True, (0, 0, 0))
        # Get the text image's rectangle
        text_rect = text_image.get_rect()
        # Set the position of the text image
        text_rect.topright = (400, 10)
        # Blit the text image to the screen
        screen.blit(text_image, text_rect)



        # draw player 
        #screen.blit(player.image, (player.x, player.y))
        screen.blit(player.image, (game_width/2.0, game_height/2.0))

        if player.player_health == 1:
            # Draw the first life points image
            screen.blit(life_points_image, (10, 10))

        if player.player_health == 2:
            # Draw the first life points image
            screen.blit(life_points_image, (10, 10))
            # Draw the first life points image
            screen.blit(life_points_image, (50, 10))

        if player.player_health == 3:
            # Draw the first life points image
            screen.blit(life_points_image, (10, 10))
            # Draw the first life points image
            screen.blit(life_points_image, (50, 10))
            # Draw the first life points image
            screen.blit(life_points_image, (90, 10))

        # Iterate over the list of projectiles
        for projectile in projectiles:
            # Update the projectile
            projectile.update(projectiles)
            # Draw the projectile image on the screen
            #screen.blit(background_image, (((-1.0)*player.x + game_width/2.0) - background_width/2.0, (((-1.0)*player.y  + game_height/2.0) - background_height/2.0)))
            #screen.blit(projectile.image, (((-1.0)*player.x + game_width/2.0) - background_width/2.0 + projectile.x, (((-1.0)*player.y  + game_height/2.0) - background_height/2.0) + projectile.y))
            #screen.blit(background_image, ((-1.0)*player.x + game_width/2.0, (-1.0)*player.y  + game_height/2.0))
            #screen.blit(projectile.image, (game_width/2.0 + projectile.x, game_height/2.0 + projectile.y))
            screen.blit(projectile.image, (game_width/2.0 + projectile.x - player.x, game_height/2.0 + projectile.y - player.y))
            #screen.blit(projectile.image, (game_width/2 + projectile.x, game_height/2 + projectile.y))
        # iterate over casts
        for cast in casts:
            # Update the cast
            cast.update(casts)
            # Draw the cast image on the screen
            screen.blit(cast.image, (game_width/2.0 + cast.x - player.x, game_height/2.0 + cast.y - player.y))

            # Update the enemy positions
        for enemy in enemies:
            enemy.update(player)
            screen.blit(enemy.image, (enemy.x + game_width/2.0 - player.x, enemy.y + game_height/2.0 - player.y))

            # Check if the game is over
        if player.player_health <= 0 :
            # The game is over, so draw the game over image
            # Set the game start flag to False
            game_start = False
            new_game()
           

        else:
            # The game is not over, so update the display
            pygame.display.flip()


        # Update the display
        pygame.display.flip()




# Set up the display window
screen = pygame.display.set_mode((500, 500))

# Load the start button image
start_button_image = pygame.image.load("button.png")

# Create a start button object
start_button = pygame.Rect(100, 100, 200, 50)  # x, y, width, height

# Define the button dimensions and position
button_width = 100
button_height = 50
button_x = (screen.get_width() - button_width) / 2
button_y = (screen.get_height() - button_height) / 2


class start_button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    # Create a start button object
start_button = start_button(50, 50, 50, 50,start_button_image )


def new_game():
    # Create a game loop
    while True:
    
            # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    # Check for mouse clicks on the start button
                    if start_button.x < mouse_x < start_button.x + start_button.image.get_width() and start_button.y < mouse_y < start_button.y + start_button.image.get_height():
                        # Set the game start flag to True
                        player.score = 0
                        player.level = 0
                        player.cast_on = False
                        player.speed = 5
                        player.player_health = 2
                        start_game()
            screen.fill((0, 0, 0))
            if not game_start:
                            # Check for mouse click event
                font = pygame.font.Font(None, 36)
                # Set the text to display
                text = f"Score: {player.score}"
                # Render the text as an image
                text_image = font.render(text, True, (0, 0, 0))
                # Get the text image's rectangle
                text_rect = text_image.get_rect()
                # Set the position of the text image
                text_rect.topright = (400, 10)
                # Blit the text image to the screen
                screen.blit(text_image, text_rect)
                # draw player 
                screen.blit(player.image, (player.x, player.y))
        
                    # Load the game over image
                game_over_image = pygame.image.load("game_over.png")
                

                # The game is over, so draw the game over image
                game_over_image = pygame.transform.scale(game_over_image, (800,800))
                screen.blit(game_over_image, (0, 0))

                       # Draw the start button image on the screen
                screen.blit(start_button.image, (start_button.x, start_button.y))

         
            else:
            
                # Update the game state
                pass
            
                # Draw the game objects
                pass
        
            # Update the display
            pygame.display.flip()

###### update button ###

# Load the update button image
update_button_image = pygame.image.load("update.png")
# Create a start button object
update_button = pygame.Rect(100, 100, 200, 50)  # x, y, width, height

class update_button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    # Create a update button object
update_button = update_button(250, 200, 50, 50,update_button_image )


###### chooice 1 ### 
# Load the update button image
update_button_choose_one_image = pygame.image.load("t5.png")
# Create a start button object
update_button_choose_one = pygame.Rect(250, 300, 200, 50)  # x, y, width, height

class update_button_choose_one:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    # Create a update button object
update_button_choose_one = update_button_choose_one(250, 300, 100, 100,update_button_choose_one_image )


###### chooice 2 ### 
# Load the update button image
update_button_choose_two_image = pygame.image.load("boots.png")
# Create a start button object
update_button_choose_two = pygame.Rect(250, 300, 200, 50)  # x, y, width, height

class update_button_choose_two:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    # Create a update button object
update_button_choose_two = update_button_choose_two(350, 300, 100, 100,update_button_choose_two_image )

###### chooice 3 ### 
# Load the update button image
update_button_choose_three_image = pygame.image.load("life_points.png")
# Create a start button object
update_button_choose_three = pygame.Rect(250, 300, 200, 50)  # x, y, width, height

class update_button_choose_three:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    # Create a update button object
update_button_choose_three = update_button_choose_three(450, 300, 100, 100,update_button_choose_three_image )






Buttons = [update_button_choose_one,update_button_choose_two]

def skilltree(): 
    screen = pygame.display.set_mode((500, 500))
    # Set the game window size
    game_width = 500
    game_height = 500



    choice_width = 100
    choice_height = 100
        # Load the background image
    update_background_image = pygame.image.load("Upgrade_Game_Background.png")
    # Create a game loop
    while True:
    
            # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                        # Get the mouse position
                            mouse_x, mouse_y = pygame.mouse.get_pos() 
                            # Check for mouse clicks on the start button
                            if update_button_choose_one.x < mouse_x < update_button_choose_one.x + update_button_choose_one.image.get_width() and update_button_choose_one.y < mouse_y < update_button_choose_one.y + update_button_choose_one.image.get_height():
                                # Set the game start flag to True
                                player.cast_on = True
                                start_game(player)
#skill 2
            if event.type == pygame.MOUSEBUTTONDOWN:
                        # Get the mouse position
                            mouse_x, mouse_y = pygame.mouse.get_pos() 
                            # Check for mouse clicks on the start button
                            if update_button_choose_two.x < mouse_x < update_button_choose_two.x + update_button_choose_two.image.get_width() and update_button_choose_two.y < mouse_y < update_button_choose_two.y + update_button_choose_two.image.get_height():
                                # Set the game start flag to True
                                player.speed += 5
                                start_game(player)
#skill 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                        # Get the mouse position
                            mouse_x, mouse_y = pygame.mouse.get_pos() 
                            # Check for mouse clicks on the start button
                            if update_button_choose_three.x < mouse_x < update_button_choose_three.x + update_button_choose_three.image.get_width() and update_button_choose_three.y < mouse_y < update_button_choose_three.y + update_button_choose_three.image.get_height():
                                # Set the game start flag to True
                                player.player_health += 1
                                start_game(player)


# Clear the screen

            screen.fill((0, 0, 0))  # fill with black
        # If the game start flag is False, draw the start button on the screen
            if not game_start:
                            # Check for mouse click event
                
                    # Load the game over image
                

               
                
        # Draw the background image on the screen
                screen.blit(update_background_image, (0, 0))
                       # Draw the start button image on the screen
                  # Scale the background image to the size of the game window
                update_background_image = pygame.transform.scale(update_background_image, (game_width, game_height))

                #screen.blit(start_button.image, (start_button.x, start_button.y))
                #screen.blit(update_button.image, (update_button.x, update_button.y))
                screen.blit(update_button_choose_one.image, (160, 220))
                screen.blit(update_button_choose_two.image, (220, 220))
                screen.blit(update_button_choose_three.image, (300, 220))
         
                

            else:
            
                # Update the game state
                pass
            
                # Draw the game objects
                pass
        
            # Update the display
            pygame.display.flip()



# Create the first game loop
while True:
    

    global player

    player3_image = pygame.transform.scale(pygame.image.load("adventurer-bow-01.png"), (90,70))
    # Create a player object
    player3 = Player_Bow(205, 200, player3_image) 
    start_background_image = pygame.image.load("Start_Game_Background.png")

    
                # Load the player image
    player2_image = pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f0.png"), (50,50))
    


    player2 = Player_Knight(160, 220, player2_image) 

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys.exit()
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    ###################################################<<<<<<<<<<<<<<<<<<<<<<------------  Player idle +1 wenn Mouse auf Charackter 
    start_time = 0

    if event.type == pygame.mouse.get_pos( player3.x < mouse_x < player3.x + player3.image.get_width() and player3.y <  mouse_y < player3.y + player3.image.get_height()):
        
        start_time = pygame.time.get_ticks()

        if start_time + pygame.time.get_ticks() -  start_time < 1000:
            
            while player3.idle <= 5:
                player3.idle +1

            player.idle = 0

        
          
            # Check for mouse click event
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Get the mouse position
        # Check for mouse clicks on the start button
        #if start_button.x < mouse_x < start_button.x + start_button.image.get_width() and start_button.y < mouse_y < start_button.y + start_button.image.get_height():
            # Set the game start flag to True
            #start_game()

        if player3.x < mouse_x < player3.x + player3.image.get_width() and player3.y <  mouse_y < player3.y + player3.image.get_height():
            
            player = Player_Bow(100, 75, player3_image) 
            start_game(player)

        if player2.x < mouse_x < player2.x + player2.image.get_width() and player2.y <  mouse_y < player2.y + player2.image.get_height():
            
            
            player = Player_Knight(100, 75, player2_image) 
            start_game(player)

    # Clear the screen
    screen.fill((0, 0, 0))  # fill with black

    # If the game start flag is False, draw the start button on the screen
    if not game_start:
                    # Draw the start button image on the screen
        screen.blit(start_button.image, (100, 50))
        screen.blit(start_background_image, (0, 0))
                       # Draw the start button image on the screen
                  # Scale the background image to the size of the game window
        start_background_image = pygame.transform.scale(start_background_image, (500, 500))

            # Load the player image
        screen.blit(player2.image, (160, 220))


        # draw player 
        #screen.blit(player.image, (player.x, player.y))
        screen.blit(player3.image, (205, 200))


    # If the game start flag is True, proceed with the game logic
    else:
        # Update the game state
        pass
        
        # Draw the game objects
        pass
        
    # Update the display
    pygame.display.flip()