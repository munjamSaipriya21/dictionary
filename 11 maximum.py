# my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# hightst=max(my_dict)
# print(hightst)

student=dict()
num=int(input("enter the number:"))
for i in range (num):
    name=input("enter the name of student:")
    marks=input("enter the name of student marks:")
    student[name]=marks
print(student)
hightst=max(student, key=student.get)
lowest= max(student.values())
# hightst=min(student, key=student.get)
# lowest= min(student.values())
print("name:" ,hightst)
print("value:" ,lowest)