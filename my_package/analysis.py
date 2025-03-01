import numpy as np
from .utils import timing

@timing
def calculate_statistics(df, column):
    """
    Oblicza podstawowe statystyki dla podanej kolumny w DataFrame:
      - średnia,
      - mediana,
      - odchylenie standardowe,
      - wartość minimalna i maksymalna.
    Parametry:
      - df: DataFrame z danymi
      - column: nazwa kolumny, dla której mają być obliczone statystyki
    Zwraca słownik ze statystykami.
    """
    if column not in df.columns:
        print("Brak kolumny {} w danych.".format(column))
        return None

    data = np.array(df[column])
    stats = {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data),
        'min': np.min(data),
        'max': np.max(data)
    }
    print("Obliczone statystyki dla kolumny {}:".format(column))
    for key, value in stats.items():
        print("  {}: {}".format(key, value))
    return stats
