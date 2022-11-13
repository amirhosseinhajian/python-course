def is_triangle(side_1, side_2, side_3):
    return False if side_1 + side_2 <= side_3 or side_1 + side_3 <= side_2 or side_2 + side_3 <= side_1 else True
