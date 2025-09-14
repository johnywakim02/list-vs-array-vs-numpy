import time
import numpy as np
import matplotlib.pyplot as plt
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


def time_numpy_insertion_op(
    arr: np.ndarray,
    element: int,
    action: str = "append",
    pos: int = None,
    n_iter: int = N_ITER,
):
    """
    Measures average time of np.append or np.insert on arr,
    discarding the new arrays to keep arr unchanged.
    """
    if action not in ("append", "insert"):
        raise ValueError(f"action cannot have value '{action}'")

    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        if action == "append":
            _ = np.append(arr, element)
        else:
            _ = np.insert(arr, pos, element)
        total += time.perf_counter() - start

    avg = total / n_iter
    print(f"Average {action} time over {n_iter} iterations: {avg:.10f} seconds")
    return avg


def run_benchmarks():
    tests = [
        (
            "Append with numpy array of 3 elements",
            np.array([1, 2, 3], dtype=np.int32),
            4,
            "append",
            None,
        ),
        (
            "Append with numpy array of 1000 elements",
            np.arange(1001, dtype=np.int32),
            1001,
            "append",
            None,
        ),
        (
            "Append with numpy array of 100000 elements",
            np.arange(100001, dtype=np.int32),
            51,
            "append",
            None,
        ),
        (
            "Insert with numpy array of 10 elements at beg/mid/end",
            np.arange(11, dtype=np.int32),
            999,
            "insert",
            [2, 5, 8],
        ),
        (
            "Insert with numpy array of 1000 elements at beg/mid/end",
            np.arange(1001, dtype=np.int32),
            999,
            "insert",
            [50, 450, 850],
        ),
        (
            "Insert with numpy array of 100000 elements at beg/mid/end",
            np.arange(100001, dtype=np.int32),
            999,
            "insert",
            [50, 50000, 99500],
        ),
        (
            "Insert with numpy array of 100_000_000 elements at beg/mid/end",
            np.arange(100_000_001, dtype=np.int32),
            999,
            "insert",
            [50, 50000000, 99999500],
        ),
    ]

    for desc, arr, elem, action, positions in tests:
        print(f"> {desc}")
        print("-" * len(desc))
        if positions is None:
            time_numpy_insertion_op(arr, elem, action)
        else:
            for pos in positions:
                print(f"Insert at index {pos}:", end=" ")
                time_numpy_insertion_op(arr, elem, action, pos)
        print()

    # draw graph for large insertions
    print("> Insert with numpy array of 10,000,000 elements at various positions")
    print("-" * 61)
    base = np.arange(10_000_000, dtype=np.int32)
    pos_list = [
        0,
        1_000_000,
        2_000_000,
        4_000_000,
        6_000_000,
        8_000_000,
        10_000_000,
    ]
    times = [time_numpy_insertion_op(base, 999, "insert", pos) for pos in pos_list]

    plot_title = "Insert Time vs Position in Numpy Array of 10,000,000 Elements"
    plot_graph(pos_list, times, plot_title, "Insert Position", "Average Time (seconds)")

    # draw graph of insertion at position 0 for increasing array sizes
    print("> Insert with numpy arrays of various sizes up to 10M, at position 0")
    print("-" * 61)
    sizes = [0, 1_000_000, 2_000_000, 4_000_000, 6_000_000, 8_000_000, 10_000_000]
    base_arrays = [np.zeros(size, dtype=np.int32) for size in sizes]
    times = [time_numpy_insertion_op(arr, 999, "insert", 0) for arr in base_arrays]

    plot_title = "Insert Time vs Length of Numpy Array, Inserting at Position 0"
    plot_graph(
        sizes,
        times,
        plot_title,
        "Array Length",
        "Average Time (seconds)",
    )


if __name__ == "__main__":
    run_benchmarks()
