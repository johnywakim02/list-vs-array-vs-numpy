import numpy as np
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


def create_np_array(n_el: int, value: float = 0.0) -> np.ndarray:
    return np.full(n_el, value)


def create_random_float_np_array(n_el: int) -> np.ndarray:
    return np.random.rand(n_el) * 100


@timeit(n_iter=N_ITER)
def iterate_np_array(arr: np.ndarray):
    for _ in arr:
        pass


@timeit(n_iter=N_ITER)
def iterate_np_array_summing(arr: np.ndarray):
    total = 0.0
    for el in arr:
        total += el
    return total


def main():
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

    # Warm-up
    warmup_arr = create_random_float_np_array(1000)
    iterate_np_array_summing(warmup_arr)

    # Tests
    np_array = create_random_float_np_array(100_000_000)
    iterate_np_array(np_array)

    times = []
    for size in array_sizes:
        arr = create_np_array(n_el=size)
        time = iterate_np_array(arr)[0]
        times.append(time)

    plot_graph(
        array_sizes,
        times,
        title="Iterate Time vs NumPy array size",
        x_label="Array Size",
        y_label="Average Full Iteration Time (seconds)",
    )


if __name__ == "__main__":
    main()
