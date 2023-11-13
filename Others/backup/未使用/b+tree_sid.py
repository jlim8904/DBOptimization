import csv
#我到底寫了啥@@

num = 30
with open("Index/MyDB_sid_fmt1.csv", newline='') as f:
    rows = csv.reader(f)
    data = list(rows)
del data[0]
#1
root_data = []
for i in range(0, len(data),int(len(data)/num)+1):
    root_data.append(data[i])

#2
node_list = []
node_list.append(root_data)
for i in range(len(root_data)+1):
    for j in range(i+int(len(data)/num)*i,i+int(len(data)/num)*(i+1)+1):
        if j < len(data):
            if j == i+int(len(data)/num)*i:
                node_list.append([[data[j][0],],])
                node_list[i+1][0].append(data[j][1])
            else:
                node_list[i+1].append(data[j])

for i,x in enumerate(node_list[0]):
    x[1] = str(i + 2)
temp_list = []
#3
tree = []
tree.append(node_list[0])
for row in range(1,len(node_list)):
    data_list = []
    for i in range(0, len(node_list[row]), int(len(node_list[row])/num)+1):
        data_list.append(node_list[row][i])
        temp_list.append(node_list[row][i][1])
    tree.append(data_list)

for row in range(1,len(node_list)):
    for i in range(len(tree[row])+1):
        data_list = []
        for j in range(i+int(len(node_list[row])/num)*i,i+int(len(node_list[row])/num)*(i+1)+1):
            if j < len(node_list[row]):
                if j == i+int(len(node_list)/num)*i:
                    data_list.append([['',],])
                    data_list[0] = node_list[row][j]
                else:
                    data_list.append(node_list[row][j])
        if data_list != []:
            tree.append(data_list)

index = len(node_list)
for i in range(1,len(node_list)):
    for j in range(len(tree[i])):
        tree[i][j][1] = str(index)
        index += 1


with open("Index/MyDB_sid_fmt1_tree.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(tree)


with open("Index/MyDB_sid_fmt1_tree.csv", newline='') as f:
    rows = csv.reader(f)
    data = list(rows)
    
for i,x in enumerate(data[31:]):
    x[0]=x[0][:13] + '\''+str(temp_list[i])+'\']'
    
with open("Index/MyDB_sid_fmt1_tree.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(data)



num = 35
with open("Index/MyDB_sid_fmt2.csv", newline='') as f:
    rows = csv.reader(f)
    data = list(rows)
del data[0]
#1
root_data = []
for i in range(0, len(data),int(len(data)/num)+1):
    root_data.append(data[i])

#2
node_list = []
node_list.append(root_data)
for i in range(len(root_data)+1):
    for j in range(i+int(len(data)/num)*i,i+int(len(data)/num)*(i+1)+1):
        if j < len(data):
            if j == i+int(len(data)/num)*i:
                node_list.append([[data[j][0],],])
                node_list[i+1][0].append(data[j][1])
            else:
                node_list[i+1].append(data[j])

for i,x in enumerate(node_list[0]):
    x[1] = str(i + 2)
temp_list = []
#3
tree = []
tree.append(node_list[0])
for row in range(1,len(node_list)):
    data_list = []
    for i in range(0, len(node_list[row]), int(len(node_list[row])/num)+1):
        data_list.append(node_list[row][i])
        temp_list.append(node_list[row][i][1])
    tree.append(data_list)

for row in range(1,len(node_list)):
    for i in range(len(tree[row])+1):
        data_list = []
        for j in range(i+int(len(node_list[row])/num)*i,i+int(len(node_list[row])/num)*(i+1)+1):
            if j < len(node_list[row]):
                if j == i+int(len(node_list)/num)*i:
                    data_list.append([['',],])
                    data_list[0] = node_list[row][j]
                else:
                    data_list.append(node_list[row][j])
        if data_list != []:
            tree.append(data_list)

index = len(node_list)
for i in range(1,len(node_list)):
    for j in range(len(tree[i])):
        tree[i][j][1] = str(index)
        index += 1

with open("Index/MyDB_sid_fmt2_tree.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(tree)


with open("Index/MyDB_sid_fmt2_tree.csv", newline='') as f:
    rows = csv.reader(f)
    data = list(rows)
    
for i,x in enumerate(data[36:]):
    x[0]=x[0][:15] + '\''+str(temp_list[i])+'\']'
    
with open("Index/MyDB_sid_fmt2_tree.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(data)
