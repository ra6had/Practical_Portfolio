"""
Project Name: Building an Agent Based Model
Author: Rashad a.k. Ahmed
Version: Classes and Agents v.1 (06.03.2019)

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
    
    """
    Compute the distances between all agents wihtout redundancies i.e. without 
    the distance between an agent and itself and the distances between an 
    agent and the ones before it
    """
    for i in range(len(agents)):
        for j in range(len(agents)):
            if j > i:
                distance = (((agents[i].y - agents[j].y)**2 + \
                             ((agents[i].x - agents[j].x)**2))**0.5)
                distance_set.append(distance)
    return distance_set
    

# Set the number of agents and iterations
num_of_agents = 10
num_of_iterations = 100 

# Initializing agents list
agents = []

# Create the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent())
    
# Plot initial agents position
matplotlib.pyplot.xlim(0, 99)    
matplotlib.pyplot.ylim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
       
matplotlib.pyplot.show()


# Move agents num_of_iteration steps
for agent in agents:
    agent.move(num_of_iterations)
    


# Plot the final position of agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
       
matplotlib.pyplot.show()

