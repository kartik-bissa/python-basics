units = int(input("Enter Units Of Electricity Consumed: "))
if units <= 100:
    rate = 5 * 100 
    print("TOTAL BILL: ",rate)
elif units <= 200:
    rate = 5 * 100 + 7 * (units-100)
    print("TOTAL BILL: ",rate)
else:
    rate = 5 * 100 + 7 * 100 + 10 * (units-200)
    print("TOTAL BILL: ",rate) 