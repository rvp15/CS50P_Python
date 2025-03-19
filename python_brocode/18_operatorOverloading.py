class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self): # print statement is customized
        return f"point customized({self.x},{self.y}),"

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)

    #create 2 pont object
p1=Point(2,3)
p2=Point(3,4)
p3 =p1+p2
print(p3)