# SNAKE_AI
## [Video presentation](https://youtu.be/KuUbKE5kM2M)

## Table of Contents

1. [Introduction](#introduction)
2. [Background Literature](#background-literature)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Training](#training)
8. [Evaluation](#evaluation)
9. [Results](#results)
10. [Contributing](#contributing)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

## Introduction

SNAKE_AI is an AI-driven implementation of the classic Snake game. The project utilizes the Deep Q-Network (DQN) algorithm, a reinforcement learning technique, to train an intelligent agent capable of mastering the game. The agent learns to navigate the game grid, collect food, grow in length, and avoid collisions with itself and obstacles, demonstrating strategic gameplay and achieving high scores.

## Background Literature

### Overview

The Deep Q-Network (DQN) algorithm has revolutionized reinforcement learning by enabling agents to learn optimal policies in high-dimensional environments directly from pixel input. The seminal work by Mnih et al. (2015) demonstrated the capability of DQN to achieve human-level performance on various Atari 2600 games.

### Related Work

1. **Volodymyr Mnih et al. (2015)**: Introduced DQN, which uses deep neural networks to approximate the optimal action-value function. The algorithm was demonstrated to achieve human-level performance on multiple games.
2. **Planning-Based DQN (2017)**: Combines planning approaches with model-free DQN agents to improve efficiency and scores in dynamic environments.
3. **Real-Time Fighting Games (2018)**: Applied DQN to a visual fighting game, highlighting its potential effectiveness in real-time scenarios.
4. **OpenAI Gym (2019)**: Investigated the effectiveness of DQN and other reinforcement learning techniques for video games using the OpenAI Gym's Arcade Learning Environment.
5. **Lightweight CNNs for DRL (2020)**: Addressed resource-intensive requirements in DRL by using lightweight CNNs to demonstrate reasonable performance with compressed imagery data.

### Research Contributions

1. Designed the Snake Game environment and trained an agent using the baseline DQN algorithm.
2. Analyzed and compared the performance of the DQN algorithm with different hyperparameter settings, such as learning rate, batch size, and epsilon decay rate.

## Project Structure

The project repository is structured as follows:

```
SNAKE_AI/
├── data/
│   └── checkpoints/         # Saved model checkpoints
├── src/
│   ├── snake_game.py        # Core game implementation
│   ├── dqn_agent.py         # DQN agent implementation
│   └── train.py             # Training script
├── config/
│   └── config.yaml          # Configuration file
├── notebooks/
│   └── analysis.ipynb       # Jupyter notebook for analysis
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Installation

To install the project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AIMSIIITA/SNAKE_AI.git
   cd SNAKE_AI
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the Snake game with the trained DQN agent, use the following command:

```sh
python src/snake_game.py
```

## Configuration

The configuration for the project is stored in `config/config.yaml`. It includes settings for the game environment, DQN parameters, and training hyperparameters. Modify the configuration file to customize the agent's training and evaluation process.

## Training

To train the DQN agent, run the training script:

```sh
python src/train.py
```

The training script will save model checkpoints in the `data/checkpoints/` directory. The training process includes experience replay and target network updates to stabilize learning and improve convergence.

## Evaluation

To evaluate the performance of the trained DQN agent, run the evaluation script:

```sh
python src/evaluate.py
```

The script will load the saved model checkpoints and display the agent's performance metrics, including average score and strategic gameplay analysis.

## Results

The results of the training and evaluation processes are documented in the `notebooks/analysis.ipynb` notebook. The notebook provides detailed visualizations and analysis of the agent's performance, including:

- Learning curves
- Hyperparameter optimization
- Game play strategies

## Contributing

Contributions to the project are welcome. To contribute, follow these steps:

1. **Fork the repository:**
   ```sh
   git clone https://github.com/your-username/SNAKE_AI.git
   cd SNAKE_AI
   ```

2. **Create a feature branch:**
   ```sh
   git checkout -b feature/your-feature-name
   ```

3. **Commit your changes:**
   ```sh
   git commit -m 'Add some feature'
   ```

4. **Push to the branch:**
   ```sh
   git push origin feature/your-feature-name
   ```

5. **Open a pull request:**

Visit the repository on GitHub and open a pull request to the `main` branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank the authors of the following papers and resources that significantly contributed to this project:

1. Volodymyr Mnih et al., "Human-level control through deep reinforcement learning," Nature, 2015.
2. OpenAI Gym
3. Pygame Community

For more detailed information, please refer to the [Deep_Q_Snake__An_Intelligent_Agent_Mastering_the_Snake_Game_with_Deep_Reinforcement_Learning.pdf](./Deep_Q_Snake__An_Intelligent_Agent_Mastering_the_Snake_Game_with_Deep_Reinforcement_Learning.pdf) file included in this repository.
