employee_file = open("employees.txt", "r")
# r means you can just read the info in the file

# print(employee_file.read())


# print(employee_file.readline())

# print(employee_file.readlines()[1])


for employee in employee_file.readlines():
    print(employee)


employee_file.close()

# open("employees.txt", "w")
# w means you can write, modify info in the file
#
# open("employees.txt", "r+")
# r+ means you can read or write



