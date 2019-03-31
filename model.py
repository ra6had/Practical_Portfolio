"""
Author: Rashad A.K.Ahmed
Lisence: GNU

This appilcation uses the agentframework.py module to instantiate Agent
objects in an environment. The Agent objects are given random positions
confining them to their environment. The environment is an image like
csv file where every pixel value represents the amount of resources in the
pixel's location.

The Agent objects then move randomly in their environment consuming the
available resources and sharing them with their neighbours.

An update(frames) function is defined to update the plot with every iteration.
The plot shows the Agent objects moving and the environment changing as the
Agents consume it.

Finally a DataFrame is created with every Agent's initial and final locations
together with the amount of resources they consumed from the environment.


"""


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import pandas as pd
import agentframework

#Set the number of agents and iterations
num_of_agents = 10
num_of_iterations = 10
bite = 100
steps = 10
neighbourhood = 100
fig = plt.figure(figsize=(15, 15))
plt.style.use('classic')
plt.set_cmap('Greens')

def update(frames):
	"""
	Update the animation frames.

	This function is passed into animation.FuncAnimation(). It utelizes
	the	global variable "num_of_iterations" to simultaneously iterate through
	the agents making them perform certain methods and update the animation
	frame after each iteration.

	"""
	# Declare the global variables
	global num_of_iterations
	global dataframe

	"""
	The following if statement ensures that the animation and the methods
	are called a definate number of times, i.e. "num_of_iterations"

	Once the iterations are finished, record the final locations and the
	amount of resources in each agents store and finally convert the output
	into a dataframe and write it to a csv file
	"""
	if num_of_iterations > 0:
		fig.clear()
		plt.title('Sheep are busy eating') # Sheep are still eating
		# make each agent move, eat and share
		for agent in agents:
			agent.move(steps)
			agent.eat(bite)
			agent.share_with_neighbours(neighbourhood)
		plt.imshow(environment, origin='lower')
		plt.colorbar()
		plt.xlim(0, len(environment[0]))
		plt.ylim(0, len(environment))
		for i in range(num_of_agents):
			plt.scatter(agents[i].x,agents[i].y)
		num_of_iterations -= 1 # Reduce by one
#		print('Another bite, please!') #should be printed num_of_iterations
	else:
#		print('baa baa, no more grass please!')
		plt.title('Sheep are done eating')
		dataframe = pd.DataFrame()
		end_location_x = []
		end_location_y = []

		# Record the agents' final location
		for i in range(len(agents)):
			end_location_x.append(agents[i].x)
			end_location_y.append(agents[i].y)

		# Construct a dictionary for each aggent then append it to dataframe
		for i in range(len(agents)):
			df = {}
			df['Store'] = agents[i].store
			df['Final Location X'] =  end_location_y[i]
			df['Final Location Y'] =  end_location_y[i]
			df['Initial Location X'] = st_location_x[i]
			df['Initial Location Y'] = st_location_y[i]
			dataframe = dataframe.append(df, ignore_index=True)
		print(dataframe)

		# Write the output dataframe to a csv file
		with open('output.csv', 'w') as datafile:
			dataframe.to_csv(datafile)


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




# Instantiate agents and populate the agents list
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Record the initial location of agents
st_location_x = []
st_location_y = []
for agent in agents:
	st_location_x.append(agent.x)
	st_location_y.append(agent.y)


# Animate the agents
ani = animation.FuncAnimation(fig, update, num_of_iterations,\
							   interval=1, repeat=False)
plt.show()