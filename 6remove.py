dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dict1={}
for i in dic:
    if dic[i] not in dict1:
        dict1.update (dic)
print(dict1)


# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# print(dic)

