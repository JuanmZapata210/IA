a = int(input("Ingresa un numero:"))
b = int(input("Ingresa otro numero:"))
c = int(input("Ingresa un tercer numero:"))

if(a==b):
    if(a>c):
        print(c,a,b)
    else:
        print(a,b,c)
elif(a==c):
    if(a>b):
        print(b,a,c)
    else:
        print(a,c,b)
elif(a==b==c):
    print(a,b,c)
elif(a>b):
    if(a>c):
        if(b>c):
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        (b,a,c)
elif(b>a):
    if(c>a):
        if(b>c):
            print(a,c,b)
        else:
            print(a,b,c)
    else:
        print(c,a,b)

    


        

    