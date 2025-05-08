"""Speed test for different sorting algorithms
"""


from random import sample
from timeit import default_timer as timer
import matplotlib.pyplot as plt
# Import the algorithms
from bubble_sort import bubbleSort
from merge_sort import mergeSort
from selection_sort import selectionSort
from quick_sort import quickSort
from insertion_sort import insertionSort


if __name__ == "__main__":
    sorting_algorithms = [bubbleSort, mergeSort, selectionSort, quickSort, insertionSort]
    x_vals = list(range(10, 2000, 200))

    for algo in sorting_algorithms:
        y_vals = []
        for n in x_vals:
            total = 0
            for i in range(10):
                unsorted_list = sample(range(1, 2001), n)
                start = timer()
                res = algo(unsorted_list)
                end = timer()
                total += (end - start)
            mean = total / 10
            y_vals.append(end - start)
        plt.plot(x_vals, y_vals, label=algo.__name__)
    plt.legend()
    plt.title("Running time for sorting algorithms")
    plt.xlabel("n")
    plt.ylabel("Time / s")
    plt.show()
