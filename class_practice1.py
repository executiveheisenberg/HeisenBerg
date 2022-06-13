class person:
    country = 'INDIA'
    def takebreath(self):
        print('IM BREATHING')

class employe(person):
    company = 'honda'
    def getsalary(self):
        print(f'Salary is {self.salary}')
    def takebreath(self):
        print('im programmer and luckily breathing')

class programmer(employe):
    company = 'fiverr'
    def getsalary(self):
        print('no salary')

p = person()
e = employe()
pr = programmer() 
e.takebreath()        

