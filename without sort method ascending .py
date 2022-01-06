l=[1,2,5,7,3,9]
i=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
        j+=1
    i+=1
print(l)