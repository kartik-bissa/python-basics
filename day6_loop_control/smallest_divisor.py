n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print(f"Smallest Divisor of {n} is {i}")
        break
    else:
        print(f"{n} is a prime number")
