import random

Loop = 0
MxLoop = 10000000
H = 0
X = 0
Y = 0
#0,1,2,3,4,5
Result =  [0,0,0,0,0,0]
error =0
End =0
while Loop < MxLoop:
    while X < 5:
        H+= random.randint(0,1)
        X +=1
    X = 0
    if H == 0:
        Result[0] += 1
    elif H == 1:
        Result[1] += 1
    elif H == 2:
        Result[2] += 1
    elif H == 3:
        Result[3] += 1
    elif H == 4:
        Result[4] += 1
    elif H == 5:
        Result[5] += 1
    else:
        error +=1
    if Loop % 100000 == 0:
        End +=1
        print(f'{End}/100')
    H = 0
    Loop += 1

print(f'{Result[0]}|| {Result[1]} || {Result[2]} || {Result[3]} || {Result[4]} || {Result[5]}')
print(f'{Result[0]/MxLoop}|| {Result[1]/MxLoop} || {Result[2]/MxLoop} || {Result[3]/MxLoop} || {Result[4]/MxLoop} || {Result[5]/MxLoop}')
print(f'{Result[0]/MxLoop + Result[1]/MxLoop + Result[2]/MxLoop + Result[3]/MxLoop + Result[4]/MxLoop + Result[5]/MxLoop}')
print(f'Error = {error}')

input("press enter to exit")
