import time
import numpy as np
import matplotlib.pyplot as plt
from code.utils.methods.draw import plot_graph
from config import config

N_ITER = config.N_ITER


def time_list_insertion_op(
    lst: list,
    element: object,
    action: str = "append",
    pos: int = None,
    n_iter: int = N_ITER,
):
    if action not in ("append", "insert"):
        raise ValueError(f"action cannot have value '{action}'")

    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        if action == "append":
            lst.append(element)
        else:
            lst.insert(pos, element)
        total += time.perf_counter() - start

        # undo
        if action == "append":
            lst.pop()
        else:
            del lst[pos]

    avg = total / n_iter
    print(f"Average {action} time over {n_iter} iterations: {avg:.10f} seconds")
    return avg


def time_array_insertion_op(
    arr: np.ndarray,
    element: object,
    action: str = "append",
    pos: int = None,
    n_iter: int = N_ITER,
):
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
    print(f"Average {action} time over {n_iter} iterations (array): {avg:.10f} seconds")
    return avg


def time_numpy_insertion_op(
    arr: np.ndarray,
    element: object,
    action: str = "append",
    pos: int = None,
    n_iter: int = N_ITER,
):
    """
    For numpy arrays, append and insert return new arrays, so
    time measured includes copying the whole array with the new element.
    """
    if action not in ("append", "insert"):
        raise ValueError(f"action cannot have value '{action}'")

    total = 0.0
    for _ in range(n_iter):
        start = time.perf_counter()
        if action == "append":
            # Append element at the end (axis=None flattens array)
            new_arr = np.append(arr, element)
        else:
            new_arr = np.insert(arr, pos, element)
        total += time.perf_counter() - start

        # no undo needed since original arr not modified

    avg = total / n_iter
    print(f"Average {action} time over {n_iter} iterations (numpy): {avg:.10f} seconds")
    return avg


def run_benchmarks():
    # List tests (same as before)
    tests = [
        (
            "Append with list of 3 elements",
            ["chihuahua", "bulldog", "butterfly"],
            "bernese",
            "append",
            None,
        ),
        ("Append with list of 1000 elements", list(range(1001)), 1001, "append", None),
        (
            "Append with list of 100000 elements",
            list(range(100001)),
            51,
            "append",
            None,
        ),
        (
            "Insert with list of 10 elements at beg/mid/end",
            list(range(11)),
            "hello",
            "insert",
            [2, 5, 8],
        ),
        (
            "Insert with list of 1000 elements at beg/mid/end",
            list(range(1001)),
            "hello",
            "insert",
            [50, 450, 850],
        ),
        (
            "Insert with list of 100000 elements at beg/mid/end",
            list(range(100001)),
            "hello",
            "insert",
            [50, 50000, 99500],
        ),
    ]

    for desc, lst, elem, action, positions in tests:
        print(f"> {desc} (list)")
        print("-" * len(desc))
        if positions is None:
            time_list_insertion_op(lst, elem, action)
        else:
            for pos in positions:
                print(f"Insert at index {pos}:", end=" ")
                time_list_insertion_op(lst, elem, action, pos)
        print()

    # Array tests (int arrays)
    import array

    array_tests = [
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
            99,
            "insert",
            [2, 5, 8],
        ),
        (
            "Insert with array of 1000 elements at beg/mid/end",
            array.array("i", range(1001)),
            99,
            "insert",
            [50, 450, 850],
        ),
        (
            "Insert with array of 100000 elements at beg/mid/end",
            array.array("i", range(100001)),
            99,
            "insert",
            [50, 50000, 99500],
        ),
    ]

    for desc, arr, elem, action, positions in array_tests:
        print(f"> {desc} (array)")
        print("-" * len(desc))
        if positions is None:
            time_array_insertion_op(arr, elem, action)
        else:
            for pos in positions:
                print(f"Insert at index {pos}:", end=" ")
                time_array_insertion_op(arr, elem, action, pos)
        print()

    # NumPy tests (integers)
    numpy_tests = [
        (
            "Append with numpy array of 3 elements",
            np.array([1, 2, 3]),
            4,
            "append",
            None,
        ),
        (
            "Append with numpy array of 1000 elements",
            np.arange(1001),
            1001,
            "append",
            None,
        ),
        (
            "Append with numpy array of 100000 elements",
            np.arange(100001),
            51,
            "append",
            None,
        ),
        (
            "Insert with numpy array of 10 elements at beg/mid/end",
            np.arange(11),
            99,
            "insert",
            [2, 5, 8],
        ),
        (
            "Insert with numpy array of 1000 elements at beg/mid/end",
            np.arange(1001),
            99,
            "insert",
            [50, 450, 850],
        ),
        (
            "Insert with numpy array of 100000 elements at beg/mid/end",
            np.arange(100001),
            99,
            "insert",
            [50, 50000, 99500],
        ),
    ]

    for desc, arr, elem, action, positions in numpy_tests:
        print(f"> {desc} (numpy)")
        print("-" * len(desc))
        if positions is None:
            time_numpy_insertion_op(arr, elem, action)
        else:
            for pos in positions:
                print(f"Insert at index {pos}:", end=" ")
                time_numpy_insertion_op(arr, elem, action, pos)
        print()


if __name__ == "__main__":
    run_benchmarks()
