import pandas as pd
import matplotlib.pyplot as plt

# Zadane wartości referencyjne
x_A = 1.3815245817028652
y_A = 0.5876863878000603

# Epsilony i iteracje
epsilon_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
iterations = [2, 4, 6, 8, 10, 12]

methods = [
    "Metoda Newtona",
    "Najszybszego Spadku",
    "Gausa-Seidla",
    "Hooka-Jeveesa"
]

# Wartości x i y przy różnych epsilonach
x_eps = [
    [1.3817391009883209, 1.3817391009883209, 1.3815245817028652, 1.3815245817028652, 1.3815245817028652, 1.3815245817028652],
    [1.1306907863259439, 1.3671431037937454, 1.3799593128033985, 1.381345926301103, 1.3815040665358465, 1.3815221939710107],
    [1.4369478889744256, 1.3871094699309858, 1.3821087584790068, 1.3816004876543935, 1.3815487592928788, 1.381543494027024],
    [1.375, 1.40625, 1.37890625, 1.3818359375, 1.381561279296875, 1.3815441131591797]
]

y_eps = [
    [0.5878294481745724, 0.5878294481745724, 0.5876863878000603, 0.5876863878000603, 0.5876863878000603, 0.5876863878000603],
    [0.5287603682746624, 0.5847607844883101, 0.5873704360394092, 0.5876503383170967, 0.587682231551334, 0.5876858872015714],
    [0.599363806277042, 0.5888780582847067, 0.5878156085611045, 0.5877075139574996, 0.587696511706294, 0.5876953918104892],
    [0.625, 0.609375, 0.587890625, 0.587890625, 0.58770751953125, 0.5876960754394531]
]

# Wartości x i y przy różnych liczbach iteracji
x_iter = [
    [1.3977849872715062, 1.3815245817028652, 1.3815245407002334, 1.3815245407002334, 1.3815245407002334, 1.3815245407002334],
    [1.1306907863259439, 1.3496514196220701, 1.3671431037937454, 1.3747537294054872, 1.3782815921311067, 1.3799593128033985],
    [1.560660171780381, 1.399045709415563, 1.3833170874270602, 1.3817234128416567, 1.3815612709362495, 1.381544767559441],
    [2.5, 2.0, 1.0, 1.375, 1.4375, 1.5625]
]

y_iter = [
    [0.5985274910657746, 0.5876863878000603, 0.5876863604649725, 0.5876863604649725, 0.5876863604649725, 0.5876863604649725],
    [0.5287603682746624, 0.5811325919713152, 0.5847607844883101, 0.586315400879357, 0.5870311399922433, 0.5873704360394092],
    [0.6246319259829505, 0.5914063132873238, 0.5880725056526712, 0.5877336584362622, 0.5876991728619192, 0.5876956626846825],
    [1.0, 0.5, 0.25, 0.625, 0.6875, 0.625]
]

# Tworzenie DataFrame'ów
df_x_eps = pd.DataFrame(x_eps, index=methods, columns=epsilon_values)
df_y_eps = pd.DataFrame(y_eps, index=methods, columns=epsilon_values)
df_x_iter = pd.DataFrame(x_iter, index=methods, columns=iterations)
df_y_iter = pd.DataFrame(y_iter, index=methods, columns=iterations)

# Funkcja błędu względnego
def relative_error(true_val, approx_val):
    return abs((true_val - approx_val) / true_val) * 100 if approx_val is not None else None

# Obliczanie błędów względnych
df_err_x_eps = df_x_eps.applymap(lambda x: relative_error(x_A, x))
df_err_y_eps = df_y_eps.applymap(lambda y: relative_error(y_A, y))
df_err_x_iter = df_x_iter.applymap(lambda x: relative_error(x_A, x))
df_err_y_iter = df_y_iter.applymap(lambda y: relative_error(y_A, y))

# Zapis do CSV
df_err_x_eps.to_csv("epsilon_x.csv")
df_err_y_eps.to_csv("epsilon_y.csv")
df_err_x_iter.to_csv("iter_x.csv")
df_err_y_iter.to_csv("iter_y.csv")

# Wykresy
def plot_errors(df, title, xlabel):
    plt.figure(figsize=(12, 6))
    df.T.plot(kind='bar', figsize=(12, 6), alpha=0.75)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Błąd względny (%)")
    plt.legend(title="Metody")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

plot_errors(df_err_x_eps, "Błąd względny zmiennej x (epsilon)", "Epsilon")
plot_errors(df_err_y_eps, "Błąd względny zmiennej y (epsilon)", "Epsilon")
plot_errors(df_err_x_iter, "Błąd względny zmiennej x (iteracje)", "Liczba iteracji")
plot_errors(df_err_y_iter, "Błąd względny zmiennej y (iteracje)", "Liczba iteracji")
