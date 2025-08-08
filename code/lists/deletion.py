from code.utils.decorators.time_decorator import timeit
from config import config
import time
import matplotlib.pyplot as plt

N_ITER = config.N_ITER


def time_list_deletion_op(
    lst: list,
    pos: int = None,
    n_iter: int = N_ITER,
):
    """
    Measures average time of del lst[pos],
    undoing each operation to keep the list size constant.
    """

    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        del lst[pos]
        total += time.perf_counter() - start

        # undo
        lst.insert(pos, 0)

    avg = total / n_iter
    print(f"Average time over {n_iter} iterations: {avg:.10f} seconds")
    return avg


def run_benchmarks():
    n_el = 100_000_000
    base = [0] * n_el
    positions = [
        0,
        int(0.1 * n_el),
        int(0.2 * n_el),
        int(0.4 * n_el),
        int(0.6 * n_el),
        int(0.8 * n_el),
        n_el - 1,
    ]
    times = [time_list_deletion_op(base, pos) for pos in positions]

    plt.figure(figsize=(10, 6))
    plt.plot(positions, times, marker="o")
    plt.title("Delete Time vs Position in List of 100,000 Elements")
    plt.xlabel("Delete Position")
    plt.ylabel("Average Time (seconds)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run_benchmarks()
