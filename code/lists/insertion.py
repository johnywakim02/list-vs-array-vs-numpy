import time
import matplotlib.pyplot as plt

N_ITER = 100


def list_append_timing(lst: list, element: object, n_iter: int = N_ITER):
    total_time = 0
    for _ in range(n_iter):
        start = time.perf_counter()
        lst.append(element)
        total_time += time.perf_counter() - start
        lst.pop()  # undo to keep list size constant
    duration = total_time / n_iter
    print(f"Average append time over {n_iter} iterations: {duration:.10f} seconds")
    return duration


def list_insert_timing(
    lst: list, element: object, position: int, n_iter: int = N_ITER
) -> None:
    total_time = 0
    for _ in range(n_iter):
        start = time.perf_counter()
        lst.insert(position, element)
        total_time += time.perf_counter() - start
        del lst[position]  # undo to keep list size constant
    duration = total_time / n_iter
    print(f"Average append time over {n_iter} iterations: {duration:.10f} seconds")
    return duration


def test_insert_speed_100000el_draw_graph():
    print("> Insert with list of 100000 elements at various positions")
    print("----------------------------------------------------------")
    lst = [i for i in range(100000)]
    positions = [0, 25000, 50000, 75000, 99999]
    timings = []

    for pos in positions:
        avg_time = list_insert_timing(lst, "hello", pos)
        print(f"Insert at index {pos}: {avg_time:.10f} seconds")
        timings.append(avg_time)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(positions, timings, marker="o")
    plt.title("Insert Time vs Position in List of 100,000 Elements")
    plt.xlabel("Insert Position")
    plt.ylabel("Average Time (seconds)")
    plt.grid(True)
    plt.show()


def test_append_speed_3el():
    print("> Append with list of 3 elements")
    print("--------------------------------")
    dog_breeds = ["chihuahua", "bulldog", "butterfly"]
    list_append_timing(dog_breeds, "bernese")
    print()


def test_append_speed_1000el():
    print("> Append with list of 1000 elements")
    print("--------------------------------")
    lst = [i for i in range(1001)]
    list_append_timing(lst, 1001)
    print()


def test_append_speed_100000el():
    print("> Append with list of 100000 elements")
    print("--------------------------------")
    lst = [i for i in range(100001)]
    list_append_timing(lst, 51)
    print()


def test_insert_speed_10el():
    print("> Insert with list of 10 elements, at beg than mid then end")
    print("--------------------------------")
    lst = [i for i in range(11)]
    list_insert_timing(lst, "hello", 2)
    list_insert_timing(lst, "hello", 5)
    list_insert_timing(lst, "hello", 8)
    print()


def test_insert_speed_1000el():
    print("> Insert with list of 1000 elements, at beg than mid then end")
    print("--------------------------------")
    lst = [i for i in range(1001)]
    list_insert_timing(lst, "hello", 50)
    list_insert_timing(lst, "hello", 450)
    list_insert_timing(lst, "hello", 850)
    print()


def test_insert_speed_100000el():
    print("> Insert with list of 100000 elements, at beg than mid then end")
    print("--------------------------------")
    lst = [i for i in range(100001)]
    list_insert_timing(lst, "hello", 50)
    list_insert_timing(lst, "hello", 50000)
    list_insert_timing(lst, "hello", 99500)
    print()


def test_insert_speed_100000000el():
    print("> Insert with list of 100_000_000 elements, at beg than mid then end")
    print("--------------------------------")
    lst = [i for i in range(100000001)]
    list_insert_timing(lst, "hello", 50)
    list_insert_timing(lst, "hello", 50000000)
    list_insert_timing(lst, "hello", 99999500)
    print()


if __name__ == "__main__":
    test_append_speed_3el()
    test_append_speed_1000el()
    test_append_speed_100000el()
    test_insert_speed_10el()
    test_insert_speed_1000el()
    test_insert_speed_100000el()
    test_insert_speed_100000000el()
    test_insert_speed_100000el_draw_graph()
