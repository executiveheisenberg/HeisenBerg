import random
randnum = random.randint(1,10)
user1="hi"
guesses = 0

while(user1 != randnum):
    user1=int(input('Guess the number: '))
    guesses += 1
    if(user1 == randnum):
        print('You guessed it right')
        print(randnum)
    else:
        if user1 > randnum:
            print('You guessed it wrong, try smaller number ')
            
        else:
            print('You guessed it wrong, try larger number ')    

if guesses > 2:
                print('You are taking too much gyesses')
                exit()
print(f'You guessed the number in {guesses} guesses ')