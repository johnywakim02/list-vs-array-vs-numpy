import numpy as np
from code.utils.decorators.time_decorator import timeit
from numba import njit

N_ITER = 100_000_000


@timeit(n_iter=N_ITER)
@njit
def read_element(arr: np.ndarray, pos: int):
    return arr[pos]


@timeit(n_iter=N_ITER)
@njit
def write_element(arr: np.ndarray, pos: int, val: object):
    arr[pos] = val


if __name__ == "__main__":
    arr = np.random.rand(100_000_000) * 100
    read_element(arr, 100)
    read_element(arr, 100_000)
    read_element(arr, 99_999_998)
    write_element(arr, 100, 5.02)
    write_element(arr, 100_000, 72.8)
    write_element(arr, 99_999_998, 99)
