# Project Name: Building an Agent Based Model
# Author: Rashad a.k. Ahmed
# Version: Shrinking Code I (23.01.2019)



import random
import operator
import matplotlib.pyplot

# Initializing agents list
agents = []

# Initializing first agent's position and appending it to agents list.
agents.append([random.randint(0,99), random.randint(0,99)])


# Random walk one step.
if random.random() < 0.5: # motion in the y-axis
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5: # motion in the x-axis
    agents[0][1] += 1
else:
    agents[0][1] -= 1

    
# Random walk a second step
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1


# Repeating the above steps for a second agent.
agents.append([random.randint(0,99), random.randint(0,99)])


# Random walk one step.
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    

# Random walk a second step
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    



# Compute and distance between agents
dist = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(agents)
print(dist)

# Print northernmost and easternmost agents
print(max(agents))
print(max(agents, key=operator.itemgetter(1)))


# Plotting the agents
matplotlib.pyplot.ylim(0,99)
matplotlib.pyplot.xlim(0,99)
matplotlib.pyplot.scatter(agents[0][1], agents[0][0], color='red')
matplotlib.pyplot.scatter(agents[1][1], agents[1][0], color='blue')
matplotlib.pyplot.show()