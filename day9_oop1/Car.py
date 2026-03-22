class Car:
    def __init__(self,brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print(f"Car Brand: {self.brand}, Speed: {self.speed}")

c1 = Car("Toyota", 120)
c1.display()