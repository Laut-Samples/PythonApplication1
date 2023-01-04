import pygame

class Player_Knight:
    def __init__(self, x, y, image, last_update_time=0, level = 1, score = 0, speed = 4):
        self.x = x
        self.y = y
        self.image = image
        self.shooting_delay = 500  # time between shots (milliseconds)
        self.last_shot_time = 0  # time when player last shot
        self.last_update_time = last_update_time
        self.width = 50
        self.height = 50
        self.level = level
        self.player_health = 2
        self.score = score
        self.speed = speed
        self.cast_on = False # cast projectile off = 0, on = 1
        self.bow_on = False
        self.knight_on = False


        self.idle = [pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f0.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f1.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f2.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f3.png"), (50,50)), 
                    pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f4.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_idle_anim_f5.png"), (50,50))]

        self.walkRight = [pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f0.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f1.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f2.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f3.png"), (50,50)), 
                            pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f4.png"), (50,50)), pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f5.png"), (50,50))]

        self.walkLeft = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f0.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f1.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f2.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f3.png"), (50,50)), True, False), 
                            pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f4.png"), (50,50)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("knight_run_anim_f5.png"), (50,50)), True, False)]


class Player_Bow:
    def __init__(self, x, y, image, last_update_time=0, level = 1, score = 0, speed = 4):
        self.x = x
        self.y = y
        self.image = image
        self.shooting_delay = 500  # time between shots (milliseconds)
        self.last_shot_time = 0  # time when player last shot
        self.last_update_time = last_update_time
        self.width = 100
        self.height = 75
        self.level = level
        self.player_health = 2
        self.score = score
        self.speed = speed
        self.cast_on = False # cast projectile off = 0, on = 1

        
        self.idle = [pygame.transform.smoothscale(pygame.image.load("adventurer-idle-00.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-idle-01.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-idle-02.png"), (100,75)) , pygame.transform.smoothscale(pygame.image.load("adventurer-idle-00.png"), (100,75)), 
                    pygame.transform.smoothscale(pygame.image.load("adventurer-idle-01.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-idle-02.png"), (100,75))]

        self.walkRight = [pygame.transform.smoothscale(pygame.image.load("adventurer-run-00.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-run-01.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-run-02.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-run-03.png"), (100,75)), 
                            pygame.transform.smoothscale(pygame.image.load("adventurer-run-04.png"), (100,75)), pygame.transform.smoothscale(pygame.image.load("adventurer-run-05.png"), (100,75))]

        self.walkLeft = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("adventurer-run-00.png"), (100,75)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("adventurer-run-01.png"), (100,75)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("adventurer-run-02.png"), (100,75)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("adventurer-run-03.png"), (100,75)), True, False), 
                            pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("adventurer-run-04.png"), (100,75)), True, False), pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("adventurer-run-05.png"), (100,75)), True, False)]



