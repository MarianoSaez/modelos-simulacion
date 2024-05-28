import matplotlib.pyplot as plt

class Grapher:
    def graph(self, x, y) -> None:
        plt.title("Temperatura de un calentador en el tiempo")
        plt.xlabel("Tiempo (segundos)")
        plt.ylabel("Temperatura (grados Celsius)")
        plt.plot(x, y)        
        plt.show()