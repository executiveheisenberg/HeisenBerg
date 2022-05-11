from msvcrt import getch
from playsound import playsound


yname=input("Enter your Name ")
yb=input("Enter your Year of Birth ")
cname=input("Enter your Company name ")
sname=input("Enter Company State/City name ")
spin=input("Enter your State pin code ")
arname=input("Enter your office area name ")
arpin=input("Enter your area pin code ")

spin=int(spin)
yb=int(yb)
a=2022-yb
#a=int(a)
arpin=int(arpin)

#print(type(spin))

print("Hello ",yname)
print("Your Company name is confirmed ",cname)
print("Your Company address is confirmed ",sname)
print("You State ",sname," pin code is ",spin)
print("Your office area confirmed at ",arname)
print("Your office area pin code is ",arpin)
print("Hello",yname," your age is",a)

                                                #playsound("M:\\one\\sound.mp3")

getch()

