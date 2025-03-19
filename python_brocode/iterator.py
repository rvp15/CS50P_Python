# Obj that represent sequence of data, and it allows you to iterate over it one at a time.
#
# iter() -> returns iterator object
# next() -> returns next item in the sequence / raises StopIteration where there is no more item to iterate

#############################################################################################
# Iterating Over File Objects: File Processing
#############################################################################################

# Avoids loading the entire file into memory.
# Efficient for large files.

with open("sample_text.txt") as file:
    for line in iter(file.readline, ""):
        print(line.strip())

#############################################################################################
# iterate
stu_detail =[("Hadev",90),("Myrta",88),("retina",89)]

stu_iter = iter(stu_detail)
while True:
    try:
        print(next(stu_iter))
    except StopIteration:
        print("End of report Card")
        break
print("-----------------------------------------")
#############################################################################################
# Using iter() for Lazy Evaluation: with yeild
# #############################################################################################
# Why use lazy evaluation?
# Saves memory by not preloading data.
# Fetches elements only when required.

def fetch_data():
    data = ["User1", "User2", "User3"]
    for item in data:
        yield item

data_iterator = iter(fetch_data())

print(next(data_iterator))
print(next(data_iterator))
#############################################################################################


#############################################################################################
#############################################################################################