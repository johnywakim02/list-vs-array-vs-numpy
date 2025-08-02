from code.utils.decorators.time_decorator import timeit


@timeit(n_iter=100)
def create_list(n_el: int):
    return [0] * n_el


if __name__ == "__main__":
    create_list(0)
    create_list(10)
    create_list(1000)
    create_list(1_000_000)
    create_list(100_000_000)
