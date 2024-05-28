from numpy.random import randint, normal, exponential


class Environment:
    def __init__(self, temp: float) -> None:
        self.temp = temp
        self.prev_temp = temp
        self.delta_tick = 0
        
    def get_temp(self) -> float:
        if self.delta_tick == 0:
            self.temp = self.prev_temp
            
        if self.delta_tick > 0:
            self.delta_tick -= 1
            
        else:
            if randint(300) == 0:
                self.temp -= min(normal(25, 12), 50)
                self.delta_tick = exponential(500)
                # print(f"{self.delta_tick = } | {self.temp = }")
            
        return self.temp