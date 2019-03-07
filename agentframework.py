"""
A framework for creating agents with the ability to move in 2D and consume
resources from their environment. The environment is stored inside each agent
and therefore it can be shared among multiple agents.

Classes:

Agents -- an agent class that can move and consume from its environment
"""

import random

class Agent():
    """
    Create an Agent class.
    
    Arguments:
    environment -- 2D indexed data representing the environment with which the
                   the agents will interact.
    
    Methods:
    move -- takes in a number of steps and moves agent in random directions.
    eat -- takes in amount and makes the agent eat (consume) that amount from 
           its environment if the amount is available at the agent's location.
    """
   
    def __init__(self, environment):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0
    
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
                self.y = (self.y + 1) % 100
            else:
                self.y = (self.y - 1) % 100
            
            if random.random() > 0.5:
                self.x = (self.x + 1) % 100
            else:
                self.x = (self.x - 1) % 100
    
    
    def eat(self, amount):
        """Make the agents eat a given amount from its environment
        
        arguments:
        amount -- an intiger representing the amount to eat from the 
        environment
        """
        if self.environment[self.y][self.x] > amount:
            self.environment[self.y][self.x] -= amount
            self.store += amount