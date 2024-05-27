from Calentador import *
from Calentador_ideal import Calentador as Calentador_ideal
from stocasticVariables import resistance, voltage, temperature_normal, temperature_unif
import matplotlib.pyplot as plt
import argparse

R = 771.745 # Ohm
V = 220 # Volts
INITIAL_TEMP = 10

parser = argparse.ArgumentParser(description='Process some parameters.')

parser.add_argument('--all', action='store_true', help='Process all items')

parser.add_argument('--stoc-vars', nargs='+', type=str, choices=["R", "V", "ENV_T", "INIT_T"], help='Specify the stochastic variables')

args = parser.parse_args()


if __name__ == "__main__":
    if args.all:
        print("Processing all items")
        # Generate curves for stocastic resistance
        for r in resistance(R):
            # Generate curves for sticastic initial water temp.
            for init_temp in temperature_normal(INITIAL_TEMP, 5):
                # Generate curves for stocastic env. temperatures
                for env_temp in temperature_unif(lower=-20, upper=50):
                    # Generate curves for stocastic voltage
                    for v in voltage(V):        
                        t, T = Calentador(1, 4181, init_temp, 90, r, 0.01, 0.033, 0.3, 0.03, _voltage=v, _env_temp=env_temp).gen_data()
                        plt.plot(t, T)
    else:
        print("Processing selected items")
        if args.stoc_vars:
            if "V" in args.stoc_vars:
                print("Processing for stoc-vars: v")
                # Generate curves for stochastic voltage
                for v in voltage(V):        
                    t, T = Calentador(1, 4181, 15, 90, R, 0.01, 0.033, 0.3, 0.03, _voltage=v).gen_data()
                    plt.plot(t, T, '#ffa500')

            if "R" in args.stoc_vars:
                print("Processing for stoc-vars: R")
                # Generate curves for stochastic resistance
                for r in resistance(R):
                    t, T = Calentador(1, 4181, 15, 90, r, 0.01, 0.033, 0.3, 0.03).gen_data()
                    plt.plot(t, T, '#ff4040')

            if "ENV_T" in args.stoc_vars:
                print("Processing for stoc-vars: ENV_T")
                # Generate curves for stochastic environmental temperatures
                for env_temp in temperature_unif(lower=-20, upper=50):
                    t, T = Calentador(1, 4181, 15, 90, R, 0.01, 0.033, 0.3, 0.03, _env_temp=env_temp).gen_data()
                    plt.plot(t, T, 'lightseagreen')

            if "INIT_T" in args.stoc_vars:
                print("Processing for stoc-vars: INIT_T")
                # Generate curves for stochastic initial water temperature
                for init_temp in temperature_normal(INITIAL_TEMP, 5):
                    t, T = Calentador(1, 4181, init_temp, 90, R, 0.01, 0.033, 0.3, 0.03).gen_data()
                    plt.plot(t, T, 'green')

    plt.title("Temperatura de un calentador en el tiempo")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (grados Celsius)")

    plt.show()

    exit()

    """
    TP5
    Realizar familias de curvas con:
        - Distribucion uniforme de 5 valores de resistencia
        - Dist. mormal de temp iniciales del agua media 10 y desv estandar de 5
        - Distribucion uniforme de 8 temperaturas iniciales del ambiente entre -20 y 50
        - Distribucion normal de 5 valores de tension desv estandar de 40
    
        
    TP6
    X segundos despues de inciar el experimento y durante Y segundos llega un frente
    frio que hace descender la temperatura externa Z grados. Rehacer el grafico de temp

    La probabilidad de que llegue este frente frio en cada tick es de 1/300

    """
