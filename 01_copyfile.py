filename = 'file1.txt'
filename2 = 'file2.txt'

# with open(filename) as fl1:
#     rd=fl1.read()

with open(filename,'w') as fl1:
    rd=fl1.write('This is file 1')
    # print(rd)

with open(filename) as fl1:
    rd=fl1.read()
    print(rd)

with open(filename2,'w') as fl2:
    fl1=fl2.write(rd)
    # print(fl1)

# with open(filename2) as fl2:
#     fl1=fl2.read()
#     print(rd)