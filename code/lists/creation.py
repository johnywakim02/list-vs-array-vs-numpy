from code.utils.decorators.time_decorator import timeit
import matplotlib.pyplot as plt


@timeit(n_iter=100)
def create_list(n_el: int):
    return [0] * n_el


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
    times = [create_list(size)[0] for size in list_sizes]
    plot_graph(list_sizes, times)
