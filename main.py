from my_package import load_data, process_data, calculate_statistics, plot_data, show_histogram


def main():
    # Wczytaj przykładowe dane – podaj ścieżkę do własnego pliku CSV
    df = load_data("sample.csv")

    # Przetwórz dane (np. usunięcie braków, normalizacja)
    df = process_data(df)

    # Załóżmy, że istnieje kolumna 'norm', dla której obliczamy statystyki
    stats = calculate_statistics(df, 'norm')

    # Rysowanie wykresu – zakładamy, że w danych istnieją kolumny 'index' i 'norm'
    plot_data(df, x_column=df.columns[0], y_column='norm', title="Wykres normalizacji", xlabel="Indeks",
              ylabel="Wartość znormalizowana")

    # Rysowanie histogramu dla kolumny 'norm'
    show_histogram(df, column='norm', bins=30, title="Histogram kolumny 'norm'", xlabel="Wartość")


if __name__ == "__main__":
    main()
