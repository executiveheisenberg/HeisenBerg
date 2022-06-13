#AUTHOR : HEISENBER
#TOPIC  :   ELSE IF test
a =int(input("Enter number "))
b =int(input("Enter number "))
c =int(input("Enter number "))
d =int(input("Enter number "))

if (a>b and a>c and a>d):
    print(a ," is greater")

if (b>a and b>c and b>d):
    print(b ," is greater")

if (c>a and c>b and c>d):
    print(c ," is greater")

if (d>a and d>b and d>c):
    print(d ," is greater")

else:
    print("Its a same")
print("done")
