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
parser.add_argument('--limits', action='store_true', help='Process limit items')
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

    elif args.limits:
        voltage_list = voltage(V)
        resistance_list = resistance(R)
        env_temp_list = temperature_unif()
        init_temp_list = temperature_normal()
        
        t_lower, T_lower = Calentador(1, 4181, min(init_temp_list), 90, min(resistance_list), 0.01, 0.033, 0.3, 0.03, _voltage=min(voltage_list), _env_temp=min(env_temp_list)).gen_data()
        t_upper, T_upper = Calentador(1, 4181, max(init_temp_list), 90, max(resistance_list), 0.01, 0.033, 0.3, 0.03, _voltage=max(voltage_list), _env_temp=max(env_temp_list)).gen_data()

        plt.plot(t_lower, T_lower, color='blue', linestyle='--')
        plt.plot(t_upper, T_upper, color='blue', linestyle='--')

        plt.fill_between(t_lower, T_lower, T_upper, color='blue', alpha=0.2)
        
    else:
        print("Processing selected items")
        if args.stoc_vars:
            if "V" in args.stoc_vars:
                print("Processing for stoc-vars: v")
                # Generate curves for stochastic voltage
                for v in voltage(V):        
                    t, T = Calentador(1, 4181, 15, 90, R, 0.01, 0.033, 0.3, 0.03, _voltage=v).gen_data()
                    plt.plot(t, T,  label=f'V = {round(v, 2)}')


            if "R" in args.stoc_vars:
                print("Processing for stoc-vars: R")
                # Generate curves for stochastic resistance
                for r in resistance(R):
                    t, T = Calentador(1, 4181, 15, 90, r, 0.01, 0.033, 0.3, 0.03).gen_data()
                    plt.plot(t, T,  label=f'R = {round(r, 2)}')
                    

            if "ENV_T" in args.stoc_vars:
                print("Processing for stoc-vars: ENV_T")
                # Generate curves for stochastic environmental temperatures
                for env_temp in temperature_unif(lower=-20, upper=50):
                    t, T = Calentador(1, 4181, 15, 90, R, 0.01, 0.033, 0.3, 0.03, _env_temp=env_temp).gen_data()
                    plt.plot(t, T, label=f'ENV. TEMP. = {round(env_temp, 2)} C')
                    

            if "INIT_T" in args.stoc_vars:
                print("Processing for stoc-vars: INIT_T")
                # Generate curves for stochastic initial water temperature
                for init_temp in temperature_normal(INITIAL_TEMP, 5):
                    t, T = Calentador(1, 4181, init_temp, 90, R, 0.01, 0.033, 0.3, 0.03).gen_data()
                    plt.plot(t, T, label=f'INIT. TEMP. = {round(init_temp, 2)} C')

    plt.title("Temperatura de un calentador en el tiempo")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (grados Celsius)")
    plt.legend()

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
