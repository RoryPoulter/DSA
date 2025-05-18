"""Demo code for a binary search
"""


def binary_search(array: list, value: int) -> int:
    """Binary search of a list to find the index of a specified value.
    List must be sorted in ascending order.
    
    Time complexity: O(log(n))
    Space complexity: O(1)

    Args:
        array (list): The list to be searched
        value (int): The value being searched for

    Returns:
        int: The index of the value
    """
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l+r)//2
        if array[m] == value:
            return m
        if array[m] > value:
            r = m - 1
        else:
            l = m + 1
    return -1  # If the value is not in the list


if __name__ == "__main__":
    data = [1, 2, 3, 6, 8, 11, 14]
    print(binary_search(data, 1))
    print(binary_search(data, 4))  # Not in the list
