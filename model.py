# Project Name: Building an Agent Based Model
# Author: Rashad a.k. Ahmed
# Version: Shrinking Code 2 v.1 (01.02.2019)


# This code generates 100 simple agents represented by coordinates 
# between 0 and 99 in 2D space.
# The agents take 100 steps in random directions and their final positions 
# are plotted.
# This version includes several commented out lines that may be useful
# for testing the functionality of the code



import random
#import operator
import matplotlib.pyplot
import copy

# Initializing number of agents and iterations
num_of_agents = 10
num_of_iterations = 100 

# Initializing agents list
agents = []

# populating the agents list
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

# Uncomment the below lines to print/plot the initial positions of agents
#print("Agents' coordinates= " + str(agents))
#
#for i in range(len(agents)):
#    for k in range(2):
#        matplotlib.pyplot.scatter(agents[i][1], agents[i][0])

#matplotlib.pyplot.show() 
        
 
# copy the agents list to a new list to be used for comparison later
agents2 = copy.deepcopy(agents) 

# Make all agents take "num_of_iteration" number of steps in random directions
# Such that the iteration runs through all the agents one step at a time
# Using a pac-man approach to handle edges
for i in range(num_of_iterations):    
    for j in range(num_of_agents):  
        for k in range(len(agents2[1])):
            if random.random() < 0.5:
                agents2[j][k] = (agents2[j][k] + 1) % 100
            else:
                agents2[j][k] = (agents2[j][k] - 1) % 100
#    print("agents = " + str(agents)) # For testing, reduce the num_of_iterations


# Print the coordinates of agents
print("Agents' coordinates= " + str(agents2))




# Compute and distance between agents
#dist = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print(agents)
#print(dist)

# Print northernmost and easternmost agents
#print('Northernmost agent = ' + str(max(agents2)))
#print('Easternmost agent = ' + str(max(agents2, key=operator.itemgetter(1))))


# Plotting the final position of the agents
for i in range(len(agents2)):
    matplotlib.pyplot.scatter(agents2[i][1], agents2[i][0])
       
matplotlib.pyplot.show()

print(agents)
print(agents2)

# compute and print the components of the displacement
# vector for each agent in the 2 dimension
for i in range(len(agents)):
    print([str((agents2[i][0])-(agents[i][0])) +"," +str((agents2[i][1])-(agents[i][1]))])