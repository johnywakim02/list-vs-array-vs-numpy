import array
from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def arr_search_element_presence(arr: array.array, el: int) -> bool:
    return el in arr


@timeit(n_iter=N_ITER)
def arr_search_element_first_position(arr: array.array, el: int) -> int | None:
    try:
        return arr.index(el)
    except ValueError:
        print(f"Element {el} was not found in the array.")


@timeit(n_iter=N_ITER)
def arr_search_element_all_positions(arr: array.array, el: int) -> list[int]:
    return [i for i, x in enumerate(arr) if x == el]


# Test 1
def test_search_types_on_hundred_million():
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


def test_search_all_on_ten_thousand():
    print("************")
    print("> Searching for all occurences of an element in an array of 10k element")
    size = 10_000
    arr = array.array("I", range(1, size))
    arr_search_element_all_positions(arr, 100)


def test_search_all_on_hundred():
    print("************")
    print("> Searching for all occurences of an element in an array of 100 element")
    size = 100
    arr = array.array("I", range(1, size))
    arr_search_element_all_positions(arr, 100)


def test_search_all_on_million():
    print("************")
    print("> Searching for all occurences of an element in an array of 1M element")
    size = 1_000_000
    arr = array.array("I", range(1, size))
    arr_search_element_all_positions(arr, 100)


if __name__ == "__main__":
    TESTS = {
        test_search_types_on_hundred_million: False,
        test_search_all_on_hundred: True,
        test_search_all_on_ten_thousand: True,
        test_search_all_on_million: True,
    }

    for test, flag in TESTS.items():
        if flag:
            test()
