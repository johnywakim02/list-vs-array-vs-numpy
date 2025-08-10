from code.utils.decorators.time_decorator import timeit
from code.utils.methods.draw import plot_graph
from code.utils.models.slice_range import SliceRange
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def get_element_range(lst: list, range: SliceRange):
    return lst[range.start : range.end]


if __name__ == "__main__":
    n_el: int = 100_000_000
    lst: list[int] = [0] * n_el
    factors: list[float] = [0.000001, 0.0001, 0.01, 0.1, 0.2, 0.4, 0.8, 1.0]

    # slicing's relation with number of elements sliced
    ranges: list[SliceRange] = []
    pos = 0
    for factor in factors:
        ranges.append(SliceRange(pos, pos + int(factor * n_el)))
    times = [get_element_range(lst, slice_range)[0] for slice_range in ranges]

    plot_title = "Slicing Time vs Slice Size in a list of 100M elements, slicing from the beginning"
    plot_graph(
        [factor * n_el for factor in factors],
        times,
        plot_title,
        "Slicing Time (s)",
        "Slice Size",
    )

    # slicing's relation with position
    ranges = []
    slice_size = 1_000_000
    positions = range(0, n_el - slice_size, slice_size * 10)
    for position in positions:
        ranges.append(SliceRange(position, position + int(slice_size)))
    times = [get_element_range(lst, slice_range)[0] for slice_range in ranges]

    plot_title = "Slicing Time vs Slice Position in a list of 100M elements, for a slice Size of 1M elements"
    plot_graph(positions, times, plot_title, "Slicing Time (s)", "Slice Position")
