# Author: HeisenBerg
# Topic: Praxtice 2 (LETTER)
letter='''Dear mayank, 
you are selected.
We are happy to inform you that you
have been selected for python program as dewveloper.

Date: <DATE>
'''

name=input("Enter name\n")
date=input("Enter Date\n")
letter=letter.replace("mayank" ,name)
letter=letter.replace("<DATE>" ,date)
print(letter)
# print(date)maya