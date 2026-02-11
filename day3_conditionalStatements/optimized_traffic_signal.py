print("TRAFFIC SIGNAL SYSTEM")
print("Vehicle Type: 1.Ambulance, 2.Fire, 3.Normal")

vehicle = input("Enter Vehicle type: ").strip().capitalize()
signal_colour = input("Enter Signal Colour: ").strip().capitalize()

if vehicle in ["Ambulance", "Fire"]:
    print("GO")
elif signal_colour == "Green":
    print("GO")
elif signal_colour == "Yellow":
    print("SLOW DOWN")
elif signal_colour == "Red":
    print("STOP")
else:
    print("Invalid Signal Colour")