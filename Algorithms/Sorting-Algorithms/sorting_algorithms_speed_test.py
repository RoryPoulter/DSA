"""Speed test for different sorting algorithms
"""


from random import sample
from timeit import default_timer as timer
import matplotlib.pyplot as plt
# Import the algorithms
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort


if __name__ == "__main__":
    sorting_algorithms = [bubble_sort, merge_sort, selection_sort, quick_sort, insertion_sort]
    x_vals = list(range(10, 2000, 200))

    for algo in sorting_algorithms:
        y_vals = []
        for n in x_vals:
            TOTAL = 0
            for i in range(10):
                unsorted_list = sample(range(1, 2001), n)
                start = timer()
                res = algo(unsorted_list)
                end = timer()
                TOTAL += (end - start)
            mean = TOTAL / 10
            y_vals.append(end - start)
        plt.plot(x_vals, y_vals, label=algo.__name__)
    plt.legend()
    plt.title("Running time for sorting algorithms")
    plt.xlabel("n")
    plt.ylabel("Time / s")
    plt.show()
