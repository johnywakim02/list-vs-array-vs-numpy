import numpy as np
from code.utils.decorators.time_decorator import timeit
from config import config

N_ITER = config.N_ITER


@timeit(n_iter=N_ITER)
def iterate_np_array(np_array):
    total = 0.0
    for el in np_array:
        total += el
    return total


if __name__ == "__main__":
    np_array = np.random.rand(100_000_000) * 100
    iterate_np_array(np_array)
