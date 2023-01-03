class Enemy_1:
    def __init__(self, x, y, image, health =2):
        self.x = x
        self.y = y
        self.image = image
        self.speed = 0.8
        self.counter = 0
        self.delay_counter = 0
        self.health = health
        self.width = 50
        self.height = 50

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
