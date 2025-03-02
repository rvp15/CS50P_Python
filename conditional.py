def main():
    x = int(input("Enter value of x:"))
    if is_even(x): 
        print(f"x {x} is even")
    else:
        print("odd number")

def is_even(x):
    return True if x % 2 ==0 else False

main()