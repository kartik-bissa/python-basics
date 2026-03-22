class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

    def is_pass(self):
        return self.marks >= 40

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "D"


s1 = Student("Kartik", 101, 92)
s2 = Student("Rahul", 102, 38)

s1.display()
print("Pass Status:", "Pass" if s1.is_pass() else "Fail")
print("Grade:", s1.grade())

print()

s2.display()
print("Pass Status:", "Pass" if s2.is_pass() else "Fail")
print("Grade:", s2.grade())
