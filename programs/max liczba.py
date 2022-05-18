x=int(input("Wpusz"))
y=int(input("ok"))
z=int(input("ok"))

if(x>y and x>z):
    print(x)
elif(z>y and z>x):
    print(z)
elif(y>x and y>z):
    print(y)
elif(x==y and z==x and y==z):
    print("=")

