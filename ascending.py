my_dict1= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
list1=[]
for i in my_dict1:
    for j in my_dict1:
        if my_dict1[i]>my_dict1[j]:
            a=my_dict1[j]
            my_dict1[j]=my_dict1[i]

            my_dict1[i]=a
        list1.append(my_dict1[i])
print(list1)
# print(my_dict1)
# print(list1)
