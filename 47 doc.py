student={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
dic={}
for i in student:
    for j in student.values():
        j.clear()
        dic[i]=j
print(dic)
