from gymnasium.envs.registration import register

register(
    id='SnakeGame-v0',
    entry_point='SnakeGame.envs:SnakeEnv',
    max_episode_steps=2000,
)
