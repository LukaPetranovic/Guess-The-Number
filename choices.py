import random

def choice1():
    randomNumber = random.randint(0, 1000000)
    print("Hm, hm, hm, what number could it be?\nBe careful, you only have 15 tries.")
    guessCounter = 0
    while guessCounter < 15:
        userInput = int(input("I think the number is: "))
        if userInput == randomNumber and guessCounter == 0:
            print("HOLLY GUACAMOLE! First try! You should definitely try playing jackpot.")
            break
        elif userInput == randomNumber:
            print("Well done, I knew you could do it.")
            break
        elif userInput < randomNumber:
            if guessCounter == 14:
                print("Sorry, out of tries. Number was {}.".format(randomNumber))
            else:
                print("Could be {} or {}... Maybe {}, but it is definitely higher than {}.".format(
                    random.choice(range(userInput, 1000000)), random.choice(range(userInput, 1000000)),
                    random.choice(range(userInput, 1000000)), userInput))
            guessCounter += 1
        elif userInput > randomNumber:
            if guessCounter == 14:
                print("That's it, you ran out of tries. Number was {}.".format(randomNumber))
            else:
                print("{}, {}, {}, who knows. But it is definitely lower than {}.".format(
                    random.choice(range(0, userInput)), random.choice(range(0, userInput)),
                    random.choice(range(0, userInput)), userInput))
            guessCounter += 1

def choice2():
    lowestLimit = int(input("Please tell me, what will be the lowest number possible?\n"))
    highestLimit = int(input("Please tell me, what will be the highest number possible?\n"))
    randomNumber = random.randint(lowestLimit, highestLimit)
    print("Hm, hm, hm, what number could it be?\nBe careful, you only have 10 tries.")
    guessCounter = 0
    while guessCounter < 10:
        userInput = int(input("I think the number is: "))
        if userInput == randomNumber and guessCounter == 0:
            print("HOLLY GUACAMOLE! First try!")
            break
        elif userInput == randomNumber:
            print("Well done, I knew you could do it.")
            break
        elif userInput < randomNumber:
            if guessCounter == 9:
                print("Sorry, out of tries. Number was {}.".format(randomNumber))
            else:
                print("Could it be {}? But it is definitely higher than {}.".format(
                    random.choice(range(userInput, highestLimit)), userInput))
            guessCounter += 1
        elif userInput > randomNumber:
            if guessCounter == 9:
                print("That's it, you ran out of tries. Number was {}.".format(randomNumber))
            else:
                print("Why not try {}? Maybe luck is on your side. But it is definitely lower"
                      " than {}.".format(random.choice(range(lowestLimit, userInput)), userInput))
            guessCounter += 1