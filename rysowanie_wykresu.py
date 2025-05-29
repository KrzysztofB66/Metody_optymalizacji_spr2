import numpy as np
import matplotlib.pyplot as plt

def rysuj_wykres(f, przyblizenia):
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.contour(X, Y, Z, levels=100, colors='black', linestyles='solid')

    przyblizenia = np.array(przyblizenia)
    x_vals = przyblizenia[:, 0]
    y_vals = przyblizenia[:, 1]

    ax.plot(1.3815429, 0.5876953, 'o', color='blue', label='Dokładne rozwiązanie')
    ax.scatter(x_vals[0], y_vals[0], color='green', s=50, label='Pierwszy punkt')
    if len(przyblizenia) > 1:
        ax.scatter(x_vals[1:], y_vals[1:], color='red', s=30, label='Przybliżenia')
    ax.plot(x_vals, y_vals, color='blue', linestyle='-', linewidth=1)

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_aspect('equal')
    ax.set_xlim([0, 2])
    ax.set_ylim([0, 2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)

    plt.show()
