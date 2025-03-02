name = input("What's your name?").strip().title()

print("Hello,", name)

"""  or #
( 3 qoutes-> multiline comments)
print function has arguments: print(*objects, sep=" ", end="\n")  => by default the print end with new line you can override it by reassigning end=""
"""

print("Hello, ", end="")
print(name)

# How do you use "" within """" -> you can acheive this using escape character \=> \" indicates that it is a escape character so ignore it
print("Hello, \"Friend!\"")

########################STRING METHODS################
 # Remove white space from string:
name = name.strip()

  # capitalize only the first letter
name = name.capitalize()

# title -> capitalize first letter of words
name = name.title()

# chaining methods:
name = name.strip().title()

# Atlast special srting format: print(f "hello, {name}") -> add f before qoutes and variable in {}
print(f"Hello, {name}")

# Split method:   similar to destructure 
first, last = name.split(" ")

print(f"Hello, {first}")