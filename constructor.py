class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# Example usage:
student1 = Student(name="Sajin", roll="222107020", marks={"Math": 85, "Science": 78, "History": 92})

# Accessing student information:
print(f"{student1.name} (Roll No. {student1.roll})")
print(f"Math Marks: {student1.marks['Math']}")
print(f"Science Marks: {student1.marks['Science']}")
print(f"History Marks: {student1.marks['History']}")

#O/P 
'''
Sajin (Roll No. 222107020)
Math Marks: 85
Science Marks: 78
History Marks: 92
'''