# Binary Search

## How does it work?
**Binary search** is a search algorithm which uses **divide-and-conquer** to efficiently locate a value in an array. It does this by initialising two pointers `l` and `r` to be 0 and the length of the array - 1 respectively. It then uses these to calculate the midpoint m and compares the value at this index `A[m]` to the search value `x`. If they are equal, it returns m. If `A[m] > x` then it sets `r = m - 1`. Else it sets `l = m + 1`. This repeats until either the value is found or `l < r`, in which case it returns -1 to show the search value is not present in the list.

It requires the list to be sorted, so for an unsorted list it would be faster to perform a **linear search** (i.e. check every value in order until all have been checked or it is found) as this approach would have a time complexity of $O(n)$, while sorting the list first would take $O(n*log_{}(n))$ time.

### Example
![Diagram for binary search](../../../media/binary_search.jpg)

## Efficiency
### Time Complexity
Worst-case it has to carry out $log_{2}(n)$ comparisons as it splits the list in half after each failed check. Thus it has a worst-case time complexity of $O(log_{2}(n))$.

### Space Complexity
As it only requires 3 pointers to be declared, the space complexity is $O(1)$.

## Code
### Python
```py
def binary_search(array: list, value: int) -> int:
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
```

### JavaScript
```js
function binary_search(array, n){
    let l = 0
    let r = array.length
    while (l <= r){
        m = Math.floor((l + r) / 2)
        if (array[m] == n){
            return m
        }
        if (array[m] > n){
            r = m - 1
        } else {
            l = m + 1
        }
    }
    return -1 // If n is not in the array
}
```