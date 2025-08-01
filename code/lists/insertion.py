import time
import matplotlib.pyplot as plt

N_ITER = 100


def time_list_insertion_op(lst, element, action="append", pos=None, n_iter=N_ITER):
    """
    Measures average time of lst.append(element) or lst.insert(pos, element),
    undoing each operation to keep the list size constant.
    """
    # Validate action once
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


def run_benchmarks():
    # (description, initial_list, element, action, positions or None)
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
        (
            "Insert with list of 100_000_000 elements at beg/mid/end",
            list(range(100000001)),
            "hello",
            "insert",
            [50, 50000000, 99999500],
        ),
    ]

    for desc, lst, elem, action, positions in tests:
        print(f"> {desc}")
        print("-" * len(desc))
        if positions is None:
            time_list_insertion_op(lst, elem, action)
        else:
            for pos in positions:
                print(f"Insert at index {pos}:", end=" ")
                time_list_insertion_op(lst, elem, action, pos)
        print()

    # Special: draw graph for 100k‐element insert
    print("> Insert with list of 100000 elements at various positions")
    print("-" * 58)
    base = list(range(100000))
    pos_list = [0, 12500, 25000, 37500, 50000, 62500, 75000, 87500, 99999]
    times = [time_list_insertion_op(base, "hello", "insert", pos) for pos in pos_list]

    plt.figure(figsize=(10, 6))
    plt.plot(pos_list, times, marker="o")
    plt.title("Insert Time vs Position in List of 100,000 Elements")
    plt.xlabel("Insert Position")
    plt.ylabel("Average Time (seconds)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run_benchmarks()
