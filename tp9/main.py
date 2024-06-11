import multiprocessing
from Conduct import Conduct
from Dispatcher import Dispatcher
from Graphics import animate_simulation

def run_simulation(shape, dimensions, particle_size, max_distance, video_file):
    conduct = Conduct(shape, dimensions)
    dispatcher = Dispatcher(conduct, particle_size, max_distance)
    animate_simulation(conduct, dispatcher, scale=2, video_file=video_file)

def run_simulation_parallel(args):
    shape, dimensions, particle_size, max_distance, video_file = args
    run_simulation(shape, dimensions, particle_size, max_distance, video_file)

if __name__ == '__main__':
    # Definimos los argumentos para cada simulación
    simulations = [
        ('circle', [150, 150], 1, 100, "particle_min_circle.avi"),
        ('circle', [150, 150], 10, 100, "particle_max_circle.avi"),
        ('square', [150, 150], 5, 100, "square_conduct.avi"),
        ('rectangle', [200, 300], 5, 100, "rectangle_conduct.avi"),
        # ('circle', [1000, 1000], 5, 100, "max_circle_conduct.avi")
    ]

    # Ejecutamos las simulaciones en paralelo
    with multiprocessing.Pool() as pool:
        pool.map(run_simulation_parallel, simulations)