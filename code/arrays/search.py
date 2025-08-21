import array
from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def arr_search_element_presence(arr: array.array, el: int):
    return el in arr


@timeit(n_iter=N_ITER)
def arr_search_element_first_position(arr: array.array, el: int):
    try:
        return arr.index(el)
    except ValueError:
        print(f"Element {el} was not found in the array.")


@timeit(n_iter=N_ITER)
def arr_search_element_all_positions(arr: array.array, el: int):
    return [i for i, x in enumerate(arr) if x == el]


if __name__ == "__main__":
    arr = array.array("I", range(1, 100_000_001))  # 'I' = unsigned int
    elements = [100, 10_000, 1_000_000, 100_000_000]
    methods = [
        arr_search_element_presence,
        arr_search_element_first_position,
        arr_search_element_all_positions,
    ]
    for method in methods:
        for el in elements:
            method(arr, el)

    size = 10_000
    arr = array.array("I", range(1, size))
    arr_search_element_all_positions(arr, 100)
