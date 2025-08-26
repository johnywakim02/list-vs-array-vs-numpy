import numpy as np
from numba import njit
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


def create_np_array(n_el: int) -> np.ndarray:
    return np.zeros(n_el, dtype=np.int32)


def create_random_float_np_array(n_el: int) -> np.ndarray:
    return np.random.rand(n_el) * 100


@timeit(n_iter=N_ITER)
@njit
def iterate_np_array_wnumba(arr: np.ndarray):
    for _ in arr:
        pass


@timeit(n_iter=N_ITER)
@njit
def iterate_np_array_summing_wnumba(arr: np.ndarray):
    total = 0.0
    for el in arr:
        total += el
    return total


def test_iteration_on_million():
    print("************")
    print("> Testing iteration on 1 million")
    np_array = create_random_float_np_array(100_000_000)
    iterate_np_array_wnumba(np_array)


def test_iteration_and_draw():
    print("************")
    print("> Testing iteration for different sizes and plotting")
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

    # test
    times = []
    for size in array_sizes:
        arr = create_np_array(n_el=size)
        time = iterate_np_array_wnumba(arr)[0]
        times.append(time)

    plot_graph(
        array_sizes,
        times,
        title="Iterate Time vs NumPy array size",
        x_label="Numpy Array Size",
        y_label="Average Full Iteration Time (seconds)",
    )


if __name__ == "__main__":
    # Warm-up to avoid measuring initialization overhead
    print("***********")
    print("> Warm Up")
    warmup_array_sizes = [1000, 10_000, 100_000, 1_000_000, 100_000_000]
    for size in warmup_array_sizes:
        warmup_array = create_np_array(size)
        iterate_np_array_wnumba(warmup_array)

    # real tests
    TESTS = {
        test_iteration_on_million: False,
        test_iteration_and_draw: True,
    }

    for test, flag in TESTS.items():
        if flag:
            test()
