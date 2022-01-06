dict1 = { 'Alexandra' : 27,      
            'Shelina Gomez' : 22,  
            'James' : 29,  
            'Peterson' : 30 }   
dict2 = {'Jasmine' : 19,  
            'Maria' : 26,  
            'Helena' : 30 }                          
dict3 = dict1.copy()  
for i,j in dict2.items():  
    dict3[i] = j   
print(dict3)   

# dict1 = {'Student' : 'Butler',  
#     'Course' : 'Computer Science',  
#     'Address' : 'Los Angeles'}  
# dict2 = {'Teacher' : 'Rosy',  
#     'Subject' : 'Computer Science'}  
# dict3 = dict1.copy()  
# dict3.update(dict2)  
# print(dict3)