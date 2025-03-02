

def main():
   height = int(input("enter how many bricks u want?"))
   build(height)


def build(n):
    for i in range(n):
        print("#", end="\n")

main()