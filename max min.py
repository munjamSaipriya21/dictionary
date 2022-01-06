# my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# first_large=0
# second_large=0
# thired_large=0
# list1=[]
# for i in my_dict:
#     if  my_dict[i]>first_large:
#         first_large=my_dict[i]
#         list1.append ( my_dict[i])
#     # print(first_large)
# print(list1)

my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
first_large=0
second_large=0
thired_large=0
list1=[]
for i in my_dict:
    for my_dict[i] in i:
        if  my_dict[i]==first_large:
            my_dict[i]=first_large
        list1.append ( my_dict[i])
        # if first_large==second_large:
        #     my_dict[i]==second_large
        # list1.append (second_large)
    # print(first_large)
print(list1)


