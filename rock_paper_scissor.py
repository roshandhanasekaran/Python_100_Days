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

#Write your code below this line 👇
import random 
choice = int (input("choose a number between 1 to 3 "))
value = random.randint(0 ,choice-1)
if value == 0:
  print(rock)
elif value == 1:
  print(paper)  
else:
  print(scissors)

computer = random.randint(0, 2)
print (computer)
if computer == 0 :
  print (rock)
if computer == 1:
  print(paper)  
if computer == 2:
  print(scissors)
if value == computer:
  print("Its a draw")
if value == 0 & computer == 2:
  print("You win")
if value == 0 & computer == 1:
  print("the computer wins")
if value == 1 & computer == 0:
  print("You win")
if value == 1 & computer == 2:
  print("the computer wins")
if value == 0 & computer == 1:
  print("the computer wins")
if value == 2 & computer == 0:
  print("the computer wins")
elif value == 2 & computer == 1:
  print("you win")
