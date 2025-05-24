// JavaScript code for selection sort

/**
 * Sorts an array of numbers in ascending order using the selection sort algorithm
 * @param {array} data The unsorted array
 * @returns The sorted array
 */
function selection_sort(data){
    let n = data.length;
    for (let i = 0; i < n; i++){
        let min_val = data[i]; // The minimum value after index `i`
        let t = i  // The index of the minimum value
        for (let j = i; j < n; j++){
            if (data[j] < min_val){
                min_val = data[j];
                t = j;
            }
        }
        // Swap the ith value with the smallest value after it
        let temp = data[i];
        data[i] = data[t];
        data[t] = temp;
    }
    return data
}


const DATA = [10, 5, 2, 4, 8];
console.log(selection_sort(DATA));
