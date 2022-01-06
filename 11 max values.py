my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
first_max=0
second_max=0
third_max=0
list1=[]
for i in my_dict:
    if my_dict[i]>first_max:
        second_max=first_max
        first_max=my_dict[i]
        # list1.append (first_max) 
        # print(list1)
    elif my_dict[i]>second_max:
        second_max=my_dict[i]
        # print(second_max)
    elif my_dict[i]>third_max:
        third_max=second_max
list1.append(first_max)
list1.append(second_max)
list1.append(third_max)
print("first_max",first_max)
print("second_max",second_max)
print("third_max",third_max)
print(list1)




