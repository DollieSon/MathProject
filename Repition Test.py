Loop=int(input("Insert Input:"))
word=[]
seq=""
rep = False
print("input Seq:\n")
while Loop > 0 :
    seq=str(input())
    for x in word:
        if x == seq:
            print("Already Exists")
            rep = True
    if rep == False:
        word.append(str(seq))
    else:
        rep = False
    Loop -=1
for x in word:
    print(x)

input("press enter to exit")