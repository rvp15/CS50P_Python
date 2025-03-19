# shopping cart program

foods =[]
prices= []
total =0

while True:
    food = input("Enter food you want to buy or q to quit:")
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input(f"Enter price of {food}"))
        prices.append(price)

print("============Your Cart============")

for food,price in zip(foods,prices): # Correct way to iterate over both lists
    print(f"{food}: {price}")

print(f"Total :{sum(prices)}")
