"""Speed test for different sorting algorithms
"""


from random import sample
from timeit import default_timer as timer
import matplotlib.pyplot as plt


# The Sorting Algorithms
def bubble_sort(array: list) -> list:
    """Sorts a list in ascending order using the bubble sort algorithm
    
    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        array (list): The unsorted list

    Returns:
        list: The sorted list
    """

    valid = False
    while not valid:
        valid = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                valid = False
    return array


def insertion_sort(array: list) -> list:
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



def selection_sort(array: list) -> list:
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



def merge_sort(arr: list[int]) -> list[int]:
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
    arr_1 = merge_sort(arr[:mid])
    arr_2 = merge_sort(arr[mid:])
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



def quick_sort(array: list) -> list:
    """Sorts a list of integers using the quicksort algorithm.

    Args:
        array (list): The unsorted list

    Returns:
        list: The sorted list
    """
    if len(array) <= 1:
        return array
    left, pivot, right = partition(array)
    return quick_sort(left) + pivot+ quick_sort(right)


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
    sorting_algorithms = [bubble_sort, merge_sort, selection_sort, quick_sort, insertion_sort]
    x_vals = list(range(10, 2000, 200))

    for algo in sorting_algorithms:
        y_vals = []
        for x in x_vals:
            TOTAL = 0
            for _ in range(10):
                unsorted_list = sample(range(1, 2001), x)
                start = timer()
                res = algo(unsorted_list)
                end = timer()
                TOTAL += (end - start)
            mean = TOTAL / 10
            y_vals.append(mean)
        plt.plot(x_vals, y_vals, label=algo.__name__)
    plt.legend()
    plt.title("Running time for sorting algorithms")
    plt.xlabel("n")
    plt.ylabel("Time / s")
    plt.show()
