dict=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
dic={}
for d in dict:
    if d['item'] not in dic:
        dic[d['item']] = d['amount']
    else:
        dic[d['item']] += d['amount'] 
print(dic) 

# a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
# dic={}
# for d in a:
#     if d['item'] not in dic:
#         dic[d['item']]=d['amount']
# print(dic)  


