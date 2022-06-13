txt=input("Do you want to create new file? ")
if txt == 'y':
    fname=input('Enter filename with .txt extension ')
    fname2=open(fname, 'w')
    rd=fname2.write(fname)
    fname3=input('you want to add contents to your file ')
    if fname3 == 'y':
        wrt=input('Write something\n')
    fname2=open(fname, 'a')
    rd=fname2.write(wrt)
    fname2=open(fname)#, 'a')
    print(rd)
    print()    
elif txt != 'y':
    print('OK')
    ok=input("enter name of file you want to run ")
    if '.txt' in ok:
        fname4=open(ok)
        rd=fname4.read()
        print(rd)
        exit()
    else:
        print("invalid file, please add .txt at the end of file")
        exit()
