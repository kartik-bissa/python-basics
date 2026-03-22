class Mobile:
    def __init__(self, brand, price, battery):
        self.brand = brand
        self.price = price
        self.battery = battery

    def display(self):
        print(f"Mobile Brand: {self.brand}, Price: {self.price}, Battery: {self.battery}mAh")

    def is_expensive(self):
        if self.price > 5000:
            return "Expensive"
        else:
            return "Affordable"
        
m1 = Mobile("Samsung", 6000, 4000)
m1.display()
print(m1.is_expensive())