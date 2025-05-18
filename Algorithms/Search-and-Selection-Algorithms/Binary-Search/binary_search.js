// JavaScript code for binary search


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


const DATA = [1, 2, 3, 6, 8, 11, 14]
console.log(binary_search(DATA, 1))
console.log(binary_search(DATA, 4))
