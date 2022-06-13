class remote():
    def pressed(self):
            print("""                    
                        ***Type read to Read Guest List 
                        ***Type exit to Exit the Program 
                        ***Type add to Add more Guests in file 
                        ***Type repl for Replace somthing in file
                        ***Type clr to Clear the file contents""")
select=input('Enter choice: ')
hotel = 'hotel.txt'
if select == 'r':
                with open (hotel,'r') as hotel1:
                    hotel0 = hotel1.read()
                    print(hotel0)
else:
                exit()
remote0 = remote()
chk = input('You want to see menu?: ')
if chk == 'y':
    remote0.pressed()
elif chk == 'x':
    remote0.pressed()
else:
    exit()

# class player(): 
#         def guest(self):
#             print("""                    
#                         ***Type read to Read Guest List 
#                         ***Type exit to Exit the Program 
#                         ***Type add to Add more Guests in file 
#                         ***Type repl for Replace somthing in file
#                         ***Type clr to Clear the file contents""")
#         # guest1=guest()
#         # chk=input('What you want to do: ')
# remote1 = remote()
# player1 = player()
# if(remote0.pressed()):
#     player1.guest()
# else:
#     exit()
        # def guestname(self):
        #     print("Guest name is: ", self.sfirstname, self.slastname)

        # myapp = guest()
        # myapp.firstname = 'Mayank'
        # myapp.lastname = 'Sharma'
        # myapp.guestname()
        