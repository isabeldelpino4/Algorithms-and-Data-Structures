def merge_sort(arr):
    """Sort a list using merge sort and return a new sorted list"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists into one sorted list"""
    result = []
    i = j = 0

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
          
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# DEMO
nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = merge_sort(nums)
print(sorted_nums)  # [3, 9, 10, 27, 38, 43, 82]
