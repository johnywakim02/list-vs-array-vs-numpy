from __future__ import annotations
import random
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


@timeit(N_ITER)
def sort_numeric_list(lst: list[int | float]) -> list[int | float]:
    return sorted(lst)


if __name__ == "__main__":
    # max_el: int = 100_000
    # factors: list[float] = [i/50 for i in range(1, 51)]
    # sizes: list[int] = [int(factor * max_el) for factor in factors]
    # times: list[float] = []
    # for size in sizes:
    #     lst: list[float] = [random.uniform(0, 100) for _ in range(size)]
    #     print(size)
    #     time, _ = sort_numeric_list(lst)
    #     times.append(time)
    # plot_title: str = "Sorting time vs List size for a list of floats"
    # plot_graph(sizes, times, plot_title, "List Size", "Sorting Time (s)")

    lst = [random.uniform(0, 100) for _ in range(10_000_000)]
    sort_numeric_list(lst)
