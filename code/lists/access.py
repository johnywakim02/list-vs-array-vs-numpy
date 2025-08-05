import random
from code.utils.decorators.time_decorator import timeit


N_ITER = 100


@timeit(n_iter=N_ITER)
def read_element(lst: list, pos: int):
    return lst[pos]


@timeit(n_iter=N_ITER)
def write_element(lst: list, pos: int, val: object):
    lst[pos] = val


if __name__ == "__main__":
    lst = [random.uniform(0, 100) for _ in range(100_000_000)]
    read_element(lst, 100)
    read_element(lst, 100_000)
    read_element(lst, 99_999_998)
    write_element(lst, 100, 5.02)
    write_element(lst, 100_000, 72.8)
    write_element(lst, 99_999_998, "hmmm")
