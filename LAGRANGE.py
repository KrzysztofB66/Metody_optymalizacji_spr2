from sympy import symbols, Eq, diff, solve

def lagrange(f, h, vars):
    # Lambda, ograniczenie
    lambdaa = symbols('lambda')

    #Funkcja Lagrange’a
    L = f + lambdaa * h[0]

    rownania = []
    for var in vars:
        #dla każdej x, y pochodną cząstkową funkcji L względem tej zmiennej
        dLdvar = diff(L, var)
        rownania.append(Eq(dLdvar, 0))

    #Dodanie ograniczenia h1 =0
    rownania.append(Eq(h[0], 0))

    #Rozwiązywanie układu
    wynik = solve(rownania, vars + [lambdaa], dict=True)
    return wynik

x, y = symbols('x y')
f = x**2 + y**2
h = [2*x + y - 2]
zmienne = [x, y]

wyniki = lagrange(f, h, zmienne)

for i in wyniki:
    for j in i:
        print(f"{j} = {round(i[j].evalf(), 4)}")
