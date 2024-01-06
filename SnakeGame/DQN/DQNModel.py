import math
import numpy as np
from keras.layers import Dense, Activation
from keras.models import Sequential, load_model
from keras.optimizers import Adam

from SnakeGame.utils.ExperienceBuffer import ReplayBuffer

class DQN:
    def __init__(self, gamma, alpha, batch_size, n_actions, input_dims):
        self.gamma = gamma
        self.alpha = alpha
        self.batch_size = batch_size
        self.layer1_dims = 128
        self.layer2_dims = 128
        self.dqn_model = self.build_dqn(alpha, n_actions, input_dims, self.layer1_dims, self.layer2_dims)
        self.dqn_target_model = self.build_dqn(alpha, n_actions, input_dims, self.layer1_dims, self.layer2_dims)
        
    def build_dqn(self, lr, n_actions, input_dims, fc1_dims, fc2_dims):
        model = Sequential([
                Dense(fc1_dims, input_shape=(input_dims,)),
                Activation('relu'),
                Dense(fc2_dims),
                Activation('relu'),
                Dense(n_actions)])
        model.compile(optimizer=Adam(learning_rate=lr), loss='mse')

        return model

class DQNAgent:
    def __init__(self, action_space, state_space, n_actions, n_states, snake_position, food_position, params):
        self.action_space = action_space
        self.state_space = state_space
        
        self.dist = math.sqrt((snake_position[0] - food_position[0])**2 + 
                              (snake_position[1] - food_position[1])**2)
                              
        self.learning_rate = params['alpha']
        self.gamma = params['gamma']
        self.epsilon = params['epsilon']
        self.epsilon_min = params['min_epsilon']
        self.epsilon_dec = params['epsilon_decay']
        self.batch_size = params['batch_size']
        self.mem_size = params['mem_size']
        
        self.memory = ReplayBuffer(self.mem_size, n_states, n_actions, discrete=True)
        self.DQN = DQN(self.gamma, self.learning_rate, self.batch_size, n_actions, n_states)
        
    def get_action(self, state):
        #state = state[np.newaxis, :]
        rand = np.random.random()
        
        if rand < self.epsilon:
            action = np.random.choice(self.action_space)
        else:
            actions = self.DQN.dqn_model.predict(state)
            action = np.argmax(actions)
        return action
        
    def action_perform(self, Snake):
        # Moving the snake
        if Snake.DIRECTION == 'UP':
            Snake.SNAKE_POSITION[1] -= 20
        elif Snake.DIRECTION == 'DOWN':
            Snake.SNAKE_POSITION[1] += 20
        elif Snake.DIRECTION == 'LEFT':
            Snake.SNAKE_POSITION[0] -= 20
        elif Snake.DIRECTION == 'RIGHT':
            Snake.SNAKE_POSITION[0] += 20
            
        Snake.SNAKE_BODY.insert(0, list(Snake.SNAKE_POSITION))
        
    def _get_obs(self, Snake, Food):
        food_dir = []
        food_y, snake_y = Food.FOOD_POSITION[1], Snake.SNAKE_POSITION[1]
        
        # Y coordinate decides UP and Down direction
        if food_y < snake_y:  
            food_dir = [1, 0]
        elif food_y > snake_y:
            food_dir = [0, 1] 
        else:
            food_dir = [0, 0]
        food_x, snake_x = Food.FOOD_POSITION[0], Snake.SNAKE_POSITION[0]
        
        # X coordinate decides UP and Down direction
        if food_x < snake_x:  
            food_dir = food_dir + [1, 0] 
        elif food_x > snake_x:
            food_dir = food_dir + [0, 1]
        else:
            food_dir = [0, 0]
            
        # Snake direction [UP, DOWN, LEFT, RIGHT]        
        obs_dir = []
        if Snake.DIRECTION == 'UP':
            obs_dir = [1, 0, 0, 0]
            #print('OBS Direction')  
        elif Snake.DIRECTION == 'DOWN':
            obs_dir = [0, 1, 0, 0]
            #print('OBS Direction')
        elif Snake.DIRECTION == 'LEFT':
            obs_dir = [0, 0, 1, 0]
            #print('OBS Direction')
        elif Snake.DIRECTION == 'RIGHT':
            obs_dir = [0, 0, 0, 1]
            #print('OBS Direction')
        
        # Wall direction w.r.t snake [UP, DOWN, LEFT, RIGHT]   
        wall_dir = []
        if food_y < snake_y:
            if food_x == snake_x:
                wall_dir = [0, 1, 1, 1]
            else:
                wall_dir = [1, 0, 0, 0]
            #print('Wall Direction')
        elif food_y > snake_y: 
            if food_x == snake_x:
                wall_dir = [1, 0, 1, 1]
            else:
                wall_dir = [0, 1, 0, 0]
            #print('Wall Direction')
        if food_x < snake_x:
            if food_y == snake_y:
                wall_dir = [1, 1, 0, 1]
            else:
                wall_dir = [0, 0, 1, 0]
            #print('Wall Direction')
        elif food_x > snake_x:
            if food_y == snake_y:
                wall_dir = [1, 1, 1, 0]
            else:
                wall_dir = [0, 0, 0, 1]
            #print('Wall Direction')
            
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
        
    def remember(self, state, action, reward, new_state, done):
        self.memory.store_transition(state, action, reward, new_state, done)
        
    def train_model(self):
        if self.memory.mem_cntr > self.DQN.batch_size:
            state, action, reward, state_, done = self.memory.sample_buffer(self.DQN.batch_size)
            
            action_values = np.array(self.action_space, dtype=np.int8)
            action_indices = np.dot(action, action_values)
            
            q_values = self.DQN.dqn_model.predict(state)
            predicted_Q_values = self.DQN.dqn_target_model.predict(state_)
            
            batch_index = np.arange(self.DQN.batch_size, dtype=np.int32)
