class Student():
    name = ""
    age = 21
    year = 2
    color = "blue"
    Teacher = "John"

    # constructor
    def __init__(self):
        print("Making a new student")

    # Creating another function
    def change_details(self):
        print("Please enter your name: ")
        self.name = input()

        print("Please enter your age: ")
        self.age = int(input())

    def show_details(self):
        print("The details of the students are: \n")
        print(self.name, "\n", self.age, "\n", self.year, "\n", self.color, "\n", self.Teacher)

Mahid = Student()
Bob = Student()

Mahid.change_details()
Mahid.show_details()


Bob.change_details()
Bob.show_details()


