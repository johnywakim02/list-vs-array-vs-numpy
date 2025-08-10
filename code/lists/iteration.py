import matplotlib.pyplot as plt
from code.lists.creation import create_list, create_random_float_list
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def iterate_list(lst: list):
    for _ in lst:
        pass


@timeit(n_iter=N_ITER)
def iterate_list_summing(lst: list):
    total = 0.0
    for el in lst:
        total += el
    return total


def main():
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
    _, lst = create_random_float_list(n_el=list_sizes[-1])
    iterate_list_summing(lst)
    times = []
    for size in list_sizes:
        _, lst = create_list(n_el=size)
        time = iterate_list(lst)[0]
        times.append(time)

    plot_graph(
        list_sizes,
        times,
        "Iterate Time vs list size",
        "List Size",
        "Average full iteration Time (seconds)",
    )


if __name__ == "__main__":
    main()
