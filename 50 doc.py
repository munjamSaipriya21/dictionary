dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
list1=[]
for i,j in dict.items():
    list2=[]
    if i not in list1:
        list2.append(i)
        list2.append(j)
    list1.append(list2)
print(list1)



# dict={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# list1=[]
# for i,j in dict.items():
#     list2=[]
#     if i not in list1:
#         list2.append(i)
#         list2.append(j)
#     list1.append(list2)
# print(list1)