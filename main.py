from choices import choice1, choice2

print("Choose one of the following two options:\n1. Computer will choose any number.\n2. I will choose lowest and highest limit."
      "\nNOTE: Computer will choose numbers from 0 to 1 million.")

while True:
    try:
        userChoice = int(input("Your choice: "))
        if userChoice == 1:
            choice1()
        elif userChoice == 2:
            choice2()
        else:
            print("Please enter 1 or 2.")
            continue

        playAgainFlag = True
        while True:
            again = input("Do you want to play again?\nNOTE: New number will be randomized.\nY/N\n").lower()
            if again == "y":
                break
            elif again == "n":
                print("Thank you for playing.")
                playAgainFlag = False
                break
            else:
                print("Please refer to Y/N")
                continue
        if playAgainFlag == False:
            break

    except ValueError:
        print("Unallowed value entered. Please enter 1 or 2.")
