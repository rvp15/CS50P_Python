def main():
    name = input("What is your name?")
    hello(name)

def hello(name ="vedha"): # without argument it sets default value
    print(f"Hello {name}!") 
hello()
#hello(name) # here you can call the function only after it is defined else you get NameErro: that it is not defined
main()

# To resolve this function calling order, use main()
# define main(), define all functions inside main now calling before defining will not give error
# Python does not "hoist" functions like JavaScript, but the interpreter reads and compiles the whole script before execution begins.
# when the main() function is executed, all the functions defined above it in the script are already loaded into memory and callable.

