def metoda_simplex(funkcja_celu, lewa_strona_ograniczen, prawa_strona_ograniczen, maksimum=True):
    liczba_zmiennych = len(funkcja_celu)
    liczba_ograniczen = len(lewa_strona_ograniczen)

    #Dodanie zmiennych dodatkowych
    for i in range(liczba_ograniczen):
        for j in range(liczba_ograniczen):
            if i == j:
                lewa_strona_ograniczen[i].append(1)
            else:
                lewa_strona_ograniczen[i].append(0)
        funkcja_celu.append(0)
    suma_zmiennych = len(funkcja_celu)
    zmienne_bazowe = list(range(liczba_zmiennych, suma_zmiennych))

    iteracja = 0
    while True:
        #Obliczanie współczynnikiów bazowych cb
        wsp_cb = []
        for i in range(liczba_ograniczen):
            wsp_cb.append(funkcja_celu[zmienne_bazowe[i]])

        #Obliczanie wartości zj
        zj = []
        for j in range(suma_zmiennych):
            suma = 0
            for i in range(liczba_ograniczen):
                suma += wsp_cb[i] * lewa_strona_ograniczen[i][j]
            zj.append(suma)

        #Obliczanie różnicy cj - zj
        roznica_cj_zj = []
        for j in range(suma_zmiennych):
            roznica_cj_zj.append(funkcja_celu[j] - zj[j])

        print(f"\nIteracja {iteracja}")
        print(lewa_strona_ograniczen)
        print(prawa_strona_ograniczen)

        print("Zmienne bazowe:")
        print(f"{zmienne_bazowe}")

        print("cj - zj:")
        print(f"{roznica_cj_zj}")

        #Kryterium stopu
        stop = True
        for j in range(suma_zmiennych):
            warunek = roznica_cj_zj[j] > 0 if maksimum else roznica_cj_zj[j] < 0
            if warunek:
                stop = False
                break
        if stop:
            print("Kryterium stopu spełnione.")
            break

        #Zmienna wchodząca
        indeks_wchodzacy = 0
        najlepsza = roznica_cj_zj[0]
        for j in range(1, suma_zmiennych):
            warunek = roznica_cj_zj[j] > najlepsza if maksimum else roznica_cj_zj[j] < najlepsza
            if warunek:
                najlepsza = roznica_cj_zj[j]
                indeks_wchodzacy = j

        print("Zmienna wchodząca: x", indeks_wchodzacy + 1)

        #Kryterium wyjścia
        min_stosunek = float('inf')
        indeks_wychodzacy = -1
        for i in range(liczba_ograniczen):
            wsp = lewa_strona_ograniczen[i][indeks_wchodzacy]
            if wsp > 0:
                stosunek = prawa_strona_ograniczen[i] / wsp
                if stosunek < min_stosunek:
                    min_stosunek = stosunek
                    indeks_wychodzacy = i

        if indeks_wychodzacy == -1:
            print("Problem nieograniczony.")
            return

        print("Zmienna wychodząca: x", zmienne_bazowe[indeks_wychodzacy] + 1)

        #Operacja Gaussa
        wsp_pivot = lewa_strona_ograniczen[indeks_wychodzacy][indeks_wchodzacy]
        for j in range(suma_zmiennych):
            lewa_strona_ograniczen[indeks_wychodzacy][j] /= wsp_pivot
        prawa_strona_ograniczen[indeks_wychodzacy] /= wsp_pivot

        for i in range(liczba_ograniczen):
            if i != indeks_wychodzacy:
                mnoznik = lewa_strona_ograniczen[i][indeks_wchodzacy]
                for j in range(suma_zmiennych):
                    lewa_strona_ograniczen[i][j] -= mnoznik * lewa_strona_ograniczen[indeks_wychodzacy][j]
                prawa_strona_ograniczen[i] -= mnoznik * prawa_strona_ograniczen[indeks_wychodzacy]

        zmienne_bazowe[indeks_wychodzacy] = indeks_wchodzacy
        iteracja += 1

    #Wynik
    print("\nWynik")
    wynik = [0] * suma_zmiennych
    for i in range(liczba_ograniczen):
        wynik[zmienne_bazowe[i]] = prawa_strona_ograniczen[i]

    for i in range(liczba_zmiennych):
        print(f"x{i+1} = {wynik[i]}")

    wartosc_funkcji = 0
    for i in range(liczba_zmiennych):
        wartosc_funkcji += funkcja_celu[i] * wynik[i]
    print(f"f(x) = {wartosc_funkcji}")


funkcja_celu = [1, 2] #f(x) = x1 + 2x2
ograniczenia_lewa = [
    [1, 1], #x1 + x2 <= 10
    [-2, 1] #-2x1 + x2 <= 4
]
ograniczenia_prawa = [10, 4]
metoda_simplex(funkcja_celu, ograniczenia_lewa, ograniczenia_prawa, maksimum=True)