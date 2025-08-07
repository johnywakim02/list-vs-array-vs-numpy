import numpy as np
from numba import njit
from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
@njit
def create_floats_np_array_numba(n_el: int):
    result = np.empty(n_el)
    for i in range(n_el):
        result[i] = np.random.random() * 100
    return result


if __name__ == "__main__":
    create_floats_np_array_numba(100_000_000)
