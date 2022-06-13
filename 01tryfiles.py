new1=input("Do you want to create a new file? ")
if new1 == 'y':
        print("OK")
        fname=input("Enter file name ")
        txt=open(fname,'w')
        # print(txt)
        print("Done Sucessfully")
        fedit=input("You want to Enter contents in file now? ")
if fedit == 'y':
        txt1=input("Enter contents\n")
        rd=txt.write(txt1)
        print("Entered ")
        txt=open(fname, 'r')
        rd=txt.read()
        print(rd)
        exit()
elif fedit != 'y':
        exit()

# rd=t.write('Mayank\tAkash\tVibha\n')
# rd=t.read()
# t=open('exmaple.txt')
# rd=t.read()
        
elif new1 != 'y':
        exit()
# print("OK")

#     f=open('products.txt', 'a')#1234
# prod=input("Enter product details\n")
# rd=f.write(prod)#tell text file to complete writing