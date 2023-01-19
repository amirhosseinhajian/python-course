import arcade
import random

class Ball(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.radius = 7
        self.speed = 5
        self.change_x = 0
        self.change_y = 1
        self.width = 14
        self.height = 14
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
    
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def breaking(self, game, bricks):
        self.change_y = -self.change_y
        self.change_x = random.choice([1, -1, 0])

        for brick in bricks:
            if brick.color != arcade.color.DARK_GRAY:
                game.bricks.remove(brick)
                del brick
                game.score += 100