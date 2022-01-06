# dict = {'a': 10, 'b':20, 'c':30}
# sum=0
# for i in dict:
#     sum+=dict[i]
# print(sum)

# def Sum(dict):
#     sum = 0
#     for i in dict.values():
#         sum = sum + i
#     return sum
# dict = {'a': 10, 'b':20, 'c':30}
# print("Sum :", Sum(dict))


def my_sum(myDict):
    list1 = []
    for i in myDict:
        list1.append(myDict[i])
    final = sum(list1)
    return final
myDict = {'a': 60, 'b':40, 'c':30}
print("Sum :",my_sum(myDict))



