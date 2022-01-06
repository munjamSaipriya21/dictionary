dic={1:["priya"],2:["sai"],3:["saipriya"]}
d={}
for i,j in dic.items():
    for  val in j:
        d[val]=i
    print(d)