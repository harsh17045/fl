def validtri():
    a=int(input("enter one angle of triangle : "))
    b=int(input("enter second angle of triangle : "))
    c=int(input("enter third angle of triangle : "))
    add=a+b+c
    if add>180:
        print("triangle is not valid.")
    elif add<180:
        print("triangle is not valid.")
    else :
        print("triangle is valid.")

validtri()
