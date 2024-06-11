from Particle import Particle
from Conduct import Conduct
from Dispatcher import Dispatcher
import pygame
import sys
import cv2
import numpy as np

def animate_simulation(conduct, dispatcher, scale=1, video_file="simulation.avi"):
    pygame.init()
    
    width, height = conduct.dimensions[0] * scale, conduct.dimensions[1] * scale
    screen = pygame.display.set_mode((width, height))
    
    # Configuración del video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_file, fourcc, 30.0, (width, height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not dispatcher.run_simulation_step():
            running = False  # Termina la simulación si colisiona inmediatamente
        
        screen.fill((255, 255, 255))  # Fondo blanco

        # Dibujar el conducto
        if conduct.shape == 'circle':
            center = (conduct.dimensions[0] // 2 * scale, conduct.dimensions[1] // 2 * scale)
            radius = conduct.dimensions[0] // 2 * scale
            pygame.draw.circle(screen, (0, 0, 0), center, radius, 1)
        elif conduct.shape in ['square', 'rectangle']:
            rect = pygame.Rect(0, 0, width, height)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        
        # Dibujar las partículas en movimiento
        for particle in dispatcher.moving_particles:
            pygame.draw.rect(screen, (255, 0, 0), 
                             (particle.position[0] * scale, particle.position[1] * scale, 
                              particle.size * scale, particle.size * scale))

        # Dibujar las partículas adheridas
        for particle in conduct.particles:
            pygame.draw.rect(screen, (0, 0, 255), 
                             (particle.position[0] * scale, particle.position[1] * scale, 
                              particle.size * scale, particle.size * scale))

        pygame.display.flip()
        
        # Capturar el cuadro actual de pygame y escribirlo en el archivo de video
        frame = pygame.surfarray.array3d(screen)
        frame = np.transpose(frame, (1, 0, 2))  # Convertir de (width, height, channels) a (height, width, channels)
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    pygame.quit()
    out.release()
    # sys.exit()

# # Ejemplo de uso
# conduct = Conduct('circle', [100, 100])  # Cambié a 200x200 para una mejor visualización
# dispatcher = Dispatcher(conduct, particle_size=5, max_distance=100)
# animate_simulation(conduct, dispatcher, scale=2)




