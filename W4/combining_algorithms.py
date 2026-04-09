# A Clean .py file for task 4

# Sorting Algorithms
import random
import time
import timeit


def insertion_sort(arr):
    """
    Insertion Sort: A simple sorting algorithm that builds the final sorted
    array one item at a time. It takes each element from the input list and
    inserts it into its correct position in the sorted part of the array.

    Args:
    arr (list): The input list to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """

    # Traverse through all elements in the list, starting from the second element (index 1)
    for i in range(1, len(arr)):

        # Store the current element to be compared and inserted into the sorted part of the list
        current_element = arr[i]

        # Move elements of the sorted part of the list that are greater than the current element
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element into its correct position in the sorted part of the list
        arr[j + 1] = current_element

    return arr

def bubble_sort(arr):
    """
    Bubble Sort: A simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.

    Args:
    arr (list): The input list to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """

    # Get the length of the input list
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):

        # Flag to optimize the algorithm
        # If no swaps are performed in an iteration, the list is already sorted, and we can stop early
        swapped = False

        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:

                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Set the swapped flag to True to indicate that a swap occurred in this iteration
                swapped = True

        # If no two elements were swapped in the inner loop, the list is sorted, and we can exit early
        if not swapped:
            break

    return arr

# Search Algorithms
def binary_search(array, target):

    # Initialize 'pointers'
    left = 0
    right = len(array) - 1 # Account for indexing to get the right most element index
    mid = int((left + right)/2)

    while left <= right:
        if array[mid] == target: # If target is found 
            return mid
        elif target > array[mid]:
            left = mid + 1 # We already checked the mid element, so we shift the index by 1 for the next search.
        elif target < array[mid]:
            right = mid - 1

        mid = int((left + right)/2) # Recalculate mid

    return -1

def linear_search(array, target):

    for i in range(len(array)):
        if array[i] == target:
            return i
        
    return -1


# Random Array's for testing
random_arr_100 = [random.randint(1, 100) for n in range(100)]
random_arr_1000 = [random.randint(1, 1000) for n in range(1000)]
random_arr_10000 = [random.randint(1, 10000) for n in range(10000)]
random_arr_100000 = [random.randint(1, 100000) for n in range(100000)]


#1 Insertion Sort and linear search
start = time.time()
sorted_arr_100_i = insertion_sort(random_arr_100.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_100)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_100_i, random.randint(1, 100)), number=100):.6f} seconds for length {len(sorted_arr_100_i)}")

start = time.time()
sorted_arr_1000_i = insertion_sort(random_arr_1000.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_1000)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_1000_i, random.randint(1, 1000)), number=100):.6f} seconds for length {len(sorted_arr_1000_i)}")

start = time.time()
sorted_arr_10000_i = insertion_sort(random_arr_10000.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_10000)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_10000_i, random.randint(1, 10000)), number=100):.6f} seconds for length {len(sorted_arr_10000_i)}")

start = time.time()
sorted_arr_100000_i = insertion_sort(random_arr_100000.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_100000)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_100000_i, random.randint(1, 100000)), number=100):.6f} seconds for length {len(sorted_arr_100000_i)}")

print()
#2 Bubble Sort and linear search
start = time.time()
sorted_arr_100_b = bubble_sort(random_arr_100.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_100)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_100_b, random.randint(1, 100)), number=100):.6f} seconds for length {len(sorted_arr_100_b)}")

start = time.time()
sorted_arr_1000_b = bubble_sort(random_arr_1000.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_1000.copy())} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_1000_b, random.randint(1, 1000)), number=100):.6f} seconds for length {len(sorted_arr_1000_b)}")

start = time.time()
sorted_arr_10000_b = bubble_sort(random_arr_10000.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_10000)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_10000_b, random.randint(1, 10000)), number=100):.6f} seconds for length {len(sorted_arr_10000_b)}")

start = time.time()
sorted_arr_100000_b = bubble_sort(random_arr_100000.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_100000)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Linear search execution time: {timeit.timeit(lambda: linear_search(sorted_arr_100000_b, random.randint(1, 100000)), number=100):.6f} seconds for length {len(sorted_arr_100000_b)}")

print()
#3 Insertion Sort and binary search
start = time.time()
sorted_arr_100_i = insertion_sort(random_arr_100.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_100)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_100_i, random.randint(1, 100)), number=100):.6f} seconds for length {len(sorted_arr_100_i)}")

start = time.time()
sorted_arr_1000_i = insertion_sort(random_arr_1000.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_1000)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_1000_i, random.randint(1, 1000)), number=100):.6f} seconds for length {len(sorted_arr_1000_i)}")

start = time.time()
sorted_arr_10000_i = insertion_sort(random_arr_10000.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_10000)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_10000_i, random.randint(1, 10000)), number=100):.6f} seconds for length {len(sorted_arr_10000_i)}")

start = time.time()
sorted_arr_100000_i = insertion_sort(random_arr_100000.copy())
insertion_sort_time = time.time() - start
print(f"Insertion Sorted Array ({len(random_arr_100000)} elements) and time to sort: {insertion_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_100000_i, random.randint(1, 100000)), number=100):.6f} seconds for length {len(sorted_arr_100000_i)}")

print()
#4 Bubble Sort and binary search
start = time.time()
sorted_arr_100_b = bubble_sort(random_arr_100.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_100)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_100_b, random.randint(1, 100)), number=100):.6f} seconds for length {len(sorted_arr_100_b)}")

start = time.time()
sorted_arr_1000_b = bubble_sort(random_arr_1000.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_1000)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_1000_b, random.randint(1, 1000)), number=100):.6f} seconds for length {len(sorted_arr_1000_b)}")

start = time.time()
sorted_arr_10000_b = bubble_sort(random_arr_10000.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_10000)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_10000_b, random.randint(1, 10000)), number=100):.6f} seconds for length {len(sorted_arr_10000_b)}")

start = time.time()
sorted_arr_100000_b = bubble_sort(random_arr_100000.copy())
bubble_sort_time = time.time() - start
print(f"Bubble Sorted Array ({len(random_arr_100000)} elements) and time to sort: {bubble_sort_time:.6f} seconds")
print(f"Binary search execution time: {timeit.timeit(lambda: binary_search(sorted_arr_100000_b, random.randint(1, 100000)), number=100):.6f} seconds for length {len(sorted_arr_100000_b)}")
