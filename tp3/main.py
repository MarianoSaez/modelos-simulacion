from Calentador import *
from Grapher import *

R = 771.745 #Ohm


if __name__ == "__main__":
    c = Calentador(1, 4181, 15, 90, R) # Faltan las condiciones iniciales
    g = Grapher()

    x, y = c.gen_data()
    g.graph(x, y)

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
