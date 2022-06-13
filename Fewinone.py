    #   Counting 1 to 20
def count1():
    i=0
    for i in range(1, 21):
        print(i)
    start1=start()

    #   Mulplication of entered number
def multi():
    num1=int(input('Enter number to multiply: '))
    for i in range(1, 11):
        print(f'{num1} x {i} = {num1*i}')
    start1=start()
        
    #   Game time
def game():
    import random
    gm=input("Enter r for Rock, p for Paper, s for Scissor: ")
    if gm == 'r':
        print('You chose Rock')
    elif gm == 'p':
        print('You chose Paper')
    elif gm == 's':
        print('You chose Scissor')
    rdm=random.randint(1,3)
    if rdm == 1:
        print('Computer chose Rock')
    elif rdm == 2:
        print('Computer chose Paper')
    elif rdm == 3:
        print('Computer chose Scissor')
    start1=start()

    # Creating office file
def office():
    ofc0="officefile.txt"
    with open(ofc0,'a') as ofc:
        ofc1=ofc.write('\nThis is my file')
        print(ofc1)

    #   Program start from here
def start():
    choice=input('Enter your choice: ')
    if choice == 'c':
      cnt1=count1() 
    elif choice == 'm':
       multi1=multi()
    elif choice == 'g':
        game1=game()
    elif choice == 'o':
        office1=office()
        return 'File created'
        exit()
start1=start()
