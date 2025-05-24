// JavaScript code for insertion sort


/**
 * Sorts an array of numbers in ascending order using the insertion sort algorithm
 * @param {array} data The unsorted array
 * @returns The sorted array
 */
function insertion_sort(data){
    let n = data.length;
    for (let i = 1; i < n; i++){
        let j = i;
        // While the element is in the wrong relative position in the sorted partition
        while (j > 0 && data[j] < data[j-1]){
            // Swap the values
            let temp = data[j];
            data[j] = data[j-1];
            data[j-1] = temp;
            // Update the pointer
            j = j - 1;
        }
    }
    return data
}


// Example
const DATA = [17, 6, 5, 3, 12, 7, 10, 19, 9, 4, 0, 18, 1, 15, 16, 2, 11, 13, 14, 8];
console.log(insertion_sort(DATA))
