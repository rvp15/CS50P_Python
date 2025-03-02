shoes = ["nike air max", "Adidas ultraBoost     ", "puma suede", "Reebok Classic"];


cleanedShoes =[]
for shoe in shoes:
        #print(shoe.capitalize()) # only capitalize first letter
        cleanedShoes.append(shoe.strip().title()) # capitalize every first letter
        print(cleanedShoes)
    
print(" ".join(cleanedShoes)) # joins all the strings in array with a space or comma. first spcify formate, then join method with input as argument



word = "racefcar"

reversed_word = word[::-1]
if (reversed_word == word):
        print("Its a palindrome")
else:
     print("Not a Palindrome")   