list = []

list.append([60,"2020-03-20","NULL","Welimada","Badulla","NULL","NULL","NULL","NULL"])
list.append([61,"2020-03-20","NULL","Welimada","Badulla","NULL","NULL","NULL","NULL"])

processed_list = []
for i in range(len(list)):
    row = list[i]
    processed_list.append([None if v is 'NULL' else v for v in row])

print(processed_list)


