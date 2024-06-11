from Client import Client
from numpy.random import randint, normal, random, uniform
from scipy.stats import norm

OFFSET = 0

class Dispatcher:
    def __init__(self):
        self.sigma = 2 * 60 * 60
        self.mu = 10 * 60 * 60
    
    def spawn(self, t: int):
        adjust = self.adjustment_value(t)
        print(adjust)
        # Calcular la probabilidad de spawn en el intervalo [t, t+1]
        prob_t = self._interval_probability(t) 
        # Decidir si generar un cliente basado en la probabilidad
        if uniform() < prob_t * adjust:
            return Client(30 * 60)
        return None

    def _interval_probability(self, t: int) -> float:
        # Calcular la probabilidad acumulada hasta t+1 segundos
        cdf_t1 = norm.cdf(t + 0.12 * 3600, self.mu, self.sigma)
        # Calcular la probabilidad acumulada hasta t segundos
        cdf_t = norm.cdf(t - 0.12 * 3600, self.mu, self.sigma)
        # La probabilidad de que el evento ocurra exactamente en [t, t+1]
        return cdf_t1 - cdf_t   
    
    def adjustment_value(self, t: int) -> float:
        
        return 0.18
        if t <= 8.5 * 3600:
            return 0.15
        elif t <= 9 * 3600:
            return 0.2
        elif t <= 9.5 * 3600:
            return 0.25
        elif t <= 10 * 3600:
            return 0.3
        elif t <= 10.5 * 3600:
            return 0.25
        elif t <= 11 * 3600:
            return 0.2
        else:
            return 0.15

        
        
