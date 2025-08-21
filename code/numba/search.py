import numpy as np
from numba import njit
from code.utils.decorators.time_decorator import timeit
from numba.typed import List
from config import config

N_ITER = config.N_ITER


@njit
def njit_search_element_presence(arr, el):
    for i in range(arr.size):
        if arr[i] == el:
            return True
    return False


@njit
def njit_search_element_first_position(arr, el):
    for i in range(arr.size):
        if arr[i] == el:
            return i
    return -1  # not found


@njit
def njit_search_element_all_positions(arr, el):
    indices = List()
    for i in range(arr.size):
        if arr[i] == el:
            indices.append(i)
    return list(indices)


@timeit(n_iter=N_ITER)
def np_search_element_presence(arr: np.ndarray, el: int):
    return njit_search_element_presence(arr, el)


@timeit(n_iter=N_ITER)
def np_search_element_first_position(arr: np.ndarray, el: int):
    return njit_search_element_first_position(arr, el)


@timeit(n_iter=N_ITER)
def np_search_element_all_positions(arr: np.ndarray, el: int):
    return njit_search_element_all_positions(arr, el)


if __name__ == "__main__":
    arr = np.arange(1, 100_000_001)
    elements = [100, 10_000, 1_000_000, 100_000_000]
    methods = [
        np_search_element_presence,
        np_search_element_first_position,
        np_search_element_all_positions,
    ]
    # eliminate compilation overhead:
    for i in range(3):
        njit_search_element_presence(arr, elements[0])
        njit_search_element_first_position(arr, elements[0])
        njit_search_element_all_positions(arr, elements[0])
    # get the timing results
    # for method in methods:
    #     for el in elements:
    #         method(arr, el)

    size = 10_000
    arr = np.arange(1, size)
    np_search_element_all_positions(arr, 100)
