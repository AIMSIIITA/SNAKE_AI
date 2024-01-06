from SnakeGame.envs.SnakeGameEnv import SnakeGameEnv
rewards=[]
scores=[]
import matplotlib.pyplot as plt
def main():
    SnakeGame = SnakeGameEnv(mode='agent')
    MAX_EPISODES = 5
    
    while SnakeGame.running:
        SnakeGame.game_env.event_on_game_window(SnakeGame)
        if SnakeGame.mode == 'agent':
            for episode in range(MAX_EPISODES):
                state = SnakeGame.reset()
                step, total_reward, score, done = 0, 0, 0, False
                
                while step < 50:
                    action = SnakeGame.agent.get_action(state)
                    state_, reward, terminate, truncate, info = SnakeGame.step(action)
                    done = terminate or truncate
                    print(state, action, state_, reward, done)
                    SnakeGame.agent.remember(state, action, reward, state_, done)
                    score += reward
                    rewards.append(reward)
                    scores.append(score)

                    state = state_
                    SnakeGame.agent.train_model()
                    SnakeGame.render()
                    step += 1
                print("\n Episode {} ended in {} steps".format(episode+1, step))

            SnakeGame.running = False

    # plotting the points
    plt.plot(rewards,scores)

    # naming the x axis
    plt.xlabel('rewards')
    # naming the y axis
    plt.ylabel('scores')

    # giving a title to my graph
    plt.title('Rewards v/s scores')

    # function to show the plot
    plt.show()

if __name__ == '__main__':
   main()
