"""
Project Name: Building an Agent Based Model
Author: Rashad a.k. Ahmed
Version: I/O v.2 (08.03.2019)

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

# Set the number of agents and iterations
num_of_agents = 100
num_of_iterations = 5 
bite = 40
neighbourhood = 50




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
matplotlib.pyplot.imshow(environment, origin='lower')
matplotlib.pyplot.show()
    


# Initialize and populate the agents list
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    


# Move agents num_of_iteration steps and eat a bite off the environment
for agent_a in agents:
    agent_a.move(num_of_iterations)
    agent_a.eat(bite)
    print(agent_a.store)
    agent_a.share_with_neighbours(neighbourhood)
    print(agent_a.store)

for agent in agents:
    print("agent's store is: " + str(agent.store))
# Plot the final position of agents on top of the altered environment
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment, origin='lower')
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