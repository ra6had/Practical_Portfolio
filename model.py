"""
Project Name: Building an Agent Based Model
Author: Rashad a.k. Ahmed
Version: Classes and Agents v.1 (06.03.2019)

This code generates 10 simple agents represented by a set of random
coordinates in a confined 2D space.
The agents take 100 steps in random directions, and handle edges like pac-man
The final position of the agents are printed and plotted.
"""

#import random
import matplotlib.pyplot
import agentframework
import csv
import contextlib

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



# Open and read in the data file as a csv and store values in reader as floats
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    # Create and populate the environment variable with data 
    #from the csv file just read.
    environment = []
    for line in reader:
        rowlist = []
        for value in line:
            rowlist.append(value)
        environment.append(rowlist)
   

# Plot the environment 
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
    
  

# Set the number of agents and iterations
num_of_agents = 10
num_of_iterations = 100 


# Initialize and populate the agents list
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    


# Move agents num_of_iteration steps and eat 10 environment values
for agent in agents:
    agent.move(num_of_iterations)
    agent.eat(15)
    


# Plot the final position of agents on top of the altered environment
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)  
matplotlib.pyplot.show()

# Store the altered environment in dataout.csv
with open('dataout.csv', 'w', newline='') as f2:
    writer = csv.writer(f2)

    for row in environment:
        writer.writerow(row)

# Compute the amount of environment values stored by all agents
with open('store.txt', 'a') as f3:
    with contextlib.redirect_stdout(f3):
        total_store = 0
        for agent in agents:
            total_store += agent.store
        print(total_store)
print(agents[1])
print(help(agentframework.Agent.eat))