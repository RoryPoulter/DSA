// JavaScript code for bubble sort


/**
 * Sorts an array of numbers in ascending order using the bubble sort algorithm
 * @param {array} data The unsorted array
 * @returns The sorted array
 */
function bubble_sort(data){
    let is_sorted = false;  // Flag used to indicate if any swaps have occurred in the iteration
    while (!is_sorted){
        is_sorted = true;
        for (let i = 0; i < data.length - 1; i++){
            if (data[i] > data[i+1]){
                is_sorted = false;
                // Swap the adjacent elements
                let temp = data[i];
                data[i] = data[i+1];
                data[i+1] = temp;
            }
        }
    }
    return data
}


// Example data
const DATA = [6, 5, 2, 3, 4, 1];
console.log(bubble_sort(DATA))
