#                                 #   Hotel Management Program

def hotels():
    hotel='Hotel.txt'
    with open(hotel) as hotl:
            hotl1=hotl.read()
            print(hotl1)
            addguest2=addguest()

def addguest():
    more=input('Do you want to Add Guest Name: ')
    if more == 'y':
        guestfirstname=input('Enter first name of the guest: ')
        guestsecondname=input('Enter last name of the guest: ')   
        preffood=input('Enter food preference VEG/NON-VEG: ')

        hotel = 'hotel.txt'
        with open(hotel,'a') as hotl2:
            hotl2.write('\n' + guestfirstname + '\t' + guestsecondname + '\t\t\tFood Prefered: ' + '\t' + preffood)
            print(' ********Information Added********')
        hotel = 'hotel.txt'
        with open(hotel) as hotl2:
            hotelr=hotl2.read()
            print(hotelr)
            menu=menu() 
    else:
        exit()
def guestclr():
    sure=input('Do you want to clear the file? ')
    if sure == 'y':
        code=input('Input code to clear the file ')
        if code == '1231':
            hotel='hotel.txt'
            with open(hotel,'w') as clr:
                clr.write('')
                print('File Cleared')
                exit()
        
        elif code != '1231': 
            exit() 
    else:
        exit()
def replace():
        
        repl1 = input('What tyou want to replace ')
        repl2 = input('and replace with?: ')
        hotelr = 'hotel.txt'
        with open (hotelr, 'r') as hotelrp:
                content = hotelrp.read()
        if repl1 in content:
                content = content.replace(repl1, repl2) # to confirm the replacement
                with open(hotelr, 'w') as hotelreplace: # to replace
                        hotelreplace.write(content)
                        print('Done Replacement')
                        print(content)
        elif repl1 not in content:
                print('word not available')
                exit()

print("""                    
                        ***Type read to Read Guest List 
                        ***Type exit to Exit the Program 
                        ***Type add to Add more Guests in file 
                        ***Type repl for Replace somthing in file
                        ***Type clr to Clear the file contents""")
chk=input('What you want to do: ')
if chk == 'read':
        hotels=hotels()
elif chk =='add':
        addguest=addguest()
elif chk == 'repl':
        replend=replace()
elif chk == 'exit':
        exit()
elif chk == 'clr':
        hotelclr=guestclr()

else:
        print('You mistype')
        exit()

# def repl():
#     hot=hotel()
#     wname=input('Enter the word you want to replace: ')
#     wname2=input('Enter the words you want to replace with: ')
#     with open('hotel.txt') as pr:
#             content=pr.read()
#             print(content)
#     if wname in content:
#             content = content.replace(wname, wname2)
#             with open('hotel.txt', 'w') as pr:
#                 pr.write(content)
#                     # print(pr)
#             print(content)
#     # elif wname not in 'hotel.txt':
#             # exit()
#         # replx.replace('infmration', 'ADD')
#     # repl09=repl()# exit()

