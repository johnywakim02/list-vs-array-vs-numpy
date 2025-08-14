import time
from functools import wraps


def timeit(n_iter: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            for _ in range(n_iter):
                result = func(*args, **kwargs)
            end = time.perf_counter()
            duration = (end - start) / n_iter
            print(f"{func.__name__} took {duration:.8f} seconds")
            return duration, result

        return wrapper

    return decorator
