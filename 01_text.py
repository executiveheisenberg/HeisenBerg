def def1():    
    txt=input('Enter text: ')
    if 'hey' in txt:
        
        txt1=txt.replace('hey', 'hola')
        print(txt1)
        print('Thanks')
        cn1=def1()
        print(cn1)
    # exit()
    elif 'hey' not in txt:
        txt2=txt.replace(txt, 'not compatible')
        print(txt2)
        print('No Thanks')
cn1=def1()
print(cn1)