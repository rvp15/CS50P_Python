# both doesnt have index
#iterator
nums =  [1,2,3]
it = iter(nums) #The iter() function returns an iterator object, which can be used with next()
print(next(it))
print(next(it))
print(sum(nums))



#Enum: index and value while iterating
num1 = [3,5,6]

for index,value in enumerate(num1):
    print(f"index:{index} value:{value}")