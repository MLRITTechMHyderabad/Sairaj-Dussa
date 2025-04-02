a=[[1,2],[3,4],[5,6]]
min=a[0][0]
max=a[0][0]
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if a[i][j]>max:
            max=a[i][j]
        if a[i][j]<min:
            min=a[i][j]
print("minimun value",min)
print("maximunm value",max)