# Project Name: Building an Agent Based Model
# Author: Rashad a.k. Ahmed
# Version: Timing Code  v.1 (23.02.2019)

"""
This code 
"""


import random
import matplotlib.pyplot
import time


def distances(agents):
    """compute the distance between agents"""
    distance_set = []
    for i in range(len(agents)):
        for j in range(len(agents)):
            if j > i:
                distance = (((agents[i][0] - agents[j][0])**2 + ((agents[i][1] - agents[j][1])**2))**0.5)
                distance_set.append(distance)
    return distance_set
    

# Initializing number of agents and iterations
num_of_agents_list = list(range(10,100,10))
num_of_iterations = 100 

# Initializing agents list
duration = []

# populating the agents list with random integers
for i in range(len(num_of_agents_list)):
    agents = []
    start = time.clock()
    for j in range(num_of_agents_list[i]):
        agents.append([random.randint(0,100),random.randint(0,100)])
        for m in range(num_of_iterations):            
            if random.random() < 0.5:
                agents[j][0] = (agents[j][0] + 1) % 100
                agents[j][0] = (agents[j][0] + 1) % 100
            else:
                agents[j][1] = (agents[j][1] - 1) % 100
                agents[j][1] = (agents[j][1] - 1) % 100
    distances(agents)
    end = time.clock()
    dur = end - start
    duration.append(dur)

print(duration)
print(' ')
print(num_of_agents_list)
print(' ')
matplotlib.pyplot.scatter(num_of_agents_list, duration)
matplotlib.pyplot.show()