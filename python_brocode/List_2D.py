

fruits = ["Apple", "Banana", "Cherry","Mango", "Papaya", "Pineapple"]
vegetables = [ "Carrot", "Broccoli", "Spinach", "Potato", "Tomato", "Onion", "Cucumber", "Lettuce", "Bell Pepper"]
meat = ["Chicken", "Beef", "Pork", "Lamb", "Turkey", "Duck",  "Fish", "Shrimp", "Crab"]

groceries =[fruits,vegetables,meat]
# 1. Access 2d_list:
print(groceries[0][0]) #Apple
print(groceries[2][1]) #Beef

# 2. iterate: using nested loop:

for grocery in groceries:
    for item in grocery:
        print(item, end =" ")
    print()