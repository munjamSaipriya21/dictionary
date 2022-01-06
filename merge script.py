 
# d2 = {'Tennis ' : 'Maria',  
#     'Stadium  ' : 'Amsterdam',  
#     'Basketball' : 'Washington',  
#     'Actress' : 'Elizabeth'}  
# d1.update(d2) 
# print(d1) 
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)


# def merge_twoDict(a, b):   
#     return (a.update(b)) 
# n = {'USA' : 'New York',  
#       'Jermany' : 'Jakarta',  
#       'England' : 'London' }  
# m = {  
#     'India' : 'Delhi',  
#     'Russia' : 'Russian',  
#     'Australia' : 'Sydney'} 
# merge_twoDict(n, m)
# print(n) 


dict1 = {'Student' : 'Butler',  
    'Course' : 'Computer Science',  
    'Address' : 'Los Angeles'}  
dict2 = {'Teacher' : 'Rosy',  
    'Subject' : 'Computer Science'}  
d3 = dict(dict1, **dict2)  
print( d3)