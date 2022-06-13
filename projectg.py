

b=input("Player's turn: select (r) for Rock, (p) for Paer, (s) for Scissor ")
if b == "r":
        print("You have selected Rock")

if b == "p":
        print("You have selected Paper")

if b == "s":
        print("You have selected Scissor")


# print("Compter turn: Conputer selected ")
import random
rdno = random.randint(1, 3)

print(rdno)
if rdno == 1:
        print("Computer have selected Rock")

if rdno == 2:
        print("Computer have selected Paper")

if rdno == 3:
        print("Computer have selected Scissor")
