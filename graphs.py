from data import extract

rewards_1, cum_rewards_1, episode_l_1=extract('q_learning.txt')
# rewards_2, cum_rewards_2, episode_l_2=extract('batch_size_64.txt')
# rewards_3, cum_rewards_3, episode_l_3=extract('batch_size_128.txt')

def positive_cumulative_sum(input_array):
    # Make all entries positive
    positive_array = [abs(x) for x in input_array]

    # Calculate cumulative sum
    cumulative_sum = [positive_array[0]]
    for i in range(1, len(positive_array)):
        cumulative_sum.append(cumulative_sum[i - 1] + positive_array[i])

    return cumulative_sum


import numpy as np

episode_ori = np.arange(1, episode_l_1[-1]+1)
import matplotlib.pyplot as plt
figure, axis1 = plt.subplots(1, 1)


# # Plotting REWARDS V/S LENGTH
# axis.plot(episode_l, rewards)
# axis.set_title('REWARDS V/S LENGTH')
# axis.set_xlabel('Episode Length')
# axis.set_ylabel('Rewards')

# Plotting REWARDS V/S EPISODES
axis1.plot(episode_l_1[0:len(cum_rewards_1)], positive_cumulative_sum(cum_rewards_1),label='Cumulative rewards',  color='blue')
axis1.plot(episode_l_1[0:len(rewards_1)], rewards_1,label='Rewards',  color='red')
# axis1.plot(episode_l_1, rewards_3,label='Rewards (Batch=256)',  color='green')

axis1.set_xlabel('Episodes')
axis1.set_ylabel('Rewards')

# Plotting CUMULATIVE REWARDS V/S EPISODES
# axis2.plot(episode_ori, cum_rewards_1,label='Cumulative Rewards (LR=0.01)',  color='blue')
# axis2.plot(episode_ori, cum_rewards_2,label='Cumulative Rewards (LR=0.1)',  color='red')
# axis2.plot(episode_ori, cum_rewards_3,label='Cumulative Rewards (LR=0.001)',  color='green')
# # axis.set_title('CUMULATIVE REWARDS V/S EPISODES')
# axis2.set_xlabel('Episodes')
# axis2.set_ylabel('Cumulative Rewards')

# Hide the empty subplot (if any)
# axis[1,0].axis('off')
# axis[1, 1].axis('off')
axis1.legend(loc='best')
# axis2.legend(loc='best')
plt.show()
