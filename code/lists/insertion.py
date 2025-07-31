from code.utils.decorators.time_decorator import timeit

N_ITER = 1_000_000


@timeit(n_iter=N_ITER)
def append_element(list: list, element: object):
    list.append(element)


def test_append_speed_3el():
    dog_breeds = ["chihuahua", "bulldog", "butterfly"]
    append_element(dog_breeds, "bernese")


def test_append_speed_1000el():
    my_list = [i for i in range(1001)]
    append_element(my_list, 1001)


if __name__ == "__main__":
    test_append_speed_3el()
    test_append_speed_1000el()
