"""Demo code for quick select algorithm.
"""


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
    if i > len(array):
        raise ValueError("'i' is greater than length of 'array'")
    i -= 1
    if len(array) == 1:
        return array[0]
    left, pivot, right = partition(array)
    k = len(left)
    if k == i:
        return pivot
    if k > i:
        return quick_select(left, i+1)
    return quick_select(right, i - k + 1)


def partition(array: list) -> tuple:
    """Simple partition function. Chooses the first element as the pivot

    Args:
        array (list): The array of numbers

    Returns:
        tuple: The left list, pivot, and right list
    """
    pivot = array[0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    return left, [pivot], right


if __name__ == "__main__":
    data = [5,2,4,1,3]
    print(quick_select(data, 1))
