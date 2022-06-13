
with open('deftest.txt', 'w') as def1:
        # print('\n')
    for i in range(1,11):
        defx="Hello",+i
        def0=def1.write(str(defx))
        print('file created', defx)
        # pass
        
        # return def0# print(def0)
def call_file1():

     with open('deftest.txt') as def1:
             def0=def1.read()
             return 'reading'
             exit()
callread=call_file1()
print(callread)

def calladd():
    txt1=input('do you want to enter text to add in file?\n')
    if txt1 == 'n':
        print('ok')
        print(callread)
    elif txt1 == 'y':
        txt=input('\nEnter text to add: ')
        with open('deftest.txt', 'a') as defa:
            rd=defa.write(txt)
            print(rd)
            exit()
callinput=calladd()
print(callinput)

num1=int(input("Input 1st number "))
num2=int(input("Input 2md number "))
if num1 > num2:
        print(callinput)
elif num2 > num1:
        print('not applicable')
        print(callread)
        exit()
    



