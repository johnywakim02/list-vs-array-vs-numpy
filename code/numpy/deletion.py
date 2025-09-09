import numpy as np
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from config import config
import time
import matplotlib.pyplot as plt

N_ITER = config.N_ITER


def time_numpy_deletion_op(
    arr: np.ndarray,
    pos: int = None,
    n_iter: int = N_ITER,
) -> float:
    """Measures average time of deleting from a numpy array,
    undoing each operation to keep the array size constant.


    Args:
        arr (np.ndarray): the initial numpy array
        pos (int, optional): the position at which to delete. Defaults to None.
        n_iter (int, optional): the number of iterations. Defaults to N_ITER.

    Returns:
        float: the average iteration time
    """

    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        arr = np.delete(arr, pos)
        total += time.perf_counter() - start

        # undo
        arr = np.insert(arr, pos, 0)

    avg = total / n_iter
    print(f"Average time over {n_iter} iterations: {avg:.10f} seconds")
    return avg


def run_numpy_benchmarks():
    n_el = 100_000_000
    base = np.zeros(n_el, dtype=np.int32)
    positions = [
        0,
        int(0.1 * n_el),
        int(0.2 * n_el),
        int(0.4 * n_el),
        int(0.6 * n_el),
        int(0.8 * n_el),
        n_el - 1,
    ]
    times = [time_numpy_deletion_op(base.copy(), pos) for pos in positions]

    plot_title = "Delete Time vs Position in NumPy Array of 100,000,000 Elements"
    plot_graph(
        positions, times, plot_title, "Delete Position", "Average Time (seconds)"
    )


if __name__ == "__main__":
    run_numpy_benchmarks()
