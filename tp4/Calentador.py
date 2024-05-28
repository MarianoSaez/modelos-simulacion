from const import *


class Calentador:
    def __init__(self, mass, constant, t_init, t_final, resistor, thickness, radius, height, thermic_conductivity) -> None:
        self.mass = mass
        self.constant = constant
        self.t_init = t_init
        self.t_final = t_final
        self.resistor = resistor
        self.thickness = thickness
        self.area = 2 * PI * radius * height + 2 * PI * radius**2
        self.k = thermic_conductivity

    def calculate_temp(self, t) -> float:
        """
        Esta es la funcion que a medida que el modelo se vaya
        complejizando se debera modificar para alcanzar los
        requerimientos
        """
        P = V**2 / self.resistor # Watts
        Q = P * STEP # Joules
        DELTA_T = Q / (self.mass * self.constant) # Grados C
        T_IDEAL = DELTA_T + self.t_init

        # Perdidas
        Q_PERDIDO = STEP * ( self.k * self.area * (T_IDEAL - ENV_T) ) / self.thickness
        Q_REAL = Q - Q_PERDIDO
        DELTA_T_REAL = Q_REAL / (self.mass * self.constant)
        T = self.t_init + DELTA_T_REAL

        self.t_init = T

        return T


    def gen_data(self) -> tuple[list, list]:
        time_axis = range(0, TOTAL_TIME, STEP)
        temp_axis = [self.calculate_temp(x) for x in time_axis]
        return time_axis, temp_axis
