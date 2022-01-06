# my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# first_max=0
# second_max=0
# third_max=0
# dict={}
# for i in my_dict:
#     for j in my_dict:
#         if my_dict[j]>first_max:
#             first_max=my_dict[j]
#             max1_key=j
#         elif first_max>my_dict[j] and second_max<my_dict[j]:
#             second_max=my_dict[i]
#             second_key=j
#         elif second_max >my_dict[j] and third_max<my_dict[j]:  
#             third_max=my_dict[j]
#             third_key=j
# dict[max1_key]=first_max
# dict[second_key]=second_max
# dict[third_key]=third_max
# print(dict)

my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
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


