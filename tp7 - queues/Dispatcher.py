from Client import Client
from numpy.random import randint


class Dispatcher:
    def __init__(self):
        pass
    
    def spawn(self) -> Client:
        if randint(144) == 0: return Client(30 * 60)