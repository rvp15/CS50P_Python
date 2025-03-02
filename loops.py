### while
i=0
while i<3:
    print("hello")
    i = i+1
 
##### While True: ask a question repeatedly until its true, break out if it is true, here it keep asking value of n untill user enters a positive value
while True:
    n = int(input("enter value of n:"))
    if n > 0:
        break  

for _ in range(n):
    print("meoww")
#####################################################################################################################
#FOR LOOP -> works with list (similar to array)

for i in range(4):    # range gives list of numbers range(4) == [0,1,2,3]
    print(f"hello {i}")
# here i is not used anywhere so you can replace it with _ :  for _ range(3): print("hello")

# intersting way to repeat print:
print("meow \n" *3)

