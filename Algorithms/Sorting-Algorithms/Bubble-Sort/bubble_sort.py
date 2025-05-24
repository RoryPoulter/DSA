"""Demo code for a bubble sort
"""


def bubble_sort(array: list) -> list:
    """Sorts a list in ascending order using the bubble sort algorithm
    
    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        array (list): The unsorted list

    Returns:
        list: The sorted list
    """

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                is_sorted = False
    return array


if __name__ == "__main__":
    data = [6, 5, 2, 3, 4, 1]
    print(bubble_sort(data))
