import math

class DQNAgent:
    def __init__(self, action_space, state_space, snake_position, food_position):
        self.action_space = action_space
        self.state_space = state_space
        self.dist = math.sqrt((snake_position[0] - food_position[0])**2 + 
                              (snake_position[1] - food_position[1])**2)
        #self.model = DQN()
        
    def _get_obs(self, Snake, Food):
        food_dir = []
        food_y, snake_y = Food.FOOD_POSITION[1], Snake.SNAKE_POSITION[1]
        
        # Y coordinate decides UP and Down direction
        if food_y < snake_y:  
            food_dir = [1, 0]
        elif food_y > snake_y:
            food_dir = [0, 1]
        food_x, snake_x = Food.FOOD_POSITION[0], Snake.SNAKE_POSITION[0]
        
        # X coordinate decides UP and Down direction
        if food_x < snake_x:  
            food_dir = food_dir + [1, 0]
        elif food_x > snake_x:
            food_dir = food_dir + [0, 1]
        
        # Snake direction        
        obs_dir = []
        if Snake.DIRECTION == 'UP':
            obs_dir = [1, 0, 0, 0]
        elif Snake.DIRECTION == 'DOWN':
            obs_dir = [0, 1, 0, 0]
        elif Snake.DIRECTION == 'LEFT':
            obs_dir = [0, 0, 1, 0]
        elif Snake.DIRECTION == 'RIGHT':
            obs_dir = [0, 0, 0, 1]
        
        # Wall direction w.r.t snake    
        wall_dir = []
        if food_y < snake_y and food_x == snake_x:
            wall_dir = [0, 1, 1, 1]
        elif food_y > snake_y and food_x == snake_x:
            wall_dir = [1, 0, 1, 1]
        if food_x < snake_x and food_y == snake_y:
            wall_dir = [1, 1, 0, 1]
        elif food_x > snake_x and food_y == snake_y:
            wall_dir = [1, 1, 1, 0]
            
        return food_dir + obs_dir + wall_dir
        
    def evaluation(self, Snake, Food):
        score = 0
        curr_dist = math.sqrt((Snake.SNAKE_POSITION[0] - Food.FOOD_POSITION[0])**2 + 
                              (Snake.SNAKE_POSITION[1] - Food.FOOD_POSITION[1])**2)
                              
        if Snake.SNAKE_POSITION[0] == Food.FOOD_POSITION[0] and Snake.SNAKE_POSITION[1] == Food.FOOD_POSITION[1]:
            score = 10
            Food.FOOD_SPAWN = False
        else:
            Snake.SNAKE_BODY.pop()
        
        if self.dist >= curr_dist:
            score = 1
        else:
            score = -1
        self.dist = curr_dist
          
        return score
    
    def is_game_over(self, Snake, WINDOW_WIDTH, WINDOW_HEIGHT):
        # Game Over conditions
        if Snake.SNAKE_POSITION[0] < 0 or Snake.SNAKE_POSITION[0] > WINDOW_WIDTH-10:
            return True
            
        if Snake.SNAKE_POSITION[1] < 0 or Snake.SNAKE_POSITION[1] > WINDOW_HEIGHT-10:
            return True
            
        # Touching the snake body
        for block in Snake.SNAKE_BODY[1:]:
            if Snake.SNAKE_POSITION[0] == block[0] and Snake.SNAKE_POSITION[1] == block[1]:
                return True
        
        return False
        
    def _get_info(self):
        pass
        
    def action_perform(self, action, Snake):
        # Moving the snake
        if Snake.DIRECTION == action:
            Snake.SNAKE_POSITION[1] -= 20
        elif Snake.DIRECTION == action:
            Snake.SNAKE_POSITION[1] += 20
        elif Snake.DIRECTION == action:
            Snake.SNAKE_POSITION[0] -= 20
        elif Snake.DIRECTION == action:
            Snake.SNAKE_POSITION[0] += 20
            
        Snake.SNAKE_BODY.insert(0, list(Snake.SNAKE_POSITION))
