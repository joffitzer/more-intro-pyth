#student class is defined in the classes.py file
from classes import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.6, True)


print(student1.major)

print(student2.is_on_probation)