import time

def timing(func):
    """Dekorator mierzący czas wykonania funkcji."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Czas wykonania funkcji {}: {:.4f} s".format(func.__name__, end - start))
        return result
    return wrapper
