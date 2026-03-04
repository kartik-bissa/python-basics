'''Program To calculate sum of elements in list'''
def sum_list(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum_list([1,2,3,4]))

''' Python program to count even numbers'''
def count_even(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    return count

print(count_even([12,55,63,61,78,26]))

'''To take user input'''
n = int(input("How many elements?? "))
arr=[]
for i in range(n):
    value = int(input())
    arr.append(value)

print(arr)
