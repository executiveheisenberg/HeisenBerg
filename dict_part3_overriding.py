# Author: HeisenBerg
# Topic: ADVANCED Dictionary 3
dict1={
    "dk" : "bigo friend",
    "humming" : "bigo friend 2",   
    "harsh" : "bigo friend 3",
    "dict2" : {"mayankk":"double k"},
}

# print(dict1)
udict={#make normal dictionary first with any name
    "akash":"up friend",
    "isha":"up friend 2",
}
dict1.update(udict)#then update to that name
print(dict1.get("harsh"))#same as []
print(dict1["harsh"])
