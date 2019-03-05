"""
Project Name: Building an Agent Based Model
Author: Rashad a.k. Ahmed
Version: Shrinking Code 2 v.2 (03.02.2019)

This code generates 10 simple agents represented by a set of random
coordinates in a confined 2D space.
The agents take 100 steps in random directions, and handle edges like pac-man
The final position of the agents are printed and plotted.
"""

import random
import matplotlib.pyplot
import agentframework



def distances(agents):
    """
    compute distances between agents
    
    arguments:
    agents -- a list of (lists of) coordinate pairs
    
    returns:
    a list of all the distances between coordinate pairs
    """
    distance_set = []
    i = 0
    for i in range(len(agents)):
        for j in range(len(agents)):
            if j > i:
                distance = (((agents[i].y - agents[j].y)**2 + \
                             ((agents[i].x - agents[j].x)**2))**0.5)
                distance_set.append(distance)
    return distance_set
    

# Initializing number of agents and iterations
num_of_agents = 10
num_of_iterations = 100 

# Initializing agents list
agents = []

for i in range(num_of_agents):
    agents.append(agentframework.Agent())
    
matplotlib.pyplot.ylim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
       
matplotlib.pyplot.show()



for agent in agents:
    agent.move(num_of_iterations)
    


#Plot the final position of agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
       
matplotlib.pyplot.show()

