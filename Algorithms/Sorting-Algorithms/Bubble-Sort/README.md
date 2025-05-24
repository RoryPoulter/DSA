# Bubble Sort
## How does it work?

**Bubble sort** is an **iterative sorting algorithm**. It works by looking at adjacent elements in the array `A`, and if `A[i]` is greater than `A[i+1]`, it swaps the two values. This repeats until all adjacent pairs have been compared. If, during this iteration, a pair of elements have been swapped, the whole process will repeat. Otherwise, the list is sorted.

After the $ith$ iteration, the last $i$ elements will be in the correct order.

### Example
![Diagram for bubble sort](path/to/image)

## Efficiency

### Time Complexity
The worst-case input would be an array in reverse order. This would require $n-1$ swaps in the first iteration, $n-2$ in the second, up until $1$ in the $(n-1)$th iteration. Thus the total number of swaps is $(n-1) + (n-2) + ... + 2 + 1 = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$. The worst-case time complexity of bubble sort is $O(n^2)$.

### Space Complexity
The algorithm only declares one temporary variable to swap adjacent elements, so the space complexity is $O(1)$.

## Code
### Python
```py
def bubble_sort(array: list) -> list:
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
```
