class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def compare(self,other):  # self=> calling object,
        if self.score >other.score:
            return print(f"student: {self.name} has higher score")
        else:
            return print(f"student: {other.name} has higher score")

student1 = Student("ved", 400)
student2 =Student("pri",500)

student1.compare(student2) # here,student1 is the calling object(self) # student2 is other object
