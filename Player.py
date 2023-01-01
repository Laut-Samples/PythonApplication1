class Player:
    def __init__(self, x, y, image, last_update_time=0, level = 1, score = 0, speed = 5):
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
