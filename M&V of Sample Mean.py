import math

##mean and variance of sample mean with random samples
#Deviation, Sample Size
f=[20,5,12,12]
x=[225,64,121,400]
ans=[]
tempans=0
#Number Of Deviation and Random Sample Size
loop=0
while loop < len(x):
    ans.append(float(f[loop]/math.sqrt(x[loop])))
    loop+=1
for x in ans:
    print(x)

input("press enter to exit")