# dict1={"name":"mamatha","class":"12","collage":"TSWRDC"}
# dict2=dict1.values()
# print(dict2)

# dict1=[{"name":"mamatha","class":"12","collage":"TSWRDC"}]
# a=dict1[0]
# l=[]
# for i in a.values():
#     l.append(i)
# print(l)

# dict1=[{"name":"mamatha","class":"12","collage":"TSWRDC"}]
# l=[]
# for i in dict1:
#     for j in i:
#         l.append (j)
#     print(l)


dict1=[{"name":"mamatha","class":"12","collage":"TSWRDC"}]
l=[]
for i in dict1:
    for j in i:
        l.append (i[j])
    print(l)

