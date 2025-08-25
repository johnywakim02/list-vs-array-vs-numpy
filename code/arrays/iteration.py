from array import array
import random
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def iterate_array(arr: array):
    for _ in arr:
        pass


@timeit(n_iter=N_ITER)
def iterate_array_summing(arr: array):
    total = 0.0
    for el in arr:
        total += el
    return total


def create_array(n_el: int) -> array:
    return array("i", [0] * n_el)


def create_random_float_array(n_el: int) -> array:
    return array("f", [random.uniform(0, 100) for _ in range(n_el)])


def test_iteration_on_million():
    print("************")
    print("> Testing iteration on 1 million")
    lst = create_random_float_array(n_el=100_000_000)
    iterate_array_summing(lst)


def test_iteration_and_draw():
    print("************")
    print("> Testing iteration for different sizes and plotting")
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
    times = []
    for size in list_sizes:
        lst = create_array(n_el=size)
        time = iterate_array(lst)[0]
        times.append(time)

    plot_graph(
        list_sizes,
        times,
        "Iterate Time vs array size",
        "Array Size",
        "Average full iteration Time (seconds)",
    )


if __name__ == "__main__":
    # Warm-up to avoid measuring initialization overhead
    print("***********")
    print("> Warm Up")
    warmup_array = create_random_float_array(1000)
    iterate_array_summing(warmup_array)
    # test_iteration_on_million()
    test_iteration_and_draw()
