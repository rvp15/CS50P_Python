
def print_brick(size):
    #For each row in square
    for i in range(size):
        for j in range(size):
            #for each brick in a row, print brick
            print("#",end="")
        print()


print_brick(4)

## same think can also be done without inner loop 

def print_brick1(n):
    for i in range(n):
        print("#" * n)

print_brick1(3)