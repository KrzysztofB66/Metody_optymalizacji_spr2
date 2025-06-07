import numpy as np
from rysowanie_wykresu import rysuj_wykres

def f(x, y):
    return 4 * y**3 + x**2 - 3 * x * y - x + 9

def metoda_zlotego_podzialu(f, a, b, e, mode="min", iter=None):
    k = (5 ** 0.5 - 1) / 2
    x1 = b - k * (b - a)
    x2 = a + k * (b - a)
    iteracje = 0

    while abs(x2 - x1) > e:
        iteracje += 1

        if iter is not None and iteracje >= iter:
            break

        f_x1, f_x2 = f(x1), f(x2)

        if (mode == "min" and f_x1 < f_x2) or (mode == "max" and f_x1 > f_x2):
            b = x2
            x2 = x1
            x1 = b - k * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + k * (b - a)


    return (a + b) / 2

def gradient(f, x, y, h=0.0000001):
    dfdx = (f(x + h, y) - f(x, y)) / h
    dfdy = (f(x, y + h) - f(x, y)) / h
    return np.array([dfdx, dfdy])

def gradient_dokladny(x, y):
    dfdx = 2 * x - 3 * y - 1
    dfdy = 12 * y**2 - 3 * x
    return np.array([dfdx, dfdy])

def metoda_gaussa_seidla(f, x0, e=None, max_iter=None):
    xk, yk = x0
    lista_przyblizen = []
    iteracje = 0
    while True:
        xk = metoda_zlotego_podzialu(lambda x: f(x, yk), 0, 200, 0.00000001)
        yk = metoda_zlotego_podzialu(lambda y: f(xk, y), 0, 200, 0.00000001)
        lista_przyblizen.append([xk, yk])

        iteracje += 1
        if max_iter is not None:
            if iteracje >= max_iter:
                break
        else:
            gradnext = gradient(f, xk, yk)
            # gradnext = gradient_dokladny(xk, yk)
            if  np.linalg.norm(gradnext) < e:
                break

    print(iteracje)
    return [xk, yk], lista_przyblizen


wynik = metoda_gaussa_seidla(f, x0=[1, 1], e=0.000001)
print(wynik[0])
print(wynik[1])
# rysuj_wykres(f, wynik[1])