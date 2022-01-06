# my_dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in my_dict1:
#     for j in my_dict1:
#         if  my_dict1[i]<my_dict1[j]:
#         # if  my_dict1[i]<my_dict1[j]:
#             a=my_dict1[i]
#             my_dict1[i]=my_dict1[j]
#             my_dict1[j]=a
# print(my_dict1)


my_dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dic=list(my_dict1.values())
dic.sort()
# d=dic.copy()
# d.reverse()
# print(dic)
dic2={}
for i in dic:
    for j in my_dict1:
        if i==my_dict1[j]:
            dic2[j]=i
print(dic2)


