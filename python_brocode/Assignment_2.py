# 2. Below are the details in 'student_marks.csv' data file.
#
# "RollNo","Spark","Python"
# 100,80,85
# 200,85,89
# 300,82,90
# 400,83,98
# 500,82,90
#
# 	Write a program to read the above 'student_marks.csv'.
# 	For each student record, find the total and write to a 'student_report.csv'
# Output Expected:
# 100,165
# 200,174
# 300,172
# 400,181
# 500,172

import csv

from Assignment_1 import total

# "RollNo","Spark","Python"
student_marks = [
   [100,80,85],
   [200,85,89],
   [300,82,90],
   [400,83,98],
   [500,82,90]
]
with open("student_marks.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RollNo","Spark","Python"]) # write header
    writer.writerows(student_marks) # write remaining rows
print("Data converted to CSV file is successful")

# For each student record, find the total and write to a 'student_report.csv'

with open("student_marks.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    temp =[]
    for row in reader:
        total_each =sum(map(int,row[1:]))
        print(f"{row[0]},{total_each}")
        temp.append([row[0],total_each])
        with open("student_report.csv","w",newline="") as file_1:
            writer = csv.writer(file_1)
            writer.writerows(temp)
    print("final Student report is successful")

