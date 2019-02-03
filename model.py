# Project Name: Building an Agent Based Model
# Author: Rashad a.k. Ahmed
# Version: Shrinking Code 2 v.2 (03.02.2019)

# This code generates 10 simple agents represented by a set of random
# coordinates in a confined 2D space.
# The agents take 100 steps in random directions, and handle edges like pac-man
# The final position of the agents are printed and plotted.



import random
import matplotlib.pyplot

# Initializing number of agents and iterations
num_of_agents = 10
num_of_iterations = 100 

# Initializing agents list
agents = []

# populating the agents list with random integers
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
   
    
# Make all agents take "num_of_iteration" steps
# Such that the iteration runs through all agents one step at a time
for i in range(num_of_iterations):    
    for j in range(num_of_agents):  
        for k in range(len(agents[1])):
            if random.random() < 0.5:
                agents[j][k] = (agents[j][k] + 1) % 100
            else:
                agents[j][k] = (agents[j][k] - 1) % 100
 
# Print the final coordinates of agents
print("Agents' coordinates= " + str(agents))


# Plot the final position of agents
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
       
matplotlib.pyplot.show()