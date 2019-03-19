"""
A framework for creating agents with the ability to move in a 2D environment
and consume resources from it. The environment is stored inside each agent
and therefore, the same environment can be shared among multiple agents.

Classes:

Agents -- an agent class that can move withn, and consume from its environment
"""

import random

class Agent():
    """
    Create an Agent class.
    
    Arguments:
    environment -- 2D indexed data representing the environment with which the
                   the agents will interact.
	agents -- a list of agents with which the agent shares the enevironment
    
    Methods:
    move -- takes in a number of steps and moves agent in random directions.
    eat -- takes in amount and makes the agent eat (consume) that amount from 
           its environment if the amount is available at the agent's location.
    """
   
    def __init__(self, environment, agents):
	    self.environment = environment
	    self.agents = agents
	    self.store = 0
	    self.y = random.randint(0, len(self.environment))
	    self.x = random.randint(0, len(self.environment[0]))
        
    def __str__(self):
        return "I'm an agent in: (" + str(self.x) + ',' + str(self.y) + ").\
With a store of: " + str(self.store)
        
    
    def move(self, steps=10):
        """Moves the agent a number of steps in random directions
        
        keyword arguments:
        steps -- an intiger representing the number of steps
        """
        for i in range(steps):
            
            if random.random() < 0.5:
                self.y = (self.y + 1) % len(self.environment[0])
            else:
                self.y = (self.y - 1) % len(self.environment[0])
            
            if random.random() > 0.5:
                self.x = (self.x + 1) % len(self.environment)
            else:
                self.x = (self.x - 1) % len(self.environment)
    
    
    def eat(self, amount):
        """Make the agents eat a given amount from its environment
        
        arguments:
        amount -- an intiger representing the amount to eat from the 
        environment
        """
        if self.environment[self.y][self.x] > amount:
            self.environment[self.y][self.x] -= amount
            self.store += amount
	
    def distance_between(self, agent):
	    """
	    compute distances between agent and other agents in its environment.
	    
	    arguments:
	    agent -- an with agent.x and agent.y attributes
		
		returns distances between self and agent.	
	    """
	    return abs(((self.y - agent.y)**2 + ((self.x - agent.x))**0.5))
		
    def share_with_neighbours(self, neighbourhood):
        """
        Share store with neighbouring agents.
		
		arguments:
		neighbourhood -- a number representing the neighbourhood
						 radius around the agent.
	    """
        self.neighbourhood = neighbourhood
        for agent in self.agents:
            if self.distance_between(agent) <= self.neighbourhood:
                sum_store = self.store + agent.store
                average = sum_store/2
                self.store = average
                agent.store = average
