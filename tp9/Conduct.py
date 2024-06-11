import numpy as np

class Conduct:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions
        self.particles = []
        
    def is_within_bounds(self, position):
        if self.shape == 'circle':
            center = np.array(self.dimensions) / 2
            radius = self.dimensions[0] / 2
            return np.linalg.norm(position - center) <= radius
        elif self.shape in ['square', 'rectangle']:
            return np.all(position >= 0) and np.all(position < self.dimensions)
        
    def is_near_wall(self, position, tolerance):
        if self.shape == 'circle':
            center = np.array(self.dimensions) / 2
            radius = self.dimensions[0] / 2
            distance_to_center = np.linalg.norm(position - center)
            return radius - distance_to_center <= tolerance
        elif self.shape in ['square', 'rectangle']:
            return np.any(position < tolerance) or np.any(self.dimensions - position < tolerance)
        
    def is_near_other_particles(self, position, tolerance):
        for particle in self.particles:
            if np.linalg.norm(particle.position - position) <= tolerance:
                return True
        return False

    def add_particle(self, particle):
        self.particles.append(particle)