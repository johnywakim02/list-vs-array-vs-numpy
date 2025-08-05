from array import array
from code.arrays.creation import create_random_float_array
from code.utils.decorators.time_decorator import timeit

N_ITER = 100


@timeit(n_iter=N_ITER)
def iterate_array(arr: array):
    total = 0.0
    for el in arr:
        total += el
    return total


if __name__ == "__main__":
    _, arr = create_random_float_array(100_000_000)
    print(type(arr[0]))
    iterate_array(arr)
