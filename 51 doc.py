dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for i in dic:
    v=dic[i]
    dict1=[]
    for j in v:
        if j%2==0:
            dict1.append(j)
        dic[i]=dict1
print(dic)


# dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# for i in dic:
#     v=dic[i]
#     dict1=[]
#     for j in v:
#         if j%2==0:
#             dict1.append(j)
#         dic[i]=dict1
# print(dic)
    
        

