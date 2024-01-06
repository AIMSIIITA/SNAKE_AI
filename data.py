# Read data from learning_rate_0.01.txt
def cumulative_sum(input_list):
    cumulative_result = 0
    result_list = []

    for element in input_list:
        cumulative_result += element
        result_list.append(cumulative_result)

    return result_list
# Extracting lists from the content
def extract(filename):
    with open(filename, 'r') as file:
        content = file.read()
    rewards_start = content.find("REWARDS:") + len("REWARDS:")
    rewards_end = content.find("EPISODES:")
    rewards_str = content[rewards_start+1:rewards_end].strip().rstrip(',').lstrip('[').rstrip(']')
    rewards = list(map(int, rewards_str.split(',')))

    episodes_start = content.find("EPISODES:") + len("EPISODES:")
    episodes_end = content.find("CUMULATIVE REWARDS:")
    episode_l = list(map(int, content[episodes_start+1:episodes_end].strip().lstrip('[').rstrip(']').rstrip(',').split(',')))
    print(episode_l.count(100))
    cum_rewards_start = content.find("CUMULATIVE REWARDS:") + len("CUMULATIVE REWARDS:")
    cum_rewards = list(map(int, content[cum_rewards_start+1:].strip().lstrip('[').rstrip(']').rstrip(',').split(',')))

    cumulative_rewards = []
    current_episode = episode_l[0]
    max_reward = float('-inf')

    for episode, reward in zip(episode_l, rewards):
        if episode == current_episode:
            max_reward = max(max_reward, reward)
        else:
            cumulative_rewards.append(max_reward)
            max_reward = reward
            current_episode = episode

    # Append the last cumulative reward for the last episode
    cumulative_rewards.append(max_reward)

    return rewards, cumulative_sum(cumulative_rewards), episode_l