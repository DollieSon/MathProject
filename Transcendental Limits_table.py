ans = int(input("insert number of sets: "))
loop = 0
x = []
y = []
find_y= lambda a:pow(a,2)+(7*a)+6
while loop < ans:
    x.append(float(input("x value:")))
    loop+=1
loop = 0
print(x)
while loop < len(x):
     print(find_y(x[loop]))
     loop+=1
loop=0

input("press enter to exit")
