# len -> tells length of list len(students)

students = ["hermione", "harry", "ron"]

# traditional way
for student in students:
    print(student)

# anotherway to access using index

for i in range(len(students)):  #range(3)
    print(i+1, students[i])