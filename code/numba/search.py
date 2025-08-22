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


def test_search_types_on_hundred_million():
    arr = np.arange(1, 100_000_001)
    elements = [100, 10_000, 1_000_000, 100_000_000]
    methods = [
        np_search_element_presence,
        np_search_element_first_position,
        np_search_element_all_positions,
    ]
    # get the timing results
    for method in methods:
        for el in elements:
            method(arr, el)


def test_search_all_on_ten_thousand():
    print("**************")
    print("search an array with numba of 10k elements")
    size = 10_000
    arr = np.arange(1, size)
    np_search_element_all_positions(arr, 100)


def test_search_all_on_hundred():
    print("**************")
    print("search an array with numba of 100 elements")
    size = 100
    arr = np.arange(1, size)
    np_search_element_all_positions(arr, 100)


def test_search_all_on_million():
    print("**************")
    print("search an array with numba of 1M elements")
    size = 1_000_000
    arr = np.arange(1, size)
    np_search_element_all_positions(arr, 100)


if __name__ == "__main__":
    # eliminate compilation overhead:
    arr = np.arange(1, 1001)
    for i in range(3):
        njit_search_element_presence(arr, 10)
        njit_search_element_first_position(arr, 50)
        njit_search_element_all_positions(arr, 80)

    TESTS = {
        test_search_types_on_hundred_million: False,
        test_search_all_on_hundred: True,
        test_search_all_on_ten_thousand: True,
        test_search_all_on_million: True,
    }

    for test, flag in TESTS.items():
        if flag:
            test()
