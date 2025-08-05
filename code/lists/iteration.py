import matplotlib.pyplot as plt
from code.lists.creation import create_list, create_random_float_list
from code.utils.decorators.time_decorator import timeit

N_ITER = 100


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
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, times, marker="o")
    plt.title("Iterate Time vs list size")
    plt.xlabel("List Size")
    plt.ylabel("Average full iteration Time (seconds)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
