import re

#1.Pattern
row = r"222,'ved',\n200,'abc_8.9@gmail.com'"
row1 = r"'priya.45@gmail.com"

pattern = r"[a-z]+@gmail.com"  #[a-z] leftside of @gmail.com=> there may be any letter a-z and + => there may be any number of alphabet
pattern = r"[a-z]+@gmail.com"
pattern = r"[a-z]+@[a-z]+.[a-z]+" # any_no_letters@any_no_letter.any_no_letter

#numerical values
pattern = r"[a-z0-9]+@[a-z]+.[a-z]+" # any_no_letters/numerals@any_no_letter.any_no_letter  eg: ved89@gmail.com

#special Symbol:
pattern = r"[a-z0-9_]+@[a-z]+.[a-z]+" # any_no_letters/numerals@any_no_letter.any_no_letter  eg: ved_89@gmail.com

# Dot Symbol:
pattern = r"[a-z0-9_.]+@[a-z]+.[a-z]+" # any_no_letters/numerals@any_no_letter.any_no_letter  eg: ved.89@gmail.com
re.search(pattern,row1)

# {n} number of occurrence: here, there will be 3 occurrences in [a-z]
pattern = r"[a-z0-9_.]+@[a-z]+.[a-z]{3}" # any_no_letters/numerals@any_no_letter.any_no_letter  eg: ved.89@gmail.com

# https://quickref.me/regex.html

# 2. \w+ - Matches the Username (Before @)
# \w → Matches any word character (letters, digits, underscores) → [a-zA-Z0-9_]
# + → Matches one or more occurrences
# So, \w+ ensures there is at least one character before the @

emails = ["test@example.com", "invalid-email", "user@domain.org", "hello@world.net"]

pattern = r"^\w+@\w+\.\w+$"  # Simple email pattern

# Using list comprehension to filter matching emails
valid_emails = [email for email in emails if re.match(pattern, email)]

print(valid_emails)


