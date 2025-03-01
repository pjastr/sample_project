import matplotlib.pyplot as plt

def plot_data(df, x_column, y_column, title="Wykres", xlabel="", ylabel=""):
    """
    Rysuje wykres liniowy na podstawie podanych kolumn z DataFrame.
    Parametry:
      - df: DataFrame z danymi
      - x_column: nazwa kolumny na osi X
      - y_column: nazwa kolumny na osi Y
      - title: tytuł wykresu
      - xlabel: etykieta osi X
      - ylabel: etykieta osi Y
    """
    if x_column not in df.columns or y_column not in df.columns:
        print("Podana kolumna nie istnieje w danych.")
        return

    plt.figure()
    plt.plot(df[x_column], df[y_column], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_column)
    plt.ylabel(ylabel if ylabel else y_column)
    plt.grid(True)
    plt.show()

def show_histogram(df, column, bins=20, title="Histogram", xlabel="Wartości"):
    """
    Rysuje histogram dla danej kolumny.
    Parametry:
      - df: DataFrame z danymi
      - column: nazwa kolumny, dla której ma być rysowany histogram
      - bins: liczba koszyków (bins) w histogramie
      - title: tytuł wykresu
      - xlabel: etykieta osi X
    """
    if column not in df.columns:
        print("Kolumna {} nie istnieje.".format(column))
        return

    plt.figure()
    plt.hist(df[column], bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Częstotliwość")
    plt.grid(True)
    plt.show()
