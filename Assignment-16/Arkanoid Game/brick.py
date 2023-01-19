import arcade

class Brick(arcade.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.center_x = x
        self.center_y = y
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        # arcade.draw