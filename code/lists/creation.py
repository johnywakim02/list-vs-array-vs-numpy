from typing import Callable
from code.utils.decorators.time_decorator import timeit
import matplotlib.pyplot as plt
import random
from enum import Enum
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def create_list(n_el: int) -> list[int]:
    return [0] * n_el


@timeit(n_iter=N_ITER)
def create_list_from_iterable(n_el: int) -> list[int]:
    return list(range(n_el))


@timeit(n_iter=N_ITER)
def create_list_comprehension(n_el: int) -> list[int]:
    return [i for i in range(n_el)]


@timeit(n_iter=N_ITER)
def create_random_float_list(n_el: int) -> list[float]:
    return [random.uniform(0, 100) for _ in range(n_el)]


def compute_time_and_draw(msg: str, method, list_sizes: list[int]) -> None:
    print(f"> {msg}")
    print("-" * 58)
    times = [method(size)[0] for size in list_sizes]
    plot_graph(
        list_sizes,
        times,
        title="Create Time vs list size",
        x_label="List Size",
        y_label="Average Create Time (seconds)",
    )


if __name__ == "__main__":
    list_sizes = [
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
        create_list: "Creating lists",
        create_list_from_iterable: "Creating lists from iterables",
        create_list_comprehension: "Creating lists using list comprehensions",
        create_random_float_list: "Creating lists of random floats between 0 and 100",
    }

    for method, msg in methods_dict.items():
        compute_time_and_draw(msg, method, list_sizes)
