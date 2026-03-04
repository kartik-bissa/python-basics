def max_element(arr):
    largest = arr[0]
    for x in arr:
        if x > largest:
            largest = x
    return largest

print(max_element([12,45,99,56]))
