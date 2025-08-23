import random
from array import array
from typing import Callable
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def create_array(n_el: int) -> array:
    return array("i", [0] * n_el)


@timeit(n_iter=N_ITER)
def create_array_from_iterable(n_el: int) -> array:
    return array("i", range(1, n_el + 1))


@timeit(n_iter=N_ITER)
def create_array_from_list_comprehension(n_el: int) -> array:
    return array("i", [i for i in range(n_el + 1)])


@timeit(n_iter=N_ITER)
def create_random_float_array(n_el: int) -> array:
    return array("f", [random.uniform(0, 100) for _ in range(n_el)])


def compute_time_and_draw(msg: str, method, array_sizes: list[int]) -> None:
    print(f"> {msg}")
    print("-" * 58)
    times = [method(size)[0] for size in array_sizes]
    plot_graph(
        array_sizes,
        times,
        title="Create Time vs array size",
        x_label="Array Size",
        y_label="Average Create Time (seconds)",
    )


if __name__ == "__main__":
    array_sizes = [
        0,
        1_000,
        1_000_000,
        10_000_000,
        20_000_000,
        40_000_000,
        80_000_000,
        100_000_000,
    ]
    methods_dict: dict[Callable, str] = {
        create_array: "Creating arrays",
        create_array_from_iterable: "Creating arrays from iterables",
        create_array_from_list_comprehension: "Creating arrays using list comprehensions",
        create_random_float_array: "Creating arrays of random floats between 0 and 100",
    }
    for method, msg in methods_dict.items():
        compute_time_and_draw(msg, method, array_sizes)
