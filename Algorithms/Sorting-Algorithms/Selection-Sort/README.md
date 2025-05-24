# Selection Sort
## How does it work?

**Selection sort** is an **iterative sorting algorithm**. It works by swapping the $ith$ element with the smallest element after it. In each iteration, it initialises two variables: `min_val = A[i]` to store the minimum value after the $ith$ element, and `t = i` to store the index of this value. If `t != i`, the two values in the array are swapped.

### Example
![Diagram for selection sort](path/to/image)

## Efficiency

### Time Complexity
To sort an array of $n$ elements, it would carry out $n-1$ comparisons in the first iteration, $n-2$ in the second, and so on until the $(n-1)$th iteration where it would carry out $1$ comparison. This would add up to $(n-1) + (n-2) ... + 1 = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$, thus the time complexity is $O(n^2)$.

### Space Complexity
The algorithm uses a constant number of varialbles, so the space complexity is $O(1)$.

## Code
### Python
```py
def selection_sort(array: list) -> list:
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
```
