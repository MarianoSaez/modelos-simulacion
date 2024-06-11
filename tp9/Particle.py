import numpy as np

class Particle:
    def __init__(self, size, initial_position):
        self.size = size
        self.position = np.array(initial_position)
        
    def move(self):
        direction = np.random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1