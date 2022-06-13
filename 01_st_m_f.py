def game():
    num1=int(input('Enter number '))
    for i in range(1, 11):
        num2=(f"{num1},x, {i},=,{num1*i}")
        print(num2)
    cn1=input("you want to add this in your file? ")
    if cn1 == 'y':
        with open('multiplication.xls','a') as txt:
            for i in range(1, 11):
                # num2=(num1, "x" , i, '='  , num1*i)
        # print``
                txt.write(f"{num1}\tx \t{i}\t=\t{num1*i}\n")
 
        txt=open('multiplication.xls')
        rd=txt.read()
        print(" \n")
        print(rd)
        y=input('you want to continue? ')
        if y == 'y':
            score = game()
            print(score)
        else:
            exit()
    else:
        exit()
score = game()