"""Demo code for insertion sort
"""


from random import sample


def insertionSort(array: list) -> list:
    """Sorts an array in ascending order using the insertion sort algorithm

    Args:
        array (list): The unsorted array

    Returns:
        list: The sorted array
    """
    n = len(array)
    for i in range(1, n):
        for j in range(i, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1
    return array


if __name__ == "__main__":
    data = sample(range(20), 20)
    print(f"Unsorted data: \n{data}")
    sorted_data = insertionSort(data)
    print(f"Sorted data: \n{sorted_data}")
