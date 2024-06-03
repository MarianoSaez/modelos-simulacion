from numpy.random import normal

MEAN_SERVING = 5 * 60
STDEV_SERVING = 10 * 60


class Box:
    def __init__(self):
        self.client = None
        self.serving_time = abs(round(normal(MEAN_SERVING, STDEV_SERVING)))
        self.served_clients = 0
        self.max_serving_time = self.serving_time
        self.min_serving_time = self.serving_time
    
    def serve(self) -> None:
        if self.client != None:
            if self.serving_time > 0:
                self.serving_time -= 1
            else:
                # print(f"Client {self.client} leaving")
                self.client = None
                t = abs(round(normal(MEAN_SERVING, STDEV_SERVING)))
                self.max_serving_time = max(self.serving_time, t)
                self.min_serving_time = min(self.serving_time, t)
                self.serving_time = t
        return