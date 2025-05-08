"""Example of MergeSort
"""


def mergeSort(arr: list[int]) -> list[int]:
    """Sorts a list of integers using a recursive merge sort.
    
    T(n) = 2 * T(n/2) + O(n)

    Args:
        arr (list[int]): The unsorted list

    Returns:
        list[int]: The sorted list
    """
    # Base case
    if len(arr) == 1:
        return arr
    # Split the list in half
    mid = len(arr) // 2
    arr_1 = mergeSort(arr[:mid])
    arr_2 = mergeSort(arr[mid:])
    return merge(arr_1, arr_2)


def merge(arr_1: list[int], arr_2: list[int]) -> list[int]:
    """Merges two ordered lists into one ordered list.
    
    O(n)

    Args:
        arr_1 (list[int]): The first list
        arr_2 (list[int]): The second list

    Returns:
        list[int]: The sorted merged list
    """
    # Pointers for arr_1 and arr_2 respectively
    i = 0
    j = 0
    arr = []
    # Repeats until all elements in one of the lists has been added
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            arr.append(arr_1[i])
            i += 1
        else:
            arr.append(arr_2[j])
            j += 1
    # Adds the remaining values to the list
    if i < len(arr_1):
        arr += arr_1[i:]
    else:
        arr += arr_2[j:]
    return arr


if __name__ == "__main__":
    data = [1, 5, 2, 4, 3, 9, 6, 8, 7]
    print(mergeSort(data))
