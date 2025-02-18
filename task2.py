class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I am {self.name}. I am {self.age} years old and I am studying {self.course}.")

# Create three student objects
student1 = Student("Patrick", 20, "Computer Science")
student2 = Student("Bobby", 22, "Mathematics")
student3 = Student("Charlot", 21, "Physics")

# Call their introduce method
student1.introduce()
student2.introduce()
student3.introduce()
