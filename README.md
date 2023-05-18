# Flappy Bird AI

This project implements an AI agent that plays the classic game of Flappy Bird using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm. The AI agent learns to navigate through a series of pipes by evolving a neural network through genetic algorithms.

## Prerequisites

To run the Flappy Bird AI, you need to have the following dependencies installed:

- Python 3.x
- pygame
- neat-python
- graphviz (optional, for visualizing the neural network)

You can install the required dependencies by running the following command:

```
pip install requirements.txt
```

## Getting Started
To run the Flappy Bird AI, follow these steps:

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `main.py` file using Python:

4. The AI agent will start training using the NEAT algorithm. You can observe the progress in the console output.

5. Once the training is complete or you want to stop the training process, you can close the game window to exit the program.


## Configuration
The NEAT algorithm can be configured through the config-feedforward.txt file. This file contains various parameters that control the evolution process, such as population size, mutation rates, and fitness functions. You can modify these parameters to experiment with different settings and observe their effects on the AI agent's performance.

## Acknowledgements
This Flappy Bird AI implementation is based on the tutorial series by Tech With Tim. Special thanks to Tech With Tim for providing the initial resources and explanation.
