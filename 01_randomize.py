from pyparsing import WordStart

# words=['will','to']
fname=input('Enter the word you want to replace: ')
fname2=input('Enter the word you want to replace with: ')
words=fname
with open('sample2.txt') as f:
    content=f.read()
    print(content)
    
for word in words:
    content=content.replace(word, fname2
    with open('sample2.txt', 'w') as f:
        f.write(content)
        print(f)








# import random
# txt=print("q,w,e,rt,y,u,i,o,p")
# rd=random.randint(1,9)
# print(str(txt))