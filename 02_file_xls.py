num1=int(input('Enter number '))
for i in range(1, 11):
    num2=(f"{num1},x, {i},=,{num1*i}")
    print(num2)
cn1=input("you want to add date in your file? ")
if cn1 == 'y':
    cn2=input("Enter date")
    with open('multiplication.xls','a') as txt:
        
                txt.write(f"\n\n\n{cn2}")
                txt=open('multiplication.xls')
                rd=txt.read()
    print(rd)
else:
    exit()