import pygame as pg
from Graphics import draw_system, draw_final_stats, capture_frame
from Queue import Queue
from Dispatcher import Dispatcher
from pprint import pprint
import cv2
import matplotlib.pyplot as plt


# CONSTANTS
OFFSET = 8 * 60 * 60
END_OF_QUEUEING = 4 * 60 * 60 + OFFSET # 4hs of service
COST_OF_BOX = 1000
COST_OF_LOSS = 10000


if __name__ == "__main__":
    for n_box in range(5,6):  
        NO_OF_BOXES = n_box
        
        # STATS
        stats = {
            "total_clients" : 0,
            "served_clients" : 0,
            "unserved_clients" : 0,
            "min_serving_time": 0,
            "max_serving_time": 0,
            "max_waiting_time": 0,
            "min_waiting_time": 0,
            "cost_of_ops": 0,
        }
        
        arrival_times = []
        # Pygame setup
        pg.init()
        screen = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Queue System Simulation")
        clock = pg.time.Clock()
        font = pg.font.Font(None, 36)
        
        # Queue system setup
        d = Dispatcher()
        q = Queue([], NO_OF_BOXES)
        
        # OpenCV setup for video recording
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(f'simulation_{n_box}_boxes.avi', fourcc, 120, (1280, 720))
        
        
        i = OFFSET
        while True:
            # Pygame event poll
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            
            i += 1
            if i < END_OF_QUEUEING:
                possible_client = d.spawn(i)

            if possible_client != None:
                q.clients.append(possible_client)
                stats["total_clients"] += 1
                arrival_times.append(i)
                possible_client = None
                
            q.lookup_box()
            
            for box in q.boxes:
                box.serve()

            # Update display
            draw_system(screen, q, q.boxes, font, stats, i)
            frame = capture_frame(screen)
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            
            stats["served_clients"] = sum([b.served_clients for b in q.boxes])
            stats["unserved_clients"] = q.unserved_clients
            stats["cost_of_ops"] = stats["unserved_clients"]*COST_OF_LOSS + NO_OF_BOXES*COST_OF_BOX
            stats["max_serving_time"] = round(max([b.max_serving_time for b in q.boxes]) * (1/60), 2)
            stats["min_serving_time"] = round(min([b.min_serving_time for b in q.boxes]) * (1/60), 2)
            stats["max_waiting_time"] = round(q.max_waiting_time * (1/60), 2)
            stats["min_waiting_time"] = round(q.min_waiting_time * (1/60), 2)
            
            clock.tick(120)
            
            if i >= END_OF_QUEUEING and len(q.clients) == 0: break
        
        # Show final stats
        draw_final_stats(screen, stats, font)
        
        # Wait for user to close the window
        i = 0
        waiting_for_close = True
        while i < 720:
            i += 1
            frame = capture_frame(screen)
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    i = 720
            

        plt.hist(arrival_times, bins=8, edgecolor='black')
        plt.title('Histogram of Client Arrivals')
        plt.xlabel('Time')
        plt.ylabel('Number of Clients')
        plt.show()
        
        pg.quit()
        
    pprint(stats)