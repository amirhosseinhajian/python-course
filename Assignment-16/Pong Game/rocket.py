import arcade 

class Rocket(arcade.Sprite):
    def __init__(self, x, y, color, name):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = color
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.name = name
        self.speed = 4
        self.score = 0
    
    def move(self, ball, game):
        if self.center_y > ball.center_y:
            self.change_y = -1
        elif self.center_y < ball.center_y:
            self.change_y = 1
        if self.center_y < 60 and self.change_y == -1 or self.center_y > game.height - 60 and self.change_y == 1:
            ...
        else:
            self.center_y += self.change_y * self.speed
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)