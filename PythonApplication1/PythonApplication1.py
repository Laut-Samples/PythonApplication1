from io import SEEK_SET
import pygame
import math
import random

# In the game loop...

# Generate a random number between 0 and 100
rand = random.randint(0, 100)

class Level:
    def __init__(self, number_of_enemies):
        self.number_of_enemies = number_of_enemies





# Define the Projectile class
class Projectile:
    def __init__(self, x, y,radius=5):
        self.x = x
        self.y = y
        self.speed = 10
        self.radius = radius  # add radius attribute
        self.image = pygame.image.load("firearrow.png")  # load projectile image
        self.timer = 0  # elapsed time since projectile was created
        self.delay = 1000  # delay before projectile disappears (milliseconds)
        self.created_time = pygame.time.get_ticks()  # time when projectile was created



    def update(self, projectiles):
    # Update the projectile's position
        
        self.speed = 10

        # Get the current time
        current_time = pygame.time.get_ticks()

        # Calculate the elapsed time
        self.timer = current_time - self.created_time

        # Check if the projectile has been on the screen for more than the delay
        if self.timer > self.delay:
            # Remove the projectile from the list
            projectiles.remove(self)



def start_game():
    # Initialize Pygame
    pygame.init()

    # Set up the display window
    screen = pygame.display.set_mode((400, 300))


    # Load the background image
    background_image = pygame.image.load("background.jpg")

    # Create a rect object for the background image
    background_rect = pygame.Rect(0, 0, 400, 300)  # (x, y, width, height)

    # Get the size of the game window
    game_width, game_height = screen.get_size()

    # Scale the background image to the size of the game window
    background_image = pygame.transform.scale(background_image, (game_width, game_height))


    # Load the player image
    player_image = pygame.image.load("player.png")

    class Player:
        def __init__(self, x, y, image, last_update_time=0):
            self.x = x
            self.y = y
            self.image = image
            self.shooting_delay = 250  # time between shots (milliseconds)
            self.last_shot_time = 0  # time when player last shot
            self.last_update_time = last_update_time
            self.width = 50
            self.height = 50


   

    # Create a player object
    player = Player(50, 50, player_image)

    # Set the player's movement speed
    speed = 5

    # Set a flag to track whether the image has been flipped
    image_flipped = False
    player_flipped = False


    ## Set the game window size
    #game_width = 600
    #game_height = 500

    class Enemy:
        def __init__(self, x, y, image, speed):
            self.x = x
            self.y = y
            self.image = image
            self.speed = 1
 

        def update(self, player):
        # Update the enemy's position based on the player's position
            if self.x < player.x:
                self.x += 1
            elif self.x > player.x:
                self.x -= 1
            if self.y < player.y:
                self.y += 1
            elif self.y > player.y:
                self.y -= 1


    # Load the enemy image
    enemy_image = pygame.image.load("enemy1.png")

    # Create an enemy object
    enemy = Enemy(200, 50, enemy_image, 1)

    # Add the enemy to the list of enemies
    enemies = [enemy]
    
    

    # Initialize a variable to store the minimum distance to an enemy
    min_distance = float('inf')

    # Create an empty list of enemies to remove
    enemies_to_remove = []

    # Enable key repeating
    pygame.key.set_repeat(50, 50)  # delay, interval (milliseconds)

    # Create a list to store the projectiles
    projectiles = []

    enemy_count = 0

    # Set the game start flag to False
    game_start = False

    

    # Create a game loop
    while True:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


   
        # Create a new level with 10 enemies and a background image
        level = Level(10)

        # Check if the space bar is being held down
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            # Check if this is the first frame that the space bar is being held down
            if not space_down:
                # Update the state of the space bar
                space_down = True
                last_space_down_time = pygame.time.get_ticks()
            else:
                # Get the current time
                current_time = pygame.time.get_ticks()

                # Check if the elapsed time since the player last shot is greater than the shooting delay
                if current_time - last_space_down_time > player.shooting_delay:
                    # Create a new projectile 2 pixels away from the player's position
                    projectile = Projectile(player.x + speed, player.y)

                    # Add the projectile to the list
                    projectiles.append(projectile)

                    # Update the time when the player last shot
                    last_space_down_time = current_time
        else:
            # Update the state of the space bar
            space_down = False

        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Get the current time
                current_time = pygame.time.get_ticks()

                # Check if the elapsed time since the player last shot is greater than the shooting delay
                if current_time - player.last_shot_time > player.shooting_delay:
                    # Create a new projectile 2 pixels away from the player's position
                    projectile = Projectile(player.x + speed, player.y)

                    # Add the projectile to the list
                    projectiles.append(projectile)

                    # Update the player's last shot time
                    player.last_shot_time = current_time


        # Limit the frame rate to 60 FPS
        clock = pygame.time.Clock()
        clock.tick(60)

            # Generate a random number between 0 and 100
        rand = random.randint(0, 100)

        # If the random number is greater than 95, create a new enemy
        if rand > 99 and enemy_count <= 10:
            # Generate a random position for the enemy
            x = random.randint(0, game_width - 50)  # 50 is the enemy's radius
            y = random.randint(0, game_width - 50)
            # Create a new enemy object
            enemy = Enemy(x, y, enemy_image, 1)
            # Add the enemy to the list of enemies
            enemies.append(enemy)
            enemy_count += 1

    
            
        # Check if the enemy has collided with the player
        if enemy.x < player.x + 50 and enemy.x + 50 > player.x and enemy.y < player.y + 50 and enemy.y + 50 > player.y:
            # The enemy has collided with the player, so handle the collision
            pass
   
        
    
        
        # Initialize a variable to store the position of the nearest enemy
        nearest_enemy = None

        # Iterate over the list of enemies
        for enemy in enemies:
        
            # Update the enemy's position
            # Calculate the distance between the enemy and the player
            dx = player.x - enemy.x
            dy = player.y - enemy.y
            # Calculate the angle between the enemy and the player
            angle = math.atan2(dy, dx)
            # Calculate the new enemy position based on the angle and movement speed
            enemy.x += enemy.speed * math.cos(angle)
            enemy.y += enemy.speed * math.sin(angle)

            # Calculate the distance between the enemy and the player
            distance = math.sqrt((enemy.x - player.x)**2 + (enemy.y - player.y)**2)

            # Update the nearest enemy if this enemy is closer to the player
            if distance < min_distance:
                min_distance = distance
                nearest_enemy = enemy

        

     

                # Keep the enemy within the   game window
        if enemy.x < 0:
            enemy.x = 0
        elif enemy.x > game_width - 50:  # 50 is the player's radius
            enemy.x = game_width - 50
        if enemy.y < 0:
            enemy.y = 0
        elif enemy.y > game_height - 50:  # 50 is the player's radius
            enemy.y = game_height - 50



        # Update the player's position (example code)
            # Check for arrow key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:                                                                                                         
                # Check if the image has already been flipped
                if not image_flipped:
                # Flip the image horizontally
                    player_image = pygame.transform.flip(player_image, True, False)
                # Update the flag
                    image_flipped = True
                # Update the player's x position
                player.x -= speed
            elif  event.key == pygame.K_LEFT & pygame.K_UP:
                player.x -= speed 
                player.y -= speed
                       

            if event.key == pygame.K_RIGHT:
                # Check if the image has already been flipped
                if image_flipped:
                # Flip the image horizontally
                    player_image = pygame.transform.flip(player_image, True, False)
                    # Update the flag
                    image_flipped = False
                    # Update the player's x position
                player.x += speed
            elif event.key == pygame.K_UP:
                player.y -= speed
            elif event.key == pygame.K_DOWN:           
                player.y += speed
         




            # Keep the player within the game window
        if player.x < 0:
            player.x = 0
        elif player.x > game_width - 50:  # 50 is the player's radius
            player.x = game_width - 50
        if player.y < 0:
            player.y = 0
        elif player.y > game_height - 50:  # 50 is the player's radius
            player.y = game_height - 50




            # Remove the enemies from the list
        for enemy in enemies_to_remove:
            try:
                enemies.remove(enemy)
            except ValueError:
                # Do nothing, because the enemy is not in the list
                pass


        if nearest_enemy is not None:
                # Iterate over the list of projectiles
            for projectile in projectiles:
                # Update the projectile's position
                for enemy in enemies:
                    projectile.speed = 1
                    # Calculate the distance between the projectile and the enemy
                    dx = enemy.x - projectile.x
                    dy = enemy.y - projectile.y
                    # Calculate the angle between the projectile and the enemy
                    angle = math.atan2(dy, dx)
                    # Calculate the new projectile position based on the angle and movement speed
                    projectile.x += projectile.speed * math.cos(angle)
                    projectile.y += projectile.speed * math.sin(angle)

                if nearest_enemy.x < projectile.x + 2 and nearest_enemy.x + 50 > projectile.x and nearest_enemy.y < projectile.y + 2 and nearest_enemy.y + 50 > projectile.y:
                    enemies_to_remove.append(nearest_enemy)
                    projectiles.remove(projectile)









        # Clear the screen
        screen.fill((0, 0, 0))  # fill with black



        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))


        
        # draw player 
        screen.blit(player_image, (player.x, player.y))
        

        # Iterate over the list of projectiles
        for projectile in projectiles:
            # Update the projectile
            projectile.update(projectiles)
            # Draw the projectile image on the screen
            screen.blit(projectile.image, (projectile.x, projectile.y))
      
            # Update the enemy positions
        for enemy in enemies:
            enemy.update(player)
            screen.blit(enemy.image, (enemy.x, enemy.y))




        # Update the display
        pygame.display.flip()



# Initialize Pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((400, 300))

# Load the start button image
start_button_image = pygame.image.load("button.png")

# Create a start button object
start_button = pygame.Rect(100, 100, 200, 50)  # x, y, width, height

# Set the game start flag to False
game_start = False


# Define the button dimensions and position
button_width = 100
button_height = 50
button_x = (screen.get_width() - button_width) / 2
button_y = (screen.get_height() - button_height) / 2

# Load the button image
start_button_image = pygame.image.load("button.png")

class start_button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image


    # Create a start button object
start_button = start_button(50, 50, 50, 50,start_button_image )


# Create a game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

           # Check for mouse click event
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        # Check for mouse clicks on the start button
        if start_button.x < mouse_x < start_button.x + start_button.image.get_width() and start_button.y < mouse_y < start_button.y + start_button.image.get_height():
            # Set the game start flag to True
            start_game()

    # Clear the screen
    screen.fill((0, 0, 0))  # fill with black

    # If the game start flag is False, draw the start button on the screen
    if not game_start:
            # Draw the start button image on the screen
        screen.blit(start_button.image, (start_button.x, start_button.y))
    # If the game start flag is True, proceed with the game logic
    else:
        # Update the game state
        pass
        
        # Draw the game objects
        pass
        
    # Update the display
    pygame.display.flip()







