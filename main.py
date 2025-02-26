import timeit
import random

# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position


def hybridSort(arr, threshold):
    n = len(arr)

    if n <= threshold:
        insertionSort(arr)
        return

    mid = n // 2
    L1 = arr[:mid]
    L2 = arr[mid:]
    hybridSort(L1, threshold)
    hybridSort(L2, threshold)
    merge_together(L1, L2, arr)

# CSE 331 Code from a project
def merge_together(L1, L2, arr):
    i = j = 0
    while i + j < len(arr):
        if j == len(L2) or (i < len(L1) and L1[i] < L2[j]):
            arr[i+j] = L1[i]
            i += 1
        else:
            arr[i+j] = L2[j]
            j += 1

threshold = 12
size = 10000

test_list = list(range(1, size+1))
random.shuffle(test_list)

def run_hybridSort(arr, threshold):
    hybridSort(arr.copy(), threshold)

hybridSort_times = timeit.repeat(lambda: run_hybridSort(test_list, threshold), number=1, repeat=10)

print(f"Average Hybrid Sort time: {sum(hybridSort_times) / len(hybridSort_times)}")

# hybridSort(test_list, threshold)
# 
# print(test_list)


