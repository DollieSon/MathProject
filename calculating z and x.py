#x, mean, variance
find_z= lambda a,b,c:(a-b)/c
#z, mean, variance
find_x= lambda a,b,c:b+(a*c)
x=[]
y=[]
z=[]
loop=0
grad=int(input("[0]finding z [1]finding x: "))
ans=int(input("digits: "))
if grad == 0:
    while ans>loop:
        x.append(float(input("X:")))
        y.append(float(input("mean:")))
        z.append(float(input("variance:")))
        ans-=1
    while loop < len(x):
        print(find_z(x[loop],y[loop],z[loop]))
        loop+=1
elif grad == 1:
    while ans>loop:
        x.append(float(input("Z:")))
        y.append(float(input("mean:")))
        z.append(float(input("variance:")))
        ans-=1
    while loop < len(x):
        print(find_x(x[loop],y[loop],z[loop]))
        loop+=1


input("press enter to exit")