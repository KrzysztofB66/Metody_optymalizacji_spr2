import numpy as np
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


def metoda_newtona(f, x0, e=1e-6, max_iter=None):
    xk, yk = x0
    iteracje = 0

    while True:
        grad = gradient(f, xk, yk)
        hess = macierz_hessego(f, xk, yk)
        hess_inv = np.linalg.inv(hess)

        delta = hess_inv @ grad
        xk_plus1 = xk - delta[0]
        yk_plus1 = yk - delta[1]

        iteracje += 1

        if max_iter is not None:
            if iteracje >= max_iter:
                xk, yk = xk_plus1, yk_plus1
                break
        else:
            if np.linalg.norm(grad) <= e:
                break
            if abs(xk_plus1 - xk) <= e and abs(yk_plus1 - yk) <= e:
                xk, yk = xk_plus1, yk_plus1
                break

        xk, yk = xk_plus1, yk_plus1

    print("Liczba iteracji:", iteracje)
    return [xk, yk]


# print(metoda_newtona(f, x0=[1, 1], e=0.000001))

print(metoda_newtona(f, x0=[1, 1], max_iter=12))

