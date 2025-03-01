import pandas as pd
import numpy as np

def load_data(file_path, sep=','):
    """
    Wczytuje dane z pliku CSV do DataFrame.
    Parametry:
      - file_path: ścieżka do pliku CSV
      - sep: separator kolumn (domyślnie przecinek)
    Zwraca:
      - obiekt DataFrame
    """
    try:
        df = pd.read_csv(file_path, sep=sep)
        print("Dane wczytane poprawnie z {}".format(file_path))
        return df
    except Exception as e:
        print("Błąd przy wczytywaniu danych:", e)
        return None

def process_data(df):
    """
    Przykładowa funkcja przetwarzająca dane.
    W tym przykładzie:
      - Usuwamy wiersze z brakującymi wartościami.
      - Dodajemy kolumnę 'norm' będącą normalizacją pierwszej kolumny numerycznej.
    """
    if df is None or df.empty:
        print("DataFrame jest pusty lub nie istnieje!")
        return df

    # Usunięcie wierszy z brakującymi danymi
    df = df.dropna()

    # Wyszukanie pierwszej kolumny numerycznej
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        # Normalizacja – (wartość - min) / (max - min)
        df['norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        print("Dodano kolumnę 'norm' na podstawie kolumny {}".format(col))
    else:
        print("Brak kolumn numerycznych do normalizacji.")
    return df
