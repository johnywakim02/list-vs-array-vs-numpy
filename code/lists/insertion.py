from code.utils.decorators.time_decorator import timeit


@timeit
def insert_element(list: list, element: object):
    list.append(element)


def test_insert_speed():
    dog_breeds = ["chihuahua", "bulldog", "butterfly"]
    insert_element(dog_breeds, "bernese")


if __name__ == "__main__":
    test_insert_speed()
