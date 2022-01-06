Data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
list1 =[]
# list1={}
# for i in Data.values(): 
#   if i in list1: 
#     continue 
#   else:
#     list1.append(i)
# print(list1)
# u_value = set( val for dic in Data for val in dic.values())
# print(u_value)
for i in Data:
    # print(i)
    for j,l in i.items():
        if i not in list1:
            list1.append(l) 
            # Data.update(list1)
# print(Data)
print(list1) 


 