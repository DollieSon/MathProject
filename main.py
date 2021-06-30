x = [0,1,2,3,4,5]
y = [0, 0, 0, 0, 0,0]
f = [0, 0, 0, 0, 0,0]
d = [0, 0, 0, 0, 0,0]

lop = 6
z = 0
# solving
while lop > 0:
    y[z] = ((22 + x[z])/(25 + x[z]))
    lop -= 1
    z += 1

# printing
lop = 6
z = 0
while lop > 0:
    print(f" x={x[z]}  y={y[z]}")
    lop -= 1
    z += 1


input("press enter to exit")