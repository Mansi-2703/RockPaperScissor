import random as rd
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
l=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user>=3 or user<0:
    print("Invalid input")
print("Your choice is: ", l[user])

a=rd.randint(0,2)
print("Computer's choice is:",l[a])
if user==a:
    print("It's a DRAW !!")
elif user==0 and a==2:
    print("You Won!!")
elif user==2 and a==1:
    print("You Won!!")
elif user< a:
    print("You Lose...Wanna try again?")
elif user> a:
    print("You Won!!")
