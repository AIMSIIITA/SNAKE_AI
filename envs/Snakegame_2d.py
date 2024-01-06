import pygame
import math
import sys
import numpy as np

screen_width = 500
screen_height = 700
    
class SnakeGame2D:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        #self.map = pygame.image.load('map.png')
        self.caption = pygame.display.set_caption("Snake Game")
        self.game_speed = 60
        self.font = pygame.font.SysFont("Arial", 30)

    def action(self, action):
        pass
         
    def evaluate(self):
        return 1000
        
    def is_done(self):
        pass
        
    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}
        
    def _get_info(self):
        return {"distance": np.linalg.norm(self._agent_location - self._target_location, ord=1)}
        info = {'a': 1}
        obs = [0, 0, 0, 0, 0]
        return (tuple(obs), info)

    def view(self):
    	# Display the game window and start play
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()
        self.clock.tick(self.game_speed)

