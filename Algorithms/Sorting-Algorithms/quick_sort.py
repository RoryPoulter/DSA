"""Demo code for quick sort
"""


from random import sample


def quickSort(array: list) -> list:
    """Sorts a list of integers using the quicksort algorithm.

    Args:
        array (list): The unsorted list

    Returns:
        list: The sorted list
    """
    if len(array) <= 1:
        return array
    left, pivot, right = partition(array)
    return quickSort(left) + pivot+ quickSort(right)


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
    data = sample(range(20), 20)
    print(f"Unsorted data: \n{data}")
    sorted_data = quickSort(data)
    print(f"Sorted data: \n{sorted_data}")
