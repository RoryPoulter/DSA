"""Demo code for selection sort
"""


def selectionSort(array: list) -> list:
    """Sorts an list in ascending order using selection sort algorithm

    Args:
        array (list): The unsorted list

    Returns:
        list: The sorted list
    """
    n = len(array)
    for i in range(n):
        min_val = array[i]
        t = i
        for j in range(i, n):
            if array[j] < min_val:
                min_val = array[j]
                t = j
        array[i], array[t] = array[t], array[i]
    return array


if __name__ == "__main__":
    data = [10, 5, 2, 4, 8]
    print(selectionSort(data))
