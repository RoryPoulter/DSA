"""Demo code for insertion sort
"""


from random import sample


def insertion_sort(array: list) -> list:
    """Sorts an array in ascending order using the insertion sort algorithm

    Args:
        array (list): The unsorted array

    Returns:
        list: The sorted array
    """
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


if __name__ == "__main__":
    data = sample(range(20), 20)
    print(f"Unsorted data: \n{data}")
    sorted_data = insertion_sort(data)
    print(f"Sorted data: \n{sorted_data}")
