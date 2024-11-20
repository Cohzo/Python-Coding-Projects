import random

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

user_input = int(input('Choose either 0 for rock, 1 for paper or 2 for scissors: '))
options = [rock, paper, scissors]
computer_choice = random.choice(options)

if user_input == 0:
    print(rock)
    print("Computer's Choice", "\n", computer_choice)
    if computer_choice == paper:
        print("You Lose")
    elif computer_choice == scissors:
        print("You Win")
    else:
        print("Draw")
elif user_input == 1:
    print(paper)
    print("Computer's Choice", "\n", computer_choice)
    if computer_choice == scissors:
        print("You Lose")
    elif computer_choice == rock:
        print("You Win")
    else:
        print("Draw")
elif user_input == 2:
    print(scissors)
    print("Computer's Choice", "\n", computer_choice)
    if computer_choice == rock:
        print("You Lose")
    elif computer_choice == paper:
        print("You Win")
    else:
        print("Draw")
else:
    print("That was not a option")

