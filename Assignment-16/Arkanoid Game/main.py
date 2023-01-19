import arcade
from rocket import Rocket
from brick import Brick
from ball import Ball

class Game(arcade.Window):
    def __init__(self):
        super().__init__(500, 500, "Arkanoid")
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.me  = Rocket(self.width//2, 40)
        self.number_of_bricks_per_line = 10
        self.space_between_each_brick_in_row = 1
        self.bricks_width = self.width//self.number_of_bricks_per_line - self.space_between_each_brick_in_row
        self.bricks_height = 20
        self.bricks = arcade.SpriteList()
        for i in range(self.number_of_bricks_per_line):
            self.bricks.append(Brick(i*(self.bricks_width+self.space_between_each_brick_in_row) + 25, 337, self.bricks_width, self.bricks_height, arcade.color.YELLOW_GREEN))
        for i in range(self.number_of_bricks_per_line):
            self.bricks.append(Brick(i*(self.bricks_width+self.space_between_each_brick_in_row) + 25, 358, self.bricks_width, self.bricks_height, arcade.color.ORANGE))
        for i in range(self.number_of_bricks_per_line):
            self.bricks.append(Brick(i*(self.bricks_width+self.space_between_each_brick_in_row) + 25, 379, self.bricks_width, self.bricks_height, arcade.color.RED))
        for i in range(self.number_of_bricks_per_line):
            self.bricks.append(Brick(i*(self.bricks_width+self.space_between_each_brick_in_row) + 25, 400, self.bricks_width, self.bricks_height, arcade.color.DARK_GRAY))
        self.ball = Ball(self.me.center_x, self.me.center_y+self.me.height)
        self.score = 0
        self.is_ball_moving = False
        self.heart = 3
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        for brick in self.bricks:
            brick.draw()
        self.ball.draw()
        arcade.draw_text(f"Score: {self.score}", 25, self.height-50, color=arcade.color.WHITE, font_size=14)
        for i in range(self.heart):
            arcade.draw_ellipse_filled(i*30+30 + i*6, 15, 33, 11, arcade.color.LIGHT_MOSS_GREEN)
        if self.heart < -1:
            arcade.draw_text("GAME OVER!", self.width//2-110, self.height//2, arcade.color.LEMON, 26)
        arcade.finish_render()
    
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.me.width//2 < x < self.width - self.me.width//2:
            if not self.is_ball_moving:
                self.me.center_x = x
                self.ball.center_x = x
            else:
                self.me.center_x = x
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT and self.me.center_x-self.me.speed > self.me.width//2:
            if not self.is_ball_moving:
                self.me.center_x -= self.me.speed
                self.ball.center_x -= self.me.speed
            else:
                self.me.center_x -= self.me.speed

        if symbol == arcade.key.RIGHT and self.me.center_x+self.me.speed < self.width-self.me.width//2:
            if not self.is_ball_moving:
                self.me.center_x += self.me.speed
                self.ball.center_x += self.me.speed
            else:
                self.me.center_x += self.me.speed

        if symbol == arcade.key.SPACE:
            self.me.to_knock(self.ball, self)
    
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.me.to_knock(self.ball, self)
        
    def on_update(self, delta_time: float):
        if self.is_ball_moving:
            self.ball.move()

        colision = arcade.check_for_collision_with_list(self.ball, self.bricks)
        if colision:
            self.ball.breaking(self, colision)
        
        if self.is_ball_moving and arcade.check_for_collision(self.ball, self.me):
            if(self.ball.center_y >= self.me.center_y):
                self.me.to_knock(self.ball, self)
        
        if self.ball.center_x < 5:
            self.ball.change_x = 1
        elif self.ball.center_x > self.width-5:
            self.ball.change_x = -1
        
        if self.ball.center_y < 0:
            self.heart -= 1
            if self.heart > -1:
                self.is_ball_moving = False
                self.ball.center_x = self.me.center_x
                self.ball.center_y = self.me.center_y + self.me.height

game = Game()
arcade.run()