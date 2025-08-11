import numpy as np
from code.utils.decorators.time_decorator import timeit
from config import config
from numba import jit

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
@jit
def sort_numpy_array(arr: np.ndarray) -> np.ndarray:
    return np.sort(arr)


if __name__ == "__main__":
    n_el = 10_000_000
    arr = np.random.uniform(0, 100, n_el)
    sort_numpy_array(arr)
