"""Demo code for quick select algorithm.
"""
from random import sample, randint


def quick_select(array: list, i: int) -> int:
    """Quick select algorithm for finding ith smallest element in an array.

    Args:
        array (list): The array to be searched
        i (int): The order of magnitude of the value. `1` represents the smallest value.

    Raises:
        ValueError: If `i > len(array)`

    Returns:
        int: The ith smallest number
    """
    i -= 1
    if i > len(array):
        raise ValueError(f"'{i=}' is greater than length of 'array {len(array)=}'")
    if len(array) == 1:
        return array[0]
    left, pivot, right = partition(array)
    k = len(left)
    if k == i:
        return pivot
    if k > i:
        return quick_select(left, i+1)
    return quick_select(right, i - k)


def partition(array: list) -> tuple:
    """Simple partition function. Chooses the last element as the pivot

    Args:
        array (list): The array of numbers

    Returns:
        tuple: The left list, pivot, and right list
    """
    pivot = array[0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    return left, pivot, right


if __name__ == "__main__":
    data = sample(range(1, 100), 10)
    index = randint(1, 10)
    print(f"{index=}, {data=}")
    x = quick_select(data, index)
    print(f"{x=}")
    assert sorted(data)[index-1] == x
