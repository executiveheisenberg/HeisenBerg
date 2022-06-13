i=input("Enter R for rock P for paper and S for scissor\n")
if i == 'r':
    print("You selected rock\n")
if i == 'p':
    print("You selected paper\n")
if i == 's':
    print("You selected scissor\n")

import random
rin=random.randint(1,3)
print(rin)

if rin == 1:
    print("Computer selected Rock")
if rin == 2:
    print("Computer selected Paper")
if rin == 3:
    print("Computer selected Scissor")

if rin == 1 and i == 'r':
    print("Its A TIE")
if rin == 2 and i == 'p':
    print("Its A TIE")
if rin == 3 and i == 's':
    print("Its A TIE")
