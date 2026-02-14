n = int(input("Enter a numer: "))
if n <= 1:
    print("Not a prime number")

for i in range(2, n-1):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
    else:
        print(f"{n} is a prime number")
    
