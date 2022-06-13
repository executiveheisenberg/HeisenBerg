#AUTHOR : HEISENBER
#TOPIC  :   ELSE IF
print('''
    "878"     : "Anabond 878 tube size 100gm",
    "879"   :   "Anabond 879 tube size 150gm",
    "870"   :   "Anabond 870, tube size 100gm",
    "8784" :   "Anabond 878, 4.5kg size",
    "202i"  :   "Anabond 202i, tube size 20gm",
    "679c"  :   "Anabond 679 Clear, tube size 310gm"    ,
    "221"   :   "Anabond 221, tube size 1kg",
    "681"   :   "Anabond 681, tube size 100gm",
    "681hm" :   "Anabond 681HM, tube size 25gm","''')

prod=input("Enter product name\n ")
if (prod == "878"):

    prodq8=input("How much quantity you want\n")
    print("Anabond 878 tube size 100gm")
    print("Quantity is ",prodq8, "and price is 700+GST")
    prodq8=int(prodq8)
    c=700
    d=prodq8*c
    print("Your Total amount is ", d)
    print("+18% GST is ", d*.18)
    print("Grand total is ", d*.18+d)


elif (prod == "879"):
    prodq8=input("How much quantity you want\n")
    print("Anabond 879 tube size 150gm")
    print("Quantity is ",prodq8, "and price is 650+GST")
    prodq8=int(prodq8)
    c=650
    d=prodq8*c
    print("Your Total amount is ", d)
    print("+18% GST is ", d*.18)
    print("Grand total is ", d*.18+d)


elif (prod == "870"):
    prodq8=input("How much quantity you want\n")
    print("Anabond 870 tube size 100gm")
    print("Quantity is ",prodq8, "and price is 600+GST")
    prodq8=int(prodq8)
    c=600
    d=prodq8*c
    print("Your Total amount is ", d)
    print("+18% GST is ", d*.18)
    print("Grand total is ", d*.18+d)

elif (prod == "8784"):
    prodq8=input("How much quantity you want\n")
    print("Anabond 878 tube size 4.5kg")
    print("Quantity is ",prodq8, "and price is 1000+GST")
    prodq8=int(prodq8)
    c=1000
    d=prodq8*c
    print("Your Total amount is ", d)
    print("+18% GST is ", d*.18)
    print("Grand total is ", d*.18+d)

else:
    print("We dont have this product yet")

print("done")