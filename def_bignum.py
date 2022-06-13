def grt1(num1, num2, num3):
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    num3=int(input("enter third number\n"))
    
    if (num1 > num2 and num1 > num3):
        # if (num1 > num3):
            return num1
    
    if (num2 > num1 and num2 > num3):
        # if (num1 > num3):
            return num2
    else:
            return num3
    
    # else:
    #     if (num2 > num3):
    #         return num2
    #     else:
    #         return num3

s=grt1('z','x','c')
print("Big number is " + str(s))
# grt1(num1,num2,num3)