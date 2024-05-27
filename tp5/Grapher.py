import matplotlib.pyplot as plt

class Grapher:
    def graph(self, x, y) -> None:
        plt.plot(x, y)
        plt.show()