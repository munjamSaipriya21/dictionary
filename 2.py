dict_name= {"name":"saipriya","name2":"priya" }
a=dict_name.values()
print(a)

dict_name= {"name":"saipriya","name2":"priya" }
dict_name["name3"]=("sai")
print(dict_name)

dict_name= {"name":"saipriya","name2":"priya" }
dict_name.update({"name2":"sai"})
print(dict_name)

dict_name= {"name":"saipriya","name2":"priya","name3":"sai" }
dict_name.pop("name2")
print(dict_name)

dict_name= {"name":"saipriya","name2":"priya", "name3":"sai" }
dict_name.popitem()
print(dict_name)

dict2= {"name":"saipriya","name2":"priya", "name3":"sai" }
del dict2["name2"]
print(dict2)
