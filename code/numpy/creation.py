from typing import Callable
import numpy as np
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def create_zeros_np_array(n_el: int) -> np.ndarray:
    return np.zeros(n_el, dtype=np.int32)


@timeit(n_iter=N_ITER)
def create_ints_np_array(n_el: int) -> np.ndarray:
    return np.arange(1, n_el + 1, dtype=np.int32)


@timeit(n_iter=N_ITER)
def create_floats_np_array(n_el: int):
    return np.random.rand(n_el) * 100


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
        80_000_000,
        100_000_000,
    ]
    print("removing setup costs")
    for i in range(5):
        create_zeros_np_array(1000)
        create_ints_np_array(1000)
        create_floats_np_array(1000)
    print("*******************")

    methods_dict: dict[Callable, str] = {
        create_zeros_np_array: "Creation time of numpy array of zeros vs numpy array size",
        create_ints_np_array: "Creation time of numpy array of range of ints vs numpy array size",
        create_floats_np_array: "Creation time of numpy array of random floats vs numpy array size",
    }
    for method, msg in methods_dict.items():
        compute_time_and_draw(msg, method, array_sizes)
