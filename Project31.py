class login1:
    def loginmenu1(self):
        loginorreg = input('You have to login first, do you want to login or register, press l for login or r for register first: ')
        if loginorreg == 'l':
                id = input('Enter Login ID: ')
                passw = input('Enter Password: ')
                loginfile = 'loginfile.txt'
                with open (loginfile, 'r') as lgfile:
                    lfile = lgfile.read()
                if id in lfile and passw in lfile:
                    print('Details Registered')
                
                else:
                    print('Details not registered or mismatch')
                    exit()
        elif loginorreg == 'r':
                userid = input('Enter new user id: ')
                userpass = input('Enter new password: ')
                name1 = input('Enter Name: ')
                userage = input('Enter your age: ')
                state1 = input('Enter State: ')
                loginfile = 'loginfile.txt'
                with open(loginfile,) as content1:
                    content = content1.read()
                with open(loginfile,'w') as contentw:
                    contentw.write(userid + '\n' + userpass + '\n' + name1 + '\n' + userage + '\n' + state1 + '\n')
                    print(contentw)
                    exit()

        else:
                exit()

class menu01(login1):
    def menu1(self):
                menu = input("""           
                                ******** Type 'read' to View file contents ********
                                ******** Type 'clear' to Clear file contents ********
                                ******** Type 'write' to Write something in file ********
                                ******** Type 'replace' to Replace something in file ********
                                ******** Type 'add' to Add Text in file ********
                                ******** Type 'backup' to Make Backup of file ********
                                ******** Type 'password' to Generate Random Password ********
                                ******** Type 'rps' to Play Rock Paper Scissor ********
                                 Enter choice or type 'exit' to EXiT--""")
                if menu == 'read':
                    mf.read()
                    m.menu1()
                elif menu == 'clear':
                    fileo.clear()
                    mf.read()
                    m.menu1()
                elif menu == 'write':
                    mf.read()
                    filet.write()
                    mf.read()
                    m.menu1()
                elif menu == 'replace':
                    mf.read()
                    filer.replace()
                    mf.read()
                    m.menu1()
                elif menu == 'add':
                    addtext0.add1()
                    mf.read()
                    print('Updated file')
                    mf.read()
                    m.menu1()
                elif menu == 'backup':
                    backupfil.backup1()
                    m.menu1()
                elif menu == 'password':
                    randompassc.randompas()
                    m.menu1()
                elif menu == 'rps':
                    rpsrun.randomdef()
                elif menu == 'exit':
                    exit()

                else:
                    m.menu1()
        
class mainfile(menu01):
    def read(self):
        file = 'officefile.txt'
        with open(file) as rd:
            rd1 = rd.read()
            print('File contents\n', rd1)

class file1(mainfile):
    def clear(self):
        confirm1 = input("Are you sure you want to clear the contents of this file? ")
        if confirm1 == 'y':
            code1=input("Input clearing code ")
            if code1 == '1231':
                file = 'officefile.txt'
                with open(file, 'w') as rd:
                    rd.write('')
                print('File cleared')
            elif code1 != '1231':
                   print('Wrong clearing code')
            exit()
        if confirm1 =='n':
            exit()

class file2(file1):
    def write(self):
        file = 'officefile.txt'
        with open(file, 'w') as rd:
            content = input('Enter text for the file: ')
            rd.write(content)
            print('Contents added')

class file3(file2):
    def replace(self):
        vname1 = input('Enter word to replace: ')
        vname2 = input('Enter word to replace with: ')
        txtfile = 'officefile.txt'
        with open(txtfile) as txtf:
            content = txtf.read()
        if vname1 in content:
            content = content.replace(vname1, vname2)
            with open(txtfile, 'w') as txf:
                txf.write(content)
                print(txf)
                print('done')
        else:
            print('No such word')
            exit()
class add(file3):
    def add1(file2):
        addtext1 = input('Enter text to add\n')
        file = 'table1.htm'
        with open(file, 'a') as addtext:
            addtext.write('\n' + addtext1)
            print(addtext)
class backup(add):
    def backup1(add):
        file = 'officefile.txt'
        with open(file) as rd:
            content = rd.read()
        fileb = 'oficefilebackup.txt'
        with open(fileb,'w') as backupfile:
               backupfile.write(content) 
class randompass(backup):
    def randompas(self):
        import random
        rnd1 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd2 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd3 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd4 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd5 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd6 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd7 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        rnd8 = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_@')
        print(rnd1 + rnd2 + rnd3 + rnd4 + rnd5 + rnd6 + rnd7 + rnd8)
        m.menu1()

class rps(randompass):
    def randomdef(self):
        import random
        # rock = rock
        random1 = random.randint(1,3)
        if random1 == 1:
            print('Rock')
        elif random1 == 2:
            print('Paper')
        elif random1 == 3:
            print("Scissor")
        m.menu1()

lg1 = login1()
m = menu01()
mf = mainfile()
fileo = file1()
filet = file2()
filer = file3()
addtext0 = add()
backupfil = backup()
rpsrun = rps()
randompassc = randompass()
lg1.loginmenu1()