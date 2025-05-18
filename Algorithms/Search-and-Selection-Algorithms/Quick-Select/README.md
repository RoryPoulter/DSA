# Quick Select
## How does it work?
**Quick select** is a **recursive algorithm** for selecting the $ith$ smallest value in an array. It is similar to quick sort in the sense that it partitions a list about a pivot. However, it uses the rank of the pivot to choose which partition to pass into the recursive call.

## Efficiency
### Time Complexity
The worst-case scenario would occur if following are true:
* Partition function chooses pivot to be the last value in the array
* The array is in reverse order
* The value for `i` is 1

This would result in a worst-case time complexity of $O(n^2)$.

The best-case scenario would occur when the partition function chooses the $ith$ smallest value as the pivot. This would result in a best-case time complexity of $O(n)$.

## Code
### Python
```py
def quick_select(array: list, i: int) -> int:
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


# Simple partition function - pivots on last element
def partition(array: list) -> tuple:
    pivot = array[~0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    return left, [pivot], right
```
