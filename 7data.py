dict1=[

     {"first":"1"}, 

     {"second": "2"}, 

     {"third": "1"}, 

     {"four": "5"}, 

     {"five":"5"}, 

     {"six":"9"},

     {"seven":"7"}

]
a=[]
for i in dict1:
     for j in i.values():
          if j not in a:
               a.append(j)
print(a)

