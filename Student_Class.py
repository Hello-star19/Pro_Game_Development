class Student():
   

    # constructor
    def __init__(self, name, age, year, color, Teacher):
        print("Making a new student")
        self.name = name
        self.age = age
        self.year = year   
        self.color = color
        self.Teacher = Teacher
   
   
    # Creating another function
    def change_details(self):
        print("Please enter your name: ")
        self.name = input()

        print("Please enter your age: ")
        self.age = int(input())

    def show_details(self):
        print("The details of the students are: \n")
        print(self.name, "\n", self.age, "\n", self.year, "\n", self.color, "\n", self.Teacher)

Mahid = Student("Mahid", 21, 2004, "Green", "Taylor")
Bob = Student("Bob", 22, 2003, "Blue", "Smith")
Mahid.show_details()

Mahid.change_details()
Mahid.show_details()


Bob.change_details()
Bob.show_details()


