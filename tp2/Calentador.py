STEP = 1
TOTAL_TIME = 5000
V = 220 # Volts
P = 62.715 # Watts Tambien es P = V^2 / R
ENV_T = 15


class Calentador:
    def __init__(self, mass, constant, t_init, t_final, resistor, thermic_conductivity, thickness) -> None:
        self.mass = mass
        self.constant = constant
        self.t_init = t_init
        self.t_final = t_final
        self.resistor = resistor
        self.k = thermic_conductivity
        self.thickness = thickness

    def calculate_delta_temp(self, t) -> float:
        """
        Esta es la funcion que a medida que el modelo se vaya
        complejizando se debera modificar para alcanzar los
        requerimientos
        """
        P = V**2 / self.resistor # Watts
        P_PERDIDA = self.k * (ENV_T - self.t_final)
        Q = P * STEP # Joules
        DELTA_T = Q / (self.mass * self.constant) # Grados C
        
        return  DELTA_T


    def gen_data(self) -> tuple[list, list]:
        time_axis = range(0, TOTAL_TIME, STEP)
        temp_axis = [self.calculate_delta_temp(x) * x + self.t_init for x in time_axis]
        return time_axis, temp_axis
