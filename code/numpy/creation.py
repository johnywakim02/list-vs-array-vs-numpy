import numpy as np
from code.utils.decorators.time_decorator import timeit

N_ITER = 100


@timeit(n_iter=N_ITER)
def create_floats_np_array(n_el: str):
    return np.random.rand(n_el) * 100


if __name__ == "__main__":
    create_floats_np_array(100_000_000)
