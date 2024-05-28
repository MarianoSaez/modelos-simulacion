from Calentador import *
from Calentador_ideal import Calentador as Calentador_ideal
from Grapher import *
from matplotlib.pyplot import plot

R = 771.745 #Ohm


if __name__ == "__main__":
    c = Calentador(1, 4181, 15, 90, R, 0.01, 0.033, 0.3, 0.03) # Faltan las condiciones iniciales

    t, T_REAL = c.gen_data()
    plt.plot(t, T_REAL)

    t, T_IDEAL = c2.gen_data()
    plt.plot(t, T_IDEAL)

    plt.title("Temperatura de un calentador en el tiempo")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (grados Celsius)")
    plt.legend(["Real", "Ideal"], loc="lower right")

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
