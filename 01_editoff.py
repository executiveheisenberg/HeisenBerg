from tkinter import S


def products():
    print('\nA for Adding Products\nC for Clear contents of a file\nR for Read the file contents\nP for Replace\nG to Play Rock Paper Scissor')
    prd=input("\nPlease select your option\n")
    # prd=input('Do you want to add Products to a file?\n')
    if prd == 'a':
        ent1=input('Enter details:\n')
        print("\n")
        with open('products.txt', 'a') as pr:
            rd=pr.write(str('\n' +ent1))
        # print(rd)
        cnt=input('Do you want to add more products? Y/N: ')
        if cnt == 'y':
            prend = products()
            print(prend) 
        else:
                exit()
    elif prd == 'c':
        clr=input('Do you want to clear your file? Y/N: ')
        if clr == 'y':
            pass1=input('Enter code to clear: ')
            if pass1 != '1231':
                exit()
            else:
                with open('products.txt', 'w') as pr:
                    rd=pr.write(clr)
                    print('File Cleared')
                    prend = products()
                print(prend) 
        else:
                    exit()
    elif prd == 'r':
       
            with open('products.txt') as pr:
                rd=pr.read()
            print(rd)
            prend = products()
            print(prend) 
    elif prd == 'p':
            clr2=input('Do you want to Replace Something? Y/N: ')
            if clr2 == 'y':
                    pass1=input('Enter code to clear: ')
                    if pass1 != '1231':
                         exit()
                    else:
                        wname=input('Enter the word you want to replace: ')
                        wname2=input('Enter the words you want to replace with: ')
                        with open('products.txt') as pr:
                         content=pr.read()
                        print(content)
                    for word in wname:
                      content = content.replace(wname, wname2)
                    with open('products.txt', 'w') as pr:
                     pr.write(content)
                    # print(pr)
                    print(content)
                    prend = products()
                    print(prend) 
            elif clr2 == 'n':
                    prend = products()
                    print(prend) 
    elif prd == 'g':
        import random
        rdm=random.randint(1,3)

        print('         Welcome to Rock Paper Scissor')

        ut=input('Choose between "r" for Rock "p" for Paper or "s" Scissor\n')
        if ut == 'r':
            print("You have Selected Rock\n")
        elif ut =='p':
            print("You have Selected Paper\n")       
        elif ut =='s':
            print("You have Selected Scissor\n") 

        if rdm == 1 and ut == 'r' or rdm == 2 and ut == 'p' or rdm == 3 and ut == 's':
            tie='Tie'
            print("Computer have selected the same so its a", tie)
            prend = products()
            print(prend)
        elif rdm == 2 and ut == 's' or rdm == 1 and ut == 'p' or rdm == 3 and ut == 'r':
            print('Computer have selected ', rdm, '\n')
            print('***********************You Win***********************\n')
            prend = products()
            print(prend)
        elif rdm == 3 and ut == 'p' or rdm == 2 and ut == 'r' or rdm == 1 and ut == 's':
            print('********You loose********')
            prend = products()
            print(prend)
        
        elif rdm == 1:
            print("Computer have Rock")
            prend = products()
            print(prend)
        elif rdm == 2:
            print("Computer have Paper")
            prend = products()
            print(prend)
        elif rdm == 3:
            print("Computer have Scissor")
            prend = products()
            print(prend)
        elif rdm == 2 and ut == 's' or rdm == 1 and ut == 'p' or rdm == 3 and ut == 'r':
            print('***********************You Win***********************\n')
            prend = products()
            print(prend)
        elif rdm == 3 and ut == 'p' or rdm == 2 and ut == 'r' or rdm == 1 and ut == 's':
            print('********You loose********')
            prend = products()
            print(prend)

    else:
        exit()
    

prend = products()
print(prend)