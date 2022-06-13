cn=input('do you want to create new file now? ')
if cn == 'y':
    fname=input("enter file name with txt extension\n")
    txt=open(fname, 'r')#gives a name to variable open then bracket
    rd=txt.read()
    print('Done\n',rd)
    cn2=input('Do you want to add contents now? ')
if cn2 == 'y':
    cnt=input("Enter contents to your file\n")
    txt=open(fname, 'w')
    rd=txt.write(cnt)
    if 'welcome' in cnt:
        print("Thanks for welcoming\n")
    else:
        print('no welcome\n')
    print('Done writing')
        
else:
    exit()


    # txt=open(fname,'r')
    # rd=txt.read()
    # print(rd)