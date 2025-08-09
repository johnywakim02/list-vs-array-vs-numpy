from code.utils.decorators.time_decorator import timeit
from code.utils.models.slice_range import SliceRange
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def get_element_range(lst: list, range: SliceRange):
    return lst[range.start : range.end]


if __name__ == "__main__":
    n_el: int = 100_000_000
    lst: list[int] = [0] * n_el
    factors: list[float] = [0.000001, 0.0001, 0.01, 1.0]
    positions: list[int] = [0, 100_000, 10_000_000, n_el - 1_000_000]

    # slicing's relation with number of elements sliced
    ranges: list[SliceRange] = []
    for factor in factors:
        ranges.append(SliceRange(positions[0], positions[0] + int(factor * n_el)))
    times = [get_element_range(lst, slice_range)[0] for slice_range in ranges]

    # slicing's relation with position
    ranges = []
    for position in positions:
        ranges.append(SliceRange(position, position + int(factors[-2] * n_el)))
    times = [get_element_range(lst, slice_range)[0] for slice_range in ranges]
