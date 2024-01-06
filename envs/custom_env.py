import numpy as np
import gymnasium
from gymnasium import spaces


from SnakeGame.envs.Snakegame_2d import SnakeGame2D
    
class CustomEnv(gymnasium.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}
    
    def __init__(self, render_mode=None):
        self.SnakeGame = SnakeGame2D()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(0, 1, shape=(2,))
        
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
        
        self.window = None
        self.clock = None
                
    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)
        
        del self.SnakeGame
        self.SnakeGame = SnakeGame2D()
        
        observation = self._get_obs()
        info = self._get_info()
        
        if self.render_mode == "human":
            self._render_frame()

        return observation, info
        
    def step(self, action):
        pass
        
    def render(self, mode="human", close=False):
    	self.SnakeGame.view()
    	pass
    	
