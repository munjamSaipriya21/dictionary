d = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
# print(students['Aex']["class"])
# print(students['Aex']['rolld_id'])
# print(students['Puja']["class"])
# # print(students['Puja']['roll_id'])
# for i,j in students.items():
#     print(i)
#     for k in j:
#         print(k)
#         # d={}
#         for m in k:
#             d[k]=m
#         print(d)
            
# for i,j in d.items():
#     print(i)
#     for m in j.items():
#         print(m)


for i in d:
    print(i)
    for j in d[i]:
        print(j,":",d[i][j])