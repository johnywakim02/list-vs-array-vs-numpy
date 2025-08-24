from typing import Callable
import numpy as np
from numba import njit
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER

from numba import njit
import numpy as np


@timeit(n_iter=N_ITER)
@njit
def create_zeros_numba(n_el: int) -> np.ndarray:
    arr = np.empty(n_el)
    for i in range(n_el):
        arr[i] = 0
    return arr


@timeit(n_iter=N_ITER)
@njit
def create_ints_numba(n_el: int) -> np.ndarray:
    arr = np.empty(n_el)
    for i in range(n_el):
        arr[i] = i + 1
    return arr


@timeit(n_iter=N_ITER)
@njit
def create_floats_numba(n_el: int):
    arr = np.empty(n_el)
    for i in range(n_el):
        arr[i] = np.random.random() * 100
    return arr


def compute_time_and_draw(msg: str, method, array_sizes: list[int]) -> None:
    print(f"> {msg}")
    print("-" * 58)
    times = [method(size)[0] for size in array_sizes]
    plot_graph(
        array_sizes,
        times,
        title=msg,
        x_label="Numpy Array Size",
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
        100_000_000,
    ]
    print("removing setup costs")
    for i in range(5):
        create_zeros_numba(1000)
        create_ints_numba(1000)
        create_floats_numba(1000)
    print("*******************")

    methods_dict: dict[Callable, str] = {
        create_zeros_numba: "Creation time with numba of np arrays ofzeros vs numpy array size",
        create_ints_numba: "Creation time with numba of np arrays of range of ints vs numpy array size",
        create_floats_numba: "Creation time with numba of np arrays of random floats vs numpy array size",
    }
    for method, msg in methods_dict.items():
        compute_time_and_draw(msg, method, array_sizes)
