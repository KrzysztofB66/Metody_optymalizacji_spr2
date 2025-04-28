import numpy as np
import matplotlib.pyplot as plt

def rysuj_wykres(f, przyblizenia):
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.contour(X, Y, Z, levels=50, colors='black', linestyles='solid')

    przyblizenia = np.array(przyblizenia)
    x_vals = przyblizenia[:, 0]
    y_vals = przyblizenia[:, 1]


    ax.scatter(x_vals, y_vals, color='red', marker='o', s=30, label='Przybliżenia')
    ax.plot(x_vals, y_vals, color='blue', linestyle='-', linewidth=1)

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_aspect('equal')

    ax.set_xlim([0, 2])
    ax.set_ylim([0, 2])

    plt.legend()
    plt.grid(True)
    plt.show()



