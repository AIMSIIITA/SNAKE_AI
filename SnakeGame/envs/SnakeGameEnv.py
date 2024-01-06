from SnakeGame.envs.PyGame2D import Game_setup
from SnakeGame.envs.Component import Snake, Food
from SnakeGame.DQN.DQNModel import DQNAgent

import SnakeGame.utils.hyperparameters as hp

class SnakeGameEnv:
    def __init__(self, mode):
        self.game_env = Game_setup()
        self.mode = mode
        self.action_space = [x for x in range(4)]
        self.state_space = [x for x in range(12)]
        self.n_action = 4
        self.n_state = 12
        self.snake = Snake([100, 60], self.game_env.BLACK)
        self.food = Food(self.game_env.WINDOW_WIDTH, self.game_env.WINDOW_HEIGHT, self.game_env.GREEN)
        self.params = hp.get_hyperparameters()
        self.agent = DQNAgent(self.action_space, self.state_space, self.n_action, self.n_state, \
                              self.snake.SNAKE_POSITION, self.food.FOOD_POSITION, self.params)
        self.running = True
        
    def reset(self):
        self.snake = Snake([100, 60], self.game_env.BLACK)
        self.food = Food(self.game_env.WINDOW_WIDTH, self.game_env.WINDOW_HEIGHT, self.game_env.GREEN)
        
    def render(self):
        self.game_env.view(self.snake, self.food)
        
    def step(self, action):
        if action == 0: action = 'UP'
        elif action == 1: action = 'DOWN'
        elif action == 2: action = 'LEFT'
        elif action == 3: action = 'RIGHT'
        
        self.snake.DIRECTION = action
        self.agent.action_perform(self.snake)
        
        observation = self.agent._get_obs(self.snake, self.food)
        reward = self.agent.evaluation(self.snake, self.food)
        terminated = self.agent.is_game_over(self.snake, self.game_env.WINDOW_WIDTH, self.game_env.WINDOW_HEIGHT)
        info = self.agent._get_info()
        
        return observation, reward, terminated, False, {}
