from numpy.random import normal, uniform
from const import *

"""
    TP5
    Realizar familias de curvas con:
        - Distribucion uniforme de 5 valores de resistencia +- 10%
        - Dist. mormal de 5 temp iniciales del agua media 10 y desv estandar de 5
        - Distribucion uniforme de 8 temperaturas iniciales del ambiente entre -20 y 50
        - Distribucion normal de 5 valores de tension desv estandar de 40

"""

def resistance(mean: float, tolerance: float = 10) -> float:
    return uniform(mean*(1 - 1/tolerance), mean*(1 + 1/10), 5)

def voltage(mean: float = 220, stdve: float = 40) -> float:
    return normal(mean, stdve, 5)

def temperature_normal(mean: float = 10, stdev : float = 5) -> float:
    return normal(mean, stdev, 5)

def temperature_unif(lower: float = -20, upper: float = 50) -> float:
    return normal(lower, upper, 8)
