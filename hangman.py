'hangman game'
# for providing a random no.
import random
def hang(num):
    'Drawing Hangman'
    if num == 1:
        print("  __\n |  |\n o  |\n    |\n    |")
    if num == 2:
        print("  __\n |  |\n o  |\n/   |\n    |")
    if num == 3:
        print("  __\n |  |\n o  |\n/|  |\n    |")
    if num == 4:
        print("  __\n |  |\n o  |\n/|\\ |\n    |")
    if num == 5:
        print("  __\n |  |\n o  |\n/|\\ |\n/   |")
    if num == 6:
        print("  __\n |  |\n o  |\n/|\\ |\n/ \\ |")
        print("You failed ! The name was", name)
#for obtaining random no.s
F_NAME = "hangman_names.txt"
file_name = open(F_NAME)
for lines in file_name:
    names = lines.split()
displayname = list()
FLAG = 0
FAILED = 0
guessed = list()
FAIL = 0
print("Welcome to Hangman\n Enter an alphabet ")
#Your random Name is this
variable_k = random.randint(0, 4)
name = names[variable_k]
len_name = len(name)
#dashing all the letters
for el in range(0, len_name):
    displayname.append("_ ")
while FLAG == 0:
    #printing the output name
    for element in displayname:
        print(element, end=" ")
    print("\n")
    #checking if all the letters are disclosed
    if "_ " in displayname:
        #taking the input from the user
        letter = input("Enter your letter: ")
        try:
            letter = int(letter)
            print("Enter only alphabets")
            continue
        except ValueError:
            letter = letter.upper()
            #checking if the letter is already guessed
        if letter in guessed:
            print("You already guessed that alphabet")
        else:
            guessed.append(letter)
            for let in range(0, len_name):
                if name[let] == letter:
                    displayname[let] = letter
                    FAIL = 1
                else:
                    continue
            if FAIL == 1:
                FAIL = 0
            else:
                FAILED += 1
                hang(FAILED)
                if FAILED == 6:
                    break
    else:
        print("YOU WON")
        break
