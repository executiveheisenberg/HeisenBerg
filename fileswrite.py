f=open('sample2.txt', 'a')#open to use new brand file or old file and 'a' to give add contents permissiion
# f=open('sample2.txt', 'w')#open to use new brand file and 'w' to give write new contents  permissiion
f.write("\nNew product Adsil will be added to the list")#write contents to file
f=open('sample2.txt')
rd=f.read()
print(rd)
