import random

class Agent():
    def __init__(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
    
    def move(self, steps):
        """
        Moves the agent a number of steps in random directions
        
        arguments:
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
