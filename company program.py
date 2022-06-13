
prod={
    "878"     : "Anaobond 878 tube size 100gm",
    "879"   :   "Anaobond 879 tube size 150gm",
    "870"   :   "Anabond 870, tube size 100gm",
    "878.4" :   "Anabond 878, 4.5kg size",
    "202i"  :   "Anabond 202i, tube size 20gm",
    "679c"  :   "Anabond 679 Clear, tube size 310gm"    ,
    "221"   :   "Anabond 221, tube size 1kg",
    "681"   :   "Anabond 681, tube size 100gm",
    "681hm" :   "Anabond 681HM, tube size 25gm",
}
prodp={
    "878"  :   "Packing for Anabond 878 is 50",
    "879"  :   "Packing for Anabond 879 is 50",
    "870"  :   "Packing for Anabond 870 is 50",
    "202i" :   "Packing for Anabond 202i is 300 ",
    "679c":   "Packing for Anabond 679 clear is 50",
    "221"  :   "Packing for Anabond 221 is 10 ",
    "681"  :   "Packing for Anabond 681 is 50",
    "681hm":   "Packing for Anabond 681HM is 300",
}

print("Select from list\n", prod.keys())
a=input("Enter Product name ")
print(" ", prod[a])

# b=int(b)
print("Select packing name ",prod.keys())
b=input("Enter which packing ")
# print(" ", prodp[b])

if (b=="878"):
    print("You have selected Anabond 878 to pack")
d=b+78
print("Total is ", d)
if (b=="879"):
    print("You have selected Anabond 879 to pack")
    # d=b*79
if (b=="870"):
    # d=b*70    
    print("You have selected Anabond 870 to pack")

if (b=="878.4"):
    print("You have selected Anabond 878 to pack")

else:
    print("Wrong selection")
    # d=b*84

# c=(int(c))
# s=(c*a878)
# print(s)

# # # b=input("How much you want ")
# # print(prod*5)

