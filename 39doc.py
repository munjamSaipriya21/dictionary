
marks={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
dic={}
for i in marks.items():
    for j in marks.values():
        if marks[i]>j:
            dic.update(marks[j])
        print(dic)
    # for j

    

