import numpy as np
from numba import njit
import time
import matplotlib.pyplot as plt
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


# Numba replacement for np.delete
@njit
def delete_element(arr: np.ndarray, pos: int) -> np.ndarray:
    """Delete an element from the array at a certain position

    Args:
        arr (np.ndarray): the array to delete from
        pos (int): the position of the element at which to delete

    Returns:
        np.ndarray: the array withou the deleted element
    """
    n = arr.size
    result = np.empty(n - 1, dtype=arr.dtype)
    for i in range(pos):
        result[i] = arr[i]
    for i in range(pos + 1, n):
        result[i - 1] = arr[i]
    return result


# to counterbalance deletion between operations
@njit
def insert_element(arr: np.ndarray, pos: int, value: object) -> np.ndarray:
    """Add element at a specified position

    Args:
        arr (np.ndarray): the array to add to
        pos (int): the position at which to add
        value (object): the value to add

    Returns:
        np.ndarray: the array after adding the element
    """
    n = arr.size
    result = np.empty(n + 1, dtype=arr.dtype)
    for i in range(pos):
        result[i] = arr[i]
    result[pos] = value
    for i in range(pos, n):
        result[i + 1] = arr[i]
    return result


# Benchmark function using Numba delete
def time_numba_deletion_op(arr: np.ndarray, pos: int = None, n_iter: int = N_ITER):
    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        arr = delete_element(arr, pos)
        total += time.perf_counter() - start

        # Undo
        arr = insert_element(arr, pos, 0)

    avg = total / n_iter
    print(f"Average time over {n_iter} iterations: {avg:.10f} seconds")
    return avg


# Benchmark runner
def run_numba_benchmarks():
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
    times = [time_numba_deletion_op(base.copy(), pos) for pos in positions]

    plot_title = "Delete Time vs Position in Numba Array of 100,000,000 Elements"
    plot_graph(
        positions, times, plot_title, "Delete Position", "Average Time (seconds)"
    )


if __name__ == "__main__":
    base = np.zeros(100_000_000, dtype=np.int32)
    # warmup
    for i in range(1, 100_001, 1000):
        delete_element(base, i)
    run_numba_benchmarks()
