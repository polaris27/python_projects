import random
l = ['python', 'java', 'kotlin', 'javascript']
b = random.choice(l)
length = len(b)
hyphen = "-" * (length)
print("H A N G M A N")

while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "exit":
        break
    elif choice != "play":
        continue
    itr = 8  #chances
    repeat_list = []  # characters that have already been used as input
    while itr > 0:
        print()
        print(hyphen)
        a = input("Input a letter: ")
        if len(a) != 1:
            print("You should input a single letter")
            continue
        if not(a.islower()):
            print("Please enter a lowercase English letter")
            continue
        if a in repeat_list:
            print("You've already guessed this letter")
            continue
        else:
            repeat_list.append(a)
        if a in b:
            h = ""  # creating the new letters and hyphens combo
            for i in b:
                if i in repeat_list:
                    h += i
                else:
                    h += "-"       
            hyphen = h
        
            if hyphen == b:  # checking if the full word is guessed or not
                print(b)
                print("You guessed the word {0}!".format(b))
                print("You survived!")
                print()
                
        else:
            print("That letter doesn't appear in the word")
            itr -= 1
    else:
        print("You lost!")
        print()
