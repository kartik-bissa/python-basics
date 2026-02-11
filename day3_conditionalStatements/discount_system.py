amount = int(input("Enter Purchase Amount: "))
membership = input("Enter Membership(gold/silver/none): ").lower()
if amount <= 0:
    print("Invalid Purchase amount")
    exit()

discount = 0
if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 10
elif amount >= 1000:
    discount = 5

if membership == "gold":
    discount += 5
elif membership == "silver":
    discount += 3

if discount > 25:
    discount = 25

final_amount = amount - (amount * discount / 100)
print("Discount Applied: ",discount)
print("Final Amount: ",final_amount)
