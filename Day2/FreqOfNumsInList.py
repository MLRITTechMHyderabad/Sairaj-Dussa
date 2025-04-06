li=[1,3,5,6,6,1,4,2,8,33,9,8,10]
c=li[0]
d={}
outcount =0
for i in range(len(li)):
    incount=0
    b=li[i]
    for j in range(len(li)):
        if li[i]==li[j]:
            incount+=1
    if incount>outcount:
        d[c]=incount
        c=li[i]
print(d)