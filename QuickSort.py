import random

def quicksort(arr):
    """ Sorts the list in place using quicksort"""
    def _quicksort(low, high):
        if low < high:
            # Partition the array
            pivot_index = partition(low, high)
            # Recursively sort left and right halves
            _quicksort(low, pivot_index - 1)
            _quicksort(pivot_index + 1, high)

    def partition(low, high):
      """ The partition algorithm """
        # Pick a random pivot to avoid worst-case
        pivot_index = random.randint(low, high)
        pivot_value = arr[pivot_index]

        # Move pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        store_index = low
        for i in range(low, high):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        # Move pivot to its final place
        arr[store_index], arr[high] = arr[high], arr[store_index]
        return store_index

    _quicksort(0, len(arr) - 1)
    return arr

# DEMO
nums = [10, 7, 8, 9, 1, 5]
print("Before:", nums)
quicksort(nums)
print("After: ", nums)
