my_dic={"a":[2,4,6],'b':[3,1,3]}
l=[]
d={}
for i in my_dic:
    l.append(my_dic[i])
    for j in l:
        sum=0
        for k in j:
            sum=sum+k
    d[i]=sum
print(d)