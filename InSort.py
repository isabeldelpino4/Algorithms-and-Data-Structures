def insort_left(a, x, lo=0, hi=None):
    """Insert x in a in sorted order (stable, like bisect.insort_left)."""
    if hi is None:
        hi = len(a)
    # Binary search for leftmost position
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    a.insert(lo, x)
    return lo  # index where inserted

def insort_right(a, x, lo=0, hi=None):
    """Insert x in a in sorted order (like bisect.insort_right)."""
    if hi is None:
        hi = len(a)
    # Binary search for rightmost position
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    a.insert(lo, x)
    return lo

# DEMO:
if __name__ == "__main__":
    arr = [1, 3, 4, 7]
    print("Original:", arr)

    insort_left(arr, 3)
    print("After insort_left(3):", arr)

    arr2 = [1, 3, 4, 7]
    insort_right(arr2, 3)
    print("After insort_right(3):", arr2)

