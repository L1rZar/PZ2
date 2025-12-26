import time
from functools import wraps

def log_call(func):
    """Печатает имя функции и аргументы перед вызовом."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} завершила работу")
        return result
    return wrapper

def measure_time(func):
    """Измеряет время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} заняла {end - start:.6f} сек")
        return result
    return wrapper

def validate_range(func):
    """
    Проверяет, что a < b и шаг > 0.
    Предполагаем сигнатуру: func(a, b, step, *args, **kwargs)
    """
    @wraps(func)
    def wrapper(a, b, step, *args, **kwargs):
        if step <= 0:
            raise ValueError("Шаг должен быть положительным")
        if a >= b:
            raise ValueError("a должно быть меньше b")
        return func(a, b, step, *args, **kwargs)
    return wrapper
