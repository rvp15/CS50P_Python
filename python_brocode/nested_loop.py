# nested loop = loop within another loop
#         outer loop:
#                 inner loop:

for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()

    # print a rectangle depending on users input
rows = int(input("Enter no of rows:"))
columns = int(input("Enter no of columns:"))
symbol = input("Enter a symbol:")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()