emoticon = ":("

def main():
    global emoticon  # whenu wanted to access global variable you have to specify it inside the function and then u can modify it.
    say("Hi is anyone ther?")
    emoticon =":)"
    say("Oh! Hi!")

def say(pharse):
  
    print(pharse +" " + emoticon)


main()