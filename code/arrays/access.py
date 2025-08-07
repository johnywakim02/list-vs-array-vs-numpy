from array import array
import random
import numpy as np
from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def read_element(arr: array, pos: int):
    return arr[pos]


@timeit(n_iter=N_ITER)
def write_element(arr: array, pos: int, val: object):
    arr[pos] = val


if __name__ == "__main__":
    arr = array("f", [random.uniform(0, 100) for _ in range(100_000_000)])
    read_element(arr, 100)
    read_element(arr, 100_000)
    read_element(arr, 99_999_998)
    write_element(arr, 100, 5.02)
    write_element(arr, 100_000, 72.8)
    write_element(arr, 99_999_998, 99)
