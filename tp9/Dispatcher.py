import numpy as np
from Particle import Particle

class Dispatcher:
    def __init__(self, conduct, particle_size, max_distance):
        self.conduct = conduct
        self.particle_size = particle_size
        self.max_distance = max_distance
        self.tolerance = 1.1 * particle_size  # Ajuste de tolerancia
        self.moving_particles = []

    def spawn_particle(self):
        initial_position = np.array(self.conduct.dimensions) // 2
        return Particle(self.particle_size, initial_position)

    def run_simulation_step(self):
        if not self.moving_particles:
            particle = self.spawn_particle()
            if self.conduct.is_near_wall(particle.position, self.tolerance) or self.conduct.is_near_other_particles(particle.position, self.tolerance):
                return False  # Termina la simulación si colisiona inmediatamente
            self.moving_particles.append(particle)

        new_moving_particles = []
        for particle in self.moving_particles:
            particle.move()
            if not self.conduct.is_within_bounds(particle.position):
                continue
            if self.conduct.is_near_wall(particle.position, self.tolerance) or self.conduct.is_near_other_particles(particle.position, self.tolerance):
                self.conduct.add_particle(particle)
            else:
                new_moving_particles.append(particle)
        
        self.moving_particles = new_moving_particles
        return True



