from rysowanie_wykresu import rysuj_wykres

# def f(x, y):
#     return 4 * y ** 3 + x ** 2 - 3 * x * y - x + 9

def f(x, y):
    return 2.5*((x**2-y)**2) + (1-x)**2

def hooke_jeeves_min(f, x0, e=0.01, beta=0.5, epsilon=None, max_iter=None):
    xB0 = [x0[0], x0[1]]
    xB = [x0[0], x0[1]]
    x0 = [x0[0], x0[1]]
    baza = [[1, 0], [0, 1]]
    lista_przyblizen = []
    n = 2
    iteracje = 0

    while True:
        iteracje += 1
        lista_przyblizen.append(xB[:])
        x = [x0[0], x0[1]]
        f0 = f(x[0], x[1])
        fB = f(xB[0], xB[1])

        #Etap próbny
        j = 0
        while j < n:
            kierunek = [baza[j][0], baza[j][1]]
            x_proba = [0, 0]
            for i in range(n):
                x_proba[i] = x[i] + e * kierunek[i]
            f_proba = f(x_proba[0], x_proba[1])

            if f_proba < f0:
                for i in range(n):
                    x[i] = x_proba[i]
                f0 = f_proba
            else:
                for i in range(n):
                    x_proba[i] = x[i] - 2 * e * kierunek[i]
                f_proba = f(x_proba[0], x_proba[1])
                if f_proba < f0:
                    for i in range(n):
                        x[i] = x_proba[i]
                    f0 = f_proba
                else:
                    for i in range(n):
                        x[i] = x[i] + e * kierunek[i]

            j += 1

        #Etap roboczy
        if fB > f0:
            for i in range(n):
                xB0[i] = xB[i]
                xB[i] = x[i]
                x0[i] = 2 * xB[i] - xB0[i]
        else:
            for i in range(n):
                x0[i] = xB[i]
            e = e * beta
        #Warunki zakończenia
        if max_iter is not None:
            if iteracje >= max_iter:
                break
        elif e < epsilon:

            break

    print(iteracje)
    return xB, lista_przyblizen


# wynik = hooke_jeeves_min(f, [1, 1], e=0.5, beta=0.5, epsilon=0.000001)
wynik = hooke_jeeves_min(f, [-0.5, 1], e=0.5, beta=0.5, epsilon= 0.00001)
print(wynik[0])
# rysuj_wykres(f, wynik[1])


