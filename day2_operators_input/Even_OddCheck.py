n = input("Enter number to be checked: ")

if n == '':
    print("Nothing entered")
else:
    try:
        n = int(n)
        if n == 0:
            print("0 is even")
        elif n % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")

    except ValueError:
        print("Invalid Input, Enter integer")
