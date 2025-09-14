import time
import array
import matplotlib.pyplot as plt
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


def time_array_insertion_op(
    arr: array.array,
    element: int,
    action: str = "append",
    pos: int = None,
    n_iter: int = N_ITER,
):
    """
    Measures average time of arr.append(element) or arr.insert(pos, element),
    undoing each operation to keep the array size constant.
    """
    if action not in ("append", "insert"):
        raise ValueError(f"action cannot have value '{action}'")

    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        if action == "append":
            arr.append(element)
        else:
            arr.insert(pos, element)
        total += time.perf_counter() - start

        # undo
        if action == "append":
            arr.pop()
        else:
            del arr[pos]

    avg = total / n_iter
    print(f"Average {action} time over {n_iter} iterations: {avg:.10f} seconds")
    return avg


def run_benchmarks():
    tests = [
        (
            "Append with array of 3 elements",
            array.array("i", [1, 2, 3]),
            4,
            "append",
            None,
        ),
        (
            "Append with array of 1000 elements",
            array.array("i", range(1001)),
            1001,
            "append",
            None,
        ),
        (
            "Append with array of 100000 elements",
            array.array("i", range(100001)),
            51,
            "append",
            None,
        ),
        (
            "Insert with array of 10 elements at beg/mid/end",
            array.array("i", range(11)),
            999,
            "insert",
            [2, 5, 8],
        ),
        (
            "Insert with array of 1000 elements at beg/mid/end",
            array.array("i", range(1001)),
            999,
            "insert",
            [50, 450, 850],
        ),
        (
            "Insert with array of 100000 elements at beg/mid/end",
            array.array("i", range(100001)),
            999,
            "insert",
            [50, 50000, 99500],
        ),
        (
            "Insert with array of 100_000_000 elements at beg/mid/end",
            array.array("i", range(100_000_001)),
            999,
            "insert",
            [50, 50_000_000, 99_999_500],
        ),
    ]

    for desc, arr, elem, action, positions in tests:
        print(f"> {desc}")
        print("-" * len(desc))
        if positions is None:
            time_array_insertion_op(arr, elem, action)
        else:
            for pos in positions:
                print(f"Insert at index {pos}:", end=" ")
                time_array_insertion_op(arr, elem, action, pos)
        print()

    # draw graph for 100M‐element insert
    print("> Insert with array of 100,000,000 elements at various positions")
    print("-" * 61)
    base = array.array("i", range(100_000_000))
    pos_list = [
        0,
        10_000_000,
        20_000_000,
        40_000_000,
        60_000_000,
        80_000_000,
        100_000_000,
    ]
    times = [time_array_insertion_op(base, 999, "insert", pos) for pos in pos_list]

    plot_title = "Insert Time vs Position in Array of 100,000,000 Elements"
    plot_graph(pos_list, times, plot_title, "Insert Position", "Average Time (seconds)")

    # draw graph of insertion at position 0 for increasing array sizes
    print("> Insert with arrays of various sizes up to 100M, at position 0")
    print("-" * 61)
    sizes = [0, 10_000_000, 20_000_000, 40_000_000, 60_000_000, 80_000_000, 100_000_000]
    base_arrays = [array.array("i", [0] * size) for size in sizes]
    times = [time_array_insertion_op(arr, 999, "insert", 0) for arr in base_arrays]

    plot_title = "Insert Time vs Length of Array, Inserting at Position 0"
    plot_graph(
        sizes,
        times,
        plot_title,
        "Array Length",
        "Average Time (seconds)",
    )


if __name__ == "__main__":
    run_benchmarks()
