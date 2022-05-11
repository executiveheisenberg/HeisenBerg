#Author: HeisenBerg
#Topic: String slicing, basically it works like numbers...almost
from tokenize import Name

hello="Hey wasssup...."
name="mayank"
#b=" and How's you MAYANK"
# print(type(name))#telling name of variable
# print(name[0:4])#it will show maya instead of mayank as 0 is m, : sign is to and 4 is "a"
# print(name[3])#it will show "a" instead of mayank as 3 is a of mayank as word starts with 0 
# in python m-0 a-1 y-2 a-3 n-4 k-5
# print(name[4:])#nothing zt first means starts from 0 and end means last
c=name[0:6:2]#0:6 means first alphabet to 6th alphabet and last 2 means it will skip every alternative alphabet
print(c)

#print(a+b)#a and b will come in one line
#print(a[5])#Mayank is start from 012345
