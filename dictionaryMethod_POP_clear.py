words = {
    "PAIR": 4,
    "HAIR":4,
    "CHAIR":5,
    "GRAPHIC":7
}

def main():
    print("Welcome")
    print(" Your letters are: AIPCRHG")

    while len(words)>0:
        print(f"{len(words)} left to guess!")
        guess= input("Guess a word:").upper()

        ######Check if the input is in the Dictionar and remove it if you have it
        if guess == "GRAPHIC":
            words.clear()
            print("You've won the game!")
        if guess in words.keys():
            ### remove this word from dict :POP method returns the value of your removed key 
            points = words.pop(guess) 
            print(f"Good job! you scored {points} points ")
            
    print("THATS the game")     
            


main()