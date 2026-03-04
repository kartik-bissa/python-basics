def min_element(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest

print(min_element([12, 56, 77, 2, 99]))