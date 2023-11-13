import csv

num = 20
with open("backup/MyDB_cid.csv", newline='') as f:
    rows = csv.reader(f)
    data = list(rows)
    
del data[0]

root_data = []
for i in range(0, len(data),int(len(data)/num)+1):
    root_data.append(data[i][0])
    root_data.append(data[i][1])


node_list = []
node_list.append(root_data)
for i in range(len(root_data)+1):
    for j in range(i+int(len(data)/num)*i,i+int(len(data)/num)*(i+1)+1):
        if j < len(data):
            if j == i+int(len(data)/num)*i:
                node_list.append([data[j][0],])
                node_list[i+1].append(data[j][1])
            else:
                node_list[i+1].append(data[j][0])
                node_list[i+1].append(data[j][1])

for i in range(len(node_list)-1):
    node_list[0][i*2+1] = i + 2


with open("Index/MyDB_cid_tree.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(node_list)

