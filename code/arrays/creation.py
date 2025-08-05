import random
from array import array
from code.utils.decorators.time_decorator import timeit

N_ITER = 100


@timeit(n_iter=N_ITER)
def create_random_float_array(n_el: int):
    return array("f", [random.uniform(0, 100) for _ in range(n_el)])


if __name__ == "__main__":
    create_random_float_array(100_000_000)
