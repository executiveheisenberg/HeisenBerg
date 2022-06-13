sb1=int(input("Enter 1st subject marks "))
sb2=int(input("Enter 2nd subject marks "))
sb3=int(input("Enter 3rd subject marks "))

if  (sb1<33 and sb2<33 and sb3<33):
    print("You're fail bcoz of less % in one of few subject")

if  (sb1+sb2+sb3/3<40):
    print("You're fail due to less than 40% marks")
if  (sb1+sb2+sb3/3>40):
    print("You're pass due to more than 40% marks")


