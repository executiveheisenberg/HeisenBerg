def prog(run, run2):
    run=input("Do you want to run the Product management program y/n\n")
    if run == "n":
            print("Nooooo")
            exit()
    elif run == "y":
            print("Okay")
    f=open('sample.txt')#, 'r') #to give a file name and attributes
    rd=f.read()#tell text file to read
    print(rd)

    run2=input("Do you want to add more contents?\n")
    
    if run2 == 'n':
        s=prog('a', 'b') 
        print(" " +str(s))
        # exit()

    elif run2 == 'y':

        f=open('sample.txt', 'a')#1234
    prod=input("Enter product details\n")
    rd=f.write(prod)

# s=grt1('a','b','c')

# print(rd)
# p=input("Select product you want info for\n")
# if p == '878':
#     print("You have selected Anabond 878: 100Gm\nIt is a Rubber based product\n")
#     print(rd)
# elif p == '879':
#     print("You have selected Anabond 879: 150Gm\n")
# elif p == '870':
#     print("You have selected Anabond 870: 100Gm\n")
# else:
#     print("Product not specified yet\n")
#     exit()
