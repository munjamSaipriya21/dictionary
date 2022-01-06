a=[["Rahul"],["Sheetal"],["Himani"],['saipriya']]
l=[]
l1=[]
for i in a:
    for j in i:
        l.append((i))
        l1.append((j))
    b=max(l1)
print(b,"maxnumber",len(b))

# a=[["Rahul"],["Sheetal"],["Himani"]]
# l=[]
# l1=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         j+=1
#         l.append(i)
#         l1.append(a[j])
#     b=max(l1)
#     i+=1
# print(b)


# from _typeshed import FileDescriptor


# my_dic={"a":[2,4,6],'b':[3,1,3]}
# l=[]
# # a={}
# for i in my_dic:
#     l.append(my_dic[i])
#     for j in l:
#         sum=0
#         for k in j:
#             sum=sum+l[j][k]
#             print(sum)
# my_dic={"a":[2,4,6],'b':[3,1,3]}
# l=[]
# d={}
# for i in my_dic:
#     l.append(my_dic[i])
#     for j in l:
#         sum=0
#         for k in j:
#             sum=sum+k
#     d[i]=sum
# print(d)
