n = int(input("Enter A Positive Number: "))
count = 0
sum_digits = 0
reverse = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    reverse = reverse * 10 + digit
    count += 1
    n = n // 10

print("Total Digits: ",count)
print("Sum Of Digits: ", sum_digits)
print("Reverse: ",reverse) 
