a=["sai","priya","raji","Ashu","bhavya"]
b=[1,2,3,4,5]
c=['A','B','C','D','E']
dict1={}
list1=[]
i=0
while i<len(a):
    dict1[c[i]]={a[i]:b[i]}
    i+=1
list1.append (dict1)
print(list1)

