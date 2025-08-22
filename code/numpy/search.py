import numpy as np
from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def np_search_element_presence(arr: np.ndarray, el: int):
    return el in arr


@timeit(n_iter=N_ITER)
def np_search_element_first_position(arr: np.ndarray, el: int):
    indices = np.where(arr == el)[0]
    if indices.size > 0:
        return indices[0]
    else:
        print(f"Element {el} was not found in the array.")


@timeit(n_iter=N_ITER)
def np_search_element_all_positions(arr: np.ndarray, el: int):
    return np.where(arr == el)[0].tolist()


def test_search_types_on_hundred_million():
    arr = np.arange(1, 100_000_001)  # Equivalent to [1, 2, ..., 100_000_000]
    elements = [100, 10_000, 1_000_000, 100_000_000]
    methods = [
        np_search_element_presence,
        np_search_element_first_position,
        np_search_element_all_positions,
    ]
    for method in methods:
        for el in elements:
            method(arr, el)


def test_search_all_on_ten_thousand():
    size = 10_000
    arr = np.arange(1, size)
    np_search_element_all_positions(arr, 100)


if __name__ == "__main__":
    TESTS = {
        test_search_types_on_hundred_million: True,
        test_search_all_on_ten_thousand: True,
    }

    for test, flag in TESTS.items():
        if flag:
            test()
