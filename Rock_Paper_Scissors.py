import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

userInput = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
randomNum = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
items = [rock, paper, scissors]
if userInput >= 3 or userInput < 0:
    print("You entered wrong input so you lose!")
else:
    print("Your choice: ")
    print(items[userInput])
    print("\nComputers chose: ")
    print(items[randomNum])

    # Method 1
    # if userInput == randomNum:
    #     print("It's a draw")
    # elif (userInput == 0 and randomNum == 1):
    #     print("You lose!")
    # elif (userInput == 1 and randomNum == 0):
    #     print("You won!")

    # elif userInput == 1 and randomNum == 2:
    #     print("You lose!")
    # elif userInput == 2 and randomNum == 1:
    #     print("You won!")

    # elif userInput == 0 and randomNum == 2:
    #     print("You won!")
    # elif userInput == 2 and randomNum == 0:
    #     print("You lose!")


    # Method 2
    if userInput == 0 and randomNum == 2:
        print("You won!")
    elif userInput == 2 and randomNum == 0:
        print("You lose!")
    elif userInput > randomNum:
        print("You win!") 
    elif userInput < randomNum:
        print("You lose!") 
    elif userInput == randomNum:
        print("It's a draw")