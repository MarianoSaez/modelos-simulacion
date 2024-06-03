import pygame as pg
import numpy as np
import time as t


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (64, 64, 64)

# SIZES AND POSITIONS
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
CLIENT_RADIUS = 10
CLIENT_SPACING = 30
BOX_WIDTH = 50
BOX_HEIGHT = 50
BOX_SPACING = 75

def draw_system(screen, queue, boxes, font, stats, time):
    screen.fill(GREY)
    
    # Draw time
    
    time_text = font.render(f"Time: {t.strftime('%H:%M:%S', t.gmtime(time + 8 * 60 * 60))}", True, WHITE)
    time_rect = time_text.get_rect(topright=(SCREEN_WIDTH - 50, 50))
    screen.blit(time_text, time_rect)
    
    
    # Draw clients in queue
    for idx, client in enumerate(queue.clients):
        x = 50 + idx * CLIENT_SPACING
        y = SCREEN_HEIGHT - 200
        pg.draw.circle(screen, BLUE, (x, y), CLIENT_RADIUS)
    
    # Draw boxes and serving clients
    for idx, box in enumerate(boxes):
        x = 50 + (idx % 10) * BOX_SPACING  # Distribute boxes in columns
        y = 100 + (idx // 10) * (BOX_HEIGHT + 50)  # New row for every 3 boxes
        box_color = GREEN if box.client else RED
        pg.draw.rect(screen, box_color, (x, y, BOX_WIDTH, BOX_HEIGHT))
        if box.client:
            pg.draw.circle(screen, BLUE, (x + BOX_WIDTH // 2, y + BOX_HEIGHT // 2), CLIENT_RADIUS)
            
    # Draw statistics
    stats_text = font.render(f"Total Clients: {stats['total_clients']}", True, WHITE)
    screen.blit(stats_text, (50, SCREEN_HEIGHT - 150))
    served_text = font.render(f"Served Clients: {stats['served_clients']}", True, WHITE)
    screen.blit(served_text, (50, SCREEN_HEIGHT - 120))
    unserved_text = font.render(f"Unserved Clients: {stats['unserved_clients']}", True, WHITE)
    screen.blit(unserved_text, (50, SCREEN_HEIGHT - 90))
    
def draw_final_stats(screen, stats, font):
    screen.fill(GREY)
    
    title_text = font.render("ESTADÍSTICAS DEL SISTEMA", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
    screen.blit(title_text, title_rect)
    
    stats_lines = [
        f"Total Clients: {stats['total_clients']}",
        f"Served Clients: {stats['served_clients']}",
        f"Unserved Clients: {stats['unserved_clients']}",
        f"Min Serving Time: {stats['min_serving_time']} mins",
        f"Max Serving Time: {stats['max_serving_time']} mins",
        f"Max Waiting Time: {stats['max_waiting_time']} mins",
        f"Min Waiting Time: {stats['min_waiting_time']} mins",
        f"Cost of Operations: ${stats['cost_of_ops']}",
    ]
    
    for idx, line in enumerate(stats_lines):
        stats_text = font.render(line, True, WHITE)
        stats_rect = stats_text.get_rect(center=(SCREEN_WIDTH // 2, 70 + idx * 40))
        screen.blit(stats_text, stats_rect)
    
def capture_frame(screen):
    pg.display.flip()
    frame = pg.surfarray.array3d(screen)
    frame = np.rot90(frame)
    frame = np.flipud(frame)
    return frame

    