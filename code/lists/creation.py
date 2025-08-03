from code.utils.decorators.time_decorator import timeit
import matplotlib.pyplot as plt
import random

N_ITER = 100


@timeit(n_iter=N_ITER)
def create_list(n_el: int):
    return [0] * n_el


@timeit(n_iter=N_ITER)
def create_list_from_iterable(n_el: int):
    return list(range(n_el))


@timeit(n_iter=N_ITER)
def create_list_comprehension(n_el: int):
    return [i for i in range(n_el)]


@timeit(n_iter=N_ITER)
def create_random_float_list(n_el: int):
    return [random.uniform(0, 100) for _ in range(n_el)]


def plot_graph(x_values, y_values):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker="o")
    plt.title("Create Time vs list size")
    plt.xlabel("List Size")
    plt.ylabel("Average Create Time (seconds)")
    plt.grid(True)
    plt.show()


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
    # print("> Creating lists")
    # print("-" * 58)
    # times = [create_list(size)[0] for size in list_sizes]
    # plot_graph(list_sizes, times)
    # print("> Creating lists from iterables")
    # print("-" * 58)
    # times = [create_list_from_iterable(size)[0] for size in list_sizes]
    # plot_graph(list_sizes, times)
    # print("> Creating lists using list comprehensions")
    # print("-" * 58)
    # times = [create_list_comprehension(size)[0] for size in list_sizes]
    # plot_graph(list_sizes, times)
    print("> Creating lists of random floats between 0 and 100")
    print("-" * 58)
    times = [create_random_float_list(size)[0] for size in list_sizes]
    plot_graph(list_sizes, times)
