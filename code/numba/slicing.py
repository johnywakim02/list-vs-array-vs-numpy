import numpy as np
from numba import njit
from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from code.utils.models.slice_range import SliceRange
from config import config

N_ITER = config.N_ITER


@njit
def numba_slice(arr: np.ndarray, start: int, end: int) -> np.ndarray:
    size = end - start
    result = np.empty(size, dtype=arr.dtype)
    for i in range(size):
        result[i] = arr[start + i]
    return result


# Timing wrapper to keep numba code separate from decorator for warmup
@timeit(n_iter=N_ITER)
def get_element_range(arr: np.ndarray, start: int, end: int):
    return numba_slice(arr, start, end)


if __name__ == "__main__":
    n_el: int = 100_000_000
    arr: np.ndarray = np.zeros(n_el, dtype=np.int32)
    factors: list[float] = [0.000001, 0.0001, 0.01, 0.1, 0.2, 0.4, 0.8, 1.0]

    # Warm up Numba JIT
    numba_slice(arr, 0, 10)

    # *** Slicing time vs slice size ***
    ranges: list[SliceRange] = []
    pos = 0
    for factor in factors:
        ranges.append(SliceRange(pos, pos + int(factor * n_el)))

    times = [get_element_range(arr, r.start, r.end)[0] for r in ranges]

    plot_title = "Slicing Time vs Slice Size (Numba, manual copy) in a NumPy array of 100M elements"
    plot_graph(
        [factor * n_el for factor in factors],
        times,
        plot_title,
        "Slicing Time (s)",
        "Slice Size",
    )

    # *** Slicing time vs slice position ***
    ranges = []
    slice_size = 1_000_000
    positions = range(0, n_el - slice_size, slice_size * 10)
    for position in positions:
        ranges.append(SliceRange(position, position + slice_size))

    times = [get_element_range(arr, r.start, r.end)[0] for r in ranges]

    plot_title = "Slicing Time vs Slice Position (Numba, manual copy) in a NumPy array of 100M elements"
    plot_graph(
        positions,
        times,
        plot_title,
        "Slicing Time (s)",
        "Slice Position",
    )
