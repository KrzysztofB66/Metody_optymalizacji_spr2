import numpy as np
from rysowanie_wykresu import rysuj_wykres


def f(x, y):
    return 4 * y**3 + x**2 - 3 * x * y - x + 9

def dfdx(x, y):
    return 2 * x - 3 * y - 1

def dfdy(x, y):
    return 12 * y**2 - 3 * x

def dffdxx(x, y):
    return 2

def dffdyy(x, y):
    return 24 * y

def dfffdxxx(x, y):
    return 0

def dfffdyyy(x, y):
    return 24

# metoda stycznych (newtona)
def metoda_Newtona(df, ddf, dddf, a, b, e=None, iter=None):
    # if df(a) * df(b) >= 0:
    #     raise ValueError("Warunek konieczny nie jest spełniony: df(a)*df(b) >= 0")
    #
    # if ddf(a) * ddf(b) < 0 or dddf(a) * dddf(b) < 0:
    #     raise ValueError("Ostrzeżenie: Warunki zbieżności mogą nie być spełnione")

    znak_df_a = df(a) > 0
    znak_dddf_a = dddf(a) > 0

    xn = a if znak_dddf_a == znak_df_a else b
    iteracje = 0

    while True:
        xn1 = xn - (df(xn) / ddf(xn))
        iteracje += 1

        if e is not None:
            if abs(df(xn1)) < e or abs(xn1 - xn) < e:
                break

        if iter is not None and iteracje >= iter:
            break

        if e is None and iter is None:
            print("Uwaga: ani epsilon, ani liczba iteracji nie są ustawione – potencjalna nieskończona pętla!")
            break

        xn = xn1

    return xn1

def gradient(f, x, y, h=0.00001):
    dfdx = (f(x + h, y) - f(x, y)) / h
    dfdy = (f(x, y + h) - f(x, y)) / h
    return np.array([dfdx, dfdy])

def gradient_dokladny(x, y):
    dfdx = 2 * x - 3 * y - 1
    dfdy = 12 * y**2 - 3 * x
    return np.array([dfdx, dfdy])

def metoda_gaussa_seidla(f, x0, e, max_iter=None):
    xk, yk = x0
    lista_przyblizen = [[xk, yk]]
    iteracje = 0
    while True:
        xk = metoda_Newtona(lambda x: dfdx(x, yk),
                            lambda x: dffdxx(x, yk),
                            lambda x: dfffdxxx(x, yk),
                            0, 200, 1e-8)

        yk = metoda_Newtona(lambda y: dfdy(xk, y),
                            lambda y: dffdyy(xk, y),
                            lambda y: dfffdyyy(xk, y),
                            0, 200, 1e-8)
        lista_przyblizen.append([xk, yk])

        iteracje += 1
        if max_iter is not None:
            if iteracje >= max_iter:
                break
        else:
            # gradnext = gradient(f, xk, yk)
            gradnext = gradient_dokladny(xk, yk)
            if  np.linalg.norm(gradnext) < e:
                break

    print(iteracje)
    return [xk, yk], lista_przyblizen


wynik = metoda_gaussa_seidla(f, x0=[1, 1], e=0.00001)
print(wynik[0])
rysuj_wykres(f, wynik[1])