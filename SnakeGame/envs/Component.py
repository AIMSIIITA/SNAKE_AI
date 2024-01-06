import random

class Snake:
    def __init__(self, position, color):
        self.SNAKE_POSITION = position
        self.SNAKE_BODY = [self.SNAKE_POSITION]
        self.BODY_LEN = 20
        self.SNAKE_COLOR = color
        self.DIRECTION = 'RIGHT'
        self.CHANGE_TO = self.DIRECTION
        
class Food:
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, color):
        self.FOOD_LEN = 20
        self.FOOD_POSITION = [random.randrange(1, (WINDOW_WIDTH//self.FOOD_LEN)) * self.FOOD_LEN, \
                              random.randrange(1, (WINDOW_HEIGHT//self.FOOD_LEN)) * self.FOOD_LEN]
        self.FOOD_COLOR = color
        self.FOOD_SPAWN = True
