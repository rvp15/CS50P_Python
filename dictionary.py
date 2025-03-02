# has keys and values

students ={
    "Herminoe":"gryffindor",
    "harry":"gryfindor",
    "Ron": "Slytherin"
}
 
print(students["Herminoe"]) # gives its value

# loop for dict
for student in students:
    print(student) # this gives only keys

for student in students:
    print(student, students[student],sep=",")  # gives key and its value s[s], seperated by ,

############################################33
    # dict with more proterties

studentss = [
    {
        "name":"gryffindor",
        "house": "ranipet",
        "patronus":"otter"
    },
      {
        "name":"gryffindor1",
        "house": "chennai",
        "patronus":"stage"
    },
      {
        "name":"gryffindor2",
        "house": "us",
        "patronus":None# absence of value like null
    }
]

for student in studentss:
    print(student["name"], student["house"],student["patronus"], sep=(","))  
#gryffindor,ranipet,otter
#gryffindor1,chennai,stage
#gryffindor2,us,None