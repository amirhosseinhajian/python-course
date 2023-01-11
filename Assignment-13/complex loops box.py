import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110
BLUE = arcade.color.BLUE
RED = arcade.color.RED

arcade.open_window(400, 400, "Complex Loops - Box")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for row in range(10):
    color = RED if row % 2 == 0 else BLUE
    for column in range(10):
        arcade.draw_rectangle_filled(column * COLUMN_SPACING + LEFT_MARGIN, row * ROW_SPACING + BOTTOM_MARGIN, 10, 10, color, 45)
        color = RED if color == BLUE else BLUE
arcade.finish_render()
arcade.run()