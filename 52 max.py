my_dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f':100, 'g': 57, 'h': 8, 'i': 100}
m=0
first_max=0
second_max=0
third_max=0
list1=[]
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>first_max:
            first_max=my_dict[j]
            max1_key=j
        elif first_max>my_dict[j] and second_max<my_dict[j]:
            second_max=my_dict[i]
            second_key=j
        elif second_max >my_dict[j] and third_max<my_dict[j]:  
            third_max=my_dict[j]
            third_key=j
list1.append(max1_key)
list1.append(second_key)
list1.append(third_key)
print("first_max",max1_key)
print("second_max",second_key)
print("third_max",third_key)
print(list1)
