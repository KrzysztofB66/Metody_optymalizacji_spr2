from rysowanie_wykresu import *


def f(x, y):
    return 4 * y**3 + x**2 - 3 * x * y - x + 9

# def f(x, y):
#     return 10 * x ** 2 + 12 * x * y + 10 * x ** 2

def gradient(f, x, y, h=0.00001):
    dfdx = (f(x + h, y) - f(x, y)) / h
    dfdy = (f(x, y + h) - f(x, y)) / h
    return np.array([dfdx, dfdy])

def macierz_hessego(f, x, y, h=0.00001):
    d2fdx2 = (f(x + 2 * h, y) - 2 * f(x + h, y) + f(x, y)) / h ** 2
    d2fdy2 = (f(x, y + 2 * h) - 2 * f(x, y + h) + f(x, y)) / h ** 2
    d2fdxdy = (f(x + h, y + h) - f(x + h, y) - f(x, y + h) + f(x, y)) / h ** 2
    return np.array([[d2fdx2, d2fdxdy], [d2fdxdy, d2fdy2]])

def gradient_dokladny(x, y):
    dfdx = 2 * x - 3 * y - 1
    dfdy = 12 * y**2 - 3 * x
    return np.array([dfdx, dfdy])

def macierz_hessego_dokladna(x, y):
    d2fdx2 = 2
    d2fdy2 = 24 * y
    d2fdxdy = -3
    return np.array([[d2fdx2, d2fdxdy], [d2fdxdy, d2fdy2]])

def metoda_najszybszego_spadku(f, x0, e=0.000001, max_iter=None):
    xk, yk = x0
    iteracje = 0
    lista_przyblizen = []

    while True:
        grad = gradient(f, xk, yk)
        hess = macierz_hessego(f, xk, yk)
        # grad = gradient_dokladny(xk, yk)
        # hess = macierz_hessego_dokladna(xk, yk)

        a = grad[0]
        b = grad[1]
        c = hess[0, 0]
        d = hess[0, 1]
        e_= hess[1, 0]
        f_= hess[1, 1]

        licznik = a**2 + b**2
        mianownik = (a * c + b * e_) * a + (a * d + b * f_) * b

        ak = licznik / mianownik

        xk_plus1 = xk - ak * a
        yk_plus1 = yk - ak * b

        iteracje += 1
        lista_przyblizen.append([xk_plus1, yk_plus1])

        if max_iter is not None:
            if iteracje >= max_iter:
                xk, yk = xk_plus1, yk_plus1
                break
        else:
            if abs(xk_plus1 - xk) <= e and abs(yk_plus1 - yk) <= e:
                xk, yk = xk_plus1, yk_plus1
                break

        xk, yk = xk_plus1, yk_plus1

    print("Liczba iteracji:", iteracje)
    return [xk, yk], lista_przyblizen


wynik_spadek = metoda_najszybszego_spadku(f, x0=[1, 1], e=0.000001)
print(wynik_spadek[0])

# rysuj_wykres(f, wynik_spadek[1])