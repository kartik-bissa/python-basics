num = int(input("Enter a numer: "))
temp = num
sum = 0
while(num > 0):
    digit = num % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i

    sum += fact
    num //= 10

if temp == sum:
    print("IT IS A STRONG NUMBER")
else:
    print("NOT A STRONG NUMBER")