import math


X =[]
Y =[]
A =[]
B =[]
C =[]

mean =0.0
variance = 0.0
deviation = 0.0
x2= lambda a: a**2
xPx = lambda a, b: a * b
x2px = lambda a, b: (a**2) * b
loops = 0
miterated = int(input("maxnum:"))

while loops < miterated:
    X.append(float(input("X input:")))
    Y.append(float(input("P(X) input:")))
    loops += 1
loops = 0
while loops < miterated:
    B.append(x2(X[loops]))
    A.append(xPx(X[loops],Y[loops]))
    C.append(x2px(X[loops],Y[loops]))
    mean +=A[loops]
    variance +=C[loops]
    loops+=1
deviation =math.sqrt(variance)
loops = 0

#table printing
print(f'X || P(X) || X P(X) ||X^2 || X^2 P(X)')
while loops < miterated:
    print(f'{X[loops]} ||{Y[loops]} ||{A[loops]} || {B[loops]} || {C[loops]} || ')
    loops+=1
print(f"mean = {mean} ")
print(f"variance = {variance} ")
print(f"deviation = {deviation} ")

input("press enter to exit")
