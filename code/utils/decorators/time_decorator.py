import time
from functools import wraps

N_ITER = 1000


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        for i in range(N_ITER):
            result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = (end - start) / N_ITER
        print(f"{func.__name__} took {duration:.8f} seconds")
        return result

    return wrapper
