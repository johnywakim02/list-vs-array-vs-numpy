import numpy as np
from numba import njit
from code.utils.decorators.time_decorator import timeit

N_ITER = 100


@timeit(n_iter=N_ITER)
@njit
def iterate_numpy_array_wnumba(np_array):
    total = 0.0
    for el in np_array:
        total += el
    return total


if __name__ == "__main__":
    arr = np.random.rand(100_000_000)
    iterate_numpy_array_wnumba(arr)
