import arcade

class Rocket(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = arcade.color.LIGHT_MOSS_GREEN
        self.width = 100
        self.height = 15
        self.center_x = x
        self.center_y = y
        self.speed = 40
    
    def draw(self,):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.width, self.height, self.color)
    
    def to_knock(self, ball, game):
        ball.change_y = 1
        if not game.is_ball_moving:
            ball.change_x = 0
            game.is_ball_moving = True
        elif self.center_x < ball.center_x <= self.center_x + self.width//2:
            ball.change_x = 1
        else:
            ball.change_x = -1 
