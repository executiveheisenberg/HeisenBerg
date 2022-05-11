#Author: HeisenBerg
#Topic: GST
# print("878 for Anabond 878, 879 for Anabond 879 and so on ")
product='''Porduct you have selected is <prod>\n
and you product <prod> is available in stock, \n100gm of capacity'''

tellp = input("Select product name for Anabond\n")

product=product.replace("<prod>" ,tellp)
print(product)
