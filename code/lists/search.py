from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def search_element_presence(lst: list[int], el: int):
    return el in lst


@timeit(n_iter=N_ITER)
def search_element_first_position(lst: list[int], el: int):
    try:
        lst.index(el)
    except ValueError:
        print(f"Element {el} was not found in the list")


@timeit(n_iter=N_ITER)
def search_element_all_positions(lst: list[int], el: int):
    return [i for i, x in enumerate(lst) if x == el]


@timeit(n_iter=N_ITER)
def search_element_all_positions_v2(lst: list[int], el: int):
    indices = []
    start = 0
    while True:
        try:
            idx = lst.index(el, start)
            indices.append(idx)
            start = idx + 1
        except ValueError:
            break
    return indices


def test_search_types_on_hundred_million():
    lst = [i + 1 for i in range(100_000_000)]
    elements = [100, 10_000, 1_000_000, 100_000_000]
    methods = [
        search_element_presence,
        search_element_first_position,
        search_element_all_positions,
        search_element_all_positions_v2,
    ]
    for method in methods:
        for el in elements:
            method(lst, el)


def test_search_all_on_ten_thousand():
    size = 10_000
    lst = [i + 1 for i in range(size)]
    search_element_all_positions_v2(lst, 100)


if __name__ == "__main__":
    TESTS = {
        test_search_types_on_hundred_million: True,
        test_search_all_on_ten_thousand: True,
    }

    for test, flag in TESTS.items():
        if flag:
            test()
