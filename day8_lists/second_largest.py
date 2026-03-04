def second_largest(arr):
    largest = max(arr)
    arr.remove(largest)
    largest2 = arr[0]
    for x in arr:
        if x > largest2:
            largest2 = x

    return largest2

arr = [12,34,78,89,99]
if len(arr) < 2:
    print("Second Largest element cannot be found")
else:
    print("Second Largest Element in list is: ",second_largest(arr))
