import numpy as np
import pygame
import gymnasium
from gymnasium import spaces

screen_width = 500
screen_height = 700
    
class SnakeEnv(gymnasium.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}
    
    def __init__(self, render_mode=None):
        self.screen = pygame.display.set_mode((screen_width, screen_height)).fill((0,0,0))
        self.caption = pygame.display.set_caption("Snake Game")
        self.game_speed = 60
        #self.font = pygame.font.SysFont("Arial", 30)
        
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.MultiBinary(12)
        
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
        
        self.window = None
        self.clock = None
    
    def _get_obs(self):
        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.observation_space = state
        return tuple(state)
                    
    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)
        
        #del self.SnakeGame
        #self.SnakeGame = SnakeGame2D()
        
        observation = self._get_obs()
        #info = self._get_info()
        
        if self.render_mode == "human":
            self._render_frame()

        return observation, {}
        
    def step(self, action):
        pass
        
    def render(self, mode="human", close=False):
    	self.SnakeGame.view()
    	pass
    	
